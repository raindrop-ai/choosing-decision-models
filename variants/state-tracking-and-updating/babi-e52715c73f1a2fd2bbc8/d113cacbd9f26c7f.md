# Option order · Reverse the answer choices variant

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

- **F.** kitchen
- **E.** garden
- **D.** office
- **C.** bathroom
- **B.** hallway
- **A.** bedroom

**Reference answer:** `E`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "John travelled to the garden.\nMary journeyed to the office.\nSandra went to the garden.\nJohn went back to the office.\nJohn moved to the bedroom.\nJohn moved to the garden.",
  "question": "Where is John? ",
  "choices": {
    "F": "kitchen",
    "E": "garden",
    "D": "office",
    "C": "bathroom",
    "B": "hallway",
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

**Variant ID:** `babi/e52715c73f1a2fd2bbc8/option_order/reverse`

**Input fingerprint:** `e8e2ca1cace04d1a0aeaefb7c4a774f6b8f4cf346ef86cd724fc3fe4ff2a1692`

| Change | Recorded version |
| --- | --- |
| Option order | Reverse the answer choices |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/state-tracking-and-updating/babi-e52715c73f1a2fd2bbc8.md).
