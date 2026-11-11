# Option order · Move the first answer choice to the end variant

[Original question](../../../questions/uncertainty-monitoring/selfaware-eb0490cc160fcd752726.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** answer choices or their order.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> In Australia, on which side of the road do motorists drive?

## Question

> Does this question have a determinate answer?

## Answer choices

- **no.** Unanswerable
- **yes.** Answerable

**Reference answer:** `yes`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "In Australia, on which side of the road do motorists drive?",
  "question": "Does this question have a determinate answer?",
  "choices": {
    "no": "Unanswerable",
    "yes": "Answerable"
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
| Strands Decider | `yes` — Answerable | `yes` — Answerable | Same answer |
| GLiNER2.5 Decide | `no` — Unanswerable | `yes` — Answerable | Different answer |
| Laya | `no` — Unanswerable | `no` — Unanswerable | Same answer |
| CalDec v1 | `no` — Unanswerable | `no` — Unanswerable | Same answer |

Clef and Clef Flash sort answer choices in their published input-processing code. Their choice-order results describe that preprocessing.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `selfaware/eb0490cc160fcd752726/option_order/rotate_1`

**Input fingerprint:** `f2705ec8fac0a9388c1e5208ba99430ba4d0a2f535c63e0f9db732ddb4136aa8`

| Change | Recorded version |
| --- | --- |
| Option order | Move the first answer choice to the end |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/uncertainty-monitoring/selfaware-eb0490cc160fcd752726.md).
