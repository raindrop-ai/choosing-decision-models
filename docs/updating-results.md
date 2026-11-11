# Update baseline records

The offline updater imports a complete set of predictions for the eight self-hosted models while preserving the five hosted models’ records. It requires the same 1,005 question IDs, complete input hashes, ordered choices and reference answers.

To compare your own rerun, use the [fresh-run scorer](reproduction.md#4-score-fresh-api-answers); it leaves the reference results unchanged. This updater is for maintainers deliberately replacing the reference dataset.

## Prepare two input files

Supply the **original-question outcomes** in a normalized JSONL file. Include all 1,005 cases for each of `glide`, `decider11`, `clef`, `clef-flash`, `strands`, `gliner`, `laya`, and `caldec`. Keep perturbation results in their separate dataset.

Each line has this shape (the values below illustrate the schema):

```json
{
  "case_id": "bbh/639b88b1fe80634a7d66",
  "model": "glide",
  "input_hash": "COPY_THE_EXACT_QUESTION_MANIFEST_HASH",
  "status": "ok",
  "prediction": "A",
  "probabilities": null,
  "latency_ms": 100.0,
  "billed_cost_usd": null,
  "requested_model": "fastino/GLiDE",
  "model_revision": "d199b6d7e04523d87986b8b68cd62272ed1cefc0",
  "timing_class": "subsequent_forward",
  "timing_included": true
}
```

Use saved native probabilities when available. `status` may be `ok`, `error`, or `refusal`; unsuccessful records have a null prediction. Include errors and refusals, and use the `input_hash` of the actual evaluated input.

For a first-forward observation (`first_forward_with_kernel_startup`), retain its latency and prediction but set `timing_included` to `false`. Its answer still contributes to accuracy; its startup timing does not enter the steady timing summary. Unknown cost remains null.

The second file is a JSON object keyed by the eight model aliases. Each entry supplies the actual model configuration, GPU, and percentile method:

```json
{
  "glide": {
    "configuration": {
      "backend": "modal",
      "kind": "glide",
      "model_id": "fastino/GLiDE",
      "revision": "d199b6d7e04523d87986b8b68cd62272ed1cefc0",
      "gpu": "A100-80GB",
      "max_input_tokens": 40000,
      "dtype": "bfloat16",
      "version": "1.2"
    },
    "gpu": "A100-80GB",
    "timing_percentile_method": "nearest_rank"
  }
}
```

Include the other seven entries too. Use the configurations that produced the predictions. Model IDs and pinned revisions must match the current roster. `linear` uses interpolation between adjacent observations; `nearest_rank` is also supported for sources using that convention.

## Validate, then replace

From the companion root, first perform an offline dry run:

```bash
python3 -B tools/replace_results.py \
  --predictions /path/to/new-original-predictions.jsonl \
  --configurations /path/to/new-modal-configurations.json
```

The command validates coverage, duplicate IDs, input hashes, choice keys, model identity, probabilities, timings, and costs. It builds and verifies a candidate copy in a temporary directory. The default leaves current files untouched.

To apply a validated import:

```bash
python3 -B tools/replace_results.py \
  --predictions /path/to/new-original-predictions.jsonl \
  --configurations /path/to/new-modal-configurations.json \
  --apply
python3 -B baseline.py verify
python3 -B -m unittest discover -s tests -v
```

This refreshes the current JSONL and CSV results, model configurations, all four summary CSVs, readable question pages and indexes, result tables, provenance hashes, reference tables, and bundle checksums. The five hosted models’ records are preserved verbatim.

Reference tables are regenerated from the imported outcomes and provide integrity checks. Hardware evidence, runtime code and dependency versions must describe the imported predictions; update those files if the execution environment changes.

The updater runs entirely offline.
