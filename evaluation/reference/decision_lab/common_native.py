"""Native adapters unchanged; consistent timing and durable per-case events. No gold."""
import contextlib, importlib.metadata, json, os, re, shutil, subprocess, sys, time
from pathlib import Path
import decision_lab.worker_entry as native


def event(record):
    with Path('/tmp/case-progress.jsonl').open('a') as f:
        f.write(json.dumps(record, allow_nan=False)+'\n'); f.flush(); os.fsync(f.fileno())


def device_family(name):
    # Only spelling/punctuation/order variants of the SAME explicit PCIe80GB SKU.
    value=re.sub('[^a-z0-9]','',str(name).lower()).removeprefix('nvidia')
    return 'A100-80GB-PCIe' if value in ('a10080gbpcie','a100pcie80gb') else None


def execution_hardware_policy(observation,expected,allow_variant_only):
    if device_family(observation['name']) is not None:
        family=verify_hardware(observation,expected)
        return family,'common_gpu_originals_and_variant_study',True
    value=re.sub('[^a-z0-9]','',str(observation['name']).lower()).removeprefix('nvidia')
    if (allow_variant_only and value in ('a100sxm480gb','a10080gbsxm4','a10080gbsxm')
        and observation['total_memory_bytes']>=75*1024**3
        and observation['compute_capability']==[8,0]):
        return 'A100-80GB-SXM4','variant_study_with_fresh_baselines_only',False
    raise RuntimeError('GPU cannot be used for authorized execution: '+json.dumps({'expected_for_timing':expected,'observed':observation},sort_keys=True))


def verify_hardware(observation,expected):
    family=device_family(observation['name'])
    if (family is None or family!=device_family(expected)
        or observation['total_memory_bytes']<75*1024**3
        or observation['compute_capability']!=[8,0]):
        raise RuntimeError('Common GPU hardware mismatch before model load: '+json.dumps({'expected':expected,'observed':observation},sort_keys=True))
    return family


def observe_hardware(torch):
    props=torch.cuda.get_device_properties(0)
    data={'name':torch.cuda.get_device_name(),'total_memory_bytes':int(props.total_memory),
          'compute_capability':[int(props.major),int(props.minor)],
          'multiprocessor_count':int(props.multi_processor_count),
          'uuid':str(getattr(props,'uuid','unavailable'))}
    try:
        diagnostic=subprocess.run(['nvidia-smi','--query-gpu=name,pci.device_id,memory.total,driver_version','--format=csv,noheader,nounits'],capture_output=True,text=True,timeout=10)
        data['nvidia_smi']={'exit_code':diagnostic.returncode,'stdout':diagnostic.stdout[:4000],'stderr':diagnostic.stderr[:1000]}
    except Exception as e:data['nvidia_smi']={'error_type':type(e).__name__}
    return data


def infer(job):
    import torch
    import random
    import numpy as np
    random.seed(0);np.random.seed(0);torch.manual_seed(0);torch.cuda.manual_seed_all(0);torch.set_num_threads(2)
    torch.backends.cuda.matmul.allow_tf32=False;torch.backends.cudnn.allow_tf32=False
    assert all('gold' not in c for c in job['cases'])
    root=Path('/models'); cfg=job['config']; name=job['model_name']
    manifest=root/'stage-manifest.json'
    assert native.checksum(manifest)==job['manifest_sha256']
    assert json.loads(manifest.read_text())['models'][name]['revision']==cfg['revision']
    observation=observe_hardware(torch)
    device=observation['name']
    expected_device=job.get('expected_gpu_device_name')
    event({'event':'hardware_observed','hardware':observation,'expected_gpu_device_name':expected_device})
    family,purpose,timing_eligible=execution_hardware_policy(observation,expected_device,job.get('allow_variant_only_alternate_gpu') is True)
    event({'event':'execution_hardware_policy','hardware_family':family,'execution_purpose':purpose,'original_timing_comparison_eligible':timing_eligible})
    start=time.perf_counter(); predict=native.load_predictor(cfg['kind'],native.safe_child(root,name),cfg)
    if hasattr(predict,'audit'):
        for case in job['cases']: predict.audit(case)
    torch.cuda.synchronize(); loading_ms=(time.perf_counter()-start)*1000
    event({'event':'ready','gpu':device,'model_load_ms':loading_ms})
    records=[]; failed=False
    for i,case in enumerate(job['cases']):
        row={'case_id':case['id'],'requested_model':cfg['model_id'],'model_revision':cfg['revision'],'hardware_family':family,'execution_purpose':purpose,'original_timing_comparison_eligible':timing_eligible}
        if failed:
            records.append({**row,'status':'not_run','reason':'earlier_worker_error'}); continue
        event({'event':'started','case_id':case['id']})
        torch.cuda.synchronize(); start=time.perf_counter()
        try:
            with torch.inference_mode(): values=native.probabilities(predict(case),case['choices'])
            row.update(status='ok',prediction=max(values,key=values.get),probabilities=values,probability_source='native_choice_distribution')
            if hasattr(predict,'input_fit'):row['input_fit']=predict.input_fit
        except native.ContextLimit as e:row.update(status='context_limit',reason=str(e))
        except Exception as e:row.update(status='error',reason=type(e).__name__,error_detail=str(e)[:500]);failed=True
        torch.cuda.synchronize();row['latency_ms']=(time.perf_counter()-start)*1000
        row['timing_class']='first_forward_with_kernel_startup' if i==0 else 'subsequent_forward'
        records.append(row);event({'event':'result','record':row})
    versions={p:importlib.metadata.version(p) for p in ('torch','transformers','huggingface-hub')}
    if shutil.which('cc'):versions['c_compiler']=subprocess.check_output(['cc','-dumpfullversion'],text=True).strip()
    return {'records':records,'model_load_ms':loading_ms,'gpu':device,'runtime_versions':versions,
            'hardware':observation,'hardware_family':family,'execution_purpose':purpose,'original_timing_comparison_eligible':timing_eligible,'peak_allocated_gpu_bytes':torch.cuda.max_memory_allocated(),'measurement_settings':{'seed':0,'torch_cpu_threads':torch.get_num_threads(),'matmul_allow_tf32':torch.backends.cuda.matmul.allow_tf32,'cudnn_allow_tf32':torch.backends.cudnn.allow_tf32,'batch_size':1}}


if __name__=='__main__':
    request,output=sys.argv[1:];job=json.loads(Path(request).read_text())
    with contextlib.redirect_stdout(sys.stderr):result=infer(job)
    Path(output).write_text(json.dumps(result,allow_nan=False))
