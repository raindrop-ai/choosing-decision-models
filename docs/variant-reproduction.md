# Verify or rerun the variants

[Explore inputs](../variants/README.md) · [Methods](variant-methods.md) · [Results](variant-results.md) · [Connect a model](connecting-models.md)

Run these commands from a terminal in the repository root with Python 3.10 or later. Verification uses only saved files. Fresh model requests can incur charges.

## Check saved answers offline

```bash
python3 variants.py verify
python3 variants.py summarize
```

The first command checks the inventory, input fingerprints, original-control links, coverage and recomputed comparison tables. The second writes a fresh table to `.local/variant-summaries/comparisons.csv`. No paid requests or GPU programs run.

## Inspect a question and its versions

Start with an [original question](../questions/README.md), then follow its link to the variant index. Each variant page includes its exact ID, which can be passed to:

```bash
python3 variants.py inspect --case VARIANT_ID
```

Replace `VARIANT_ID` with the complete ID shown on that page. The command prints its input when included, all recorded model answers and their linked original controls. For locally recovered text, add `--local-questions .local/variants.complete.jsonl`.

## Recover the remaining variant texts

The repository includes 20,961 full variant inputs. The remaining 3,602 derive from originals with additional redistribution requirements or unclear permission to republish. [Download and recover the original source questions](recovering-inputs.md), then assemble all 1,005 originals:

```bash
python3 tools/assemble_inputs.py
python3 variants.py recover --originals .local/questions.complete.jsonl
```

Recovery reads your original texts and the saved edit recipes, then reconstructs only the selected variants. It checks the parent input and every reconstructed variant against their recorded fingerprints. It writes all 24,563 complete inputs to `.local/variants.complete.jsonl`. There is no language-model generation step, and recovered source text remains outside Git.

## Select inputs for a fresh run

For a small example, select the variants of one bundled question:

```bash
python3 variants.py inputs --model jev \
  --original bbh/639b88b1fe80634a7d66 \
  --output .local/jev-example-variants.jsonl
```

To select the full variant set that fits every recorded model, after recovery:

```bash
python3 variants.py inputs --model jev --common \
  --local-questions .local/variants.complete.jsonl \
  --output .local/jev-variants.jsonl
```

`--common` selects the 23,374 common-fit inputs. Omit it to include all inputs supported by the chosen model. `--model` uses a recorded command name such as `jev`, `glide` or `decider11`; supported input sets differ by model. Errors and refusals do not remove inputs from this selection.

To work only with public texts, add `--available-only` and omit `--local-questions`. This explicitly creates a partial set, not the full experiment. `--original` selects a single original; `--capability` selects the capability name recorded in the manifest. The command reports the actual selected count and checks complete text, answer choices and input fingerprints before writing the file.

## Send the selected questions to an API

For the study's Jev connection:

```bash
python3 evaluation/run_api.py --model jev \
  --cases-file .local/jev-variants.jsonl \
  --local-questions .local/jev-variants.jsonl \
  --output .local/api/jev-variants
```

For a provider directly or a model server you control, first follow [Connect a model](connecting-models.md), then use its connection file:

```bash
python3 evaluation/run_api.py --model my-model \
  --connection .local/provider-model.json \
  --cases-file .local/jev-variants.jsonl \
  --local-questions .local/jev-variants.jsonl \
  --output .local/api/my-model-variants
```

The model receives the full input and ordered choices, never the reference answer. The selected file defines the question set; a new model may have a different input limit. Confirm that its complete inputs fit rather than truncating them.

## Run a downloaded decision model on a GPU

Follow the [baseline GPU setup](reproduction.md#run-the-self-hosted-models) to install Docker on a Linux GPU machine, build the pinned images, stage model files and probe the device. The program in this repository loads each model directly; it is not a separate hosted service and does not require Modal.

Select that model's supported inputs:

```bash
python3 variants.py inputs --model glide --common \
  --local-questions .local/variants.complete.jsonl \
  --output .local/glide-variants.jsonl

python3 evaluation/prepare_native.py --model glide \
  --cases-file .local/glide-variants.jsonl \
  --local-questions .local/glide-variants.jsonl \
  --stage-result .local/native/io/stage-result.json \
  --device .local/native/io/device.json \
  > .local/native/io/glide-variant-job.json
```

Run the job using the same image and mounted directories as the baseline guide:

```bash
docker run --rm --gpus "device=$JUDGMENT_GPU_UUID" \
  --user "$(id -u):$(id -g)" --network none --read-only \
  --cpus 2 --memory 64g --shm-size 1g \
  --tmpfs /tmp:rw,exec,size=16g,mode=1777 \
  --env HF_HUB_OFFLINE=1 --env TRANSFORMERS_OFFLINE=1 \
  --mount "type=bind,src=$PWD/.local/native/staged,dst=/models,readonly" \
  --mount "type=bind,src=$PWD/.local/native/io,dst=/io" \
  judgment-large python device_worker.py infer \
  /io/glide-variant-job.json /io/glide-variant-result.json
```

Change the alias and image for another model using the baseline guide's table. The recorded variant runs include reused predictions and multiple execution configurations; [the configuration records](../configs/variant-study.json) and [linked original controls](variant-methods.md#linking-each-variant-to-its-original-answer) describe the observations used in analysis. A fresh run need not reproduce individual stochastic answers exactly.

## Score fresh outputs

For API output:

```bash
python3 evaluation/score_fresh.py \
  --input .local/api/jev-variants/predictions.jsonl \
  --job .local/api/jev-variants/run.json \
  --output-dir .local/api/jev-variants/comparison
```

For the GPU receipt:

```bash
python3 evaluation/score_fresh.py \
  --input .local/native/io/glide-variant-result.json \
  --job .local/native/io/glide-variant-job.json \
  --output-dir .local/native/glide-variants-comparison
```

The scorer reports accuracy and coverage for the selected variants and compares their answers with the corresponding saved variant results. It does not mistake a fresh variant score for the full original-question baseline. For a new model, add `--compare-to glide` or another recorded alias to compare on the same selected inputs; omit it for scores alone.

## Compare fresh original and variant answers

Run the originals as well as the variants using the same model name and serving setup. The [baseline guide](reproduction.md) gives the original-question commands. For a custom model, keep its `--connection` file the same in both phases.

Create `.local/fresh-variant-runs.json` in a text editor:

```json
{
  "originals": {
    "job": "api/jev-baseline/run.json",
    "output": "api/jev-baseline/predictions.jsonl"
  },
  "variants": {
    "job": "api/jev-variants/run.json",
    "output": "api/jev-variants/predictions.jsonl"
  }
}
```

Paths in this file are relative to the file's own folder. For a GPU run, use its job and result JSON paths instead. Then run:

```bash
python3 evaluation/score_variants.py \
  --runs .local/fresh-variant-runs.json \
  --output .local/fresh-variant-comparisons.csv
```

This command uses the exact [comparison families](../data/variants/comparisons.json), linking your fresh variants to your fresh original answers. It writes the same comparison columns as the saved-results summaries, overall and by capability. Missing or unsuccessful responses reduce `paired`; they do not remove a question from `bases`. A partial run therefore produces partial coverage, rather than pretending to reproduce the entire experiment.

`score_fresh.py` compares a new run with the saved predictions on the same inputs. `score_variants.py` instead compares your fresh versions with each other to measure the manipulation effects.
