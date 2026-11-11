# Misleading details · Add an unverified claim that agrees with the evidence variant

[Original question](../../../questions/uncertainty-monitoring/selfaware-38b07d3302a5fd5b77db.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> A reader thinks the question «At 51° 23' E, what is the easternmost point of the African continent?» is Answerable.
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
  "state": "A reader thinks the question «At 51° 23' E, what is the easternmost point of the African continent?» is Answerable.\n\nAt 51° 23' E, what is the easternmost point of the African continent?",
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
| Microsoft Decision-1 | `yes` — Answerable | `no` — Unanswerable | Different answer |
| Clef | `yes` — Answerable | `yes` — Answerable | Same answer |
| Luna Decisions | `yes` — Answerable | `yes` — Answerable | Same answer |
| Clef Flash | `yes` — Answerable | `yes` — Answerable | Same answer |
| Strands Decider | `yes` — Answerable | `yes` — Answerable | Same answer |
| GLiNER2.5 Decide | `yes` — Answerable | `yes` — Answerable | Same answer |
| Laya | `no` — Unanswerable | `yes` — Answerable | Different answer |
| CalDec v1 | `no` — Unanswerable | `yes` — Answerable | Different answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `selfaware/38b07d3302a5fd5b77db/misleading_summary/accurate/clean-source_first_selfaware_short_contexts_full_0125`

**Input fingerprint:** `6be3586b47ec7fc2b3cac07a93ffa0fef2c832d03b2fcc1ef996446fd83569c1`

| Change | Recorded version |
| --- | --- |
| Misleading details | Add an unverified claim that agrees with the evidence |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/uncertainty-monitoring/selfaware-38b07d3302a5fd5b77db.md).
