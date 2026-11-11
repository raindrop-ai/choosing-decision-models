"""Recover the 30 PIQA inputs from their original source after explicit AFL acceptance."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import baseline

LICENSE = "https://opensource.org/license/afl-3.0"


def reconstruct(metadata, source_files):
    """Pure conversion with exact hashes/answers checked; no network or inference."""
    selected = [m for m in metadata if m["dataset"] == "piqa"]
    if len(selected) != 30:
        raise ValueError("Expected exactly 30 selected PIQA questions")
    tables = {}
    results = []
    for m in selected:
        path = m["source_locator"]["path"]
        if path not in tables:
            tables[path] = [json.loads(line) for line in source_files[path].decode().splitlines()]
        native = tables[path][int(m["source_locator"]["record"])]
        labels_path = path.replace(".jsonl", "-labels.lst")
        label = source_files[labels_path].decode().splitlines()[int(m["source_locator"]["record"])]
        case = {k: m[k] for k in ("id", "base_id", "group_id", "ability", "dataset", "family", "source_split", "format_status", "positive_label", "positive_definition")}
        case.update(state="", question=native["goal"], choices={"0":native["sol1"], "1":native["sol2"]},
                    gold=str(label), input_hash=m["input_hash"])
        if (baseline.input_hash(case) != m["input_hash"] or case["gold"] != m["gold_choice"]
                or list(case["choices"]) != m["choice_keys"]):
            raise ValueError("PIQA input, answer or choice order differs: " + m["id"])
        results.append(case)
    return results


def obtain_sources(metadata, source, *, local_source=None):
    paths = {m["source_locator"]["path"] for m in metadata if m["dataset"] == "piqa"}
    paths |= {p.replace(".jsonl", "-labels.lst") for p in paths}
    declared = {f["path"]: f for f in source["downloads"]}
    files = {}
    for name in sorted(paths):
        spec = declared[name]
        if local_source is not None:
            data = (Path(local_source) / name).read_bytes()
        else:
            with urllib.request.urlopen(spec["url"], timeout=40) as response:
                data = response.read(10_000_001)
            if len(data) > 10_000_000:
                raise ValueError("PIQA source exceeds expected size")
        if hashlib.sha256(data).hexdigest() != spec["sha256"]:
            raise ValueError("PIQA source checksum mismatch: " + name)
        files[name] = data
    return files


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--accept-afl-3.0", dest="accept_afl", action="store_true",
        help="Expressly accept the source's Academic Free License 3.0 before obtaining its data")
    parser.add_argument("--source-dir", type=Path,
        help="Optional existing source directory; verifies local files instead of downloading")
    args = parser.parse_args()
    if not args.accept_afl:
        parser.error("Read " + LICENSE + " and rerun with --accept-afl-3.0 only if you accept those terms. No data was obtained.")
    metadata = baseline.read_jsonl(ROOT / "data/question_manifest.jsonl")
    source = next(s for s in json.loads((ROOT / "data/sources.json").read_text()) if s["id"] == "piqa")
    rows = reconstruct(metadata, obtain_sources(metadata, source, local_source=args.source_dir))
    local = ROOT / ".local"
    local.mkdir(mode=0o700, exist_ok=True)
    destination = local / "piqa.questions.jsonl"
    destination.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows))
    (local / "piqa.acceptance.json").write_text(json.dumps({
        "license": "AFL-3.0", "license_url": LICENSE, "express_acceptance": True,
        "attribution": "Yonatan Bisk, Rowan Zellers, Jianfeng Gao, Yejin Choi and contributors; PIQA",
        "source_revision": source["revision"], "source_files_sha256": {
            f["path"]: f["sha256"] for f in source["downloads"]},
        "changes": "Selected and normalized by Raindrop; all 30 input hashes and reference choices verified.",
        "license_notice": "See licenses/sources/piqa/upstream-afl-LICENSE.txt, including the warranty disclaimer."
    }, indent=2) + "\n")
    print("Recovered and verified 30 PIQA inputs in .local/piqa.questions.jsonl.")
    print("These local files retain AFL 3.0 terms and are excluded from Git. No model calls were made.")


if __name__ == "__main__":
    main()
