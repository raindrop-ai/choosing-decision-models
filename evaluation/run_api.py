"""Run one hosted model against selected baseline inputs; standard library only."""
from __future__ import annotations

import argparse
import getpass
import json
import math
import os
from pathlib import Path
import sys
import time
import urllib.error
import urllib.request

from request_specs import ROOT, api_spec, load_cases, read_case_ids
from baseline import input_hash, read_jsonl
from connections import auth_headers, load_connection


def parse_response(raw, case, cfg):
    if not isinstance(raw, dict):
        raise ValueError("Expected a JSON response object")
    gateway = (raw.get("provider_metadata", raw.get("providerMetadata", {})) or {}).get("gateway", {}) or {}
    routing = gateway.get("routing", {}) or {}
    allowed = {cfg["model_id"], cfg["model_id"].split("/", 1)[-1], *cfg.get("reported_model_aliases", [])}
    actual = routing.get("canonicalSlug") or routing.get("originalModelId")
    if raw.get("model") not in allowed or (actual and actual not in allowed) or gateway.get("decisionFallback"):
        raise ValueError("Unexpected or missing response model identity")
    if cfg["backend"] in {"gateway_llm", "openai_compatible"}:
        outputs = raw.get("choices", [])
        if len(outputs) != 1:
            raise ValueError("Expected exactly one completion")
        output = outputs[0]
        message = output["message"]
        if message.get("refusal") and message.get("content") in (None, ""):
            return {"status": "refusal"}
        if output.get("finish_reason") != "stop" or message.get("tool_calls") or message.get("refusal"):
            raise ValueError("Incomplete or unexpected completion")
        answer = json.loads(message["content"])
        if not isinstance(answer, dict) or set(answer) != {"answer"} or answer["answer"] not in case["choices"]:
            raise ValueError("Completion is not an allowed answer key")
        return {"status": "ok", "prediction": answer["answer"]}
    answers = raw.get("answers")
    answer = (answers[0] if isinstance(answers, list) and len(answers) == 1
              else answers.get("judgment") if isinstance(answers, dict) else None)
    if not isinstance(answer, dict):
        raise ValueError("Missing judgment answer")
    if answer.get("type") == "refusal":
        return {"status": "refusal"}
    if answer.get("type") != "choice":
        raise ValueError("Expected a choice answer")
    probs = answer.get("probabilities")
    if isinstance(probs, list):
        converted = {str(p["value"]): p["probability"] for p in probs}
        if len(converted) != len(probs):
            raise ValueError("Duplicate probability key")
        probs = converted
    if not isinstance(probs, dict) or set(probs) != set(case["choices"]):
        raise ValueError("Expected probabilities for every choice")
    if any(isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v) or not 0 <= v <= 1
           for v in probs.values()):
        raise ValueError("Invalid probability")
    total = sum(probs.values())
    if abs(total - 1) > .002:
        raise ValueError("Probabilities do not sum to one")
    probs = {k: v / total for k, v in probs.items()}
    prediction = str(answer.get("choice", max(probs, key=probs.get)))
    if prediction not in case["choices"]:
        raise ValueError("Unknown answer key")
    return {"status": "ok", "prediction": prediction, "probabilities": probs}


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise ValueError("Unexpected API redirect")


def run(model, cases, cfg, directory, key, opener=None):
    """Save each response before parsing it. No retries or automatic resumes."""
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=False)
    (directory / "raw").mkdir()
    (directory / "run.json").write_text(json.dumps({"model": model, "configuration": cfg,
        "case_ids": [c["id"] for c in cases], "input_hashes": {c["id"]: input_hash(c) for c in cases}}, indent=2) + "\n")
    opener = opener or urllib.request.build_opener(NoRedirect())
    failed = False
    with (directory / "predictions.jsonl").open("x") as stream:
        for index, case in enumerate(cases):
            spec = api_spec(case, cfg)
            headers = {**spec["headers"], "Content-Type": "application/json", **auth_headers(cfg, key)}
            request = urllib.request.Request(spec["url"], data=json.dumps(spec["body"], ensure_ascii=False).encode(),
                                             headers=headers, method="POST")
            row = {"model": model, "case_id": case["id"], "input_hash": input_hash(case)}
            start = time.perf_counter()
            try:
                with opener.open(request, timeout=600) as response:
                    payload = response.read()
                (directory / "raw" / f"{index:04d}.json").write_bytes(payload)
                raw = json.loads(payload)
                row.update(parse_response(raw, case, cfg), reported_model=raw.get("model"))
            except urllib.error.HTTPError as error:
                (directory / "raw" / f"{index:04d}.http-error.txt").write_bytes(error.read())
                row.update(status="error", reason=f"HTTP {error.code}")
            except (urllib.error.URLError, TimeoutError, OSError, ValueError, KeyError, TypeError) as error:
                row.update(status="error", reason=type(error).__name__)
            row["latency_ms"] = (time.perf_counter() - start) * 1000
            stream.write(json.dumps(row, allow_nan=False) + "\n")
            stream.flush()
            os.fsync(stream.fileno())
            print(f"{index + 1}/{len(cases)} {case['id']}: {row['status']}")
            if row["status"] == "error":
                failed = True
                break
    return 1 if failed else 0


def main():
    models = json.loads((ROOT / "configs/models.json").read_text())
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", required=True, help="Recorded model alias, or a new run name with --connection")
    parser.add_argument("--connection", type=Path, help="Provider endpoint, model ID and request format")
    selection = parser.add_mutually_exclusive_group(required=True)
    selection.add_argument("--case")
    selection.add_argument("--all", action="store_true", help="Send all 1,005 questions sequentially")
    selection.add_argument("--cases-file", type=Path, help="CSV, JSONL or text file selecting question IDs")
    parser.add_argument("--local-questions", type=Path)
    parser.add_argument("--output", type=Path, required=True, help="New directory; existing runs are not overwritten")
    args = parser.parse_args()
    if args.connection:
        if args.model in models:
            parser.error("Use a new run name with --connection, such as jev-direct or my-model")
        cfg = load_connection(args.connection)
        if cfg.get("comparison_model") and cfg["comparison_model"] not in models:
            parser.error("comparison_model must be one of the recorded model aliases")
    else:
        if args.model not in models or models[args.model]["serving"] != "api":
            parser.error("Choose a recorded API model, or supply --connection for another endpoint")
        cfg = models[args.model]["configuration"]
    ids = ([args.case] if args.case else read_case_ids(args.cases_file) if args.cases_file
           else sorted(q["id"] for q in read_jsonl(ROOT / "data/question_manifest.jsonl")))
    # Validate every selected input before any HTTP request.
    cases = load_cases(ids, args.local_questions)
    env_name = cfg.get("api_key_env", "AI_GATEWAY_API_KEY")
    key = os.environ.get(env_name)
    if cfg.get("auth") != "none":
        if not key and sys.stdin.isatty():
            key = getpass.getpass("API key: ")
        if not key:
            parser.error("Set " + env_name + " or run interactively to enter a key")
    return run(args.model, cases, cfg, args.output, key)


if __name__ == "__main__":
    sys.exit(main())
