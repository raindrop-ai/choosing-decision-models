# Paraphrasing · Change individual words and phrases variant

[Original question](../../../questions/state-tracking-and-updating/babi-1f9d7560760759a7d86e.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

<details>
<summary>Read the full context</summary>

> Daniel journeyed to the kitchen.
> Sandra journeyed to the garden.
> Sandra picked up the apple there.
> Mary travelled to the kitchen.
> Daniel got the milk.
> Sandra picked up the football.
> Mary went to the bedroom.
> Daniel returned to the bedroom.
> John travelled to the hallway.
> Mary travelled to the bathroom.
> Mary returned to the hallway.
> John went to the office.
> Sandra went to the kitchen.
> Mary travelled to the bedroom.
> Daniel left the milk.
> Mary went to the kitchen.
> John returned to the bedroom.
> Daniel returned to the office.
> Sandra returned to the hallway.
> John grabbed the milk.
> Sandra returned to the kitchen.
> Daniel went to the bedroom.
> John travelled to the hallway.
> John dropped the milk.
> Sandra discarded the apple.
> Mary grabbed the apple.
> Sandra put down the football.
> Sandra got the football.
> Sandra went to the garden.
> Mary journeyed to the office.
> Sandra dropped the football.
> Mary went to the garden.
> Mary left the apple there.
> John journeyed to the kitchen.
> Sandra got the apple.
> Mary journeyed to the bedroom.
> Sandra left the apple.
> Sandra went to the bathroom.
> Daniel went to the office.
> Sandra went to the garden.
> John returned to the office.
> Sandra took the football.
> Sandra took the apple.
> Sandra discarded the football.
> Daniel went to the bathroom.
> Mary journeyed to the office.
> Sandra picked up the football.
> Sandra discarded the apple.
> Sandra left the football.
> Sandra went to the office.
> Sandra journeyed to the bedroom.
> John went to the hallway.
> John travelled to the bedroom.
> John went to the kitchen.
> Mary journeyed to the bathroom.
> Mary went to the kitchen.
> Daniel travelled to the hallway.
> Daniel got the milk.
> Daniel dropped the milk.
> John returned to the bathroom.
> Mary travelled to the bedroom.
> Sandra went to the garden.
> Sandra took the apple.
> Daniel took the milk.
> Daniel dropped the milk there.
> Sandra got the football.
> John travelled to the hallway.
> Mary went to the hallway.
> Daniel grabbed the milk.
> Daniel went to the office.
> Sandra put down the apple.
> Daniel put down the milk.
> Sandra travelled to the bedroom.
> Sandra discarded the football.
> Daniel got the milk.
> Daniel discarded the milk there.
> Mary returned to the office.
> Mary grabbed the milk.
> Daniel went to the bathroom.
> John journeyed to the kitchen.
> Daniel went to the hallway.
> Mary went to the bedroom.
> Sandra journeyed to the kitchen.
> John went to the bedroom.
> Mary put down the milk.
> Sandra journeyed to the garden.
> Mary picked up the milk.
> Sandra picked up the apple.
> Mary went to the garden.
> Sandra travelled to the kitchen.
> Daniel journeyed to the office.
> Mary went to the hallway.
> Mary journeyed to the kitchen.
> Sandra dropped the apple there.
> Mary journeyed to the bathroom.
> Sandra got the apple.
> Mary went to the bedroom.
> Mary picked up the football there.
> Mary put down the milk.
> John journeyed to the office.
> John journeyed to the bedroom.
> Sandra discarded the apple.

</details>

## Question

> Where was the milk before the kitchen? 

## Answer choices

- **A.** bathroom
- **B.** garden
- **C.** kitchen
- **D.** bedroom
- **E.** office
- **F.** hallway

**Reference answer:** `F`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Daniel journeyed to the kitchen.\nSandra journeyed to the garden.\nSandra picked up the apple there.\nMary travelled to the kitchen.\nDaniel got the milk.\nSandra picked up the football.\nMary went to the bedroom.\nDaniel returned to the bedroom.\nJohn travelled to the hallway.\nMary travelled to the bathroom.\nMary returned to the hallway.\nJohn went to the office.\nSandra went to the kitchen.\nMary travelled to the bedroom.\nDaniel left the milk.\nMary went to the kitchen.\nJohn returned to the bedroom.\nDaniel returned to the office.\nSandra returned to the hallway.\nJohn grabbed the milk.\nSandra returned to the kitchen.\nDaniel went to the bedroom.\nJohn travelled to the hallway.\nJohn dropped the milk.\nSandra discarded the apple.\nMary grabbed the apple.\nSandra put down the football.\nSandra got the football.\nSandra went to the garden.\nMary journeyed to the office.\nSandra dropped the football.\nMary went to the garden.\nMary left the apple there.\nJohn journeyed to the kitchen.\nSandra got the apple.\nMary journeyed to the bedroom.\nSandra left the apple.\nSandra went to the bathroom.\nDaniel went to the office.\nSandra went to the garden.\nJohn returned to the office.\nSandra took the football.\nSandra took the apple.\nSandra discarded the football.\nDaniel went to the bathroom.\nMary journeyed to the office.\nSandra picked up the football.\nSandra discarded the apple.\nSandra left the football.\nSandra went to the office.\nSandra journeyed to the bedroom.\nJohn went to the hallway.\nJohn travelled to the bedroom.\nJohn went to the kitchen.\nMary journeyed to the bathroom.\nMary went to the kitchen.\nDaniel travelled to the hallway.\nDaniel got the milk.\nDaniel dropped the milk.\nJohn returned to the bathroom.\nMary travelled to the bedroom.\nSandra went to the garden.\nSandra took the apple.\nDaniel took the milk.\nDaniel dropped the milk there.\nSandra got the football.\nJohn travelled to the hallway.\nMary went to the hallway.\nDaniel grabbed the milk.\nDaniel went to the office.\nSandra put down the apple.\nDaniel put down the milk.\nSandra travelled to the bedroom.\nSandra discarded the football.\nDaniel got the milk.\nDaniel discarded the milk there.\nMary returned to the office.\nMary grabbed the milk.\nDaniel went to the bathroom.\nJohn journeyed to the kitchen.\nDaniel went to the hallway.\nMary went to the bedroom.\nSandra journeyed to the kitchen.\nJohn went to the bedroom.\nMary put down the milk.\nSandra journeyed to the garden.\nMary picked up the milk.\nSandra picked up the apple.\nMary went to the garden.\nSandra travelled to the kitchen.\nDaniel journeyed to the office.\nMary went to the hallway.\nMary journeyed to the kitchen.\nSandra dropped the apple there.\nMary journeyed to the bathroom.\nSandra got the apple.\nMary went to the bedroom.\nMary picked up the football there.\nMary put down the milk.\nJohn journeyed to the office.\nJohn journeyed to the bedroom.\nSandra discarded the apple.",
  "question": "Where was the milk before the kitchen? ",
  "choices": {
    "A": "bathroom",
    "B": "garden",
    "C": "kitchen",
    "D": "bedroom",
    "E": "office",
    "F": "hallway"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `F` — hallway | `F` — hallway | Same answer |
| Decider v1.1 | `F` — hallway | `F` — hallway | Same answer |
| Jev | `F` — hallway | `F` — hallway | Same answer |
| Microsoft Decision-1 | `A` — bathroom | `A` — bathroom | Same answer |
| Clef | `D` — bedroom | `D` — bedroom | Same answer |
| Luna Decisions | `F` — hallway | `F` — hallway | Same answer |
| Clef Flash | `C` — kitchen | `C` — kitchen | Same answer |
| Strands Decider | `C` — kitchen | `C` — kitchen | Same answer |
| GLiNER2.5 Decide | `E` — office | `E` — office | Same answer |
| Laya | `C` — kitchen | `C` — kitchen | Same answer |
| CalDec v1 | `D` — bedroom | `C` — kitchen | Different answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `babi/1f9d7560760759a7d86e/paraphrasing/surface`

**Input fingerprint:** `f1d13b938e707dfe6d963af935cf0ef992f1c115933bac407dd8ac1cfb6997e5`

| Change | Recorded version |
| --- | --- |
| Paraphrasing | Change individual words and phrases |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/state-tracking-and-updating/babi-1f9d7560760759a7d86e.md).
