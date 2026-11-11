# Unrelated examples · Add examples unrelated to the question variant

[Original question](../../../questions/state-tracking-and-updating/babi-d8b4cc8682faee0edd89.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Sandra went to the garden.
> Sandra picked up the apple there.
> Daniel went back to the office.
> Sandra put down the apple.
> Mary travelled to the hallway.
> Sandra travelled to the kitchen.
> Mary went back to the bedroom.
> John moved to the hallway.
> Mary went to the office.
> Daniel went to the bedroom.
> Sandra journeyed to the bedroom.
> Mary journeyed to the hallway.
> Mary journeyed to the bedroom.
> John went to the bathroom.
> Sandra grabbed the football there.
> John took the milk there.
> Daniel travelled to the kitchen.
> Mary went to the garden.
> John discarded the milk.
> Daniel journeyed to the bathroom.
> Daniel went back to the office.
> Mary grabbed the apple there.
>
> Uppercase: comet → COMET.

## Question

> Where is the milk? 

## Answer choices

- **A.** bathroom
- **B.** hallway
- **C.** office
- **D.** bedroom
- **E.** kitchen
- **F.** garden

**Reference answer:** `A`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Sandra went to the garden.\nSandra picked up the apple there.\nDaniel went back to the office.\nSandra put down the apple.\nMary travelled to the hallway.\nSandra travelled to the kitchen.\nMary went back to the bedroom.\nJohn moved to the hallway.\nMary went to the office.\nDaniel went to the bedroom.\nSandra journeyed to the bedroom.\nMary journeyed to the hallway.\nMary journeyed to the bedroom.\nJohn went to the bathroom.\nSandra grabbed the football there.\nJohn took the milk there.\nDaniel travelled to the kitchen.\nMary went to the garden.\nJohn discarded the milk.\nDaniel journeyed to the bathroom.\nDaniel went back to the office.\nMary grabbed the apple there.\n\nUppercase: comet → COMET.",
  "question": "Where is the milk? ",
  "choices": {
    "A": "bathroom",
    "B": "hallway",
    "C": "office",
    "D": "bedroom",
    "E": "kitchen",
    "F": "garden"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `A` — bathroom | `A` — bathroom | Same answer |
| Decider v1.1 | `A` — bathroom | `A` — bathroom | Same answer |
| Jev | `A` — bathroom | `A` — bathroom | Same answer |
| Microsoft Decision-1 | `A` — bathroom | `A` — bathroom | Same answer |
| Clef | `A` — bathroom | `A` — bathroom | Same answer |
| Luna Decisions | `A` — bathroom | `A` — bathroom | Same answer |
| Clef Flash | `A` — bathroom | `A` — bathroom | Same answer |
| Strands Decider | `B` — hallway | `B` — hallway | Same answer |
| GLiNER2.5 Decide | `C` — office | `C` — office | Same answer |
| Laya | `A` — bathroom | `C` — office | Different answer |
| CalDec v1 | `A` — bathroom | `A` — bathroom | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `babi/d8b4cc8682faee0edd89/examples/irrelevant/clean-source_first_babi_object_contexts_full_0088`

**Input fingerprint:** `f060091cc2c6b1382737b1253d9f095826188909da7c8090f1ae3e033a76d756`

| Change | Recorded version |
| --- | --- |
| Unrelated examples | Add examples unrelated to the question |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/state-tracking-and-updating/babi-d8b4cc8682faee0edd89.md).
