"""Offline checks of recovery, exact comparison membership and fresh-run scoring."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT));sys.path.insert(0,str(ROOT/'evaluation'))
import baseline,variant_data
from score_fresh import score


class VariantsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.groups=json.loads((ROOT/'data/variants/comparisons.json').read_text())['groups']
        cls.metadata=variant_data.metadata()
        cls.originals={q['id']:q for q in baseline.read_jsonl(ROOT/'data/question_manifest.jsonl')}
        cls.outcomes,cls.controls=variant_data.outcome_tables()

    def stats(self,factor,model):
        group=next(g for g in self.groups if g['factor']==factor and g['main'])
        return variant_data.group_stats(group,model,self.outcomes,self.controls,self.originals)

    def test_stable_accuracy_still_has_answer_changes(self):
        r=self.stats('presentation_order','clef-flash')[0]
        self.assertEqual((r['paired'],r['before_correct'],r['after_correct'],r['changed'],r['lost'],r['gained']),
                         (335,235,235,47,17,17))

    def test_three_positions_are_required(self):
        glide=self.stats('evidence_position','glide')[0]
        laya=self.stats('evidence_position','laya')[0]
        self.assertEqual((glide['paired'],glide['any_changed']),(944,57))
        self.assertEqual((laya['paired'],laya['any_changed']),(944,422))
        luna=self.stats('evidence_position','openai-decisions')[0]
        self.assertEqual(luna['paired'],917)
        self.assertEqual(luna['bases'],944)

    def test_assessment_uses_exact_controls(self):
        glide=self.stats('misleading_summary','glide')
        self.assertEqual([(r['before_correct'],r['after_correct']) for r in glide],[(978,880),(953,978),(953,880)])
        jev=self.stats('misleading_summary','jev')
        self.assertEqual([(r['before_correct'],r['after_correct']) for r in jev],[(946,816),(891,946),(891,816)])

    def test_recipe_reconstructs_order_and_rejects_changed_parent(self):
        base={'id':'test','state':'Alice has a ball.','question':'Who has the ball?','choices':{'A':'Alice','B':'Bob'},'gold':'A'}
        edited={**base,'id':'variant','question':'Please answer: Who has the ball?','choices':{'B':'Bob','A':'Alice'}}
        recipe={'id':'variant','original_id':'test','parent_input_hash':baseline.input_hash(base),'input_hash':baseline.input_hash(edited),
                'state':[{'field':'state','start':0,'end':len(base['state'])}],
                'question':['Please answer: ',{'field':'question','start':0,'end':len(base['question'])}],
                'choices':[['B',[{'field':'choices','choice':'B','start':0,'end':3}]],['A',[{'field':'choices','choice':'A','start':0,'end':5}]]]}
        actual=variant_data.apply_recipe(recipe,{'test':base})
        self.assertEqual(list(actual['choices']),['B','A'])
        self.assertEqual(baseline.input_hash(actual),baseline.input_hash(edited))
        with self.assertRaises(ValueError):variant_data.apply_recipe(recipe,{'test':{**base,'state':'Changed'}})

    def test_select_variants_and_score_saved_outputs_as_fresh(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp=Path(tmp);inputs=tmp/'inputs.jsonl'
            subprocess.run([sys.executable,'-B',str(ROOT/'variants.py'),'inputs','--model','jev','--original','bbh/639b88b1fe80634a7d66','--output',str(inputs)],check=True,capture_output=True)
            cases=baseline.read_jsonl(inputs);ids=[c['id'] for c in cases]
            self.assertGreater(len(cases),10)
            from request_specs import load_cases
            self.assertEqual(len(load_cases(ids,inputs)),len(ids))
            records=[self.outcomes['jev',cid] for cid in ids]
            path=tmp/'predictions.jsonl';path.write_text(''.join(json.dumps(r)+'\n' for r in records))
            job=tmp/'run.json';job.write_text(json.dumps({'model':'jev','case_ids':ids,'input_hashes':{c['id']:baseline.input_hash(c) for c in cases}}))
            result=subprocess.run([sys.executable,'-B',str(ROOT/'evaluation/score_fresh.py'),'--job',str(job),'--input',str(path)],check=True,capture_output=True,text=True)
            report=json.loads(result.stdout)
            self.assertEqual(report['selected'],len(ids));self.assertEqual(report['comparison']['changed_answers'],0)
            self.assertEqual(report['answered'],report['saved_baseline']['answered'])

    def test_fresh_comparisons_preserve_missing_coverage_and_validate_identity(self):
        from score_variants import calculate,read_run
        group=next(g for g in self.groups if g['factor']=='misleading_summary')
        family=group['families'][0];base=family['original_id']
        with tempfile.TemporaryDirectory() as folder:
            folder=Path(folder)
            jobs={}
            for phase,ids in [('originals',[base]),('variants',list(family['levels'].values()))]:
                metadata=self.originals if phase=='originals' else {m['id']:m for m in self.metadata}
                job={'model':'my-model','case_ids':ids,'input_hashes':{cid:metadata[cid]['input_hash'] for cid in ids}}
                outcomes=[{'model':'my-model','case_id':cid,'input_hash':metadata[cid]['input_hash'],
                           'status':'ok','prediction':metadata[cid]['gold_choice']} for cid in ids]
                (folder/(phase+'.json')).write_text(json.dumps(job))
                (folder/(phase+'.jsonl')).write_text(''.join(json.dumps(r)+'\n' for r in outcomes))
                jobs[phase]={'job':phase+'.json','output':phase+'.jsonl'}
            rows=calculate(jobs,folder)
            r=next(r for r in rows if r['factor']=='misleading_summary' and r['capability']=='all')
            self.assertEqual((r['paired'],r['bases'],r['unavailable']),(1,1004,1003))
            self.assertEqual((r['before_correct'],r['after_correct'],r['changed']),(1,1,0))
            with self.assertRaisesRegex(ValueError,'same model'):
                read_run(jobs['originals'],folder,list(self.originals.values()),'different-model')
            changed=json.loads((folder/'variants.json').read_text())
            changed['configuration']={'model_id':'different-provider-model'}
            (folder/'variants.json').write_text(json.dumps(changed))
            with self.assertRaisesRegex(ValueError,'same model connection'):
                calculate(jobs,folder)

    def test_unresolved_attempt_is_coverage_not_answer(self):
        q=self.metadata[0]
        r=score([{'case_id':q['id'],'status':'unknown_prior_attempt','prediction':None}],[q],[q['id']])
        self.assertEqual(r['answered'],0);self.assertIsNone(r['accuracy']);self.assertEqual(r['recorded'],1)


if __name__=='__main__':unittest.main()
