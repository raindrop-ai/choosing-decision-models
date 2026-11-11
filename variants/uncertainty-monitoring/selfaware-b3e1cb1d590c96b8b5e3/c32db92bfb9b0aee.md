# Option order · Move the first answer choice to the end variant

[Original question](../../../questions/uncertainty-monitoring/selfaware-b3e1cb1d590c96b8b5e3.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** answer choices or their order.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Which large fleshy fruit of the far east has been banned from some public areas because of it's distinctive odour?

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
  "state": "Which large fleshy fruit of the far east has been banned from some public areas because of it's distinctive odour?",
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
| GLiNER2.5 Decide | `no` — Unanswerable | `no` — Unanswerable | Same answer |
| Laya | `yes` — Answerable | `yes` — Answerable | Same answer |
| CalDec v1 | `yes` — Answerable | `yes` — Answerable | Same answer |

Clef and Clef Flash sort answer choices in their published input-processing code. Their choice-order results describe that preprocessing.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `selfaware/b3e1cb1d590c96b8b5e3/option_order/rotate_1`

**Input fingerprint:** `48bad269342936cb4e61e1b2f0a65e2e787b99e0dbf159a4e5cb005a06f68250`

| Change | Recorded version |
| --- | --- |
| Option order | Move the first answer choice to the end |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/uncertainty-monitoring/selfaware-b3e1cb1d590c96b8b5e3.md).
