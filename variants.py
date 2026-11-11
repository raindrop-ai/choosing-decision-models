"""Verify, explore, reconstruct or summarize the recorded variants. No model calls."""
from __future__ import annotations
import argparse
from collections import Counter
import csv
import json
from pathlib import Path
import tempfile
import baseline
import variant_data as data

ROOT=Path(__file__).resolve().parent


def verify():
    study=json.loads((ROOT/'configs/variant-study.json').read_text())
    inventory=json.loads((ROOT/'MANIFEST.json').read_text())['sha256']
    prefixes=('data/variants/','results/variants/','summaries/variants/','variants/')
    for name,wanted in inventory.items():
        if name.startswith(prefixes) or name in {'variants.py','variant_data.py','configs/variant-study.json'}:
            if baseline.sha256(ROOT/name)!=wanted:
                raise ValueError('Variant file checksum mismatch: '+name)
    meta=data.metadata();by={q['id']:q for q in meta}
    if len(by)!=len(meta) or len(meta)!=study['variants']:
        raise ValueError('Variant inventory differs')
    original={q['id']:q for q in baseline.read_jsonl(ROOT/'data/question_manifest.jsonl')}
    for q in meta:
        parent=original[q['original_id']]
        if q['parent_input_hash']!=parent['input_hash'] or q['gold_choice']!=parent['gold_choice']:
            raise ValueError('Original/reference lineage changed')
        if set(q['choice_keys'])!=set(parent['choice_keys']):
            raise ValueError('Variant answer-choice keys changed')
    available=data.inputs()
    if len(available)!=study['full_text_variants'] or set(available)!={q['id'] for q in meta if q['text_included']}:
        raise ValueError('Released variant text inventory changed')
    recipes=baseline.read_jsonl(ROOT/'data/variants/recovery-recipes.jsonl')
    if len(recipes)!=study['recovered_text_variants'] or {r['id'] for r in recipes}!={q['id'] for q in meta if not q['text_included']}:
        raise ValueError('Variant recovery inventory differs')
    for recipe in recipes:
        q=by[recipe['id']]
        if recipe['original_id']!=q['original_id'] or recipe['input_hash']!=q['input_hash'] or recipe['parent_input_hash']!=q['parent_input_hash']:
            raise ValueError('Recovery recipe input lineage differs')
    outcomes,controls=data.outcome_tables()
    for control in controls.values():
        q=original[control['case_id']]
        if control['input_hash']!=q['input_hash'] or control['model'] not in study['models']:
            raise ValueError('Original control input/model differs')
        if control['status']=='ok':
            if control['prediction'] not in q['choice_keys']:raise ValueError('Invalid original control answer')
        elif control['prediction'] is not None or control['status'] not in {'refusal','error','unknown','unknown_prior_attempt'}:
            raise ValueError('Invalid original control status')
    if len(outcomes)!=len(meta)*len(study['models']):
        raise ValueError('Incomplete model/variant inventory')
    for model in study['models']:
        observed=Counter()
        for q in meta:
            row=outcomes[model,q['id']];observed[row['status']]+=1
            if row['input_hash']!=q['input_hash']:
                raise ValueError('Outcome input fingerprint differs')
            if row['status']=='ok':
                if row['prediction'] not in q['choice_keys']:raise ValueError('Unknown predicted choice')
            elif row['status'] not in {'error','refusal','unknown','unknown_prior_attempt','not_supported'} or row['prediction'] is not None:
                raise ValueError('Invalid outcome status/answer')
            if row['status']!='not_supported':
                control=controls[row['original_result_id']]
                if control['case_id']!=q['original_id'] or control['input_hash']!=q['parent_input_hash'] or control['model']!=model:
                    raise ValueError('Wrong original/control link')
        if dict(observed)!=study['outcomes'][model]:raise ValueError('Recorded outcome coverage differs')
    recalculated=data.summaries()
    with tempfile.TemporaryDirectory() as tmp:
        path=Path(tmp)/'comparisons.csv';data.write_summary(recalculated,path)
        if path.read_bytes()!=(ROOT/'summaries/variants/comparisons.csv').read_bytes():
            raise ValueError('Comparison tables differ from the recorded answers')
    print(f"Verified {len(meta):,} variants, {len(outcomes):,} model/variant records and {len(recalculated):,} comparison summaries.")


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    sub=parser.add_subparsers(dest='command',required=True)
    sub.add_parser('verify')
    p=sub.add_parser('summarize');p.add_argument('--output',type=Path,default=ROOT/'.local/variant-summaries/comparisons.csv')
    p=sub.add_parser('inspect');p.add_argument('--case',required=True);p.add_argument('--local-questions',type=Path)
    p=sub.add_parser('recover');p.add_argument('--originals',type=Path,default=ROOT/'.local/questions.complete.jsonl')
    p=sub.add_parser('inputs');p.add_argument('--model');p.add_argument('--common',action='store_true');p.add_argument('--capability')
    p.add_argument('--original',help='Select variants of one original question ID')
    p.add_argument('--available-only',action='store_true',help='Explicitly select only question texts present in the input files')
    p.add_argument('--local-questions',type=Path);p.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    if args.command=='verify':verify();return
    if args.command=='summarize':
        rows=data.summaries();data.write_summary(rows,args.output);print('Wrote comparison tables to '+str(args.output));return
    meta=data.metadata();by={q['id']:q for q in meta}
    if args.command=='recover':
        recovered=data.inputs(local_originals=args.originals)
        if len(recovered)!=len(meta):
            raise ValueError(f"Recovered {len(recovered):,} of {len(meta):,} variants. Supply all 1,005 verified original inputs.")
        path=ROOT/'.local/variants.complete.jsonl';path.parent.mkdir(parents=True,exist_ok=True)
        path.write_text(''.join(json.dumps(recovered[q['id']],ensure_ascii=False)+'\n' for q in meta),encoding='utf-8')
        print(f'Verified all {len(meta):,} variants; wrote .local/variants.complete.jsonl.');return
    if args.command=='inspect':
        if args.case not in by:parser.error('Use a variant ID from a variant page or manifest')
        q=by[args.case]
        if args.local_questions:
            matches=[c for c in baseline.read_jsonl(args.local_questions) if c['id']==args.case]
            if len(matches)!=1:parser.error('The input file must contain this variant exactly once')
            text=matches[0]
            if baseline.input_hash(text)!=q['input_hash'] or text['gold']!=q['gold_choice']:raise ValueError('Variant input changed')
        else:
            text=next((c for c in baseline.read_jsonl(ROOT/q['input_file']) if c['id']==args.case),None) if q['input_file'] else None
        study=json.loads((ROOT/'configs/variant-study.json').read_text());predictions=[]
        controls={r['result_id']:r for r in baseline.read_jsonl(ROOT/'results/variants/original-controls.jsonl')}
        for model in study['models']:
            row=next(r for r in baseline.read_jsonl(ROOT/f'results/variants/{model}.jsonl') if r['case_id']==args.case)
            predictions.append({**row,'original_control':controls.get(row['original_result_id'])})
        print(json.dumps({'metadata':q,'question':text,'predictions':predictions},ensure_ascii=False,indent=2));return
    if args.command=='inputs':
        study=json.loads((ROOT/'configs/variant-study.json').read_text())
        if args.model and args.model not in study['models']:parser.error('Choose a recorded decision-model alias or omit --model')
        all_inputs=({c['id']:c for c in baseline.read_jsonl(args.local_questions)} if args.local_questions else data.inputs())
        selected=[q for q in meta if (not args.common or q['common_input_fit']) and
                  (not args.capability or q['ability']==args.capability) and
                  (not args.original or q['original_id']==args.original)]
        if args.model:
            supported={r['case_id'] for r in baseline.read_jsonl(ROOT/f'results/variants/{args.model}.jsonl') if r['status']!='not_supported'}
            selected=[q for q in selected if q['id'] in supported]
        if args.available_only:selected=[q for q in selected if q['id'] in all_inputs]
        missing=[q['id'] for q in selected if q['id'] not in all_inputs]
        if missing:parser.error(f"{len(missing):,} selected texts need recovery. Run variants.py recover, then pass --local-questions .local/variants.complete.jsonl")
        if not selected:parser.error('No variants match that selection')
        output=[]
        for q in selected:
            c=all_inputs[q['id']]
            if baseline.input_hash(c)!=q['input_hash'] or c['gold']!=q['gold_choice']:raise ValueError('Input fingerprint changed')
            output.append(c)
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(''.join(json.dumps(c,ensure_ascii=False)+'\n' for c in output),encoding='utf-8')
        print(f'Wrote {len(output):,} verified variant inputs to {args.output}.');return


if __name__=='__main__':main()
