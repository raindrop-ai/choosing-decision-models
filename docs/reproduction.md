# Verify or rerun the baseline

You can check the saved scores with Python alone, or connect models and run fresh predictions. We accessed hosted models through Vercel AI Gateway and ran downloadable models using the included Python code on a GPU. You can also [connect a provider directly or use your own model server](connecting-models.md). Fresh inference can incur API or GPU charges.

Run the commands below from the repository root. The shell examples use Bash. Fresh outputs go under `.local/`, which Git ignores; they do not replace the published results.

## Check the reported numbers offline

Install Python 3.10 or later, then run:

```bash
python3 baseline.py verify
python3 baseline.py summarize
python3 -m unittest discover -s tests -v
```

These commands require no extra packages, credentials or model downloads. They check all 13,065 outcomes, input fingerprints, choice ordering, accuracy, coverage, binary error counts and saved cost/timing summaries. `summarize` writes new CSVs to `.local/summaries/`, leaving the published files unchanged. Use `--output /path/to/output-folder` to choose another destination.

## Prepare the question inputs

The repository includes 857 complete questions. [Recover the other 148 from their original sources](recovering-inputs.md), then assemble the complete input file:

```bash
python3 tools/assemble_inputs.py
```

The output is `.local/questions.complete.jsonl`. Assembly checks the exact 1,005 question IDs, full text, ordered choices and reference answers. Complete recovery is required for the `--all` examples below. The single-question examples below use a bundled input, so no recovery is needed: omit `--local-questions` for those examples. You can also [run only the questions you have available](recovering-inputs.md#work-with-fewer-than-1005-questions).

If you already have the full evaluated inputs in a JSONL file, import them instead:

```bash
python3 tools/import_local_questions.py --source /path/to/baseline-inputs.jsonl
```

## Connect the hosted models

### 1. Get access to Vercel AI Gateway

Sign in to Vercel, open **AI Gateway → API Keys** in the team you want to use, and create an API key. Check that the account has access and credits for the requested models. Vercel's [API key instructions](https://vercel.com/docs/ai-gateway/getting-started/text) explain the setup.

The client accepts `AI_GATEWAY_API_KEY` from your environment. If it is not set and you run the command interactively, it prompts for the key without echoing it. You do not need separate provider keys for this Gateway route. Keep your key out of source files and commits.

The configured models are:

| Model | Command name | Gateway model ID | Request format |
| --- | --- | --- | --- |
| Jev | `jev` | `typesafe-ai/jev` | Evaluation v4 |
| Microsoft Decision-1 | `microsoft-decision-1` | `microsoft/microsoft-decision-1` | Evaluation v4 |
| Luna Decisions | `openai-decisions` | `openai/gpt-6-luna-decisions` | Decisions v1 |
| Astra | `astra` | `openai/gpt-6-astra` | Chat completions with structured output |
| Opus 5.5 | `opus55` | `anthropic/claude-opus-5.5` | Chat completions with structured output |

These are the identifiers and request formats used in the study, recorded in [`models.json`](../configs/models.json). Availability can change. If an identifier or endpoint is no longer available to your account, retain that failure rather than silently substituting another model or API. The LLM requests use high reasoning effort and an 8,192-token output limit.

### 2. Inspect or send one request

This command only displays the exact URL, protocol headers and request body. It does not send anything or include your key:

```bash
python3 evaluation/request_specs.py \
  --model jev --case bbh/639b88b1fe80634a7d66
```

This command **sends one request** using the same request builder:

```bash
python3 evaluation/run_api.py \
  --model jev --case bbh/639b88b1fe80634a7d66 \
  --output .local/api/jev-example
```

The client adds `Content-Type: application/json` and `Authorization: Bearer …` in memory. It uses the protocol headers required by each model, sends the full question and choices, and never sends the reference answer or capability label.

The output directory contains `run.json` with the selected IDs and input hashes, `raw/` with each original response, and `predictions.jsonl` with parsed answers. Provider-reported model identity, errors and refusals remain available. Provider cost and usage fields remain in the raw responses. No automatic retries, model substitutions or overwrites are performed. A request or response-validation error stops the batch; the saved records show how far it got. An interrupted request may still have been billed.

### 3. Run all 1,005 questions

Use a new output directory for each run:

```bash
python3 evaluation/run_api.py \
  --model jev --all \
  --local-questions .local/questions.complete.jsonl \
  --output .local/api/jev-baseline
```

Repeat with the other command names in the table. To run all five sequentially with an API key already set in your environment:

```bash
for model in jev microsoft-decision-1 openai-decisions astra opus55; do
  python3 evaluation/run_api.py \
    --model "$model" --all \
    --local-questions .local/questions.complete.jsonl \
    --output ".local/api/$model-baseline" || break
done
```

This sends up to 5,025 requests. Each model processes one question at a time. For noninteractive use, supply the environment variable through your shell or secret manager; the client does not read `.env` files automatically.

To run only the article's 214-question binary subset, select its CSV instead of `--all`:

```bash
python3 evaluation/run_api.py --model jev \
  --cases-file data/binary_subset.csv \
  --local-questions .local/questions.complete.jsonl \
  --output .local/api/jev-binary
```

If you have not recovered the complete dataset, [recover just the two sources needed for this subset](recovering-inputs.md#recover-only-what-the-binary-subset-needs) and use the resulting available-input file instead.

`--cases-file` also accepts a question-input JSONL file or a text file with one question ID per line. It preserves that file's order and rejects duplicate or unknown IDs. If a selected question's text is not bundled, pass a local input file containing it with `--local-questions`; validation finishes before any requests are sent.

### 4. Score fresh API answers

```bash
python3 evaluation/score_fresh.py \
  --input .local/api/jev-baseline/predictions.jsonl \
  --job .local/api/jev-baseline/run.json \
  --output-dir .local/api/jev-baseline/comparison
```

The scorer reports correct answers, answered-question accuracy, coverage, missing records, the capability breakdown, and binary precision and recall using the same reference labels as the saved baseline. It also scores the saved baseline over exactly the same selected IDs, so a subset run is compared with the matching baseline subset.

The new comparison directory contains `report.json` and `answer_changes.csv`. The CSV identifies questions whose answer or outcome status changed. The report separates correct-to-wrong and wrong-to-correct answers from changes in coverage. An unanswered or missing prediction is not counted as a changed successful answer.

For a single-question or binary-subset run, replace `jev-baseline` with its output directory. The report's `selected` count shows which set was scored. The published full-set tables remain in [`summaries/`](../summaries/README.md).

## Run the self-hosted models

Here, **self-hosting** means running a downloaded model on hardware you control or rent, instead of sending requests to a model provider. The included Python program loads the model, prepares each question, runs a prediction and saves the answer. A “worker” here means this Python program: it loads the files and processes the questions. No separate worker service is required.

The setup uses **Docker**, which runs a program in an isolated environment with its own software dependencies. An **image** is the packaged environment; a **container** is a running instance of that image. **Model weights** are the downloaded files containing the trained model. A **job file** tells the Python program which model and questions to use. The instructions below create these files and connect them through mounted folders—directories shared between the host and container.

The host is the Linux machine with the GPU. The commands in this section are run in a terminal on that machine. If it is a rented server, connect using the terminal or SSH instructions from its provider. You do not need a Modal account to use this setup. SSH is a terminal connection to another computer; your provider supplies the username, address and login key.

Download or clone this repository onto that GPU machine, then change into the folder containing `baseline.py`, `evaluation/` and `workers/`. The `.local/` paths in the commands are folders on that machine. If you recovered questions on a different computer, copy the verified `.local/questions.complete.jsonl` file to the same relative location on the GPU host; recovered source text is not available from a Git clone. Run the remaining commands in the same terminal so the selected GPU variable stays set.

### 1. Set up a Linux GPU host

Use a Linux x86-64 machine with Docker, an NVIDIA driver compatible with the pinned PyTorch wheels, and the [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html). Install and configure Docker using [Docker's installation guide](https://docs.docker.com/engine/install/), then follow NVIDIA's instructions to configure its runtime for Docker.

For the article's measurement protocol, use one full **NVIDIA A100 80GB PCIe**, two CPU cores and 64 GiB of host memory. Keep the same physical GPU available for all eight models, running them sequentially. Allow at least 300 GB of free storage for the approximately 193 GB of model artifacts plus container images and caches. The container commands below run on this Linux host, not on a Mac laptop.

Confirm that the driver and Docker can see the GPU:

```bash
nvidia-smi
# NVIDIA's sample check; use sudo if your Docker installation requires it.
docker run --rm --runtime=nvidia --gpus all ubuntu:24.04 nvidia-smi
```

Select one device and keep that value for the entire run:

```bash
export JUDGMENT_GPU_UUID="$(nvidia-smi --query-gpu=uuid --format=csv,noheader | head -n 1)"
mkdir -p .local/native/staged .local/native/io
```

If the host has multiple GPUs, set `JUDGMENT_GPU_UUID` to the specific GPU you intend to use. Ensure no other workload is using it. NVIDIA documents the [sample workload check](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/sample-workload.html).

### 2. Build the two pinned environments

The included [`Dockerfile`](../workers/Dockerfile) installs Python 3.12, versioned compiler packages and the hash-locked dependencies. It copies only the native worker code; it does not copy credentials, datasets or local results into the image.

```bash
docker build --platform linux/amd64 \
  -f workers/Dockerfile -t judgment-core \
  --build-arg REQUIREMENTS_FILE=workers/requirements.txt .

docker build --platform linux/amd64 \
  -f workers/Dockerfile -t judgment-large \
  --build-arg REQUIREMENTS_FILE=workers/decision27.txt .
```

| Model | Command name | Image |
| --- | --- | --- |
| GLiDE v1.2 | `glide` | `judgment-large` |
| Decider v1.1 | `decider11` | `judgment-large` |
| Clef | `clef` | `judgment-core` |
| Clef Flash | `clef-flash` | `judgment-core` |
| Strands Decider | `strands` | `judgment-core` |
| GLiNER2.5 Decide | `gliner` | `judgment-core` |
| Laya | `laya` | `judgment-core` |
| CalDec v1 | `caldec` | `judgment-core` |

The environments are separate because the model loaders require different package versions. Do not install the inference requirements into your laptop's Python environment. The original experiment used Modal as the GPU rental platform; these Docker commands run the included worker on your own GPU host without requiring a Modal account.

### 3. Download the pinned weights

Prepare the download specification offline, then run staging in a networked CPU container:

```bash
python3 evaluation/prepare_native.py --stage-all > .local/native/io/stage.json

docker run --rm --user "$(id -u):$(id -g)" \
  --mount "type=bind,src=$PWD/.local/native/staged,dst=/models" \
  --mount "type=bind,src=$PWD/.local/native/io,dst=/io" \
  judgment-core python worker_entry.py stage /io/stage.json /io/stage-result.json
```

Staging downloads all eight pinned checkpoints, including the base model required by Strands. It checks required files and reviewed source hashes, then writes `/models/stage-manifest.json` and `/io/stage-result.json`. The latter supplies the manifest hash used for inference jobs. Staging downloads files without running the downloaded model code.

To try just one model, replace the first command with the following, then run the same staging container command:

```bash
python3 evaluation/request_specs.py --model glide --stage > .local/native/io/stage.json
```

This downloads only GLiDE's files. Change the model alias to choose another model. Use `--stage-all` before the full eight-model loop below.

The pinned snapshots were publicly downloadable without authentication, and the reference staging loader explicitly uses anonymous access. If a publisher removes a revision or restricts access, staging stops; do not substitute a newer revision. Model licenses still apply; checkpoint locations and revisions are in [`worker_sources.json`](../configs/worker_sources.json).

### 4. Check the GPU and prepare a job

Probe the selected device with networking disabled:

```bash
printf '{}\n' > .local/native/io/probe.json

docker run --rm --gpus "device=$JUDGMENT_GPU_UUID" \
  --network none --cpus 2 --memory 64g \
  --mount "type=bind,src=$PWD/.local/native/io,dst=/io" \
  judgment-core python device_worker.py probe /io/probe.json /io/device.json
```

The probe records the physical identity and checks for a full A100 80GB. Prepare a one-question job:

```bash
python3 evaluation/prepare_native.py \
  --model glide --case bbh/639b88b1fe80634a7d66 \
  --stage-result .local/native/io/stage-result.json \
  --device .local/native/io/device.json \
  > .local/native/io/glide-example-job.json
```

Prepare a full baseline job instead with:

```bash
python3 evaluation/prepare_native.py \
  --model glide --all --local-questions .local/questions.complete.jsonl \
  --stage-result .local/native/io/stage-result.json \
  --device .local/native/io/device.json \
  > .local/native/io/glide-job.json
```

The helper validates every input, sorts questions by ID, attaches the native encoding checks for GLiDE and Decider, and removes reference answers and capability labels before creating the inference job.

For the binary subset, replace `--all` with `--cases-file data/binary_subset.csv` and retain `--local-questions .local/questions.complete.jsonl`. For available-input runs, use `--cases-file .local/questions.available.jsonl --local-questions .local/questions.available.jsonl`. File-selected jobs retain the specified order; the full `--all` run uses sorted IDs as in the recorded measurement protocol.

### 5. Run inference

For the full GLiDE job:

```bash
docker run --rm --gpus "device=$JUDGMENT_GPU_UUID" \
  --user "$(id -u):$(id -g)" --network none --read-only \
  --cpus 2 --memory 64g --shm-size 1g \
  --tmpfs /tmp:rw,exec,size=16g,mode=1777 \
  --env HF_HUB_OFFLINE=1 --env TRANSFORMERS_OFFLINE=1 \
  --mount "type=bind,src=$PWD/.local/native/staged,dst=/models,readonly" \
  --mount "type=bind,src=$PWD/.local/native/io,dst=/io" \
  judgment-large python device_worker.py infer /io/glide-job.json /io/glide-result.json
```

For the single-question job, replace the last two paths with `/io/glide-example-job.json` and `/io/glide-example-result.json`. The GPU worker uses the staged files read-only and receives no API keys or network access. It verifies the GPU identity before and after inference and rejects input truncation.

To run all eight models sequentially on that same device:

```bash
for model in glide decider11 clef clef-flash strands gliner laya caldec; do
  case "$model" in
    glide|decider11) image=judgment-large ;;
    *) image=judgment-core ;;
  esac
  python3 evaluation/prepare_native.py \
    --model "$model" --all --local-questions .local/questions.complete.jsonl \
    --stage-result .local/native/io/stage-result.json \
    --device .local/native/io/device.json \
    > ".local/native/io/$model-job.json" || break
  docker run --rm --gpus "device=$JUDGMENT_GPU_UUID" \
    --user "$(id -u):$(id -g)" --network none --read-only \
    --cpus 2 --memory 64g --shm-size 1g \
    --tmpfs /tmp:rw,exec,size=16g,mode=1777 \
    --env HF_HUB_OFFLINE=1 --env TRANSFORMERS_OFFLINE=1 \
    --mount "type=bind,src=$PWD/.local/native/staged,dst=/models,readonly" \
    --mount "type=bind,src=$PWD/.local/native/io,dst=/io" \
    "$image" python device_worker.py infer "/io/$model-job.json" "/io/$model-result.json" || break
  python3 evaluation/score_fresh.py \
    --input ".local/native/io/$model-result.json" \
    --job ".local/native/io/$model-job.json" || break
done
```

Use a separate working directory for a later rerun to preserve its outputs. A worker receipt can include errors or unstarted questions even if the process writes its output successfully; check the scorer's statuses and coverage. Do not treat missing predictions as correct or remove failed questions from the selected set.

### 6. Score and compare

```bash
python3 evaluation/score_fresh.py \
  --input .local/native/io/glide-result.json \
  --job .local/native/io/glide-job.json \
  --output-dir .local/native/glide-comparison
```

The same scorer produces the matched baseline comparison and a CSV of answer/status changes for native outputs. It verifies the job's input hashes and the receipt's model and checkpoint before scoring.

The worker receipt contains question-level answers, probabilities, timing classes, runtime versions and GPU identity. For timing comparisons, retain the first prediction's answer but exclude its `first_forward_with_kernel_startup` timing. The wrapper sets seed zero, two CPU threads, batch size one and TF32 disabled. See [`measurement_conditions.json`](../configs/measurement_conditions.json) for the recorded protocol.

Fresh answers can differ from the saved results. API aliases, routing and sampling may change; hardware, drivers and numerical kernels can also affect a rerun. Keep the fresh outputs and configuration alongside the comparison rather than replacing `results/baseline_predictions.jsonl`.

## Setup troubleshooting

| Problem | What to check |
| --- | --- |
| Missing API key | Run interactively to enter it, or supply `AI_GATEWAY_API_KEY` in the environment. |
| API 401 or 403 | Check the key's team, validity and model access. |
| API model/endpoint unavailable | Check the account's available models; record the failure if the original identifier is unavailable. |
| HTTP 429, timeout or interrupted call | Inspect the saved records and provider dashboard. The client does not automatically resend requests. |
| Missing question text | Complete source recovery and pass `--local-questions .local/questions.complete.jsonl`. |
| Docker cannot see the GPU | Check `nvidia-smi`, the host driver and NVIDIA Container Toolkit configuration. |
| Dependency or compiler package unavailable | Keep the error and pinned versions; substituting packages creates a different environment. |
| Model artifact or encoding hash mismatch | Check the pinned revision, staged files and complete original inputs. Do not truncate or substitute. |
| GPU identity mismatch | Use the same selected full A100 80GB device for the entire comparison. |

## Rerun the altered questions

The [variant reproduction guide](variant-reproduction.md) covers recovery, selecting model-supported inputs, fresh requests and comparison with saved variant answers.
