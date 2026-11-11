"""Prepare all-model staging or a native inference job offline."""
import argparse
import json
from pathlib import Path

from request_specs import ROOT, load_cases, read_case_ids, worker_job
from baseline import read_jsonl


def main():
    models = json.loads((ROOT / "configs/models.json").read_text())
    sources = json.loads((ROOT / "configs/worker_sources.json").read_text())
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stage-all", action="store_true")
    parser.add_argument("--model", choices=list(sources))
    selection = parser.add_mutually_exclusive_group()
    selection.add_argument("--case")
    selection.add_argument("--all", action="store_true")
    selection.add_argument("--cases-file", type=Path)
    parser.add_argument("--local-questions", type=Path)
    parser.add_argument("--stage-result", type=Path)
    parser.add_argument("--device", type=Path)
    parser.add_argument("--comparison-group", default="baseline-reproduction")
    args = parser.parse_args()
    if args.stage_all:
        if args.model or args.case or args.all or args.cases_file or args.stage_result or args.device:
            parser.error("--stage-all only prepares the download specification")
        job = {"sources": sources}
    else:
        if not args.model or not args.stage_result or not (args.case or args.all or args.cases_file):
            parser.error("Choose --model, --stage-result and --case, --all or --cases-file")
        stage = json.loads(args.stage_result.read_text())
        if args.model not in stage.get("models", {}):
            parser.error("This model is not in the staging result; stage it first or use --stage-all")
        if not isinstance(stage.get("manifest_sha256"), str) or len(stage["manifest_sha256"]) != 64:
            parser.error("The staging result must contain its manifest SHA-256 hash")
        if stage["models"][args.model]["revision"] != sources[args.model]["revision"]:
            parser.error("Staged model revision does not match the configuration")
        ids = ([args.case] if args.case else read_case_ids(args.cases_file) if args.cases_file
               else sorted(q["id"] for q in read_jsonl(ROOT / "data/question_manifest.jsonl")))
        cases = load_cases(ids, args.local_questions)
        variant_path = ROOT / 'data/variants/manifest.jsonl'
        if variant_path.exists():
            variant_info = {q['id']:q for q in read_jsonl(variant_path)}
            unsupported = [cid for cid in ids if cid in variant_info and args.model not in variant_info[cid]['supported_models']]
            if unsupported:
                parser.error('Selected variants exceed the recorded model input limits; use variants.py inputs --model ' + args.model)
        job = worker_job(args.model, models[args.model]["configuration"], cases, stage["manifest_sha256"])
        if args.device:
            job.update(expected_physical_gpu=json.loads(args.device.read_text())["identity"],
                       comparison_group=args.comparison_group)
    print(json.dumps(job, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
