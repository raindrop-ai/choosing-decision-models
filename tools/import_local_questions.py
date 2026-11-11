"""Validate and import complete evaluated inputs into local storage."""
import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from baseline import input_hash, read_jsonl


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True)
    args = parser.parse_args()
    manifest = {r["id"]:r for r in read_jsonl(ROOT / "data/question_manifest.jsonl")}
    source = read_jsonl(args.source)
    if len(source) != len({r["id"] for r in source}) or set(r["id"] for r in source) != set(manifest):
        raise ValueError("Provide exactly the 1,005 baseline inputs, with no duplicates")
    for r in source:
        m = manifest[r["id"]]
        if input_hash(r) != m["input_hash"] or r["gold"] != m["gold_choice"]:
            raise ValueError("Input/order/gold differs from baseline: " + r["id"])
    destination = ROOT / ".local/questions.complete.jsonl"
    destination.parent.mkdir(exist_ok=True)
    if destination.resolve() == args.source.resolve():
        print("Existing local inputs verified.")
        return
    destination.write_text("".join(json.dumps(r,ensure_ascii=False)+"\n" for r in source))
    print("Verified complete inputs; saved only in ignored .local/questions.complete.jsonl.")


if __name__ == "__main__":
    main()
