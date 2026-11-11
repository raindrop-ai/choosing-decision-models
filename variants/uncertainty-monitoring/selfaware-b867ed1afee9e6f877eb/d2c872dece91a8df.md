# Option order · Move the first answer choice to the end variant

[Original question](../../../questions/uncertainty-monitoring/selfaware-b867ed1afee9e6f877eb.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** answer choices or their order.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Where does the lost time go to?

## Question

> Does this question have a determinate answer?

## Answer choices

- **no.** Unanswerable
- **yes.** Answerable

**Reference answer:** `no`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Where does the lost time go to?",
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
| GLiDE v1.2 | `no` — Unanswerable | `no` — Unanswerable | Same answer |
| Decider v1.1 | `no` — Unanswerable | `no` — Unanswerable | Same answer |
| Jev | `no` — Unanswerable | `no` — Unanswerable | Same answer |
| Microsoft Decision-1 | `no` — Unanswerable | `no` — Unanswerable | Same answer |
| Clef | `no` — Unanswerable | `no` — Unanswerable | Same answer |
| Luna Decisions | `yes` — Answerable | `no` — Unanswerable | Different answer |
| Clef Flash | `no` — Unanswerable | `no` — Unanswerable | Same answer |
| Strands Decider | `no` — Unanswerable | `no` — Unanswerable | Same answer |
| GLiNER2.5 Decide | `no` — Unanswerable | `no` — Unanswerable | Same answer |
| Laya | `no` — Unanswerable | `no` — Unanswerable | Same answer |
| CalDec v1 | `yes` — Answerable | `yes` — Answerable | Same answer |

Clef and Clef Flash sort answer choices in their published input-processing code. Their choice-order results describe that preprocessing.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `selfaware/b867ed1afee9e6f877eb/option_order/rotate_1`

**Input fingerprint:** `b6d49e26c63a6b91f290b698fff4024d11c72839188378abe44a1964f8d7e1d8`

| Change | Recorded version |
| --- | --- |
| Option order | Move the first answer choice to the end |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/uncertainty-monitoring/selfaware-b867ed1afee9e6f877eb.md).
