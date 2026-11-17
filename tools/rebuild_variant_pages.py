"""Build readable variant indexes and pages from the released records, offline."""
from collections import defaultdict
import html,json
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
import baseline,variant_data
from rebuild_pages import md,readable_quote,fenced


def write(name,lines):
    p=ROOT/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text('\n'.join(lines)+'\n',encoding='utf-8')


def main():
    meta=variant_data.metadata();study=json.loads((ROOT/'configs/variant-study.json').read_text())
    originals={q['id']:q for q in baseline.read_jsonl(ROOT/'data/question_manifest.jsonl')}
    base_text={q['id']:q for q in baseline.read_jsonl(ROOT/'data/questions.jsonl')}
    texts=variant_data.inputs();models=json.loads((ROOT/'configs/models.json').read_text())
    outcomes,controls=variant_data.outcome_tables()
    baseline_pages={row['id']:row['page'] for row in originals.values() if 'page' in row}
    # The baseline page convention is the same as the existing question-page generator.
    def original_page(q):
        import re
        name={'Perception and attention (retrieval)':'Retrieval','Metacognition/Uncertainty monitoring (risk)':'Uncertainty monitoring','Information seeking (information gain)':'Information seeking'}.get(q['ability'],q['ability'])
        slug=re.sub('[^a-z0-9]+','-',name.lower()).strip('-')
        file=q['id'].replace('/','-')+'.md'
        return f'questions/{slug}/{file}'
    by_cap=defaultdict(list);by_base=defaultdict(list)
    for q in meta:
        by_cap[q['page'].split('/')[1]].append(q);by_base[q['original_id']].append(q)
    labels=json.loads((ROOT/'configs/variant-labels.json').read_text())
    def label(q):
        tags=q['conditions'];first=tags[0]
        factor=labels['factors'].get(first['factor'],first['factor'])
        level=labels['levels'].get(first['factor'],{}).get(str(first['level']),str(first['level']).replace('_',' '))
        return factor+' · '+level
    def answer(row,choices):
        if row['status']!='ok':return {'refusal':'Refused','error':'Error','unknown':'Response unresolved','unknown_prior_attempt':'Earlier response unresolved','not_supported':'Outside input limit'}.get(row['status'],row['status'])
        key=row['prediction'];return '`'+key+'`'+(' — '+md(choices[key]) if choices and key in choices else '')
    root=['# Explore the question variants','','The study contains **24,563 altered versions of the 1,005 original questions**, tested on 11 decision models. Each version keeps the recorded reference answer. Start from a capability, choose an original question, then open one of its variants.','',
          '[How the variants were made](../docs/variant-methods.md) · [Read the results](../docs/variant-results.md) · [Verify or rerun](../docs/variant-reproduction.md) · [Original questions](../questions/README.md)','',
          f"Full text is included for **{study['full_text_variants']:,} variants**. The other **{study['recovered_text_variants']:,}** use original question texts with additional sharing requirements; [recover them locally](../docs/variant-reproduction.md#recover-the-remaining-variant-texts) from the original sources and saved edit recipes. All variant IDs, reference keys and recorded outcomes are included.",'',
          '| Capability | Original questions | Variants | Full texts included |','| --- | ---: | ---: | ---: |']
    for cap,qs in by_cap.items():
        title=cap.replace('-',' ').capitalize()
        root.append(f"| [{title}]({cap}/README.md) | {len({q['original_id'] for q in qs})} | {len(qs):,} | {sum(q['text_included'] for q in qs):,} |")
        cap_lines=['# '+title+' variants','','[All variants](../README.md) · [Methods](../../docs/variant-methods.md)','','Choose an original question to compare its altered versions.','',
                   '| Original question | Source | Variants |','| --- | --- | ---: |']
        for base in dict.fromkeys(q['original_id'] for q in qs):
            members=by_base[base];directory=members[0]['page'].rsplit('/',1)[0]
            index=['# Variants of '+base,'',f"[Original question](../../../{original_page(originals[base])}) · [Capability index](../README.md) · [Variant methods](../../../docs/variant-methods.md)",'',
                   'Each row is a distinct evaluated input. An input can serve more than one recorded condition; those aliases are listed on its page.','',
                   '| Variant | Text | Correct / answered |','| --- | --- | ---: |']
            for q in members:
                results=[outcomes[m,q['id']] for m in study['models']]
                ok=[r for r in results if r['status']=='ok'];correct=sum(r['prediction']==q['gold_choice'] for r in ok)
                index.append(f"| [{md(label(q))}]({q['page'].rsplit('/',1)[1]}) | {'Included' if q['text_included'] else 'Recover locally'} | {correct} / {len(ok)} |")
            write(directory+'/README.md',index)
            cap_lines.append(f"| [{base}]({directory.rsplit('/',1)[1]}/README.md) | {originals[base]['dataset']} | {len(members)} |")
        write('variants/'+cap+'/README.md',cap_lines)
    write('variants/README.md',root)
    for q in meta:
        c=texts.get(q['id']);base=originals[q['original_id']]
        page=q['page'];title=label(q)
        detail=['# '+title+' variant','',f"[Original question](../../../{original_page(base)}) · [Other versions of this question](README.md) · [All variants](../../README.md)",'',
            'This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.','',
            '**Changed fields:** '+', '.join({'state':'context','question':'question instructions','choices':'answer choices or their order'}[x] for x in q['changed_fields'])+'.','',
            '[How the edits were constructed](../../../docs/variant-methods.md)','']
        if c:
            if c['state']:
                context=fenced(c['state']) if q['dataset']=='cruxeval' else readable_quote(c['state'])
                if len(c['state'])>1500:context='<details>\n<summary>Read the full context</summary>\n\n'+context+'\n\n</details>'
                detail += ['## Context','',context,'']
            detail += ['## Question','',readable_quote(c['question']),'','## Answer choices','']
            detail += ['- **'+md(k)+'.** '+md(v).rstrip() for k,v in c['choices'].items()]
            detail += ['', '**Reference answer:** `'+q['gold_choice']+'`.','',
                '<details>','<summary>Exact evaluated input as JSON</summary>','',
                fenced(json.dumps({k:c[k] for k in ('state','question','choices')},ensure_ascii=False,indent=2)),
                '','</details>','']
        else:
            detail += ['## Recover the question text','','The original dataset’s terms do not clearly support republishing its text here, or require additional conditions. This variant’s full text is therefore reconstructed locally. [Follow the recovery instructions](../../../docs/variant-reproduction.md#recover-the-remaining-variant-texts).','',
                '**Reference answer key:** `'+q['gold_choice']+'`.','']
        detail += ['## Recorded model answers','','The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.','',
            '| Model | Original answer | Variant answer | Change |','| --- | --- | --- | --- |']
        for model in study['models']:
            r=outcomes[model,q['id']];control=controls.get(r['original_result_id'])
            before=answer(control,base_text.get(q['original_id'],{}).get('choices')) if control else 'Not selected'
            after=answer(r,c['choices'] if c else None)
            change=('Same answer' if r['prediction']==control['prediction'] else 'Different answer') if control and control['status']==r['status']=='ok' else '—'
            if r['recovered_error']:change+='; recovered after an initial error'
            detail.append(f"| {models[model]['name']} | {before} | {after} | {change} |")
        if q.get('ordering_roles'):
            detail += ['', '**Ordering comparison:** ' + ', '.join(x.replace('_',' ') for x in q['ordering_roles']) + '. Only the exact matched comparison sets contribute to the reported ordering contrasts.']
        if any(t['factor']=='option_order' for t in q['conditions']):detail += ['','Clef and Clef Flash sort answer choices in their published input-processing code. Their choice-order results describe that preprocessing.']
        detail += ['','<details>','<summary>Identifiers and recorded conditions</summary>','',
                   '**Variant ID:** `'+q['id']+'`','', '**Input fingerprint:** `'+q['input_hash']+'`','',
                   '| Change | Recorded version |','| --- | --- |']
        for t in q['conditions']:
            detail.append('| '+md(labels['factors'].get(t['factor'],t['factor']))+' | '+md(labels['levels'].get(t['factor'],{}).get(str(t['level']),str(t['level']).replace('_',' ')))+' |')
        detail += ['','</details>','','Source attribution and dataset terms are linked from the [original question](../../../'+original_page(base)+').']
        write(page,detail)
    print(f'Built {len(meta):,} variant pages, {len(by_base):,} original-question indexes and {len(by_cap)} capability indexes.')


if __name__=='__main__':main()
