"""Offline reconstruction and assembly safeguards, using synthetic source text only."""
from copy import deepcopy
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import tarfile
import tempfile
import unittest

import baseline

ROOT = Path(__file__).resolve().parents[1]

def module(name):
    spec=importlib.util.spec_from_file_location(name,ROOT/'tools'/(name+'.py'))
    obj=importlib.util.module_from_spec(spec);spec.loader.exec_module(obj);return obj

recover=module('recover_withheld')
assemble=module('assemble_inputs')


class InputRecoveryTests(unittest.TestCase):
    def test_changed_source_files_rejected_before_parsing(self):
        with tempfile.TemporaryDirectory() as folder:
            p=Path(folder)/'source.jsonl';p.write_bytes(b'original fixture')
            wanted=hashlib.sha256(p.read_bytes()).hexdigest()
            self.assertEqual(recover.source_file(folder,p.name,wanted),p)
            p.write_bytes(b'changed fixture')
            with self.assertRaisesRegex(ValueError,'checksum mismatch'):
                recover.source_file(folder,p.name,wanted)

    def test_archive_reader_does_not_extract_or_follow_links(self):
        with tempfile.TemporaryDirectory() as folder:
            p=Path(folder)/'fixture.tar.gz'
            with tarfile.open(p,'w:gz') as archive:
                data=b'{"fixture":true}';info=tarfile.TarInfo('fixture.json');info.size=len(data)
                archive.addfile(info,io.BytesIO(data))
                link=tarfile.TarInfo('link');link.type=tarfile.SYMTYPE;link.linkname='/private';archive.addfile(link)
            self.assertEqual(recover.read_source(p,'fixture.json'),data)
            self.assertFalse((Path(folder)/'fixture.json').exists())
            with self.assertRaisesRegex(ValueError,'Unexpected archive member'):
                recover.read_source(p,'link')
            with self.assertRaisesRegex(ValueError,'Unsafe archive member'):
                recover.read_source(p,'../fixture.json')

    def test_native_pair_choice_order_is_restored(self):
        case=dict(state='Synthetic conversation.',question='Synthetic belief question?',
                  choices={'A':'wrong','B':'right'})
        metadata=dict(id='fantom/fixture',base_id='fantom/fixture',group_id='fixture',ability='fixture',
            dataset='fantom',family='fixture',source_split='fixture',format_status='native_choices',
            positive_label=None,positive_definition=None,input_hash=baseline.input_hash(case),
            gold_choice='B',choice_keys=['A','B'])
        raw=dict(full_context=case['state'],beliefQAs=[dict(question=case['question'],correct_answer='right',wrong_answer='wrong')])
        result=recover.reconstruct_one(metadata,raw,'0')
        self.assertEqual(result['choices'],case['choices'])
        self.assertEqual(result['gold'],'B')
        metadata['input_hash']='changed'
        with self.assertRaisesRegex(ValueError,'differs'):
            recover.reconstruct_one(metadata,raw,'0')

    def test_missing_or_changed_fragments_stop_complete_assembly(self):
        case=dict(state='Synthetic evidence.',question='Choose first.',choices={'A':'first','B':'second'},gold='A')
        rows=[dict(case,id=f'fixture/{i}') for i in range(1005)]
        metadata=[dict(id=r['id'],input_hash=baseline.input_hash(r),gold_choice='A',choice_keys=['A','B']) for r in rows]
        result=assemble.assemble(metadata,[rows[:857],rows[857:887],rows[887:]])
        self.assertEqual([r['id'] for r in result],[m['id'] for m in metadata])
        with self.assertRaisesRegex(ValueError,'Missing 1'):
            assemble.assemble(metadata,[rows[:-1]])
        with self.assertRaisesRegex(ValueError,'Duplicate'):
            assemble.assemble(metadata,[rows,rows[:1]])
        changed=deepcopy(rows);changed[-1]['choices']={'B':'second','A':'first'}
        with self.assertRaisesRegex(ValueError,'differs'):
            assemble.assemble(metadata,[changed])

    def test_partial_assembly_still_validates_every_supplied_input(self):
        case=dict(state='Synthetic evidence.',question='Choose first.',choices={'A':'first','B':'second'},gold='A')
        rows=[dict(case,id=f'fixture/{i}') for i in range(1005)]
        metadata=[dict(id=r['id'],input_hash=baseline.input_hash(r),gold_choice='A',choice_keys=['A','B']) for r in rows]
        partial=assemble.assemble(metadata,[rows[:857]],require_complete=False)
        self.assertEqual(len(partial),857)
        with self.assertRaisesRegex(ValueError,'Missing 148'):
            assemble.assemble(metadata,[rows[:857]])
        changed=deepcopy(rows[:857]);changed[-1]['state']='Changed evidence.'
        with self.assertRaisesRegex(ValueError,'differs'):
            assemble.assemble(metadata,[changed],require_complete=False)


if __name__=='__main__':unittest.main()
