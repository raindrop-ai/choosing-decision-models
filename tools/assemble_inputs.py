"""Combine released questions and locally recovered inputs into the exact 1,005 cases."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import baseline


def assemble(metadata, fragments, *, require_complete=True):
    manifest = {m['id']:m for m in metadata}
    if len(manifest) != 1005 or len(metadata) != 1005:
        raise ValueError('Expected 1,005 unique manifest IDs')
    by_id = {}
    for fragment in fragments:
        for case in fragment:
            cid = case['id']
            if cid in by_id:
                raise ValueError('Duplicate question across input files: ' + cid)
            if cid not in manifest:
                raise ValueError('Unknown question ID: ' + cid)
            m = manifest[cid]
            if (baseline.input_hash(case) != m['input_hash'] or case['gold'] != m['gold_choice']
                    or list(case['choices']) != m['choice_keys']):
                raise ValueError('Input, answer or choice order differs: ' + cid)
            by_id[cid] = case
    if require_complete and set(by_id) != set(manifest):
        missing = [m['id'] for m in metadata if m['id'] not in by_id]
        raise ValueError(f'Missing {len(missing)} inputs; first missing ID: ' + missing[0])
    return [by_id[m['id']] for m in metadata if m['id'] in by_id]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--additional', nargs='*', type=Path,
        help='Local recovery files to combine with data/questions.jsonl')
    parser.add_argument('--partial', action='store_true', help='Validate and combine available questions without requiring all 1,005')
    args = parser.parse_args()
    metadata = baseline.read_jsonl(ROOT/'data/question_manifest.jsonl')
    fragments = [baseline.read_jsonl(ROOT/'data/questions.jsonl')]
    paths = args.additional
    if paths is None:
        paths = [ROOT/'.local/piqa.questions.jsonl',ROOT/'.local/withheld.questions.jsonl']
        if args.partial:
            paths = [p for p in paths if p.exists()]
    missing = [str(p) for p in paths if not p.is_file()]
    if missing:
        parser.error('Missing recovery file(s): '+', '.join(missing)+'. See docs/recovering-inputs.md, or use --partial for available inputs.')
    fragments += [baseline.read_jsonl(p) for p in paths]
    cases = assemble(metadata, fragments, require_complete=not args.partial)
    local = ROOT/'.local'; local.mkdir(mode=0o700,exist_ok=True)
    output = local/('questions.available.jsonl' if args.partial else 'questions.complete.jsonl')
    temporary = output.with_suffix('.jsonl.replacing')
    try:
        temporary.write_text(''.join(json.dumps(c,ensure_ascii=False)+'\n' for c in cases))
        temporary.replace(output)
    finally:
        temporary.unlink(missing_ok=True)
    print(f'Verified {len(cases):,} of 1,005 exact inputs; saved in .local/{output.name}.')


if __name__=='__main__':main()
