# Option order · Reverse the answer choices variant

[Original question](../../../questions/spatial-cognition/spartqa-5c9863f43a411486d1b2.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** answer choices or their order.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> There are three blocks. Lets call them A, B and C. Block B is to the right of A and block C is above B. Block A has one medium blue triangle and a small yellow circle. To the right of and above the small yellow circle there is the medium blue triangle. Block B has a big blue square, one medium black triangle and one medium yellow triangle. The medium yellow triangle is to the right of and above a small blue triangle. The big blue square is to the right of and above the medium yellow triangle. The small blue triangle is touching the bottom edge of this block.. The medium black triangle is near to and above the small blue triangle. And block C has one medium blue square.

## Question

> Is the medium blue square , below the small yellow object that is to the left of a black triangle?

## Answer choices

- **DK.** DK
- **No.** No
- **Yes.** Yes

**Reference answer:** `DK`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "There are three blocks. Lets call them A, B and C. Block B is to the right of A and block C is above B. Block A has one medium blue triangle and a small yellow circle. To the right of and above the small yellow circle there is the medium blue triangle. Block B has a big blue square, one medium black triangle and one medium yellow triangle. The medium yellow triangle is to the right of and above a small blue triangle. The big blue square is to the right of and above the medium yellow triangle. The small blue triangle is touching the bottom edge of this block.. The medium black triangle is near to and above the small blue triangle. And block C has one medium blue square.",
  "question": "Is the medium blue square , below the small yellow object that is to the left of a black triangle?",
  "choices": {
    "DK": "DK",
    "No": "No",
    "Yes": "Yes"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `DK` — DK | `DK` — DK | Same answer |
| Decider v1.1 | `DK` — DK | `DK` — DK | Same answer |
| Jev | `No` — No | `No` — No | Same answer |
| Microsoft Decision-1 | `No` — No | `No` — No | Same answer |
| Clef | `No` — No | `No` — No | Same answer |
| Luna Decisions | `DK` — DK | `DK` — DK | Same answer |
| Clef Flash | `No` — No | `No` — No | Same answer |
| Strands Decider | `No` — No | `No` — No | Same answer |
| GLiNER2.5 Decide | `Yes` — Yes | `Yes` — Yes | Same answer |
| Laya | `No` — No | `No` — No | Same answer |
| CalDec v1 | `No` — No | `Yes` — Yes | Different answer |

Clef and Clef Flash sort answer choices in their published input-processing code. Their choice-order results describe that preprocessing.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `spartqa/5c9863f43a411486d1b2/option_order/reverse`

**Input fingerprint:** `e6a8aefcde85630204d04fddd0ca966848261ff72eef66564f2563e724bd3125`

| Change | Recorded version |
| --- | --- |
| Option order | Reverse the answer choices |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/spatial-cognition/spartqa-5c9863f43a411486d1b2.md).
