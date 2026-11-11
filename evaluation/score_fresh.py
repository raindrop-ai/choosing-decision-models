"""Score fresh API JSONL or a native worker receipt without changing saved results."""
import argparse
from collections import Counter
import csv
import json
from pathlib import Path

from request_specs import ROOT
from baseline import ratio, read_jsonl


def score(records, manifest, expected_ids):
    questions = {q["id"]: q for q in manifest}
    expected = set(expected_ids)
    seen = set()
    counts = Counter()
    binary = Counter()
    capabilities = {q["ability"]: Counter() for q in manifest if q["id"] in expected}
    for cid in expected:
        capabilities[questions[cid]["ability"]]["selected"] += 1
    for row in records:
        cid = row["case_id"]
        if cid not in expected or cid in seen:
            raise ValueError("Unexpected or duplicate question ID")
        seen.add(cid)
        q = questions[cid]
        if row.get("input_hash", q["input_hash"]) != q["input_hash"]:
            raise ValueError("Input fingerprint mismatch")
        status = row["status"]
        if status not in {"ok", "refusal", "error", "context_limit", "not_run", "unknown", "unknown_prior_attempt", "not_supported"}:
            raise ValueError("Unknown result status")
        counts[status] += 1
        if status != "ok":
            if row.get("prediction") is not None:
                raise ValueError("An unanswered result must not contain a prediction")
            continue
        if row.get("prediction") not in q["choice_keys"]:
            raise ValueError("Unknown answer key")
        counts["correct"] += row["prediction"] == q["gold_choice"]
        capabilities[q["ability"]]["answered"] += 1
        capabilities[q["ability"]]["correct"] += row["prediction"] == q["gold_choice"]
        if q.get("positive_label") is not None and len(q["choice_keys"]) == 2:
            positive = q["gold_choice"] == q["positive_label"]
            called = row["prediction"] == q["positive_label"]
            binary["tp" if positive and called else "fn" if positive else "fp" if called else "tn"] += 1
    return {"selected": len(expected), "recorded": len(seen), "missing": len(expected - seen),
            "answered": counts["ok"], "correct": counts["correct"],
            "accuracy": ratio(counts["correct"], counts["ok"]), "coverage": ratio(counts["ok"], len(expected)),
            "statuses": {k: v for k, v in counts.items() if k != "correct"},
            "capabilities": {name: {"selected": c["selected"], "answered": c["answered"], "correct": c["correct"],
                "accuracy": ratio(c["correct"], c["answered"]), "coverage": ratio(c["answered"], c["selected"])}
                for name, c in capabilities.items()},
            "binary": {"selected": sum(questions[cid].get("positive_label") is not None
                and len(questions[cid]["choice_keys"]) == 2 for cid in expected),
            "answered": sum(binary.values()), **{k: binary[k] for k in ("tp", "fp", "fn", "tn")},
            "precision": ratio(binary["tp"], binary["tp"] + binary["fp"]),
            "recall": ratio(binary["tp"], binary["tp"] + binary["fn"])}}


def compare(records, saved, manifest, expected_ids):
    """Compare the same selected questions; report answer and coverage changes separately."""
    current = {r["case_id"]: r for r in records}
    previous = {r["case_id"]: r for r in saved}
    questions = {q["id"]: q for q in manifest}
    counts = Counter()
    changes = []
    for cid in expected_ids:
        old = previous[cid]
        new = current.get(cid, {"status": "missing"})
        old_ok, new_ok = old["status"] == "ok", new["status"] == "ok"
        old_correct = old_ok and old["prediction"] == questions[cid]["gold_choice"]
        new_correct = new_ok and new["prediction"] == questions[cid]["gold_choice"]
        counts["answered_in_both"] += old_ok and new_ok
        if old_ok and new_ok:
            counts["changed_answers"] += old["prediction"] != new["prediction"]
            counts["correct_to_wrong"] += old_correct and not new_correct
            counts["wrong_to_correct"] += not old_correct and new_correct
        counts["newly_unanswered"] += old_ok and not new_ok
        counts["newly_answered"] += not old_ok and new_ok
        if (old["status"], old.get("prediction")) != (new["status"], new.get("prediction")):
            changes.append(dict(case_id=cid, saved_status=old["status"], saved_prediction=old.get("prediction"),
                fresh_status=new["status"], fresh_prediction=new.get("prediction"),
                reference_answer=questions[cid]["gold_choice"]))
    return {key: counts[key] for key in ("answered_in_both", "changed_answers", "correct_to_wrong",
            "wrong_to_correct", "newly_unanswered", "newly_answered")}, changes


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--job", type=Path, required=True, help="API run.json or native inference-job JSON")
    parser.add_argument("--output-dir", type=Path, help="New directory for report.json and answer_changes.csv")
    parser.add_argument("--compare-to", help="Recorded baseline model alias to compare with a custom model")
    args = parser.parse_args()
    job = json.loads(args.job.read_text())
    expected = job.get("case_ids") or [c["id"] for c in job["cases"]]
    manifest = read_jsonl(ROOT / "data/question_manifest.jsonl")
    variant_manifest = ROOT / 'data/variants/manifest.jsonl'
    if variant_manifest.exists():
        manifest += read_jsonl(variant_manifest)
    hashes = {q["id"]: q["input_hash"] for q in manifest}
    if "cases" in job:
        from baseline import input_hash
        actual = {c["id"]: input_hash(c) for c in job["cases"]}
    else:
        actual = job["input_hashes"]
    if len(expected) != len(set(expected)) or any(actual[cid] != hashes[cid] for cid in expected):
        raise ValueError("Job inputs do not match the baseline")
    if args.input.suffix == ".jsonl":
        records = read_jsonl(args.input)
        if any(row.get("model") != job["model"] for row in records):
            raise ValueError("API outputs belong to another model")
    else:
        records = json.loads(args.input.read_text())["records"]
        if any(row.get("requested_model") != job["config"]["model_id"]
               or row.get("model_revision") != job["config"]["revision"] for row in records):
            raise ValueError("GPU outputs belong to another model or checkpoint")
    model = job.get("model", job.get("model_name"))
    models = json.loads((ROOT / "configs/models.json").read_text())
    reference = args.compare_to or job.get("configuration", {}).get("comparison_model") or (model if model in models else None)
    if reference and reference not in models:
        raise ValueError("Unknown comparison model")
    if model not in models and not job.get("configuration", {}).get("endpoint"):
        raise ValueError("Unknown model without a recorded custom connection")
    report = score(records, manifest, expected)
    selected = set(expected)
    saved = [r for r in read_jsonl(ROOT / "results/baseline_predictions.jsonl")
             if r["model"] == reference and r["case_id"] in selected]
    if reference and selected - {q['id'] for q in read_jsonl(ROOT/'data/question_manifest.jsonl')}:
        path = ROOT/f'results/variants/{reference}.jsonl'
        if not path.exists():
            raise ValueError('No variant results were recorded for this comparison model')
        saved += [r for r in read_jsonl(path) if r['case_id'] in selected]
    report["model"] = model
    report["comparison_model"] = reference
    report["saved_baseline"] = score(saved, manifest, expected) if reference else None
    report["comparison"], changes = compare(records, saved, manifest, expected) if reference else (None, [])
    if args.output_dir:
        args.output_dir.mkdir(parents=True, exist_ok=False)
        (args.output_dir / "report.json").write_text(json.dumps(report, indent=2, allow_nan=False) + "\n", encoding="utf-8")
        if reference:
            with (args.output_dir / "answer_changes.csv").open("w", encoding="utf-8", newline="") as stream:
                writer = csv.DictWriter(stream, fieldnames=["case_id", "saved_status", "saved_prediction", "fresh_status",
                                                           "fresh_prediction", "reference_answer"])
                writer.writeheader()
                writer.writerows(changes)
    print(json.dumps(report, indent=2, allow_nan=False))


if __name__ == "__main__":
    main()
