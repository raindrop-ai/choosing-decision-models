# Evidence position · Place the relevant information in the middle variant

[Original question](../../../questions/spatial-cognition/spartqa-0d3f975b3e4455fb632e.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> The notebook has a linen cover.
>
> The notebook's title is embossed.
>
> We have three blocks. We call them A, B and C. There is a medium yellow circle in block A. Then, we have block B. It contains one big black square. A big black circle is also in this block. The big black square is far from the big black circle. Block C is above block A and to the right of block B. It has one medium blue square and a small blue circle. The medium blue square is below the small blue circle.
>
> The notebook's pages are unruled.
>
> The notebook's binding is stitched.

## Question

> Is the medium yellow circle , below a medium shape that is below a small thing?

## Answer choices

- **Yes.** Yes
- **No.** No
- **DK.** DK

**Reference answer:** `Yes`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "The notebook has a linen cover.\n\nThe notebook's title is embossed.\n\nWe have three blocks. We call them A, B and C. There is a medium yellow circle in block A. Then, we have block B. It contains one big black square. A big black circle is also in this block. The big black square is far from the big black circle. Block C is above block A and to the right of block B. It has one medium blue square and a small blue circle. The medium blue square is below the small blue circle.\n\nThe notebook's pages are unruled.\n\nThe notebook's binding is stitched.",
  "question": "Is the medium yellow circle , below a medium shape that is below a small thing?",
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
| Clef | `No` — No | `No` — No | Same answer |
| Luna Decisions | `DK` — DK | `DK` — DK | Same answer |
| Clef Flash | `No` — No | `No` — No | Same answer |
| Strands Decider | `Yes` — Yes | `Yes` — Yes | Same answer |
| GLiNER2.5 Decide | `No` — No | `No` — No | Same answer |
| Laya | `Yes` — Yes | `Yes` — Yes | Same answer |
| CalDec v1 | `Yes` — Yes | `Yes` — Yes | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `spartqa/0d3f975b3e4455fb632e/evidence_position/middle/clean-source_first_spartqa_combined_contexts_full_0138`

**Input fingerprint:** `e8bbe4900ad02527a532d6b8f054d74261bc1928999275f118b280ab7d530d96`

| Change | Recorded version |
| --- | --- |
| Evidence position | Place the relevant information in the middle |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/spatial-cognition/spartqa-0d3f975b3e4455fb632e.md).
