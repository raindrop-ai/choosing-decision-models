<a href="https://www.raindrop.ai/">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/raindrop-wordmark-light.svg">
    <img src="docs/assets/raindrop-wordmark-ink.svg" alt="Raindrop" width="180">
  </picture>
</a>

# The subtle art of making judgment calls

Questions, model answers, and scoring code accompanying [Raindrop’s research post](https://dawn-landing-git-codex-judgment-calls-blog.previews.raindrop.ai/blog/judgment-calls/). The study compares judgment accuracy across 15 capabilities and examines how changes in wording, framing and context affect those judgments. Inspect individual answers and reproduce the reported scores.

[Read the post](https://dawn-landing-git-codex-judgment-calls-blog.previews.raindrop.ai/blog/judgment-calls/) · [Browse questions](questions/README.md) · [Variants](variants/README.md) · [Results](docs/results.md) · [Methods](docs/methods.md) · [Reproduce](docs/reproduction.md)

| Original questions | Capability areas | Baseline models | Baseline outcomes |
| ---: | ---: | ---: | ---: |
| 1,005 | 15, with 67 questions each | 11 decision models + 2 LLM baselines | 13,065 |

## Start exploring

- **[Browse the questions](questions/README.md)** by capability, with an individual page for each question and every model's recorded answer.
- **[Explore the 214-question binary subset](questions/binary-subset.md)** used for precision, recall, false alarms and missed detections.
- **[Start with the gift exchange](questions/state-tracking-and-updating/bbh-639b88b1fe80634a7d66.md)** discussed in the post.
- **[Read the baseline results](docs/results.md)** or download the [per-question model answers](results/baseline_predictions.csv).
- **[Understand the experiment](docs/methods.md)**, including answer choices, scoring, and missing answers.
- **[Recover all 1,005 inputs](docs/recovering-inputs.md)** using the bundled questions and original source files.
- **[Check source terms and attribution](docs/data-sharing.md)**. Some question text is obtained directly from its original source; every model outcome is included here.

## Context-sensitivity study

The eleven decision models also answered altered versions of these originals: **24,563 variants**, of which **23,374 fit every model**. [Explore every variant](variants/README.md), [read how the edits were made](docs/variant-methods.md), or [inspect the comparison results](docs/variant-results.md). The comparison tables include changed answers, correct-to-wrong and wrong-to-correct judgments, as well as accuracy.

Check the saved variant results offline:

```bash
python3 variants.py verify
python3 variants.py summarize
```

For fresh predictions, use the [variant reproduction guide](docs/variant-reproduction.md).

## Baseline results at a glance

<!-- RESULTS_PREVIEW_START -->
| Model | Correct / answered | Accuracy |
| --- | ---: | ---: |
| Astra (LLM baseline) | 999 / 1,005 | 99.4% |
| Opus 5.5 (LLM baseline) | 997 / 1,003 | 99.4% |
| GLiDE v1.2 | 954 / 1,005 | 94.9% |
| Decider v1.1 | 919 / 1,005 | 91.4% |
| Jev | 892 / 1,005 | 88.8% |
| Microsoft Decision-1 | 846 / 1,004 | 84.3% |
| Clef | 835 / 1,005 | 83.1% |
| Luna Decisions | 777 / 997 | 77.9% |
| Clef Flash | 768 / 1,005 | 76.4% |
| Strands Decider | 678 / 1,005 | 67.5% |
| GLiNER2.5 Decide | 429 / 1,005 | 42.7% |
| Laya | 416 / 1,005 | 41.4% |
| CalDec v1 | 408 / 1,005 | 40.6% |
<!-- RESULTS_PREVIEW_END -->

Accuracy is calculated over answered questions. Errors and refusals remain visible in coverage. [See the capability breakdown and binary error analysis](docs/results.md), or [inspect every model's answer to a question](questions/README.md).

## Verify the baseline scores

Download or clone this repository, then open a terminal in the folder containing `baseline.py`. Python 3.10 or later is enough. No extra packages, credentials, model downloads or paid calls are needed:

```bash
python3 baseline.py verify
python3 baseline.py summarize
python3 -m unittest discover -s tests -v
```

`summarize` writes fresh CSVs to `.local/summaries/`, leaving the published tables in [`summaries/`](summaries/README.md) unchanged. These cover overall accuracy, accuracy by capability, binary error counts and saved cost/timing summaries. `verify` checks the calculations against the reference tables, as well as input fingerprints, coverage and file checksums.

## Get the questions used in the experiment

**This repository includes 857 complete questions.** The source datasets have different licenses and redistribution terms, so we only bundle question text where those terms clearly support sharing it here. For the remaining 148 questions, permission to redistribute the text is unclear or involves additional requirements.

You can obtain the original files from their publishers under the applicable terms and use the recovery tools below to reconstruct the exact questions we evaluated. Those recovered texts stay in an ignored local folder and are not added to Git.

Question IDs, reference choice keys and saved model outcomes are included for all 1,005 questions. You can verify the reported scores without downloading any question text.

### 1. Download the original files you need

Choose the datasets you want to reproduce. Follow the publisher's access and use terms, then download the linked original files. You only need sources for the questions you want to recover; the 857 bundled inputs are already in [`data/questions.jsonl`](data/questions.jsonl).

Save the files beneath a local source root such as `.local/original-sources/`, using the relative folder and file names shown below. These links identify the original source versions used for the experiment.

| Original dataset | Questions used | Original files to download; save under the source root |
| --- | ---: | --- |
| [AG News](https://huggingface.co/datasets/fancyzhx/ag_news) | 6 | [ag_news/data/train-00000-of-00001.parquet](https://huggingface.co/datasets/fancyzhx/ag_news/resolve/eb185aade064a813bc0b7f42de02595523103ca4/data/train-00000-of-00001.parquet) |
| [FANToM](https://github.com/skywalker023/fantom) | 17 | [fantom/fantom.tar.gz](https://storage.googleapis.com/ai2-mosaic-public/projects/fantom/fantom.tar.gz) |
| [MiniSCAN](https://github.com/linlu-qiu/lm-inductive-reasoning) | 33 | [miniscan/data/scan_rand.jsonl](https://raw.githubusercontent.com/linlu-qiu/lm-inductive-reasoning/0eae21f3d3014b92be34c80b23c9120a7b15a51f/data/scan_rand.jsonl)<br>[miniscan/data/scan.jsonl](https://raw.githubusercontent.com/linlu-qiu/lm-inductive-reasoning/0eae21f3d3014b92be34c80b23c9120a7b15a51f/data/scan.jsonl) |
| [NEWTON](https://huggingface.co/datasets/NEWTONReasoning/NEWTON) | 31 | [newton/confident_questions.csv](https://huggingface.co/datasets/NEWTONReasoning/NEWTON/resolve/b55ed6d1ee3e1a1c3c142a5fe79df39319599626/confident_questions.csv)<br>[newton/explicit_questions.csv](https://huggingface.co/datasets/NEWTONReasoning/NEWTON/resolve/b55ed6d1ee3e1a1c3c142a5fe79df39319599626/explicit_questions.csv) |
| [ProofWriter](https://allenai.org/data/proofwriter) | 19 | [proofwriter/proofwriter.zip](https://aristo-data-public.s3.amazonaws.com/proofwriter/proofwriter-dataset-V2020.12.3.zip) |
| [SST-2](https://huggingface.co/datasets/stanfordnlp/sst2) | 6 | [sst2/data/train-00000-of-00001.parquet](https://huggingface.co/datasets/stanfordnlp/sst2/resolve/8d51e7e4887a4caaa95b3fbebbf53c0490b58bbb/data/train-00000-of-00001.parquet) |
| [TREC](https://cogcomp.seas.upenn.edu/Data/QA/QC/) | 6 | [trec/train_5500.label](https://cogcomp.seas.upenn.edu/Data/QA/QC/train_5500.label)<br>[trec/test_10.label](https://cogcomp.seas.upenn.edu/Data/QA/QC/TREC_10.label) |
| [PIQA](https://github.com/ybisk/ybisk.github.io/tree/master/piqa) | 30 | The explicit license-acceptance command below downloads the required original files and recovers the selected questions. |

A source file may contain many more questions than we used. The recovery tool extracts only our selected questions. Keep FANToM and ProofWriter as their original archives. For TREC, save the publisher's `TREC_10.label` as `trec/test_10.label`. [All dataset sources and attribution](docs/data-sharing.md) are listed separately.

For example, download MiniSCAN's two original files into the expected folders:

```bash
mkdir -p .local/original-sources/miniscan/data
curl --fail --location \
  --output .local/original-sources/miniscan/data/scan.jsonl \
  "https://raw.githubusercontent.com/linlu-qiu/lm-inductive-reasoning/0eae21f3d3014b92be34c80b23c9120a7b15a51f/data/scan.jsonl"
curl --fail --location \
  --output .local/original-sources/miniscan/data/scan_rand.jsonl \
  "https://raw.githubusercontent.com/linlu-qiu/lm-inductive-reasoning/0eae21f3d3014b92be34c80b23c9120a7b15a51f/data/scan_rand.jsonl"
```

You can also save the linked files through your browser. Preserve their bytes and names. The tool checks the recorded SHA-256 hashes before reading them; changed files are rejected.

### 2. Recover just our selected questions

After downloading MiniSCAN:

```bash
python3 -B tools/recover_withheld.py \
  --source-root .local/original-sources \
  --datasets miniscan
```

This writes only the **33 MiniSCAN questions used in the experiment** to `.local/withheld.questions.jsonl`, including the exact evaluated context, question, ordered answer choices and reference answer. The tool checks every reconstructed input against the experiment's saved hash. It reads your downloaded files; it does not download the other datasets or run any models.

To recover multiple downloaded sources together, pass their aliases, for example `--datasets miniscan newton`. AG News and SST-2 additionally require the [optional Parquet reader](docs/recovering-inputs.md#2-recover-the-118-questions). The other sources use the Python standard library.

For original URLs, expected file sizes and checksums for a selected source:

```bash
python3 -B tools/recover_withheld.py --datasets miniscan --list-files
```

Recovered text stays in `.local/`, which Git ignores. Use `--output .local/miniscan.questions.jsonl` to keep a separately named recovery file. See [the full recovery guide](docs/recovering-inputs.md) for combining multiple files or working with only the questions you have available.

### 3. Recover PIQA

Read [PIQA's AFL 3.0 terms](https://opensource.org/license/afl-3.0). If you accept them, this command downloads the required original source files and recovers the **30 PIQA questions we used**:

```bash
python3 -B tools/recover_piqa.py --accept-afl-3.0
```

The output is `.local/piqa.questions.jsonl`. PIQA question text is not bundled in this repository.

### 4. Optionally assemble all 1,005 inputs

Once you have obtained the files for all seven other sources, recover them together by omitting `--datasets`:

```bash
python3 -B tools/recover_withheld.py --source-root .local/original-sources
python3 -B tools/assemble_inputs.py
```

After PIQA recovery, assembly combines the **857 bundled + 118 recovered + 30 PIQA** inputs into `.local/questions.complete.jsonl`. It checks all 1,005 IDs, complete inputs, choice ordering and reference answers.

To work with the bundled questions and any recovery files you have already created, use `python3 tools/assemble_inputs.py --partial`. This writes `.local/questions.available.jsonl` and reports its actual question count; it does not label a partial set as the full baseline.

## Inspect one question

The question pages are intended for reading in GitHub. For the machine-readable version:

```bash
python3 baseline.py inspect --case bbh/639b88b1fe80634a7d66
```

To inspect a question recovered from another source, add `--local-questions .local/questions.complete.jsonl` (or the specific recovery file containing it). The command checks its input fingerprint before displaying the text and recorded answers.

Released inputs contain the complete evaluated `state`, `question`, and ordered `choices`, rather than a shortened display example. They also retain the reference answer and original-source attribution. For questions obtained separately, the recovery workflow supplies the exact input locally.

## Run models again

[Recover the full 1,005-question set](docs/recovering-inputs.md) from independently obtained original files. The recovery tools verify the exact inputs and keep held text in ignored local storage.

The [reproduction instructions](docs/reproduction.md) walk through API key setup, sending requests, building the GPU containers, downloading the pinned weights, running all models and scoring fresh answers. Fresh inference requires model access and infrastructure, and can incur API or GPU charges.

Fresh predictions can differ from the saved results as models, routing or sampling change.

You can also [connect directly to a provider or test your own model](docs/connecting-models.md) using the same questions and scoring code. The guide explains endpoints, API keys and model IDs, with example connection files.

## Repository map

| Folder | What you will find |
| --- | --- |
| [`questions/`](questions/README.md) | Readable capability indexes and individual question pages |
| [`data/`](data/README.md) | All 1,005 question metadata records, released full inputs, and sharing decisions |
| [`results/`](results/README.md) | All 13,065 baseline outcomes, including failed and refused requests |
| [`summaries/`](summaries/README.md) | Small CSV tables for checking the reported numbers |
| [`evaluation/`](evaluation/README.md) | Offline request construction and native inference reference code |
| [`configs/`](configs/README.md) | Model IDs, pinned checkpoints, runtime settings, and input encoding fingerprints |
| [`docs/`](docs/methods.md) | Methods, reproduction instructions, and source-sharing notes |
| [`licenses/`](licenses/README.md) | Original source notices and per-source terms |

[`release_status.json`](release_status.json) records question coverage and source-sharing counts. [`provenance.json`](provenance.json) records input and evaluation provenance. [`MANIFEST.json`](MANIFEST.json) contains file checksums.

## Attribution and licensing

The questions retain their original dataset licenses and attribution. This repository bundles 857 complete inputs; the other 148 are recovered from original source files. See [source terms and notices](licenses/README.md) and [question-sharing decisions](docs/data-sharing.md).

Third-party datasets, downloaded model code and weights, and Raindrop brand artwork retain their own terms.

## About this research

Research by Afika Nyati at [Raindrop](https://www.raindrop.ai/), accompanying *The subtle art of making judgment calls* (2026). The [post](https://dawn-landing-git-codex-judgment-calls-blog.previews.raindrop.ai/blog/judgment-calls/) explains the findings; the [methods](docs/methods.md) and saved question-level outcomes document what was measured.

## Data format and scoring

Match a result’s `case_id` to the question’s `id`. Match its `model` to a key in `configs/models.json`, and its `configuration_id` to a key in `configs/result_configurations.json`. JSONL files contain one JSON object per line. The [question-file guide](data/README.md) and [result-field guide](results/README.md) describe the fields, choice order, reference answers and input fingerprints.

The [scoring definitions](docs/methods.md#scoring) explain accuracy, coverage, precision and recall. Use the saved model configurations and [measurement conditions](configs/measurement_conditions.json) when interpreting or reproducing a result.

## Citation

Afika Nyati. *The subtle art of making judgment calls.* Raindrop, 2026. [Read the post](https://dawn-landing-git-codex-judgment-calls-blog.previews.raindrop.ai/blog/judgment-calls/).

```bibtex
@misc{nyati2026judgmentcalls,
  author = {Afika Nyati},
  title = {The subtle art of making judgment calls},
  year = {2026},
  howpublished = {Raindrop},
  url = {https://dawn-landing-git-codex-judgment-calls-blog.previews.raindrop.ai/blog/judgment-calls/}
}
```

Machine-readable citation metadata is in [CITATION.cff](CITATION.cff).

## Questions and corrections

Contact Afika Nyati at [afika@raindrop.ai](mailto:afika@raindrop.ai).

For a result or dataset issue, include the question ID, model name, the recorded answer and expected behavior, and enough detail to reproduce the issue. [CONTRIBUTING.md](CONTRIBUTING.md) explains how to prepare a useful report or a change using the saved data.
