"""Reconstruct exact held inputs from independently obtained source files, offline."""
from __future__ import annotations

import argparse
from copy import deepcopy
import csv
import hashlib
import io
import itertools
import json
from pathlib import Path
import sys
import tarfile
import zipfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import baseline

DATASETS = ('ag_news', 'fantom', 'miniscan', 'newton', 'proofwriter', 'sst2', 'trec')
PREFIX = 'Apply the same inferred rule to this new input: '
VERSION = 'choice-adaptation-v1'


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def file_hash(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def source_file(root, name, wanted):
    relative = Path(name)
    if relative.is_absolute() or '..' in relative.parts:
        raise ValueError('Unsafe source path')
    path = Path(root) / relative
    if not path.is_file():
        raise ValueError('Missing source file: ' + name)
    if file_hash(path) != wanted:
        raise ValueError('Source checksum mismatch: ' + name)
    return path


def read_source(path, member=None):
    """Read only the named member; never extract an archive or execute source code."""
    if member is not None:
        if member.startswith('/') or '..' in Path(member).parts:
            raise ValueError('Unsafe archive member')
        if path.suffix == '.zip':
            with zipfile.ZipFile(path) as archive:
                info = archive.getinfo(member)
                if info.is_dir() or info.file_size > 100_000_000:
                    raise ValueError('Unexpected archive member')
                return archive.read(member)
        with tarfile.open(path) as archive:
            info = archive.getmember(member)
            if not info.isfile() or info.size > 100_000_000:
                raise ValueError('Unexpected archive member')
            return archive.extractfile(info).read()
    return path.read_bytes()


def required_files(metadata, sources, datasets):
    """Describe original static files needed for the requested selected questions."""
    declared = {s['id']:{f['path']:f for f in s['downloads']} for s in sources}
    needed = {}
    for m in metadata:
        sid = m['dataset']
        if sid not in datasets:
            continue
        name = m['source_locator']['path']
        if sid == 'fantom': name = 'fantom.tar.gz'
        if sid == 'proofwriter': name = 'proofwriter.zip'
        spec = declared[sid][name]
        needed[(sid, name)] = dict(dataset=sid, **spec)
    return list(needed.values())


def native_record(metadata, cache, paths):
    sid = metadata['dataset']
    loc = metadata['source_locator']
    name = loc['path']
    key = sid, name
    if key not in cache:
        if sid in {'ag_news', 'sst2'}:
            try:
                import pyarrow.parquet as pq
            except ImportError as exc:
                raise ValueError('Parquet recovery requires the optional tools/requirements-recovery.txt dependencies') from exc
            cache[key] = pq.read_table(paths[(sid, name)]).to_pylist()
        elif sid == 'fantom':
            member = name.removeprefix('extracted/fantom.tar.gz/')
            cache[key] = json.loads(read_source(paths[(sid, 'fantom.tar.gz')], member))
        elif sid == 'proofwriter':
            member = name.removeprefix('extracted/proofwriter.zip/')
            cache[key] = [json.loads(line) for line in read_source(paths[(sid, 'proofwriter.zip')], member).decode().splitlines() if line]
        elif sid == 'trec':
            cache[key] = paths[(sid, name)].read_text(encoding='latin1').splitlines()
        elif sid == 'newton':
            with paths[(sid, name)].open(encoding='utf-8-sig', newline='') as stream:
                cache[key] = list(csv.DictReader(stream))
        else:
            cache[key] = baseline.read_jsonl(paths[(sid, name)])
    row, _, sub = loc['record'].partition('/')
    return cache[key][int(row)], sub


def miniscan_grammar(examples):
    primitive={e['input']:e['output'].split() for e in examples if len(e['input'].split())==1}
    if len(primitive)!=4 or any(len(v)!=1 for v in primitive.values()):raise ValueError('Unexpected MiniSCAN primitive schema')
    unary=set();sandwich=set();swap=set()
    for e in examples:
        words=e['input'].split();out=e['output'].split()
        if len(words)==2 and words[0] in primitive and out==primitive[words[0]]*3:unary.add(words[1])
        if len(words)==3 and words[0] in primitive and words[2] in primitive:
            a,b=primitive[words[0]],primitive[words[2]]
            if out==a+b+a:sandwich.add(words[1])
            if out==b+a:swap.add(words[1])
    if any(len(x)!=1 for x in (unary,sandwich,swap)):raise ValueError('Ambiguous grammar operators')
    return primitive,next(iter(unary)),next(iter(sandwich)),next(iter(swap))


def translate(words,grammar,repeat=3,sandwich='aba',reverse=True,associativity='left'):
    prim,unary,mid,low=grammar
    for op in (low,mid):
        spots=[i for i,x in enumerate(words) if x==op]
        if spots:
            i=spots[-1] if associativity=='left' else spots[0]
            if i==0 or i==len(words)-1:raise ValueError('Invalid grammar expression')
            a=translate(words[:i],grammar,repeat,sandwich,reverse,associativity)
            b=translate(words[i+1:],grammar,repeat,sandwich,reverse,associativity)
            return (b+a if reverse else a+b) if op==low else [v for key in sandwich for v in {'a':a,'b':b}[key]]
    if words and words[-1]==unary:return translate(words[:-1],grammar,repeat,sandwich,reverse,associativity)*repeat
    if len(words)==1 and words[0] in prim:return prim[words[0]]
    raise ValueError('Unparsed grammar expression')


def miniscan_choices(case, gold, position):
    """Reproduce the historical competing-grammar choices, including their order."""
    examples = json.loads(case['state'])
    grammar = miniscan_grammar(examples)
    words = case['question'].removeprefix(PREFIX).split()
    valid = [a for a in ('left', 'right') if all(
        translate(e['input'].split(), grammar, associativity=a) == e['output'].split() for e in examples)]
    if not valid or any(translate(words, grammar, associativity=a) != gold.split() for a in valid):
        raise ValueError('MiniSCAN grammar does not reproduce source answers')
    pool = {gold: None}
    variants = [dict(repeat=n) for n in (1, 2, 4)]
    variants += [dict(sandwich=s) for s in ('ab', 'ba', 'abb', 'bab')]
    variants += [dict(reverse=False)]
    for kw in variants:
        value = ' '.join(translate(words, grammar, associativity=valid[0], **kw))
        if value != gold: pool.setdefault(value, None)
    for a, b in itertools.combinations(grammar[0], 2):
        changed = deepcopy(grammar[0]); changed[a], changed[b] = changed[b], changed[a]
        value = ' '.join(translate(words, (changed, *grammar[1:]), associativity=valid[0]))
        if value != gold: pool.setdefault(value, None)
    wrong = sorted((x for x in pool if x != gold), key=lambda x: digest([VERSION, case['id'], x]))[:3]
    if len(wrong) != 3: raise ValueError('Missing historical distractors')
    wrong.insert(position, gold)
    return {chr(65+i): text for i, text in enumerate(wrong)}


def reconstruct_one(m, row, sub):
    sid = m['dataset']
    case = {k:m[k] for k in ('id','base_id','group_id','ability','dataset','family','source_split',
                             'input_hash','format_status','positive_label','positive_definition')}
    state = ''; question = ''; choices = {}; gold = None
    if sid == 'ag_news':
        state = row['text']; question = 'Which news topic best describes this article?'
        choices = {'0':'World','1':'Sports','2':'Business','3':'Science/Technology'}; gold = str(row['label'])
    elif sid == 'sst2':
        state = row['sentence']; question = 'What sentiment does this text express?'
        choices = {'0':'Negative','1':'Positive'}; gold = str(row['label'])
    elif sid == 'trec':
        label, state = row.split(' ', 1); question = 'What type of answer does this question request?'
        choices = {'ABBR':'Abbreviation','DESC':'Description','ENTY':'Entity','HUM':'Person or group',
                   'LOC':'Location','NUM':'Number or quantity'}; gold = label.split(':')[0]
    elif sid == 'newton':
        state = row.get('context', ''); question = row['question']
        if 'result_majority' in row:
            choices = {str(k):row[f'option_{k}'] for k in range(1,4)}
            gold = str(int(float(row['result_majority'])))
        else:
            choices = {str(k):row[f'choice_{k}'] for k in range(1,5) if row.get(f'choice_{k}') not in {'','N/A'}}
            gold = next((k for k,v in choices.items() if v == row['gt']), None)
    elif sid == 'fantom':
        item = row['beliefQAs'][int(sub)]
        state = row['full_context']; question = item['question']; gold = m['gold_choice']
        choices = {k:item['correct_answer'] if k == gold else item['wrong_answer'] for k in ('A','B')}
    elif sid == 'proofwriter':
        item = row['questions'][sub]; state = row['theory']; question = item['question']
        choices = {'true':'Entailed by the supplied facts and rules',
                   'false':'Contradicted by the supplied facts and rules','unknown':'Neither established nor contradicted'}
        gold = {True:'true',False:'false','Unknown':'unknown'}[item['answer']]
    elif sid == 'miniscan':
        item = row['test'][int(sub)]; state = json.dumps(row['train'], ensure_ascii=False)
        question = PREFIX + item['input']; gold = m['gold_choice']
        case.update(state=state, question=question)
        choices = miniscan_choices(case, item['output'], ord(gold)-65)
    else:
        raise ValueError('Unsupported source')
    case.update(state=state, question=question, choices=choices, gold=gold)
    if (baseline.input_hash(case) != m['input_hash'] or gold != m['gold_choice']
            or list(choices) != m['choice_keys']):
        raise ValueError('Recovered input, choice order or answer differs: ' + m['id'])
    return case


def recover(metadata, sources, source_root, datasets=DATASETS):
    if not datasets or set(datasets) - set(DATASETS):
        raise ValueError('Select supported datasets')
    needed = required_files(metadata, sources, datasets)
    paths = {(s['dataset'],s['path']):source_file(Path(source_root)/s['dataset'],s['path'],s['sha256']) for s in needed}
    cache = {}; results = []
    for m in metadata:
        if m['dataset'] in datasets:
            row, sub = native_record(m, cache, paths)
            results.append(reconstruct_one(m, row, sub))
    if len({r['id'] for r in results}) != len(results) or not results:
        raise ValueError('Duplicate or missing recovery inventory')
    return results, needed


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-root', type=Path, help='Directory containing dataset-named folders with original source files')
    parser.add_argument('--datasets', nargs='+', choices=DATASETS, default=list(DATASETS))
    parser.add_argument('--list-files', action='store_true', help='List required original URLs, paths and checksums without obtaining data')
    parser.add_argument('--output', type=Path, help='Recovery JSONL path inside .local/; defaults to .local/withheld.questions.jsonl')
    args = parser.parse_args()
    metadata = baseline.read_jsonl(ROOT/'data/question_manifest.jsonl')
    sources = json.loads((ROOT/'data/sources.json').read_text())
    if args.list_files:
        print(json.dumps(required_files(metadata,sources,args.datasets),indent=2)); return
    if args.source_root is None:
        parser.error('Supply independently obtained source files with --source-root, or use --list-files')
    rows, files = recover(metadata,sources,args.source_root,args.datasets)
    local = ROOT/'.local'; local.mkdir(mode=0o700,exist_ok=True)
    output = args.output.resolve() if args.output else local/'withheld.questions.jsonl'
    if not output.resolve().is_relative_to(local.resolve()):
        parser.error('Save recovered question text under .local/ so it stays out of Git')
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows))
    receipt = output.with_suffix('.recovery.json') if args.output else local/'withheld.recovery.json'
    receipt.write_text(json.dumps(dict(
        questions=len(rows),datasets=args.datasets,source_files_sha256={
            s['dataset']+'/'+s['path']:s['sha256'] for s in files},
        authorization='Source files supplied by the reader; reconstruction is not a grant of permission.',
        verification='All recovered input hashes, answer keys and choice orders match the frozen manifest.'),indent=2)+'\n')
    print(f'Recovered and verified {len(rows)} exact inputs in {output.relative_to(ROOT)}.')
    print('Original source terms still apply. No downloads, model calls or public data changes were made.')


if __name__ == '__main__':main()
