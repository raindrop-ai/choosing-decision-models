# Option order · Move the first answer choice to the end variant

[Original question](../../../questions/state-tracking-and-updating/babi-e52715c73f1a2fd2bbc8.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** answer choices or their order.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> John travelled to the garden.
> Mary journeyed to the office.
> Sandra went to the garden.
> John went back to the office.
> John moved to the bedroom.
> John moved to the garden.

## Question

> Where is John? 

## Answer choices

- **B.** hallway
- **C.** bathroom
- **D.** office
- **E.** garden
- **F.** kitchen
- **A.** bedroom

**Reference answer:** `E`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "John travelled to the garden.\nMary journeyed to the office.\nSandra went to the garden.\nJohn went back to the office.\nJohn moved to the bedroom.\nJohn moved to the garden.",
  "question": "Where is John? ",
  "choices": {
    "B": "hallway",
    "C": "bathroom",
    "D": "office",
    "E": "garden",
    "F": "kitchen",
    "A": "bedroom"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `E` — garden | `E` — garden | Same answer |
| Decider v1.1 | `E` — garden | `E` — garden | Same answer |
| Jev | `E` — garden | `E` — garden | Same answer |
| Microsoft Decision-1 | `E` — garden | `E` — garden | Same answer |
| Clef | `E` — garden | `E` — garden | Same answer |
| Luna Decisions | `E` — garden | `E` — garden | Same answer |
| Clef Flash | `E` — garden | `E` — garden | Same answer |
| Strands Decider | `E` — garden | `E` — garden | Same answer |
| GLiNER2.5 Decide | `E` — garden | `E` — garden | Same answer |
| Laya | `A` — bedroom | `E` — garden | Different answer |
| CalDec v1 | `E` — garden | `E` — garden | Same answer |

Clef and Clef Flash sort answer choices in their published input-processing code. Their choice-order results describe that preprocessing.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `babi/e52715c73f1a2fd2bbc8/option_order/rotate_1`

**Input fingerprint:** `4b0375e9fdc3e0c0c999b3767a3c8515a311bc500805f63bd99f0c375051d3c4`

| Change | Recorded version |
| --- | --- |
| Option order | Move the first answer choice to the end |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/state-tracking-and-updating/babi-e52715c73f1a2fd2bbc8.md).
