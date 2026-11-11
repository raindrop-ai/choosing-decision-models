# Option order · Reverse the answer choices variant

[Original question](../../../questions/retrieval/babi-362577e03d1a583615b5.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** answer choices or their order.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Mary journeyed to the kitchen.
> Sandra went back to the garden.

## Question

> Where is Sandra? 

## Answer choices

- **F.** garden
- **E.** bathroom
- **D.** office
- **C.** hallway
- **B.** kitchen
- **A.** bedroom

**Reference answer:** `F`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Mary journeyed to the kitchen.\nSandra went back to the garden.",
  "question": "Where is Sandra? ",
  "choices": {
    "F": "garden",
    "E": "bathroom",
    "D": "office",
    "C": "hallway",
    "B": "kitchen",
    "A": "bedroom"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `F` — garden | `F` — garden | Same answer |
| Decider v1.1 | `F` — garden | `F` — garden | Same answer |
| Jev | `F` — garden | `F` — garden | Same answer |
| Microsoft Decision-1 | `F` — garden | `F` — garden | Same answer |
| Clef | `F` — garden | `F` — garden | Same answer |
| Luna Decisions | `F` — garden | `F` — garden | Same answer |
| Clef Flash | `F` — garden | `F` — garden | Same answer |
| Strands Decider | `F` — garden | `F` — garden | Same answer |
| GLiNER2.5 Decide | `F` — garden | `F` — garden | Same answer |
| Laya | `F` — garden | `F` — garden | Same answer |
| CalDec v1 | `F` — garden | `F` — garden | Same answer |

Clef and Clef Flash sort answer choices in their published input-processing code. Their choice-order results describe that preprocessing.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `babi/362577e03d1a583615b5/option_order/reverse`

**Input fingerprint:** `40121ce6eaf016f0ba8f5c1b926ea534952db2e32aefe94f24cba268b6acd43c`

| Change | Recorded version |
| --- | --- |
| Option order | Reverse the answer choices |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/retrieval/babi-362577e03d1a583615b5.md).
