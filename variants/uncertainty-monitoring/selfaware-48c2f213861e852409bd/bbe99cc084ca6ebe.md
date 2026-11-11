# Option order · Move the first answer choice to the end variant

[Original question](../../../questions/uncertainty-monitoring/selfaware-48c2f213861e852409bd.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** answer choices or their order.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Carol and her mom were picking carrots from their garden. Carol picked 29 and her mother picked 16. If only less than 38 of the carrots were good, how many bad carrots did they have?

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
  "state": "Carol and her mom were picking carrots from their garden. Carol picked 29 and her mother picked 16. If only less than 38 of the carrots were good, how many bad carrots did they have?",
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
| Jev | `no` — Unanswerable | `yes` — Answerable | Different answer |
| Microsoft Decision-1 | `no` — Unanswerable | `no` — Unanswerable | Same answer |
| Clef | `no` — Unanswerable | `no` — Unanswerable | Same answer |
| Luna Decisions | `no` — Unanswerable | `no` — Unanswerable | Same answer |
| Clef Flash | `yes` — Answerable | `yes` — Answerable | Same answer |
| Strands Decider | `yes` — Answerable | `yes` — Answerable | Same answer |
| GLiNER2.5 Decide | `no` — Unanswerable | `no` — Unanswerable | Same answer |
| Laya | `yes` — Answerable | `yes` — Answerable | Same answer |
| CalDec v1 | `yes` — Answerable | `yes` — Answerable | Same answer |

Clef and Clef Flash sort answer choices in their published input-processing code. Their choice-order results describe that preprocessing.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `selfaware/48c2f213861e852409bd/option_order/rotate_1`

**Input fingerprint:** `ecf689de0a7e838f333ff99778a37254bbf42078a94febf51820ecbf8d5d0868`

| Change | Recorded version |
| --- | --- |
| Option order | Move the first answer choice to the end |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/uncertainty-monitoring/selfaware-48c2f213861e852409bd.md).
