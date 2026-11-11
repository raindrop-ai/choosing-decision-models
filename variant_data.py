"""Read, reconstruct and score the released question variants. No inference calls."""
from __future__ import annotations
from collections import Counter, defaultdict
import csv
import json
from pathlib import Path
import baseline

ROOT = Path(__file__).resolve().parent


def metadata(root=ROOT):
    return baseline.read_jsonl(Path(root) / 'data/variants/manifest.jsonl')


def apply_recipe(recipe, originals):
    base = originals[recipe['original_id']]
    if baseline.input_hash(base) != recipe['parent_input_hash']:
        raise ValueError('Original input differs from the recipe reference')
    def field(parts):
        result = []
        for part in parts:
            if isinstance(part, str):
                result.append(part)
                continue
            source = originals[part.get('original_id', recipe['original_id'])]
            value = source['choices'][part['choice']] if part['field'] == 'choices' else source[part['field']]
            start, end = part['start'], part['end']
            if not 0 <= start <= end <= len(value):
                raise ValueError('Invalid original-text reference')
            result.append(value[start:end])
        return ''.join(result)
    result = dict(id=recipe['id'], state=field(recipe['state']), question=field(recipe['question']),
                  choices={key:field(parts) for key,parts in recipe['choices']}, gold=base['gold'])
    if baseline.input_hash(result) != recipe['input_hash']:
        raise ValueError('Recovered variant does not match the evaluated input')
    return result


def inputs(root=ROOT, local_originals=None):
    root = Path(root)
    info = metadata(root)
    result = {}
    for path in sorted({q['input_file'] for q in info if q['input_file']}):
        for row in baseline.read_jsonl(root / path):
            if row['id'] in result:raise ValueError('Duplicate variant input ID')
            result[row['id']] = row
    if local_originals:
        original_rows = baseline.read_jsonl(local_originals)
        originals = {c['id']: c for c in original_rows}
        manifest = {c['id']:c for c in baseline.read_jsonl(root/'data/question_manifest.jsonl')}
        if len(originals) != len(original_rows):
            raise ValueError('Duplicate original question IDs')
        for cid, c in originals.items():
            if cid not in manifest or baseline.input_hash(c) != manifest[cid]['input_hash'] or c['gold'] != manifest[cid]['gold_choice']:
                raise ValueError('Original input does not match the baseline')
        for recipe in baseline.read_jsonl(root/'data/variants/recovery-recipes.jsonl'):
            if recipe['original_id'] in originals:
                result[recipe['id']] = apply_recipe(recipe, originals)
    for q in info:
        if q['id'] in result:
            c = result[q['id']]
            if baseline.input_hash(c) != q['input_hash'] or c['gold'] != q['gold_choice'] or list(c['choices']) != q['choice_keys']:
                raise ValueError('Variant input, answer or choice order changed')
    return result


def outcome_tables(root=ROOT):
    root = Path(root)
    study = json.loads((root/'configs/variant-study.json').read_text())
    rows = {}
    for model in study['models']:
        for row in baseline.read_jsonl(root/f'results/variants/{model}.jsonl'):
            key = (model, row['case_id'])
            if key in rows:
                raise ValueError('Duplicate variant/model outcome')
            rows[key] = row
    control_rows = baseline.read_jsonl(root/'results/variants/original-controls.jsonl')
    controls = {r['result_id']:r for r in control_rows}
    if len(controls)!=len(control_rows):raise ValueError('Duplicate original control ID')
    return rows, controls


def group_stats(group, model, rows, controls, by_id, capability=None):
    families = [f for f in group['families'] if capability is None or by_id[f['original_id']]['ability'] == capability]
    result = []
    for contrast in group['contrasts']:
        counts = Counter(); unavailable = Counter()
        for family in families:
            after = rows[model, family['levels'][contrast['after']]]
            before = (controls[after['original_result_id']] if contrast['before'] == 'original'
                      else rows[model, family['levels'][contrast['before']]])
            required = [("before",before),("after",after)]
            if group.get('require_complete_levels'):
                required = [(level,rows[model,cid]) for level,cid in family['levels'].items()]
            if group.get('require_original_controls'):
                required += [('original_'+level,controls[rows[model,cid]['original_result_id']])
                             for level,cid in family['levels'].items()]
            failed = [(label,r) for label,r in required if r['status']!='ok']
            if failed:
                for label,r in failed:unavailable[label+'_'+r['status']] += 1
                continue
            if before['status'] != 'ok' or after['status'] != 'ok':
                unavailable['before_'+before['status']] += before['status'] != 'ok'
                unavailable['after_'+after['status']] += after['status'] != 'ok'
                continue
            gold = by_id[family['original_id']]['gold_choice']
            old, new = before['prediction'] == gold, after['prediction'] == gold
            counts['paired'] += 1
            counts['before_correct'] += old
            counts['after_correct'] += new
            counts['changed'] += before['prediction'] != after['prediction']
            counts['any_changed'] += len({r['prediction'] for _,r in required}) > 1
            counts['lost'] += old and not new
            counts['gained'] += new and not old
        n = counts['paired']
        result.append(dict(comparison_id=contrast['id'], label=contrast['label'], model=model,
            factor=group['factor'], capability=capability or 'all', bases=len(families), paired=n,
            unavailable=len(families)-n, unavailable_statuses={k:v for k,v in unavailable.items() if v},
            before_correct=counts['before_correct'], after_correct=counts['after_correct'], changed=counts['changed'],
            lost=counts['lost'], gained=counts['gained'],
            any_changed=counts['any_changed'], any_change_pct=100*counts['any_changed']/n if n else None,
            before_accuracy=baseline.ratio(counts['before_correct'], n), after_accuracy=baseline.ratio(counts['after_correct'], n),
            delta_pp=100*(counts['after_correct']-counts['before_correct'])/n if n else None,
            change_pct=100*counts['changed']/n if n else None,
            normalized=group['factor']=='option_order' and model in {'clef','clef-flash'}))
    return result


def summaries(root=ROOT):
    root = Path(root)
    study = json.loads((root/'configs/variant-study.json').read_text())
    groups = json.loads((root/'data/variants/comparisons.json').read_text())['groups']
    by_id = {c['id']:c for c in baseline.read_jsonl(root/'data/question_manifest.jsonl')}
    outcomes, controls = outcome_tables(root)
    abilities = list(dict.fromkeys(q['ability'] for q in by_id.values()))
    result = []
    for group in groups:
        for model in study['models']:
            for ability in [None, *abilities]:
                selected = group_stats(group, model, outcomes, controls, by_id, ability)
                result.extend(r for r in selected if r['bases'])
    return result


def write_summary(rows, output):
    output = Path(output);output.parent.mkdir(parents=True,exist_ok=True)
    fields = ['comparison_id','label','factor','model','capability','bases','paired','unavailable',
        'before_correct','after_correct','changed','lost','gained','before_accuracy','after_accuracy','delta_pp','change_pct',
        'any_changed','any_change_pct','normalized']
    with output.open('w',encoding='utf-8',newline='') as stream:
        writer = csv.DictWriter(stream,fieldnames=fields,extrasaction='ignore');writer.writeheader();writer.writerows(rows)
