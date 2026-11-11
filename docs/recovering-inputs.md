# Recover all 1,005 evaluated inputs

The companion includes 857 complete questions. The other 148 can be reconstructed locally from the original files: 30 with the PIQA tool and 118 with the remaining-source tool. Every recovered input must match the recorded question ID, input hash, reference answer and choice order.

Obtain the source files under their publishers’ access and use terms. Recovery stores the selected texts in an ignored local folder and verifies them against the evaluated inputs.

## 1. Obtain the original files

We include question text only where the source terms clearly support sharing it in this repository. For these 148 questions, permission to redistribute the text is unclear or additional license conditions apply, so we provide links and recovery tools instead. The [data-sharing guide](data-sharing.md) explains the source-specific reasons. Download the original files from the links below, or use matching source files you already have under the applicable terms. The recovery tool then reads those local files and reconstructs only the questions selected for this experiment.

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

The [README's worked MiniSCAN example](../README.md#1-download-the-original-files-you-need) shows the exact download commands. The generic recovery tool does not download files; PIQA's separate explicit-acceptance command does.

List the required files and their original URLs, pinned revisions, sizes and SHA-256 checksums:

```bash
python3 -B tools/recover_withheld.py --list-files
```

Obtain those files from the listed publishers where permitted. Place them under a local source root with this structure:

```text
/path/to/original-sources/
├── ag_news/data/train-00000-of-00001.parquet
├── fantom/fantom.tar.gz
├── miniscan/data/scan.jsonl
├── miniscan/data/scan_rand.jsonl
├── newton/confident_questions.csv
├── newton/explicit_questions.csv
├── proofwriter/proofwriter.zip
├── sst2/data/train-00000-of-00001.parquet
├── trec/train_5500.label
└── trec/test_10.label
```

The original download for `trec/test_10.label` is named `TREC_10.label`; save it under the local name shown here. Preserve the file bytes. Keep FANToM and ProofWriter as their original archives; the tool reads only the needed members without extracting or executing anything.

If an original URL is unavailable, use a lawfully obtained copy with the matching checksum or ask the source maintainer about availability. Follow any access or use restrictions stated by that source; ask for clarification only where the intended use is not clearly covered. The tool rejects a different file rather than silently replacing questions. Original URLs and hashes remain available in [`data/sources.json`](../data/sources.json).

## 2. Recover the 118 questions

AG News and SST-2 use Parquet files and need the optional data-reading dependency:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r tools/requirements-recovery.txt
```

These activation commands are for Bash on macOS or Linux. Keep using the activated environment for Parquet recovery. If you already have a virtual environment, activate it instead of creating another. Offline scoring and recovery of the other sources use the Python standard library. Reconstruct the seven sources from your local files:

```bash
python3 -B tools/recover_withheld.py \
  --source-root /path/to/original-sources
```

This writes `.local/withheld.questions.jsonl` and a local recovery receipt. The tool makes no downloads or inference calls. It checks the original file hashes before reading them, then verifies all 118 reconstructed inputs. MiniSCAN's answer choices are regenerated using the experiment's original deterministic grammar procedure. FANToM's correct/incorrect native answers are placed in the exact saved choice order.

### Recover only selected datasets

Use `--datasets` to select one or more sources whose original files you have obtained. For example:

```bash
python3 -B tools/recover_withheld.py \
  --source-root /path/to/original-sources \
  --datasets miniscan newton
```

Only MiniSCAN's 33 questions and NEWTON's 31 questions are reconstructed. The tool does not read or require the other datasets' source files. It writes those **64 exact inputs** to `.local/withheld.questions.jsonl`.

Supported aliases are `ag_news`, `fantom`, `miniscan`, `newton`, `proofwriter`, `sst2`, and `trec`. PIQA has its separate license-acceptance command below. To list only the selected sources' required original files:

```bash
python3 -B tools/recover_withheld.py --datasets miniscan newton --list-files
```

The recovered questions are available in the local JSONL file. Use that partial file directly when preparing a request for one of its questions:

```bash
python3 -B evaluation/request_specs.py \
  --model jev --case miniscan/3ccbac4b6dd01753ac46 \
  --local-questions .local/withheld.questions.jsonl
```

This prints the request without sending it. You can use a partial input file without assembling the complete set.

The default output is `.local/withheld.questions.jsonl`. Give separate batches their own output names so one does not replace another:

```bash
python3 tools/recover_withheld.py \
  --source-root .local/original-sources --datasets miniscan \
  --output .local/miniscan.questions.jsonl
```

The output path must be inside `.local/`. Assembly accepts these separately named files with `--additional`.

## 3. Recover PIQA

Read [AFL 3.0](https://opensource.org/license/afl-3.0). If you accept its terms:

```bash
python3 -B tools/recover_piqa.py --accept-afl-3.0
```

This downloads only the required original PIQA files, checks their recorded hashes, and writes `.local/piqa.questions.jsonl`. A local receipt records license acceptance and source attribution; it is ignored by Git along with the recovered text.

If you already have the source files, recover them without downloading:

```bash
python3 tools/recover_piqa.py --accept-afl-3.0 \
  --source-dir /path/to/piqa-source-root
```

That directory must contain `piqa/data/train.jsonl` and `piqa/data/train-labels.lst` from the recorded source revision. The same license acceptance and hash checks apply.

## 4. Assemble the complete set

```bash
python3 -B tools/assemble_inputs.py
```

This combines the 857 released questions, 30 PIQA inputs and 118 other recovered inputs, verifies the complete 1,005-question inventory, and saves `.local/questions.complete.jsonl`. Missing inputs, duplicates, changed answers, changed text or changed choice order stop assembly before the output is replaced.

For separately named recovery fragments:

```bash
python3 -B tools/assemble_inputs.py \
  --additional .local/piqa.questions.jsonl .local/part-one.jsonl .local/part-two.jsonl
```

The `.local/` directory is ignored by Git. Assembly does not change what is distributed in `data/questions.jsonl` or on the public question pages.

### Work with fewer than 1,005 questions

You can inspect or run the 857 bundled questions without recovering any additional text:

```bash
python3 tools/assemble_inputs.py --partial
```

This creates `.local/questions.available.jsonl`, containing only the verified available inputs. To add separately recovered files:

```bash
python3 tools/assemble_inputs.py --partial \
  --additional .local/miniscan.questions.jsonl
```

This combines the 857 bundled and 33 recovered MiniSCAN inputs, for 890 questions. Omit `--additional` to include whichever default PIQA and remaining-source recovery files exist. Partial assembly always reports its actual count and uses `questions.available.jsonl`; the default complete-set command still requires all 1,005 questions.

Use the available file both to select questions and to supply their text:

```bash
python3 evaluation/run_api.py --model jev \
  --cases-file .local/questions.available.jsonl \
  --local-questions .local/questions.available.jsonl \
  --output .local/api/jev-available
```

That command sends one request per question in the file. Scoring compares exactly those same questions with the saved baseline. It does not present a partial run as a full-baseline score.

### Recover only what the binary subset needs

Of the 214 binary questions, 205 have their full text bundled. The remaining nine are six SST-2 questions and three NEWTON questions. You do not need the other held datasets to rerun this subset.

Download the SST-2 and NEWTON source files listed above, install the optional Parquet reader, then run:

```bash
python3 tools/recover_withheld.py \
  --source-root .local/original-sources --datasets sst2 newton \
  --output .local/binary-sources.questions.jsonl
python3 tools/assemble_inputs.py --partial \
  --additional .local/binary-sources.questions.jsonl
python3 evaluation/run_api.py --model jev \
  --cases-file data/binary_subset.csv \
  --local-questions .local/questions.available.jsonl \
  --output .local/api/jev-binary
```

Recovery reconstructs all 37 selected SST-2/NEWTON questions; the CSV then selects exactly the 214 binary questions for inference. The source-file and input-hash checks remain the same.

## 5. Verify results or prepare a fresh evaluation

The saved results can be scored without recovering any held text:

```bash
python3 -B baseline.py verify
python3 -B baseline.py summarize
```

The regenerated summaries are written to `.local/summaries/`. To read a recovered question together with its saved model answers:

```bash
python3 baseline.py inspect --case QUESTION_ID \
  --local-questions .local/questions.complete.jsonl
```

Use the actual question ID and a complete or partial input file containing it.

To prepare an API request using a recovered input:

```bash
python3 -B evaluation/request_specs.py \
  --model jev --case QUESTION_ID \
  --local-questions .local/questions.complete.jsonl
```

That constructs a request without sending it. [Reproduction instructions](reproduction.md) describe the separate API and isolated GPU evaluation steps. Fresh model outputs can differ; rebuilding exact inputs makes the experiment repeatable but does not guarantee identical future predictions.
