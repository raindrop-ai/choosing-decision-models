# Option order · Move the first answer choice to the end variant

[Original question](../../../questions/retrieval/babi-c333d401e3cf768f77c8.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** answer choices or their order.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Daniel went back to the bathroom.
> Mary went back to the bathroom.
> Mary went to the garden.
> Sandra moved to the bedroom.
> Mary moved to the kitchen.
> Mary went to the bathroom.

## Question

> Where is Sandra? 

## Answer choices

- **B.** garden
- **C.** office
- **D.** kitchen
- **E.** hallway
- **F.** bathroom
- **A.** bedroom

**Reference answer:** `A`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Daniel went back to the bathroom.\nMary went back to the bathroom.\nMary went to the garden.\nSandra moved to the bedroom.\nMary moved to the kitchen.\nMary went to the bathroom.",
  "question": "Where is Sandra? ",
  "choices": {
    "B": "garden",
    "C": "office",
    "D": "kitchen",
    "E": "hallway",
    "F": "bathroom",
    "A": "bedroom"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `A` — bedroom | `A` — bedroom | Same answer |
| Decider v1.1 | `A` — bedroom | `A` — bedroom | Same answer |
| Jev | `A` — bedroom | `A` — bedroom | Same answer |
| Microsoft Decision-1 | `A` — bedroom | `A` — bedroom | Same answer |
| Clef | `A` — bedroom | `A` — bedroom | Same answer |
| Luna Decisions | `A` — bedroom | `A` — bedroom | Same answer |
| Clef Flash | `A` — bedroom | `A` — bedroom | Same answer |
| Strands Decider | `A` — bedroom | `A` — bedroom | Same answer |
| GLiNER2.5 Decide | `F` — bathroom | `F` — bathroom | Same answer |
| Laya | `A` — bedroom | `A` — bedroom | Same answer |
| CalDec v1 | `A` — bedroom | `F` — bathroom | Different answer |

Clef and Clef Flash sort answer choices in their published input-processing code. Their choice-order results describe that preprocessing.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `babi/c333d401e3cf768f77c8/option_order/rotate_1`

**Input fingerprint:** `e4cc4cd60628a02e4c15bff298764762f37ded5f68cb1f45996574974a62fde3`

| Change | Recorded version |
| --- | --- |
| Option order | Move the first answer choice to the end |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/retrieval/babi-c333d401e3cf768f77c8.md).
