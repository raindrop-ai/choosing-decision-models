"""Exercise replacements using synthetic edits; never consume an active rerun."""
from copy import deepcopy
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest

import baseline

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("replace_results", ROOT / "tools/replace_results.py")
replacement = importlib.util.module_from_spec(spec)
spec.loader.exec_module(replacement)


class ReplacementTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.questions, cls.old, cls.models = baseline.load_bundle()
        cls.rows = [{k: v for k, v in row.items() if k in replacement.FIELDS}
                    for row in cls.old if cls.models[row["model"]]["serving"] == "self-hosted"]
        cls.configs = {m: {"configuration": info["configuration"], "gpu": info["gpu"],
                           "timing_percentile_method": "nearest_rank"}
                       for m, info in cls.models.items() if info["serving"] == "self-hosted"}

    def merged(self, rows=None, configs=None):
        return replacement.merge_results(self.questions, self.old, self.models,
            self.rows if rows is None else rows, self.configs if configs is None else configs)

    def test_api_rows_preserved_and_old_modal_configurations_removed(self):
        rows, models, configs = self.merged()
        before = {(r["model"], r["case_id"]): r for r in self.old if r["model"] not in self.configs}
        after = {(r["model"], r["case_id"]): r for r in rows if r["model"] not in self.configs}
        self.assertEqual(before, after)
        self.assertTrue(all(not r["reused_result"] for r in rows if r["model"] in self.configs))

    def test_missing_duplicate_and_wrong_input_rejected(self):
        for bad in (self.rows[:-1], self.rows + self.rows[:1],
                    [dict(self.rows[0], input_hash="wrong")] + self.rows[1:]):
            with self.subTest(length=len(bad)), self.assertRaises(ValueError):
                self.merged(bad)

    def test_checkpoint_changes_and_unexpected_fields_rejected(self):
        configs = deepcopy(self.configs)
        configs["glide"]["configuration"]["revision"] = "different"
        with self.assertRaisesRegex(ValueError, "checkpoint"):
            self.merged(configs=configs)
        with self.assertRaisesRegex(ValueError, "Unexpected result fields"):
            self.merged([dict(self.rows[0], private_response="never copy")] + self.rows[1:])

    def test_first_forward_excluded_from_timings_but_counts_for_accuracy(self):
        original = baseline.summarize(self.questions, self.old, self.models)
        modified = deepcopy(self.rows)
        index = next(i for i, r in enumerate(modified) if r.get("timing_included", True))
        modified[index].update(timing_class="first_forward_with_kernel_startup", timing_included=False, latency_ms=1e12)
        combined, models, _ = self.merged(modified)
        current = baseline.summarize(self.questions, combined, models)
        self.assertEqual(current["overall"], original["overall"])
        alias = modified[index]["model"]
        old_t = next(r for r in original["cost_timing"] if r["model"] == alias)
        new_t = next(r for r in current["cost_timing"] if r["model"] == alias)
        self.assertEqual(new_t["timed"], old_t["timed"] - 1)
        self.assertLess(new_t["p95_ms"], 1e12)
        modified[index]["timing_included"] = True
        with self.assertRaisesRegex(ValueError, "first-forward"):
            self.merged(modified)

    def test_percentile_methods(self):
        self.assertEqual(baseline.percentile(list(range(20)), .95), 18)
        self.assertAlmostEqual(baseline.percentile(list(range(20)), .95, "linear"), 18.05)
        with self.assertRaises(ValueError):
            baseline.percentile([], .95, "unknown")

    def test_seal_preserves_audited_workflow_but_rejects_private_files(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            name = ".github/workflows/companion-pages.yml"
            (root / name).parent.mkdir(parents=True)
            (root / name).write_text("name: companion\n")
            (root / "MANIFEST.json").write_text(json.dumps({"sha256": {name: "previous"}}))
            replacement.seal(root)
            self.assertIn(name, json.loads((root / "MANIFEST.json").read_text())["sha256"])
            (root / ".private").write_text("private")
            with self.assertRaisesRegex(ValueError, "Private file"):
                replacement.seal(root)

    def test_dry_run_and_apply_refresh_all_derived_outputs(self):
        with tempfile.TemporaryDirectory() as folder:
            tmp = Path(folder)
            root = tmp / "companion"
            root.mkdir()
            manifest = json.loads((ROOT / "MANIFEST.json").read_text())
            for name in list(manifest["sha256"]) + ["MANIFEST.json"]:
                target = root / name
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(ROOT / name, target)
            predictions = deepcopy(self.rows)
            changed = next(r for r in predictions if r["case_id"] == "bbh/639b88b1fe80634a7d66" and r["model"] == "glide")
            changed["prediction"] = "B"
            changed["probabilities"] = None
            incoming = tmp / "incoming.jsonl"
            incoming.write_text("".join(json.dumps(r) + "\n" for r in predictions))
            configs = tmp / "models.json"
            configs.write_text(json.dumps(self.configs))
            before = (root / "MANIFEST.json").read_bytes()
            replacement.replace(root, incoming, configs)
            self.assertEqual(before, (root / "MANIFEST.json").read_bytes())
            replacement.replace(root, incoming, configs, apply=True)
            self.assertNotEqual(before, (root / "MANIFEST.json").read_bytes())
            questions, rows, models = baseline.load_bundle(root)
            baseline.verify_reference(baseline.summarize(questions, rows, models),
                json.loads((root / "reference/expected_metrics.json").read_text()))
            page = (root / "questions/state-tracking-and-updating/bbh-639b88b1fe80634a7d66.md").read_text()
            self.assertIn("| GLiDE v1.2 | purple present | Incorrect |", page)
            self.assertFalse(json.loads((root / "release_status.json").read_text())["results_temporary"])
            files = set(json.loads((root / "MANIFEST.json").read_text())["sha256"])
            self.assertEqual(files, set(manifest["sha256"]))
            self.assertFalse(any("archive" in p or "rollback" in p for p in files))


if __name__ == "__main__":
    unittest.main()
