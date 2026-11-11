# Unrelated examples · Add examples unrelated to the question variant

[Original question](../../../questions/uncertainty-monitoring/selfaware-38b07d3302a5fd5b77db.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Capitalization: harbor → Harbor
>
> At 51° 23' E, what is the easternmost point of the African continent?

## Question

> Does this question have a determinate answer?

## Answer choices

- **yes.** Answerable
- **no.** Unanswerable

**Reference answer:** `yes`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Capitalization: harbor → Harbor\n\nAt 51° 23' E, what is the easternmost point of the African continent?",
  "question": "Does this question have a determinate answer?",
  "choices": {
    "yes": "Answerable",
    "no": "Unanswerable"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `yes` — Answerable | `yes` — Answerable | Same answer |
| Decider v1.1 | `yes` — Answerable | `yes` — Answerable | Same answer |
| Jev | `yes` — Answerable | `yes` — Answerable | Same answer |
| Microsoft Decision-1 | `yes` — Answerable | `yes` — Answerable | Same answer |
| Clef | `yes` — Answerable | `yes` — Answerable | Same answer |
| Luna Decisions | `yes` — Answerable | `yes` — Answerable | Same answer |
| Clef Flash | `yes` — Answerable | `yes` — Answerable | Same answer |
| Strands Decider | `yes` — Answerable | `no` — Unanswerable | Different answer |
| GLiNER2.5 Decide | `yes` — Answerable | `yes` — Answerable | Same answer |
| Laya | `no` — Unanswerable | `no` — Unanswerable | Same answer |
| CalDec v1 | `no` — Unanswerable | `no` — Unanswerable | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `selfaware/38b07d3302a5fd5b77db/examples/irrelevant/clean-source_first_selfaware_short_contexts_full_0125`

**Input fingerprint:** `eab469c7b33ebcd5909f50fd5be4b634cdd9fb8f6d6d95385ede322fd99d83a7`

| Change | Recorded version |
| --- | --- |
| Unrelated examples | Add examples unrelated to the question |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/uncertainty-monitoring/selfaware-38b07d3302a5fd5b77db.md).
