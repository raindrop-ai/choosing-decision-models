# Recorded variant answers

[Read results](../../docs/variant-results.md) · [Explore questions](../../variants/README.md) · [Comparison methods](../../docs/variant-methods.md)

Each of the eleven model files contains one row per variant: **24,563 rows per model**. These include successful answers, errors, refusals, unresolved requests and inputs outside the model's supported limit. An unsupported input is not an attempted prediction.

Model files are named by their [command aliases](../../configs/models.json): `glide.jsonl`, `decider11.jsonl`, `jev.jsonl`, `microsoft-decision-1.jsonl`, `clef.jsonl`, `openai-decisions.jsonl`, `clef-flash.jsonl`, `strands.jsonl`, `gliner.jsonl`, `laya.jsonl` and `caldec.jsonl`.

| Field | Meaning |
| --- | --- |
| `case_id`, `model`, `input_hash` | Variant ID, model alias and fingerprint of its complete evaluated input. |
| `status` | `ok`, `refusal`, `error`, `unknown`, `unknown_prior_attempt` or `not_supported`. Unresolved outcomes are not successful answers. |
| `prediction` | The chosen answer key; null when no usable answer is available. |
| `original_result_id` | Exact linked original response in [original-controls.jsonl](original-controls.jsonl), or null for an unsupported input. |
| `source_result_id` | Opaque identity of the saved response supplying this logical outcome. |
| `source_case_id`, `source_input_hash`, `input_alias` | Proven native-input equivalence can let more than one logical condition use the same response. These retain the source relationship. |
| `recovered_error` | True for a Clef answer recovered after an initial execution error. The analysis uses the recovered answer. |

The same original can have more than one control response. Join through `original_result_id`, rather than selecting an arbitrary row by original ID and model. Reference answer keys and links to the full-text pages are in [the manifest](../../data/variants/manifest.jsonl).
