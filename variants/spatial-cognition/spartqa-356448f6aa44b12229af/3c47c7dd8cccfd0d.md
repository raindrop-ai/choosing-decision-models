# Evidence order · Present the evidence in a shuffled order variant

[Original question](../../../questions/spatial-cognition/spartqa-356448f6aa44b12229af.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> We have three blocks, A, B and C. Then, we have block B. It has a medium black circle and a medium yellow square. The medium yellow square is to the right of and below a medium blue circle. The medium black circle is near to and above the medium blue circle. Block A has one big black triangle. The big black triangle is touching the right edge of this block. This block also has a big yellow circle. Near to, to the right of, touching and above the big yellow circle there is the big black triangle. The big yellow circle is touching the bottom edge of this block. To the left of block A and above block B there is block C with a medium blue square and a big yellow square in it. Below the big yellow square there is the medium blue square.

## Question

> Is there a square that is below a blue square , to the right of a medium blue thing that is near to a black circle?

## Answer choices

- **Yes.** Yes
- **No.** No
- **DK.** DK

**Reference answer:** `Yes`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "We have three blocks, A, B and C. Then, we have block B. It has a medium black circle and a medium yellow square. The medium yellow square is to the right of and below a medium blue circle. The medium black circle is near to and above the medium blue circle. Block A has one big black triangle. The big black triangle is touching the right edge of this block. This block also has a big yellow circle. Near to, to the right of, touching and above the big yellow circle there is the big black triangle. The big yellow circle is touching the bottom edge of this block. To the left of block A and above block B there is block C with a medium blue square and a big yellow square in it. Below the big yellow square there is the medium blue square.",
  "question": "Is there a square that is below a blue square , to the right of a medium blue thing that is near to a black circle?",
  "choices": {
    "Yes": "Yes",
    "No": "No",
    "DK": "DK"
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
| Luna Decisions | `No` — No | `DK` — DK | Different answer |
| Clef Flash | `No` — No | `No` — No | Same answer |
| Strands Decider | `Yes` — Yes | `Yes` — Yes | Same answer |
| GLiNER2.5 Decide | `Yes` — Yes | `Yes` — Yes | Same answer |
| Laya | `Yes` — Yes | `Yes` — Yes | Same answer |
| CalDec v1 | `Yes` — Yes | `Yes` — Yes | Same answer |

**Ordering comparison:** literal requested source unit permutation. Only the exact matched comparison sets contribute to the reported ordering contrasts.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `spartqa/356448f6aa44b12229af/presentation_order/shuffled_presentation/clean-source_first_spartqa_block_bundle_orders_full_0147`

**Input fingerprint:** `d0590eba588c2963a87653768c5282f9ae73b31c10b40d2effd9e8d4a0243e75`

| Change | Recorded version |
| --- | --- |
| Evidence order | Present the evidence in a shuffled order |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/spatial-cognition/spartqa-356448f6aa44b12229af.md).
