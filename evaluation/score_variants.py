"""Score the exact manipulation comparisons from fresh original and variant runs."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
import baseline,variant_data
from score_fresh import score


def read_run(spec,folder,manifest,expected_model=None):
    """Validate job identity, selected inputs and every returned answer offline."""
    if not isinstance(spec,dict) or set(spec)!={'job','output'}:
        raise ValueError('Each run needs job and output file paths')
    job=json.loads((folder/spec['job']).read_text())
    model=job.get('model',job.get('model_name'))
    if not isinstance(model,str) or expected_model is not None and model!=expected_model:
        raise ValueError('Original and variant runs must use the same model name')
    ids=job.get('case_ids') or [c['id'] for c in job['cases']]
    hashes=job.get('input_hashes') or {c['id']:baseline.input_hash(c) for c in job['cases']}
    by={q['id']:q for q in manifest}
    if not ids or len(ids)!=len(set(ids)) or any(cid not in by or hashes[cid]!=by[cid]['input_hash'] for cid in ids):
        raise ValueError('Fresh job does not match the selected study inputs')
    output=folder/spec['output']
    if output.suffix=='.jsonl':
        records=baseline.read_jsonl(output)
        if any(r.get('model')!=model for r in records):raise ValueError('Response model differs from the job')
    else:
        records=json.loads(output.read_text())['records']
        if any(r.get('requested_model')!=job['config']['model_id'] or r.get('model_revision')!=job['config']['revision'] for r in records):
            raise ValueError('GPU response model/checkpoint differs from the job')
    score(records,manifest,ids)
    return model,records


def calculate(spec,folder,root=ROOT):
    root=Path(root)
    originals=baseline.read_jsonl(root/'data/question_manifest.jsonl')
    meta=variant_data.metadata(root);by={q['id']:q for q in originals}
    groups=json.loads((root/'data/variants/comparisons.json').read_text())['groups']
    if not isinstance(spec,dict) or set(spec)!={'originals','variants'}:
        raise ValueError('Supply originals and variants, each with job and output paths')
    phase_jobs=[json.loads((folder/spec[phase]['job']).read_text()) for phase in ('originals','variants')]
    settings=[job.get('configuration',job.get('config')) for job in phase_jobs]
    if settings[0]!=settings[1]:
        raise ValueError('Original and variant runs must use the same model connection and settings')
    model,before=read_run(spec['originals'],folder,originals)
    _,after=read_run(spec['variants'],folder,meta,model)
    if not before or not after:raise ValueError('Both phases need recorded outcomes')
    controls={f'original:{cid}':dict(case_id=cid,status='not_run',prediction=None) for cid in by}
    for row in before:controls['original:'+row['case_id']]=row
    rows={(model,q['id']):dict(case_id=q['id'],status='not_run',prediction=None,original_result_id='original:'+q['original_id']) for q in meta}
    for row in after:
        record=rows[model,row['case_id']]
        control=record['original_result_id']
        record.update(row)
        record['original_result_id']=control
    abilities=list(dict.fromkeys(q['ability'] for q in originals))
    results=[]
    for g in groups:
        for ability in [None,*abilities]:
            results.extend(r for r in variant_data.group_stats(g,model,rows,controls,by,ability) if r['bases'])
    return results


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--runs',type=Path,required=True,help='JSON describing original and variant jobs and output files')
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    result=calculate(json.loads(args.runs.read_text()),args.runs.resolve().parent)
    if args.output.exists():parser.error('Choose a new output path')
    variant_data.write_summary(result,args.output)
    print(f'Wrote {len(result):,} fresh comparison rows to {args.output}. Check paired counts: missing original or variant responses reduce coverage.')

if __name__=='__main__':main()
