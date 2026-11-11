"""One fresh model process on an already-held GPU; native inference unchanged."""
import contextlib,json,shutil,sys
from pathlib import Path
from decision_lab import common_native as native_worker

def identity(observation):
 return {k:observation[k] for k in ('name','uuid','total_memory_bytes','compute_capability','multiprocessor_count')}
def verify_initial(observation):
 name=observation['name'].lower()
 if ('a100' not in name or 'mig' in name or observation['total_memory_bytes']<75*1024**3 or observation['compute_capability']!=[8,0] or observation['multiprocessor_count']!=108 or not observation.get('uuid') or observation['uuid']=='unavailable'):
  raise RuntimeError('Full A10080GB hardware identity not established: '+json.dumps(observation))
 return identity(observation)
def verify_same(observation,expected):
 actual=verify_initial(observation)
 if actual!=expected:raise RuntimeError('GPU changed within common-hardware experiment; stop without replacement: '+json.dumps({'expected':expected,'observed':actual}))
 return actual

def infer(job):
 import torch
 expected=job['expected_physical_gpu'];assert torch.cuda.device_count()==1
 # Model runtimes stay separate, and the native hardcoded scratch folder is isolated.
 scratch=Path('/tmp/laya-checkpoint')
 if scratch.is_symlink():scratch.unlink()
 elif scratch.exists():shutil.rmtree(scratch)
 old_policy=native_worker.execution_hardware_policy
 def common_policy(observation,_expected_name,_alternate):
  verify_same(observation,expected)
  return 'single-physical-A10080GB','common_physical_GPU_comparison',True
 native_worker.execution_hardware_policy=common_policy
 try:result=native_worker.infer(job)
 finally:native_worker.execution_hardware_policy=old_policy
 after=native_worker.observe_hardware(torch);verify_same(after,expected)
 result.update(comparison_group=job['comparison_group'],physical_GPU_identity=expected,physical_GPU_after=identity(after))
 return result

if __name__=='__main__':
 mode,request,output=sys.argv[1:];job=json.loads(Path(request).read_text())
 with contextlib.redirect_stdout(sys.stderr):
  if mode=='probe':
   import torch
   assert torch.cuda.device_count()==1
   obs=native_worker.observe_hardware(torch);result={'observation':obs,'identity':verify_initial(obs)}
  elif mode=='infer':result=infer(job)
  else:raise ValueError('Only probe/infer are supported')
 Path(output).write_text(json.dumps(result,allow_nan=False))
