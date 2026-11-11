"""Verify and summarize the saved baseline. Standard library only; no network calls."""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import csv
from decimal import Decimal
import hashlib
import json
import math
from pathlib import Path
import statistics

ROOT = Path(__file__).resolve().parent


def read_jsonl(path):
    with Path(path).open(encoding="utf-8") as stream:
        return [json.loads(line) for line in stream if line.strip()]


def input_hash(case):
    value = {"state": case["state"], "question": case["question"],
             "choices": list(case["choices"].items())}
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def ratio(numerator, denominator):
    return numerator / denominator if denominator else None


def finite_number(value):
    return isinstance(value, (float, int)) and not isinstance(value, bool) and math.isfinite(value)


def percentile(values, p, method="nearest_rank"):
    """Use the percentile convention documented for the saved run."""
    if method not in {"nearest_rank", "linear"}:
        raise ValueError("Unknown percentile method")
    values = sorted(values)
    if not values:
        return None
    if method == "nearest_rank":
        return values[max(0, math.ceil(p * len(values)) - 1)]
    index = (len(values) - 1) * p
    lower = int(index)
    return values[lower] + (values[min(lower + 1, len(values) - 1)] - values[lower]) * (index - lower)


def validate(questions, predictions, model_ids):
    """Fail on missing/duplicate records, rather than silently changing denominators."""
    by_id = {q["id"]: q for q in questions}
    if len(by_id) != len(questions) or len(questions) != 1005:
        raise ValueError("Expected 1,005 unique baseline questions")
    if len(model_ids) != 13 or len(set(model_ids)) != 13:
        raise ValueError("Expected 13 unique baseline models")
    counts = Counter(q["ability"] for q in questions)
    if len(counts) != 15 or set(counts.values()) != {67}:
        raise ValueError("Expected 67 questions in each of 15 capability areas")
    for q in questions:
        keys = q["choice_keys"]
        if len(keys) < 2 or len(keys) != len(set(keys)) or q["gold_choice"] not in keys:
            raise ValueError("Invalid question choices: " + q["id"])
        if q.get("positive_label") is not None and (len(keys) != 2 or q["positive_label"] not in keys):
            raise ValueError("Invalid binary positive label: " + q["id"])
    seen = set()
    for r in predictions:
        key = (r["model"], r["case_id"])
        if key in seen or r["model"] not in model_ids or r["case_id"] not in by_id:
            raise ValueError("Duplicate or unknown model/question result")
        seen.add(key)
        q = by_id[r["case_id"]]
        if r["input_hash"] != q["input_hash"]:
            raise ValueError("Prediction is for a different input")
        if r["status"] not in {"ok", "refusal", "error"}:
            raise ValueError("Unrecognized outcome status")
        if r["status"] == "ok" and r.get("prediction") not in q["choice_keys"]:
            raise ValueError("Successful prediction is not an answer choice")
        if r["status"] != "ok" and r.get("prediction") is not None:
            raise ValueError("Failed/refused outcomes cannot be counted as answers")
        if "timing_included" in r and not isinstance(r["timing_included"], bool):
            raise ValueError("timing_included must be boolean")
        probabilities = r.get("probabilities")
        if probabilities is not None:
            if set(probabilities) != set(q["choice_keys"]):
                raise ValueError("Incomplete probability vector")
            if any(not finite_number(v) or not 0 <= v <= 1 for v in probabilities.values()):
                raise ValueError("Invalid probability")
            if abs(sum(probabilities.values()) - 1) > .002:
                raise ValueError("Probabilities do not sum to one")
        for field in ("latency_ms", "billed_cost_usd"):
            if r.get(field) is not None and (not finite_number(r[field]) or r[field] < 0):
                raise ValueError("Invalid " + field)
    if len(seen) != 1005 * 13:
        raise ValueError("Missing outcomes: every question/model needs an explicit record")
    return by_id


def summarize(questions, predictions, models):
    model_ids = list(models)
    by_id = validate(questions, predictions, model_ids)
    grouped = defaultdict(list)
    for r in predictions:
        grouped[r["model"]].append(r)
    overall, capabilities, binary, operating = [], [], [], []
    abilities = list(dict.fromkeys(q["ability"] for q in questions))
    for model in model_ids:
        rows = grouped[model]
        answered = [r for r in rows if r["status"] == "ok"]
        correct = sum(r["prediction"] == by_id[r["case_id"]]["gold_choice"] for r in answered)
        overall.append(dict(model=model, selected=len(rows), answered=len(answered), correct=correct,
                            accuracy=ratio(correct, len(answered)), coverage=ratio(len(answered), len(rows)),
                            errors=sum(r["status"] == "error" for r in rows),
                            refusals=sum(r["status"] == "refusal" for r in rows)))
        for ability in abilities:
            selected = [r for r in rows if by_id[r["case_id"]]["ability"] == ability]
            valid = [r for r in selected if r["status"] == "ok"]
            n = sum(r["prediction"] == by_id[r["case_id"]]["gold_choice"] for r in valid)
            capabilities.append(dict(model=model, ability=ability, selected=len(selected),
                                     answered=len(valid), correct=n, accuracy=ratio(n, len(valid)),
                                     coverage=ratio(len(valid), len(selected))))
        eligible = [r for r in rows if len(by_id[r["case_id"]]["choice_keys"]) == 2
                    and by_id[r["case_id"]].get("positive_label") is not None]
        counts = dict(tp=0, fp=0, fn=0, tn=0)
        for r in eligible:
            if r["status"] != "ok":
                continue
            q = by_id[r["case_id"]]
            positive, called = q["gold_choice"] == q["positive_label"], r["prediction"] == q["positive_label"]
            key = "tp" if positive and called else "fn" if positive else "fp" if called else "tn"
            counts[key] += 1
        binary.append(dict(model=model, selected=len(eligible), answered=sum(counts.values()), **counts,
                           precision=ratio(counts["tp"], counts["tp"] + counts["fp"]),
                           recall=ratio(counts["tp"], counts["tp"] + counts["fn"])))
        times = sorted(r["latency_ms"] for r in answered if r.get("latency_ms") is not None and r.get("timing_included", True))
        priced = [r for r in rows if r.get("billed_cost_usd") is not None]
        total = sum((Decimal(str(r["billed_cost_usd"])) for r in priced), Decimal(0))
        info = models[model]
        operating.append(dict(model=model, serving=info["serving"], gpu=info.get("gpu"),
                              timed=len(times), median_ms=statistics.median(times) if times else None,
                              p95_ms=percentile(times, .95, info.get("timing_percentile_method", "nearest_rank")),
                              priced_requests=len(priced), unknown_cost_requests=len(rows)-len(priced) if info["serving"] == "api" else None,
                              known_api_cost_usd=float(total) if priced else None,
                              api_cost_per_1000_requests=float(total / len(priced) * 1000) if priced else None))
    return dict(overall=overall, capabilities=capabilities, native_binary=binary, cost_timing=operating)


def verify_reference(summary, expected):
    """Compare to the reference tables for the current result set."""
    for table, rows in expected.items():
        actual = summary[table]
        key = (lambda r: (r["model"], r["ability"])) if table == "capabilities" else (lambda r: r["model"])
        lookup = {key(r): r for r in actual}
        if len(actual) != len(rows):
            raise ValueError("Reference table length differs: " + table)
        for row in rows:
            got = lookup[key(row)]
            for field, wanted in row.items():
                value = got[field]
                same = math.isclose(value, wanted, rel_tol=1e-12, abs_tol=1e-12) if isinstance(wanted, float) else value == wanted
                if not same:
                    raise ValueError(f"Reference mismatch: {table} {key(row)} {field}")


def load_bundle(root=ROOT, *, check_files=True):
    root = Path(root)
    if check_files:
        manifest = json.loads((root / "MANIFEST.json").read_text())
        for name, wanted in manifest["sha256"].items():
            path = (root / name).resolve()
            if root.resolve() not in path.parents or sha256(path) != wanted:
                raise ValueError("Bundle checksum mismatch: " + name)
    questions = read_jsonl(root / "data/question_manifest.jsonl")
    predictions = read_jsonl(root / "results/baseline_predictions.jsonl")
    models = json.loads((root / "configs/models.json").read_text())
    by_id = validate(questions, predictions, list(models))
    for q in read_jsonl(root / "data/questions.jsonl"):
        original = by_id[q["id"]]
        if not original["text_included"] or input_hash(q) != original["input_hash"]:
            raise ValueError("Released question changed or lacks sharing approval")
        if q["gold"] != original["gold_choice"] or list(q["choices"]) != original["choice_keys"]:
            raise ValueError("Released answer key/order differs")
    full = read_jsonl(root / "data/questions.jsonl")
    if len({q["id"] for q in full}) != len(full) or len(full) != sum(q["text_included"] for q in questions):
        raise ValueError("Released question inventory differs")
    return questions, predictions, models


def write_summaries(summary, directory):
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    for name, rows in summary.items():
        with (directory / (name + ".csv")).open("w", newline="", encoding="utf-8") as stream:
            writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["verify", "summarize", "inspect"])
    parser.add_argument("--case", dest="case_id")
    parser.add_argument("--local-questions", type=Path, help="Recovered input file for inspect")
    parser.add_argument("--output", type=Path, default=ROOT / ".local/summaries")
    args = parser.parse_args()
    questions, predictions, models = load_bundle()
    if args.command == "inspect":
        if args.case_id is None:
            parser.error("inspect requires --case")
        q = next((q for q in questions if q["id"] == args.case_id), None)
        if q is None:
            parser.error("unknown question ID")
        path = args.local_questions or ROOT / "data/questions.jsonl"
        matches = [r for r in read_jsonl(path) if r["id"] == args.case_id]
        if len(matches) > 1 or (args.local_questions and not matches):
            parser.error("The input file must contain the selected question exactly once")
        full = matches[0] if matches else None
        if full is not None and (input_hash(full) != q["input_hash"] or full["gold"] != q["gold_choice"]):
            parser.error("Question text, reference answer or choice order differs from the baseline")
        print(json.dumps(dict(metadata=q, question=full,
                              predictions=[r for r in predictions if r["case_id"] == args.case_id]),
                         ensure_ascii=False, indent=2))
        return
    if args.local_questions:
        parser.error("--local-questions is only used with inspect")
    summary = summarize(questions, predictions, models)
    verify_reference(summary, json.loads((ROOT / "reference/expected_metrics.json").read_text()))
    if args.command == "summarize":
        write_summaries(summary, args.output)
        print("Wrote baseline CSV summaries to " + str(args.output))
    else:
        print(f"Verified {len(questions):,} questions, {len(predictions):,} outcomes, "
              f"{len(models)} models, released question hashes, and current reference metrics.")


if __name__ == "__main__":
    main()
