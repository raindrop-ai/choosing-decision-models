# Option order · Move the first answer choice to the end variant

[Original question](../../../questions/spatial-cognition/babi-1a78025a4fa9d724a316.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** answer choices or their order.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> The yellow square is to the left of the red square.
> The yellow square is to the right of the blue square.

## Question

> Is the blue square to the left of the red square?

## Answer choices

- **no.** no
- **yes.** yes

**Reference answer:** `yes`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "The yellow square is to the left of the red square.\nThe yellow square is to the right of the blue square.",
  "question": "Is the blue square to the left of the red square?",
  "choices": {
    "no": "no",
    "yes": "yes"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `yes` — yes | `yes` — yes | Same answer |
| Decider v1.1 | `yes` — yes | `yes` — yes | Same answer |
| Jev | `yes` — yes | `yes` — yes | Same answer |
| Microsoft Decision-1 | `yes` — yes | `yes` — yes | Same answer |
| Clef | `yes` — yes | `yes` — yes | Same answer |
| Luna Decisions | `yes` — yes | `yes` — yes | Same answer |
| Clef Flash | `no` — no | `no` — no | Same answer |
| Strands Decider | `yes` — yes | `yes` — yes | Same answer |
| GLiNER2.5 Decide | `yes` — yes | `yes` — yes | Same answer |
| Laya | `no` — no | `no` — no | Same answer |
| CalDec v1 | `no` — no | `no` — no | Same answer |

Clef and Clef Flash sort answer choices in their published input-processing code. Their choice-order results describe that preprocessing.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `babi/1a78025a4fa9d724a316/option_order/rotate_1`

**Input fingerprint:** `3a2a9838771e6152d46353bc7347b20e3d37f3c7df617fe57a28af6bc5e29913`

| Change | Recorded version |
| --- | --- |
| Option order | Move the first answer choice to the end |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/spatial-cognition/babi-1a78025a4fa9d724a316.md).
