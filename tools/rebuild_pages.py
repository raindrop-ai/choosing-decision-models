"""Rebuild readable question pages from release data; no charts, network or inference."""
from collections import defaultdict
from datetime import date
import csv
import html
import json
from pathlib import Path
import re
import sys

DEST = Path(__file__).resolve().parents[1]
CHECKED = json.loads((DEST / "release_status.json").read_text())["sharing_checked"]
CHECKED_DISPLAY = date.fromisoformat(CHECKED).strftime("%B %d, %Y").replace(" 0", " ")
sys.path.insert(0, str(DEST))
import baseline

def write(name, text):
    path = DEST / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")

def md(value):
    value = html.escape(str(value)).replace("\\", "\\\\").replace("\n", " ")
    for mark in ("|", "`", "*", "_", "[", "]"):
        value = value.replace(mark, "\\" + mark)
    return value

def fenced(text):
    width = max([2] + [len(x) for x in re.findall(r"`+", text)]) + 1
    fence = "`" * width
    return fence + "text\n" + text + "\n" + fence

def readable_quote(text):
    def escape(line):
        line = html.escape(line, quote=False).replace("\\", "\\\\")
        for mark in ("`", "*", "_", "[", "]", "#"):
            line = line.replace(mark, "\\" + mark)
        return line
    return "\n".join("> " + escape(line) if line else ">" for line in text.splitlines())

def percent(value):
    return "—" if value is None else f"{value * 100:.1f}%"

def material_attribution_lines(entry):
    details = entry.get("source", {}).get("attribution_details", {})
    if not details:
        return []
    kind = details["kind"]
    if kind == "wikipedia_passage":
        return [f"Original Wikipedia passage: [{md(details['title'])}]({details['wikipedia_url']}); [contributor history]({details['wikipedia_history_url']}). The BoolQ excerpt is unchanged. This question material retains CC BY-SA 3.0.", ""]
    if kind == "licensed_upstream_match":
        return [f"Licensed upstream task: [{md(details['source_url'].split('/')[-2])}]({details['source_url']}). All eight supplied examples and the evaluated test input/output match the original BIG-bench data.", ""]
    if kind == "oanc_nonfiction_genre":
        return [f"Original MultiNLI pair: `{details['pair_id']}`; OANC genre: **{details['genre']}**. {details['changes']}", ""]
    if kind in {"rewardbench_component", "agentprocessbench_component"}:
        return [f"Underlying component: [{md(details['component'])}]({details['source_url']}); component terms: **{md(details['license'])}**. The [source notices](../../licenses/sources/" + entry['dataset'] + "/ATTRIBUTION.md) retain the applicable component credits and licenses.", ""]
    if kind == "synthetic_test_split":
        return [f"Origin: the synthetic WildGuardTest split described in [the original paper, section 3.2]({details['source_url']}).", ""]
    return []


def build_browse_pages(cases, manifests, shared, predictions, models, sources, summary):
    by_id = {q["id"]:q for q in shared}
    metadata = {q["id"]:q for q in manifests}
    by_result = defaultdict(dict)
    for r in predictions:
        by_result[r["case_id"]][r["model"]] = r
    source_by_id = {s["id"]:s for s in sources}
    names = {"Perception and attention (retrieval)":"Retrieval", "Metacognition/Uncertainty monitoring (risk)":"Uncertainty monitoring",
             "Information seeking (information gain)":"Information seeking"}
    abilities = list(dict.fromkeys(c["ability"] for c in cases))
    binary_rows = []
    directory_lines = ["# Browse the baseline questions", "", "Each capability links to question pages with sources and all 13 recorded model outcomes. The last column counts questions whose complete text is included in this repository.", "", "The questions come from datasets with different licenses. We include full text where the source terms clearly allow us to share it here. For 148 questions, permission to republish the text is unclear or additional license requirements apply. We therefore provide [original download links and recovery tools](../docs/recovering-inputs.md) so readers can obtain those questions from their sources instead.", "", "All 1,005 questions still have their IDs, reference answer keys and recorded model results included. You can verify the reported scores without downloading the missing texts.", "", "Choose a capability below to explore the questions and recorded model answers.", "", "| Capability | Questions | Question texts in this repo |", "| --- | ---: | ---: |"]
    for ability in abilities:
        name = names.get(ability, ability)
        slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
        cs = [c for c in cases if c["ability"] == ability]
        directory_lines.append(f"| [{name}]({slug}/README.md) | {len(cs)} | {sum(c['id'] in by_id for c in cs)} |")
        lines = [f"# {name}", "", "[All capabilities](../README.md) · [Methods](../../docs/methods.md)", "", "67 questions. ‘Correct / answered’ counts the recorded outcomes across all 13 models.", "", "| Question | Source | Correct / answered | Question text |", "| --- | --- | ---: | --- |"]
        for i,c in enumerate(cs,1):
            cid=c["id"]; m=metadata[cid]; source=source_by_id[c["dataset"]]
            file=cid.replace("/","-")+".md"
            rs=by_result[cid]
            answered=[r for r in rs.values() if r["status"]=="ok"]
            correct=sum(r["prediction"]==c["gold"] for r in answered)
            title=c["question"].replace("\n"," ") if cid in by_id else "Recover locally — "+c["family"]
            if cid in by_id and c["state"] and (title.startswith("Does this question have a determinate answer?") or title.startswith("Choose the correct answer to the supplied")):
                title = c["state"].replace("\n", " ")
            title=title[:100]+("…" if len(title)>100 else "")
            if len(c["choices"]) == 2 and c.get("positive_label") is not None:
                binary_rows.append(dict(case=c, name=name, path=f"{slug}/{file}", title=title,
                                        source=source["title"], correct=correct, answered=len(answered)))
            lines.append(f"| [{i}. {md(title)}]({file}) | {md(source['title'])} | {correct}/{len(answered)} | {'Included' if cid in by_id else 'Recover locally'} |")
            detail=[f"# {name} · question {i}", "", f"[Back to {name}](README.md) · [All capabilities](../README.md)", "", f"**Question ID:** `{cid}`  ", f"**Source:** [{md(source['title'])}]({source['url']})  ", f"**Input format:** {c['format_status'].replace('_',' ')}", ""]
            if (DEST/"data/variants/manifest.jsonl").exists():
                detail += [f"[Explore this question’s altered versions](../../variants/{slug}/{re.sub('[^a-z0-9]+', '-', cid.lower()).strip('-')}/README.md)", ""]
            if cid in by_id:
                if c["state"]:
                    context = fenced(c["state"]) if c["dataset"]=="cruxeval" else readable_quote(c["state"])
                    if len(c["state"]) > 1500:
                        context = "<details>\n<summary>Read the full context</summary>\n\n" + context + "\n\n</details>"
                    detail += ["## Context", "", context, ""]
                detail += ["## Question", "", readable_quote(c["question"]), "", "## Answer choices", ""]
                detail += [f"- **{md(k)}:** {md(v)}" for k,v in c["choices"].items()]
                detail += ["",f"**Reference answer:** {md(c['choices'][c['gold']])} (`{c['gold']}`)", ""]
                detail += ["<details>", "<summary>Exact evaluated input as JSON</summary>", "", fenced(json.dumps({k:c[k] for k in ("state","question","choices")},ensure_ascii=False,indent=2)), "", "</details>", ""]
            else:
                detail += ["## Recover the original question", "", source["reason"], "", "[Recover this question](../../docs/recovering-inputs.md) from its original source files. The recovery tool reconstructs the evaluated input and verifies its checksum.", "",f"**Reference choice key:** `{c['gold']}`. Descriptions are withheld with the question text.", ""]
            detail += ["## Recorded model answers", "", "| Model | Answer | Outcome |", "| --- | --- | --- |"]
            for model,info in models.items():
                r=rs[model]
                value=c["choices"].get(r["prediction"],"—") if cid in by_id else (r["prediction"] or "—")
                outcome=("Correct" if r["prediction"]==c["gold"] else "Incorrect") if r["status"]=="ok" else r["status"].title()
                detail.append(f"| {info['name']} | {md(value)} | {outcome} |")
            terms = f"[{md(source['license'])}]({source['license_url']})" if source["license_url"] else md(source["license"] or "Not established")
            detail += ["", "## Source and sharing", "", f"Attribution: {md(by_id[cid]['source']['attribution'] if cid in by_id else source['attribution'])}.  ",f"Terms: **{terms}**. [Source sharing decision](../../docs/data-sharing.md).  ", "The capability assignment and choice-format normalization are part of this experiment. Source data retain their own terms.", "", "<details>", "<summary>Exact source locator and input fingerprint</summary>", "", "```json", json.dumps({"source_locator":m["source_locator"],"source_revision":m["source_revision"],"input_hash":m["input_hash"]},ensure_ascii=False,indent=2), "```", "", "</details>", ""]
            if cid in by_id:
                insert_at = detail.index("## Source and sharing") + 2
                detail[insert_at:insert_at] = material_attribution_lines(by_id[cid])
            write(f"questions/{slug}/{file}","\n".join(detail))
        write(f"questions/{slug}/README.md","\n".join(lines)+"\n")
    directory_lines += ["", "[Browse the 214-question binary subset](binary-subset.md) used for precision, recall, false alarms and missed detections.", "", "[Sharing decisions for every question](../data/sharing_decisions.csv) · [Download released inputs](../data/questions.jsonl) · [All saved answers](../results/baseline_predictions.csv)"]
    write("questions/README.md","\n".join(directory_lines)+"\n")
    if len(binary_rows) != 214 or {r["selected"] for r in summary["native_binary"]} != {len(binary_rows)}:
        raise ValueError("Binary browsing inventory must match the scored 214-question subset")
    binary_lines = ["# The 214-question binary subset", "",
        "[All 1,005 questions](README.md) · [Binary results](../docs/results.md#errors-on-binary-questions) · [Scoring](../docs/methods.md#binary-error-analysis) · [Download question IDs](../data/binary_subset.csv)", "",
        "These 214 questions from the 1,005-question set supply the post's precision, recall, false-alarm and missed-detection results. Each has two answer choices and an explicit positive label from its source. Fifteen use adapted choice representations.", "",
        "Each question page shows its source, reference answer and all 13 recorded model outcomes. Positive choice is the choice key treated as positive in scoring; its meaning varies by source. ‘Correct / answered’ counts saved answers across all 13 models. Questions whose text is obtained separately remain listed with their results and recovery instructions.", ""]
    for ability in abilities:
        rows = [r for r in binary_rows if r["case"]["ability"] == ability]
        if not rows:
            continue
        binary_lines += [f"## {rows[0]['name']} · {len(rows)} questions", "",
            "| Question | Source | Positive choice | Correct / answered |",
            "| --- | --- | --- | ---: |"]
        for row in rows:
            binary_lines.append(f"| [{md(row['title'])}]({row['path']}) | {md(row['source'])} | `{md(row['case']['positive_label'])}` | {row['correct']}/{row['answered']} |")
        binary_lines.append("")
    write("questions/binary-subset.md", "\n".join(binary_lines))
    with (DEST / "data/binary_subset.csv").open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=["case_id", "ability", "dataset", "positive_label", "gold_choice", "question_page"])
        writer.writeheader()
        for row in binary_rows:
            c = row["case"]
            writer.writerow(dict(case_id=c["id"], ability=c["ability"], dataset=c["dataset"],
                                 positive_label=c["positive_label"], gold_choice=c["gold"],
                                 question_page="questions/" + row["path"]))
    lines=["# Baseline results", "", "These tables summarize the recorded outcomes. Recompute their underlying CSVs with `python3 baseline.py summarize`; the new files go to `.local/summaries/`.", "", "## Overall accuracy", "", "| Model | Correct / answered | Accuracy | Answered / selected |", "| --- | ---: | ---: | ---: |"]
    for r in summary["overall"]:
        lines.append(f"| {models[r['model']]['name']} | {r['correct']} / {r['answered']} | {percent(r['accuracy'])} | {r['answered']} / {r['selected']} |")
    lines += ["", "## Errors on binary questions", "", "The selected subset has [214 source-defined binary questions](../questions/binary-subset.md), including 15 with adapted choice representations. Each source's positive label is retained. Failed requests and refusals are excluded from confusion counts and lower answered coverage.", "", "| Model | False alarms | Missed detections | Precision | Recall |", "| --- | ---: | ---: | ---: | ---: |"]
    for r in summary["native_binary"]:
        lines.append(f"| {models[r['model']]['name']} | {r['fp']} | {r['fn']} | {percent(r['precision'])} | {percent(r['recall'])} |")
    lines += ["", "## Costs and prediction times", "", "### Self-hosted models", "", "All eight models ran on the same physical NVIDIA A100 80GB PCIe, one prediction at a time. Timing summaries exclude each model's first forward with kernel startup; every answer still counts toward accuracy. See [measurement conditions and definitions](methods.md#saved-costs-and-timings).", "", "| Model | Median prediction time | p95 prediction time |", "| --- | ---: | ---: |"]
    for r in summary["cost_timing"]:
        if r["serving"] != "self-hosted":
            continue
        lines.append(f"| {models[r['model']]['name']} | {r['median_ms']:.0f} ms | {r['p95_ms']:.0f} ms |")
    lines += ["", "### Hosted models", "", "We accessed the hosted models through Vercel AI Gateway. Costs show model inference charges for the recorded inputs, excluding Vercel AI Gateway fees. API request times include network travel and routing; GPU-worker timings measure prediction after model loading.", "", "| Model | Median request time | p95 request time | Model cost / 1,000 priced requests |", "| --- | ---: | ---: | ---: |"]
    for r in summary["cost_timing"]:
        if r["serving"] != "api":
            continue
        cost = r["api_cost_per_1000_requests"]
        value = "—" if cost is None else f"${cost:.3f}"
        lines.append(f"| {models[r['model']]['name']} | {r['median_ms']:.0f} ms | {r['p95_ms']:.0f} ms | {value} |")
    lines += ["", "CSV downloads: [overall](../summaries/overall.csv), [by capability](../summaries/capabilities.csv), [binary outcomes](../summaries/native_binary.csv), [saved costs and timings](../summaries/cost_timing.csv).", "", "[Browse individual questions and model answers](../questions/README.md).", ""]
    write("docs/results.md","\n".join(lines))
    readme = (DEST / "README.md").read_text()
    preview = ["| Model | Correct / answered | Accuracy |", "| --- | ---: | ---: |"]
    for r in summary["overall"]:
        name = models[r["model"]]["name"]
        if models[r["model"]].get("llm_baseline"):
            name += " (LLM baseline)"
        preview.append(f"| {name} | {r['correct']:,} / {r['answered']:,} | {percent(r['accuracy'])} |")
    readme = re.sub(r"<!-- RESULTS_PREVIEW_START -->.*?<!-- RESULTS_PREVIEW_END -->",
        "<!-- RESULTS_PREVIEW_START -->\n" + "\n".join(preview) + "\n<!-- RESULTS_PREVIEW_END -->", readme, flags=re.S)
    write("README.md", readme)
    lines=["# Data sharing decisions", "", "Each dataset’s terms still apply. In the table below, **Included** means we provide the question text. **Recover locally** means you download the original files and use our tools to reconstruct the questions we used. We checked the source terms on "+CHECKED_DISPLAY+".", "", "The collection keeps all 1,005 original-question metadata records and all 13,065 baseline outcomes. Full inputs are bundled for 857 questions; the other 148 can be reconstructed locally from original source files under the source terms. Recovered question texts stay in the ignored `.local/` folder and are not redistributed with the repository.", "", "| Source | Questions | Question text | Terms | Decision and remaining conditions |", "| --- | ---: | --- | --- | --- |"]
    for s in sources:
        lines.append(f"| [{md(s['title'])}]({s['url']}) | {s['questions']} | {'Included' if s['sharing']=='include' else 'Recover locally'} | {md(s['license'] or 'Not established')} | {md(s['reason'])} |")
    lines += ["", "[Recover question texts](recovering-inputs.md) · [PIQA recovery and AFL terms](recovering-inputs.md#3-recover-piqa)", "", "## Attribution and adaptation", "", "CLUTRR, EmoWOZ and ToxicChat question material is included for this noncommercial research release under CC BY-NC 4.0. Its noncommercial restriction remains applicable to downstream reuse. The full license and disclaimer are in [`licenses/CC-BY-NC-4.0.txt`](../licenses/CC-BY-NC-4.0.txt).", "", "Question records retain the source URL, revision when available, original locator, attribution, and per-source license. Where the evaluated choice format differs from the source question, released records also include the native representation. Adapted SelfAware entries remain under CC BY-SA 4.0; BoolQ entries retain CC BY-SA 3.0. Per-question Wikipedia, OANC, BIG-bench and component attribution is recorded in [`data/source_attributions.json`](../data/source_attributions.json) and displayed on the question pages. This is a collection of separately licensed source materials; there is no blanket MIT license for the questions.", "", "The original license notices are in [`licenses/sources/`](../licenses/sources/). [`data/sources.json`](../data/sources.json) records checked evidence URLs, source hashes, and license excerpts. [`data/sharing_decisions.csv`](../data/sharing_decisions.csv) gives a decision for each of the 1,005 question IDs.", "", "Publisher dataset-card declarations and source credits are recorded in `data/sources.json`. Follow each source’s terms when obtaining or reusing its text.", ""]
    write("docs/data-sharing.md","\n".join(lines))


def main():
    metadata, results, models = baseline.load_bundle(DEST, check_files=False)
    shared = baseline.read_jsonl(DEST / "data/questions.jsonl")
    by_id = {c["id"]: c for c in shared}
    cases = []
    for m in metadata:
        c = {**m, "gold": m["gold_choice"], "state": "", "question": "", "choices": dict.fromkeys(m["choice_keys"], "")}
        if m["id"] in by_id:
            c.update(by_id[m["id"]])
        cases.append(c)
    sources = json.loads((DEST / "data/sources.json").read_text())
    summary = baseline.summarize(metadata, results, models)
    baseline.verify_reference(summary, json.loads((DEST / "reference/expected_metrics.json").read_text()))
    build_browse_pages(cases, metadata, shared, results, models, sources, summary)
    print("Rebuilt question indexes, question pages, baseline result tables, and sharing notes from the release data.")

if __name__ == "__main__":
    main()
