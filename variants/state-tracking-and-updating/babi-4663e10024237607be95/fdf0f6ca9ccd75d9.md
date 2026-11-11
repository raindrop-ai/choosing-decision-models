# Evidence order · Present the evidence in reverse order variant

[Original question](../../../questions/state-tracking-and-updating/babi-4663e10024237607be95.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Sandra went to the office.
> Sandra journeyed to the kitchen.
> Mary went to the kitchen.
> Sandra travelled to the bedroom.
> Mary went to the bedroom.
> Daniel travelled to the kitchen.
> Daniel moved to the hallway.
> Sandra moved to the bathroom.
> John took the football there.
> Mary went to the hallway.
> John went back to the bathroom.
> Mary went back to the bathroom.
> Mary moved to the office.
> John discarded the football.

## Question

> Where is the football? 

## Answer choices

- **A.** garden
- **B.** hallway
- **C.** bedroom
- **D.** office
- **E.** kitchen
- **F.** bathroom

**Reference answer:** `F`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Sandra went to the office.\nSandra journeyed to the kitchen.\nMary went to the kitchen.\nSandra travelled to the bedroom.\nMary went to the bedroom.\nDaniel travelled to the kitchen.\nDaniel moved to the hallway.\nSandra moved to the bathroom.\nJohn took the football there.\nMary went to the hallway.\nJohn went back to the bathroom.\nMary went back to the bathroom.\nMary moved to the office.\nJohn discarded the football.",
  "question": "Where is the football? ",
  "choices": {
    "A": "garden",
    "B": "hallway",
    "C": "bedroom",
    "D": "office",
    "E": "kitchen",
    "F": "bathroom"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `F` — bathroom | `F` — bathroom | Same answer |
| Decider v1.1 | `F` — bathroom | `F` — bathroom | Same answer |
| Jev | `F` — bathroom | `F` — bathroom | Same answer |
| Microsoft Decision-1 | `F` — bathroom | `F` — bathroom | Same answer |
| Clef | `F` — bathroom | `F` — bathroom | Same answer |
| Luna Decisions | `F` — bathroom | `F` — bathroom | Same answer |
| Clef Flash | `F` — bathroom | `F` — bathroom | Same answer |
| Strands Decider | `F` — bathroom | `F` — bathroom | Same answer |
| GLiNER2.5 Decide | `F` — bathroom | `F` — bathroom | Same answer |
| Laya | `D` — office | `D` — office | Same answer |
| CalDec v1 | `B` — hallway | `D` — office | Different answer |

**Ordering comparison:** literal local or custom unit permutation. Only the exact matched comparison sets contribute to the reported ordering contrasts.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `babi/4663e10024237607be95/presentation_order/reverse_presentation/clean-source_first_babi_local_move_orders_full_0086`

**Input fingerprint:** `6cc62f996f9e1a03526b1d396af93071e45d517d3fe262a1d4782ba52a4b4c7f`

| Change | Recorded version |
| --- | --- |
| Evidence order | Present the evidence in reverse order |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/state-tracking-and-updating/babi-4663e10024237607be95.md).
