# Evidence order · Present the evidence in a shuffled order variant

[Original question](../../../questions/state-tracking-and-updating/babi-e52715c73f1a2fd2bbc8.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Mary journeyed to the office.
> John travelled to the garden.
> John went back to the office.
> John moved to the bedroom.
> John moved to the garden.
> Sandra went to the garden.

## Question

> Where is John? 

## Answer choices

- **A.** bedroom
- **B.** hallway
- **C.** bathroom
- **D.** office
- **E.** garden
- **F.** kitchen

**Reference answer:** `E`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Mary journeyed to the office.\nJohn travelled to the garden.\nJohn went back to the office.\nJohn moved to the bedroom.\nJohn moved to the garden.\nSandra went to the garden.",
  "question": "Where is John? ",
  "choices": {
    "A": "bedroom",
    "B": "hallway",
    "C": "bathroom",
    "D": "office",
    "E": "garden",
    "F": "kitchen"
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
| Laya | `A` — bedroom | `A` — bedroom | Same answer |
| CalDec v1 | `E` — garden | `A` — bedroom | Different answer |

**Ordering comparison:** literal local or custom unit permutation. Only the exact matched comparison sets contribute to the reported ordering contrasts.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `babi/e52715c73f1a2fd2bbc8/presentation_order/shuffled_presentation/clean-source_first_babi_qa1_full_0084`

**Input fingerprint:** `8233872d8588888341560297f8d0063db009e0e56fd62ec6c842706dfb0f70cd`

| Change | Recorded version |
| --- | --- |
| Evidence order | Present the evidence in a shuffled order |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/state-tracking-and-updating/babi-e52715c73f1a2fd2bbc8.md).
