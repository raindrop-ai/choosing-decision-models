# Similar distractors · Add more similar but irrelevant items variant

[Original question](../../../questions/spatial-cognition/spartqa-a986344d6b4bea903ff9.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** question instructions.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> We have two blocks. Lets call them A and B. Block A is to the left of B. Block A contains a small black triangle. Block B has a medium blue square, a medium black square and one small yellow triangle. The medium blue square is above and to the right of the medium black square which is near to a small black square and the small yellow triangle.

## Question

> Is the small black triangle , to the left of all black squares that are near to a black square?
>
> «Is the teal cylinder Ovelin above the amber prism Nerath?»
>
> «Does the violet pyramid Zelmin touch the silver cone Travon?»
>
> «Is the copper sphere Dervak far from the cyan cube Melvar?»

## Answer choices

- **Yes.** Yes
- **No.** No
- **DK.** DK

**Reference answer:** `Yes`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "We have two blocks. Lets call them A and B. Block A is to the left of B. Block A contains a small black triangle. Block B has a medium blue square, a medium black square and one small yellow triangle. The medium blue square is above and to the right of the medium black square which is near to a small black square and the small yellow triangle.",
  "question": "Is the small black triangle , to the left of all black squares that are near to a black square?\n\n«Is the teal cylinder Ovelin above the amber prism Nerath?»\n\n«Does the violet pyramid Zelmin touch the silver cone Travon?»\n\n«Is the copper sphere Dervak far from the cyan cube Melvar?»",
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
| Jev | `Yes` — Yes | `Yes` — Yes | Same answer |
| Microsoft Decision-1 | `Yes` — Yes | `Yes` — Yes | Same answer |
| Clef | `Yes` — Yes | `Yes` — Yes | Same answer |
| Luna Decisions | `Yes` — Yes | `DK` — DK | Different answer |
| Clef Flash | `Yes` — Yes | `Yes` — Yes | Same answer |
| Strands Decider | `Yes` — Yes | `No` — No | Different answer |
| GLiNER2.5 Decide | `Yes` — Yes | `No` — No | Different answer |
| Laya | `No` — No | `Yes` — Yes | Different answer |
| CalDec v1 | `Yes` — Yes | `Yes` — Yes | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `spartqa/a986344d6b4bea903ff9/similar_distractors/high/clean-source_first_spartqa_near_questions_full_0223`

**Input fingerprint:** `d2799146b0af1e1e730a22ef7fc8205cb1342a414724dc2760b3329ef748cdb8`

| Change | Recorded version |
| --- | --- |
| Similar distractors | Add more similar but irrelevant items |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/spatial-cognition/spartqa-a986344d6b4bea903ff9.md).
