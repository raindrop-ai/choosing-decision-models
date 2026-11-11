"""Fresh-run setup and response handling, with HTTP and GPU execution mocked."""
import contextlib
from copy import deepcopy
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
import urllib.error

import baseline

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "evaluation"))
import request_specs
import run_api
import score_fresh
import connections


class Response(io.BytesIO):
    pass


class FakeOpener:
    def __init__(self, replies):
        self.replies = iter(replies)
        self.requests = []

    def open(self, request, timeout):
        self.requests.append(request)
        reply = next(self.replies)
        if isinstance(reply, Exception):
            raise reply
        return Response(json.dumps(reply).encode())


class FreshInferenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.case = request_specs.load_case("bbh/639b88b1fe80634a7d66")
        cls.models = json.loads((ROOT / "configs/models.json").read_text())
        cls.manifest = baseline.read_jsonl(ROOT / "data/question_manifest.jsonl")

    def decision(self, model="jev"):
        return {"model": self.models[model]["configuration"]["model_id"], "answers": {"judgment": {
            "type": "choice", "probabilities": {k: float(k == self.case["gold"]) for k in self.case["choices"]}}}}

    def test_both_decision_response_formats_and_native_choice(self):
        raw = self.decision()
        cfg = self.models["jev"]["configuration"]
        result = run_api.parse_response(raw, self.case, cfg)
        self.assertEqual(result["prediction"], self.case["gold"])
        raw["answers"] = [raw["answers"]["judgment"]]
        raw["answers"][0]["probabilities"] = [{"value": k, "probability": v}
            for k, v in raw["answers"][0]["probabilities"].items()]
        self.assertEqual(run_api.parse_response(raw, self.case, cfg), result)

    def test_wrong_model_fallback_and_incomplete_probabilities_rejected(self):
        cfg = self.models["jev"]["configuration"]
        for mutate in [lambda r: r.update(model="another-model"),
                       lambda r: r.update(provider_metadata={"gateway": {"decisionFallback": True}}),
                       lambda r: r["answers"]["judgment"]["probabilities"].pop(self.case["gold"])]:
            raw = self.decision()
            mutate(raw)
            with self.assertRaises(ValueError):
                run_api.parse_response(raw, self.case, cfg)

    def test_llm_refusal_truncation_and_answer_key_validation(self):
        cfg = self.models["astra"]["configuration"]
        raw = {"model": cfg["model_id"], "choices": [{"finish_reason": "stop", "message": {
            "content": json.dumps({"answer": self.case["gold"]})}}]}
        self.assertEqual(run_api.parse_response(raw, self.case, cfg)["prediction"], self.case["gold"])
        raw["choices"][0]["finish_reason"] = "length"
        with self.assertRaises(ValueError):
            run_api.parse_response(raw, self.case, cfg)
        raw["choices"][0]["message"] = {"refusal": "Cannot answer", "content": None}
        self.assertEqual(run_api.parse_response(raw, self.case, cfg)["status"], "refusal")

    def test_api_sends_exact_payload_without_gold_or_credential_in_outputs(self):
        cfg = self.models["jev"]["configuration"]
        opener = FakeOpener([self.decision()])
        with tempfile.TemporaryDirectory() as folder, contextlib.redirect_stdout(io.StringIO()):
            directory = Path(folder) / "run"
            with patch("socket.socket", side_effect=AssertionError("Offline test")):
                result = run_api.run("jev", [self.case], cfg, directory, "test-key", opener)
            self.assertEqual(result, 0)
            req = opener.requests[0]
            self.assertEqual(json.loads(req.data), request_specs.api_spec(self.case, cfg)["body"])
            self.assertEqual(req.get_header("Authorization"), "Bearer test-key")
            for p in directory.rglob("*"):
                if p.is_file():
                    self.assertNotIn("test-key", p.read_text())
            with self.assertRaises(FileExistsError):
                run_api.run("jev", [self.case], cfg, directory, "test-key", opener)

    def test_http_error_is_saved_once_and_stops_batch_without_retry(self):
        error = urllib.error.HTTPError("https://ai-gateway.vercel.sh", 503, "Unavailable", {}, io.BytesIO(b"unavailable"))
        opener = FakeOpener([error])
        with tempfile.TemporaryDirectory() as folder, contextlib.redirect_stdout(io.StringIO()):
            directory = Path(folder) / "run"
            result = run_api.run("jev", [self.case, self.case], self.models["jev"]["configuration"], directory, "test-key", opener)
            self.assertEqual(result, 1)
            self.assertEqual(len(opener.requests), 1)
            rows = baseline.read_jsonl(directory / "predictions.jsonl")
            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0]["status"], "error")
            self.assertTrue((directory / "raw/0000.http-error.txt").exists())

    def test_scoring_preserves_failure_and_missing_coverage(self):
        ids = [q["id"] for q in self.manifest[:3]]
        records = [{"case_id": ids[0], "status": "ok", "prediction": self.manifest[0]["gold_choice"]},
                   {"case_id": ids[1], "status": "error"}]
        report = score_fresh.score(records, self.manifest, ids)
        self.assertEqual((report["correct"], report["answered"], report["missing"]), (1, 1, 1))
        self.assertEqual(report["accuracy"], 1)
        self.assertEqual(report["coverage"], 1 / 3)
        with self.assertRaises(ValueError):
            score_fresh.score(records + [records[0]], self.manifest, ids)
        invalid = deepcopy(records)
        invalid[1]["prediction"] = self.manifest[1]["gold_choice"]
        with self.assertRaisesRegex(ValueError, "unanswered"):
            score_fresh.score(invalid, self.manifest, ids)

    def test_batch_loader_rejects_changed_choice_order(self):
        case = deepcopy(self.case)
        case["choices"] = dict(reversed(list(case["choices"].items())))
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "questions.jsonl"
            path.write_text(json.dumps(case) + "\n")
            with self.assertRaisesRegex(ValueError, "does not match"):
                request_specs.load_cases([case["id"]], path)

    def test_prepare_native_builds_hash_bound_job_and_strips_labels(self):
        with tempfile.TemporaryDirectory() as folder:
            folder = Path(folder)
            stage = folder / "stage.json"
            device = folder / "device.json"
            cfg = self.models["glide"]["configuration"]
            stage.write_text(json.dumps({"manifest_sha256": "a" * 64,
                "models": {"glide": {"revision": cfg["revision"]}}}))
            device.write_text(json.dumps({"identity": {"uuid": "fixture-device"}}))
            output = subprocess.check_output([sys.executable, "-B", "evaluation/prepare_native.py", "--model", "glide",
                "--case", self.case["id"], "--stage-result", str(stage), "--device", str(device)], cwd=ROOT, text=True)
            job = json.loads(output)
            self.assertEqual(job["manifest_sha256"], "a" * 64)
            self.assertEqual(job["expected_physical_gpu"]["uuid"], "fixture-device")
            self.assertNotIn("gold", job["cases"][0])
            self.assertNotIn("ability", job["cases"][0])
            self.assertIn("input_audit", job["cases"][0])

    def test_selection_files_preserve_ids_and_reject_duplicates(self):
        binary = request_specs.read_case_ids(ROOT / "data/binary_subset.csv")
        self.assertEqual(len(binary), 214)
        self.assertEqual(len(set(binary)), 214)
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "ids.txt"
            path.write_text("\n".join(binary[:3]) + "\n")
            self.assertEqual(request_specs.read_case_ids(path), binary[:3])
            path.write_text(binary[0] + "\n" + binary[0] + "\n")
            with self.assertRaisesRegex(ValueError, "unique"):
                request_specs.read_case_ids(path)

    def test_missing_selected_text_prevents_api_execution(self):
        # Nine binary inputs are recovered separately; no partial dispatch is allowed.
        with patch.object(sys, "argv", ["run_api.py", "--model", "jev", "--cases-file",
                str(ROOT / "data/binary_subset.csv"), "--output", "unused-output"]), \
             patch.object(run_api, "run", side_effect=AssertionError("Must not dispatch")):
            with self.assertRaisesRegex(ValueError, "not in this input file"):
                run_api.main()

    def test_comparison_distinguishes_wrong_answers_and_missing_results(self):
        q = self.manifest[:3]
        ids = [row["id"] for row in q]
        wrong = next(k for k in q[0]["choice_keys"] if k != q[0]["gold_choice"])
        saved = [{"case_id": ids[0], "status": "ok", "prediction": q[0]["gold_choice"]},
                 {"case_id": ids[1], "status": "error"},
                 {"case_id": ids[2], "status": "ok", "prediction": q[2]["gold_choice"]}]
        fresh = [{"case_id": ids[0], "status": "ok", "prediction": wrong},
                 {"case_id": ids[1], "status": "ok", "prediction": q[1]["gold_choice"]}]
        comparison, changes = score_fresh.compare(fresh, saved, self.manifest, ids)
        self.assertEqual(comparison["correct_to_wrong"], 1)
        self.assertEqual(comparison["changed_answers"], 1)
        self.assertEqual(comparison["newly_answered"], 1)
        self.assertEqual(comparison["newly_unanswered"], 1)
        self.assertEqual(changes[-1]["fresh_status"], "missing")

    def test_scorer_writes_matched_baseline_and_change_csv(self):
        with tempfile.TemporaryDirectory() as folder, contextlib.redirect_stdout(io.StringIO()):
            folder = Path(folder)
            job = folder / "job.json"
            inputs = folder / "answers.jsonl"
            output = folder / "comparison"
            cid = self.case["id"]
            job.write_text(json.dumps({"model": "jev", "case_ids": [cid],
                "input_hashes": {cid: baseline.input_hash(self.case)}}))
            inputs.write_text(json.dumps({"model": "jev", "case_id": cid, "status": "ok",
                "input_hash": baseline.input_hash(self.case), "prediction": self.case["gold"]}) + "\n")
            with patch.object(sys, "argv", ["score_fresh.py", "--input", str(inputs), "--job", str(job),
                                          "--output-dir", str(output)]):
                score_fresh.main()
            report = json.loads((output / "report.json").read_text())
            self.assertEqual(report["selected"], 1)
            self.assertEqual(report["saved_baseline"]["selected"], 1)
            self.assertEqual(report["comparison"]["wrong_to_correct"], 1)
            self.assertIn(cid, (output / "answer_changes.csv").read_text())

    def test_inspect_reads_and_checks_explicit_local_inputs(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "local.jsonl"
            path.write_text(json.dumps(self.case) + "\n")
            with patch.object(sys, "argv", ["baseline.py", "inspect", "--case", self.case["id"],
                    "--local-questions", str(path)]), contextlib.redirect_stdout(io.StringIO()) as stdout:
                baseline.main()
            self.assertEqual(json.loads(stdout.getvalue())["question"]["choices"], self.case["choices"])
            changed = deepcopy(self.case); changed["state"] += "Changed."
            path.write_text(json.dumps(changed) + "\n")
            with patch.object(sys, "argv", ["baseline.py", "inspect", "--case", self.case["id"],
                    "--local-questions", str(path)]), contextlib.redirect_stderr(io.StringIO()):
                with self.assertRaises(SystemExit):
                    baseline.main()

    def test_custom_endpoint_sends_question_without_gateway_or_credentials(self):
        with tempfile.TemporaryDirectory() as folder, contextlib.redirect_stdout(io.StringIO()):
            folder = Path(folder)
            path = folder / "connection.json"
            path.write_text(json.dumps({"format": "openai-chat", "endpoint": "http://localhost:8000/v1/chat/completions",
                "model_id": "served-model", "auth": "none", "request_parameters": {"max_tokens": 100}}))
            cfg = connections.load_connection(path)
            raw = {"model": "served-model", "choices": [{"finish_reason": "stop", "message": {
                "content": json.dumps({"answer": self.case["gold"]})}}]}
            opener = FakeOpener([raw])
            with patch("socket.socket", side_effect=AssertionError("Offline test")):
                self.assertEqual(run_api.run("my-model", [self.case], cfg, folder / "run", None, opener), 0)
            request = opener.requests[0]
            self.assertEqual(request.full_url, cfg["endpoint"])
            self.assertIsNone(request.get_header("Authorization"))
            body = json.loads(request.data)
            self.assertEqual(body["model"], "served-model")
            self.assertNotIn("reasoning_effort", body)
            question = json.loads(body["messages"][1]["content"])
            self.assertEqual(set(question), {"state", "question", "choices"})
            self.assertEqual(list(question["choices"]), list(self.case["choices"]))

    def test_connections_reject_embedded_keys_and_insecure_remote_urls(self):
        base = {"format": "openai-chat", "endpoint": "https://provider.example/v1/chat/completions", "model_id": "example"}
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "connection.json"
            for extra in [{"api_key": "do-not-store"}, {"endpoint": "http://provider.example/v1/chat/completions"},
                          {"request_parameters": {"messages": []}}]:
                path.write_text(json.dumps({**base, **extra}))
                with self.assertRaises(ValueError):
                    connections.load_connection(path)
        self.assertEqual(connections.auth_headers({"auth": "x-api-key"}, "fixture"), {"x-api-key": "fixture"})

    def test_custom_model_scoring_does_not_require_a_saved_model(self):
        with tempfile.TemporaryDirectory() as folder, contextlib.redirect_stdout(io.StringIO()):
            folder = Path(folder)
            job = folder / "run.json"
            data = folder / "answers.jsonl"
            output = folder / "report"
            job.write_text(json.dumps({"model": "my-model", "configuration": {
                "endpoint": "http://localhost:8000/v1/chat/completions", "model_id": "served-model"},
                "case_ids": [self.case["id"]], "input_hashes": {self.case["id"]: baseline.input_hash(self.case)}}))
            data.write_text(json.dumps({"model": "my-model", "case_id": self.case["id"], "status": "ok",
                "prediction": self.case["gold"]}) + "\n")
            with patch.object(sys, "argv", ["score_fresh.py", "--input", str(data), "--job", str(job),
                                          "--output-dir", str(output)]):
                score_fresh.main()
            report = json.loads((output / "report.json").read_text())
            self.assertEqual(report["correct"], 1)
            self.assertIsNone(report["saved_baseline"])
            self.assertFalse((output / "answer_changes.csv").exists())


if __name__ == "__main__":
    unittest.main()
