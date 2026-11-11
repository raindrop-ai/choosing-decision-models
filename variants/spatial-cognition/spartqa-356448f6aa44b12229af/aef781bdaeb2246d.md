# Option order · Move the first answer choice to the end variant

[Original question](../../../questions/spatial-cognition/spartqa-356448f6aa44b12229af.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** answer choices or their order.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> We have three blocks, A, B and C. Block A has one big black triangle. The big black triangle is touching the right edge of this block. This block also has a big yellow circle. Near to, to the right of, touching and above the big yellow circle there is the big black triangle. The big yellow circle is touching the bottom edge of this block. Then, we have block B. It has a medium black circle and a medium yellow square. The medium yellow square is to the right of and below a medium blue circle. The medium black circle is near to and above the medium blue circle. To the left of block A and above block B there is block C with a medium blue square and a big yellow square in it. Below the big yellow square there is the medium blue square.

## Question

> Is there a square that is below a blue square , to the right of a medium blue thing that is near to a black circle?

## Answer choices

- **No.** No
- **DK.** DK
- **Yes.** Yes

**Reference answer:** `Yes`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "We have three blocks, A, B and C. Block A has one big black triangle. The big black triangle is touching the right edge of this block. This block also has a big yellow circle. Near to, to the right of, touching and above the big yellow circle there is the big black triangle. The big yellow circle is touching the bottom edge of this block. Then, we have block B. It has a medium black circle and a medium yellow square. The medium yellow square is to the right of and below a medium blue circle. The medium black circle is near to and above the medium blue circle. To the left of block A and above block B there is block C with a medium blue square and a big yellow square in it. Below the big yellow square there is the medium blue square.",
  "question": "Is there a square that is below a blue square , to the right of a medium blue thing that is near to a black circle?",
  "choices": {
    "No": "No",
    "DK": "DK",
    "Yes": "Yes"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `Yes` — Yes | `Yes` — Yes | Same answer |
| Decider v1.1 | `Yes` — Yes | `Yes` — Yes | Same answer |
| Jev | `No` — No | `No` — No | Same answer |
| Microsoft Decision-1 | `No` — No | `No` — No | Same answer |
| Clef | `No` — No | `No` — No | Same answer |
| Luna Decisions | `No` — No | `No` — No | Same answer |
| Clef Flash | `No` — No | `No` — No | Same answer |
| Strands Decider | `Yes` — Yes | `Yes` — Yes | Same answer |
| GLiNER2.5 Decide | `Yes` — Yes | `Yes` — Yes | Same answer |
| Laya | `Yes` — Yes | `Yes` — Yes | Same answer |
| CalDec v1 | `Yes` — Yes | `Yes` — Yes | Same answer |

Clef and Clef Flash sort answer choices in their published input-processing code. Their choice-order results describe that preprocessing.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `spartqa/356448f6aa44b12229af/option_order/rotate_1`

**Input fingerprint:** `0d904d3a77b36ac023c02055c96c9c35e163635a9569e44f6527884699db3166`

| Change | Recorded version |
| --- | --- |
| Option order | Move the first answer choice to the end |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/spatial-cognition/spartqa-356448f6aa44b12229af.md).
