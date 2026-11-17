"""Offline integrity/scoring checks. No sockets or model runtimes are used."""
from copy import deepcopy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import baseline

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("request_specs", ROOT / "evaluation/request_specs.py")
requests = importlib.util.module_from_spec(spec)
spec.loader.exec_module(requests)


class BaselineTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.questions, cls.predictions, cls.models = baseline.load_bundle()
        cls.reference = json.loads((ROOT / "reference/expected_metrics.json").read_text())

    def test_entire_bundle_matches_frozen_results_offline(self):
        with patch("socket.socket", side_effect=AssertionError("Network use is forbidden")):
            summary = baseline.summarize(self.questions, self.predictions, self.models)
            baseline.verify_reference(summary, self.reference)

    def test_question_text_cannot_introduce_page_headings_or_split_choices(self):
        spec = importlib.util.spec_from_file_location("page_formatting", ROOT / "tools/rebuild_pages.py")
        formatting = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(formatting)
        self.assertEqual(formatting.readable_quote("Agreement\n----\nAddress\n===="),
                         "> Agreement\n> \\----\n> Address\n> \\====")
        self.assertEqual(formatting.md("Working\n# Answer\n\n0"), "Working # Answer  0")
        self.assertEqual(formatting.md("a|b `code`"), "a\\|b \\`code\\`")

    def test_duplicate_result_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            baseline.validate(self.questions, self.predictions + [self.predictions[0]], list(self.models))

    def test_missing_result_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "Missing outcomes"):
            baseline.validate(self.questions, self.predictions[:-1], list(self.models))

    def test_wrong_input_hash_is_rejected(self):
        changed = [dict(self.predictions[0], input_hash="wrong")] + self.predictions[1:]
        with self.assertRaisesRegex(ValueError, "different input"):
            baseline.validate(self.questions, changed, list(self.models))

    def test_invalid_prediction_is_rejected(self):
        changed = [dict(self.predictions[0], prediction="not-an-answer")] + self.predictions[1:]
        with self.assertRaisesRegex(ValueError, "not an answer choice"):
            baseline.validate(self.questions, changed, list(self.models))

    def test_failed_result_cannot_become_an_answer(self):
        changed = [dict(self.predictions[0], status="error")] + self.predictions[1:]
        with self.assertRaisesRegex(ValueError, "cannot be counted"):
            baseline.validate(self.questions, changed, list(self.models))

    def test_choice_order_changes_the_input_fingerprint(self):
        q = requests.load_case("bbh/639b88b1fe80634a7d66")
        reversed_q = {**q, "choices":dict(reversed(list(q["choices"].items())))}
        self.assertNotEqual(baseline.input_hash(q), baseline.input_hash(reversed_q))

    def test_binary_subset_includes_adapted_representations(self):
        summary = baseline.summarize(self.questions, self.predictions, self.models)
        self.assertEqual({r["selected"] for r in summary["native_binary"]}, {214})
        adapted = [q for q in self.questions if q["format_status"] == "adapted_choices"
                   and len(q["choice_keys"]) == 2 and q["positive_label"] is not None]
        self.assertEqual(len(adapted), 15)

    def test_unknown_api_cost_is_not_zero(self):
        changed = [dict(r, billed_cost_usd=None, inference_cost_usd=None, gateway_fee_usd=None)
                   if r["model"] == "openai-decisions" else r for r in self.predictions]
        lone = next(i for i, r in enumerate(changed) if r["model"] == "openai-decisions")
        changed[lone] = dict(changed[lone], billed_cost_usd=.001, inference_cost_usd=.0009, gateway_fee_usd=.0001)
        summary = baseline.summarize(self.questions, changed, self.models)
        luna = next(r for r in summary["cost_timing"] if r["model"] == "openai-decisions")
        self.assertEqual(luna["priced_requests"], 1)
        self.assertEqual(luna["unknown_cost_requests"], 1004)
        self.assertGreater(luna["api_cost_per_1000_requests"], 0)

    def test_model_costs_exclude_gateway_fees_and_reconcile_to_saved_totals(self):
        from decimal import Decimal
        summary = baseline.summarize(self.questions, self.predictions, self.models)
        for model, info in self.models.items():
            if info["serving"] != "api":
                continue
            rows = [r for r in self.predictions if r["model"] == model and r["billed_cost_usd"] is not None]
            inference = sum(Decimal(str(r["inference_cost_usd"])) for r in rows)
            fees = sum(Decimal(str(r["gateway_fee_usd"])) for r in rows)
            recorded = sum(Decimal(str(r["billed_cost_usd"])) for r in rows)
            self.assertEqual(inference + fees, recorded)
            result = next(r for r in summary["cost_timing"] if r["model"] == model)
            self.assertAlmostEqual(result["api_cost_per_1000_requests"], float(inference / len(rows) * 1000))
            self.assertAlmostEqual(result["excluded_gateway_fees_usd"], float(fees))
            self.assertGreater(fees, 0)
        luna = next(r for r in summary["cost_timing"] if r["model"] == "openai-decisions")
        # Model charges retain the recorded cache-write premium.
        self.assertAlmostEqual(luna["known_api_cost_usd"], .045536075)

    def test_inconsistent_billing_components_are_rejected(self):
        row = next(r for r in self.predictions if r["model"] == "jev")
        changed = [dict(r, inference_cost_usd=r["billed_cost_usd"]) if r is row else r for r in self.predictions]
        with self.assertRaisesRegex(ValueError, "Billing components"):
            baseline.validate(self.questions, changed, list(self.models))

    def test_unseparated_total_charge_is_not_assumed_to_be_model_cost(self):
        changed = [{k: v for k, v in r.items() if k not in {"inference_cost_usd", "gateway_fee_usd"}}
                   if r["model"] == "jev" else r for r in self.predictions]
        result = next(r for r in baseline.summarize(self.questions, changed, self.models)["cost_timing"] if r["model"] == "jev")
        self.assertIsNone(result["api_cost_per_1000_requests"])
        self.assertEqual(result["unknown_cost_requests"], 1005)

    def test_api_payloads_exclude_gold_and_capability_metadata(self):
        case = dict(state="Evidence", question="Question", choices={"B":"second", "A":"first"},
                    gold="DO_NOT_SEND_GOLD", ability="DO_NOT_SEND_ABILITY", dataset="DO_NOT_SEND_SOURCE")
        for name, model in self.models.items():
            if model["serving"] != "api":
                continue
            output = requests.api_spec(case, model["configuration"])
            serialized = json.dumps(output)
            self.assertNotIn("DO_NOT_SEND", serialized)
            self.assertNotIn("Authorization", output["headers"])
            if model["configuration"]["backend"] == "gateway_llm":
                inputs = json.loads(output["body"]["messages"][1]["content"])
                self.assertEqual(list(inputs["choices"]), ["B", "A"])
            elif model["configuration"]["api"] == "decisions-v1":
                self.assertEqual([r["value"] for r in output["body"]["questions"][0]["choices"]], ["B", "A"])
            else:
                self.assertEqual(list(output["body"]["questions"]["judgment"]["criteria"]), ["B", "A"])

    def test_worker_job_excludes_gold(self):
        case = requests.load_case("bbh/639b88b1fe80634a7d66")
        job = requests.worker_job("glide", self.models["glide"]["configuration"], [case], "0"*64)
        self.assertEqual(set(job["cases"][0]), {"id","state","question","choices","input_audit"})
        self.assertNotIn("gold", job["cases"][0])

    def test_held_inputs_not_in_release_questions(self):
        released = {q["id"] for q in baseline.read_jsonl(ROOT / "data/questions.jsonl")}
        self.assertEqual(released, {q["id"] for q in self.questions if q["text_included"]})
        self.assertFalse(any(q["dataset"] in {"ag_news"}
                             for q in self.questions if q["text_included"]))
        held = next(q for q in self.questions if not q["text_included"])
        with self.assertRaisesRegex(ValueError, "not in this input file"):
            requests.load_case(held["id"])

    def test_csv_summaries_can_be_regenerated(self):
        with tempfile.TemporaryDirectory() as folder:
            baseline.write_summaries(baseline.summarize(self.questions, self.predictions, self.models), folder)
            self.assertEqual({p.name for p in Path(folder).iterdir()},
                             {"overall.csv","capabilities.csv","native_binary.csv","cost_timing.csv"})


if __name__ == "__main__":
    unittest.main()
