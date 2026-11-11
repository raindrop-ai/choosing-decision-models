"""Test the recovery safeguards with synthetic text only, never held PIQA prompts."""
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import unittest

import baseline

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('recover_piqa', ROOT/'tools/recover_piqa.py')
recovery = importlib.util.module_from_spec(spec)
spec.loader.exec_module(recovery)


class RecoveryTests(unittest.TestCase):
    def fixture(self):
        source = dict(goal='Synthetic fixture: choose the first label.', sol1='first', sol2='second')
        case = dict(state='', question=source['goal'], choices={'0':'first', '1':'second'})
        metadata = [dict(id=f'piqa/fixture-{i}',base_id=f'piqa/fixture-{i}',group_id=f'fixture-{i}',
            ability='fixture',dataset='piqa',family='fixture',source_split='fixture',
            format_status='native_choices',positive_label=None,positive_definition=None,
            source_locator=dict(path='piqa/data/train.jsonl',record=str(i)),
            input_hash=baseline.input_hash(case),gold_choice='0',choice_keys=['0','1']) for i in range(30)]
        files={'piqa/data/train.jsonl':('\n'.join(json.dumps(source) for _ in range(30))+'\n').encode(),
               'piqa/data/train-labels.lst':('0\n'*30).encode()}
        return metadata, files

    def test_complete_exact_recovery_without_network(self):
        metadata, files=self.fixture()
        result=recovery.reconstruct(metadata,files)
        self.assertEqual(len(result),30)
        self.assertEqual([r['id'] for r in result],[m['id'] for m in metadata])
        self.assertTrue(all(baseline.input_hash(r)==r['input_hash'] for r in result))

    def test_changed_source_text_or_labels_rejected(self):
        metadata, files=self.fixture()
        for altered in [dict(files,**{'piqa/data/train.jsonl':files['piqa/data/train.jsonl'].replace(b'first',b'changed')}),
                        dict(files,**{'piqa/data/train-labels.lst':b'1\n'*30})]:
            with self.assertRaisesRegex(ValueError,'differs'):
                recovery.reconstruct(metadata,altered)

    def test_acceptance_is_required_before_any_source_fetch(self):
        result=subprocess.run([sys.executable,'-B',str(ROOT/'tools/recover_piqa.py')],capture_output=True,text=True)
        self.assertEqual(result.returncode,2)
        self.assertIn('No data was obtained',result.stderr)
        self.assertIn('only if you accept',result.stderr)


if __name__=='__main__':unittest.main()
