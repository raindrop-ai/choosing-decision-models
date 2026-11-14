# Recorded baseline answers

There are **13,065 records**: 1,005 questions × 13 models. Each record contains one model’s outcome for one question. Refusals and errors are retained explicitly.

- [`baseline_predictions.csv`](baseline_predictions.csv) is convenient for a spreadsheet or GitHub's CSV viewer.
- [`baseline_predictions.jsonl`](baseline_predictions.jsonl) also includes native probability vectors where available, model identity fields, and input-fit diagnostics.

| Field | Meaning |
| --- | --- |
| `case_id`, `model` | Match `case_id` to the question manifest’s `id`; match `model` to a key in `configs/models.json` |
| `input_hash` | Fingerprint of the complete evaluated input, including choice order |
| `status` | `ok`, `refusal`, or `error` |
| `prediction` | Chosen answer key for successful outcomes; null otherwise |
| `probabilities` | Native per-choice probabilities when the runtime supplied them; null for unavailable vectors. These are not assumed calibrated or comparable across providers. |
| `latency_ms` | Saved timing observation; its scope differs between API and GPU-worker results |
| `timing_included` | Optional; false keeps a startup observation out of timing summaries while retaining its answer for accuracy |
| `billed_cost_usd` | Original recorded API charge, retained for reconciliation; may include Vercel AI Gateway fees. Null means unavailable, not zero-cost |
| `inference_cost_usd` | Model inference charge used in cost summaries, including applicable output and cache charges, excluding Vercel AI Gateway fees |
| `gateway_fee_usd` | Vercel AI Gateway portion of the original recorded charge, excluded from reported model costs; the two components sum to `billed_cost_usd` |
| `configuration_id` | Key into `configs/result_configurations.json` for the configuration of this actual saved result |
| `reused_result` | Whether an input- and configuration-matched prediction was reused |
| `runtime_input_check` | Recorded input-fit checks, where available |

Join `prediction` to a released question's `choices` to read the selected answer. For held inputs, choice keys remain available but their descriptions are not republished.


Fresh runs are saved separately. The [fresh-run scorer](../docs/reproduction.md#4-score-fresh-api-answers) compares the same selected question IDs with their saved baseline answers and can write a CSV of changes.

## Variant answers

The eleven decision models’ altered-input results and their exact original controls are in [results/variants](variants/README.md). [Read the findings and field definitions](../docs/variant-results.md).
