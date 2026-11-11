# Paraphrasing · Change individual words and phrases variant

[Original question](../../../questions/state-tracking-and-updating/babi-a1f6c6ac025c82548034.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

<details>
<summary>Read the full context</summary>

> Daniel went to the office.
> Sandra went to the garden.
> Mary journeyed to the office.
> Mary returned to the hallway.
> Mary went to the garden.
> John journeyed to the bedroom.
> Daniel took the milk there.
> Daniel left the milk.
> Daniel picked up the milk.
> John went to the hallway.
> Sandra journeyed to the kitchen.
> Daniel discarded the milk.
> Mary returned to the bathroom.
> Daniel got the milk.
> Mary picked up the football.
> Daniel put down the milk.
> Mary went to the office.
> Daniel journeyed to the bathroom.
> Mary grabbed the milk.
> Mary went to the garden.
> John returned to the bedroom.
> Mary travelled to the bedroom.
> John picked up the apple.
> Mary returned to the kitchen.
> Daniel travelled to the bedroom.
> Sandra journeyed to the bedroom.
> John left the apple there.
> John got the apple.
> John discarded the apple.
> Sandra picked up the apple.
> Mary returned to the office.
> John returned to the kitchen.
> Sandra discarded the apple.
> Daniel grabbed the apple.
> Daniel went to the hallway.
> Sandra went to the garden.
> John went to the office.
> Mary dropped the football.
> Daniel went to the garden.
> Sandra went to the kitchen.
> Sandra went to the garden.
> Daniel put down the apple there.
> Sandra took the apple.
> Mary travelled to the garden.
> John went to the garden.
> Sandra returned to the bedroom.
> Mary journeyed to the bedroom.
> John went to the bedroom.
> Sandra put down the apple.
> Daniel returned to the office.
> Sandra took the apple.
> Daniel took the football.
> Mary put down the milk there.
> John picked up the milk there.
> John put down the milk.
> Mary grabbed the milk.
> Mary dropped the milk there.
> Daniel left the football.
> Daniel went to the kitchen.
> Sandra left the apple.
> Sandra went to the kitchen.
> Mary took the milk.
> John picked up the apple.
> John discarded the apple.
> John grabbed the apple.
> Mary left the milk.
> John picked up the milk there.
> Daniel went to the bedroom.
> Mary went to the hallway.
> John discarded the apple.
> Sandra went to the bathroom.
> John took the apple there.
> Sandra travelled to the hallway.
> Daniel went to the hallway.
> Daniel went to the bathroom.
> Daniel went to the hallway.
> John went to the office.
> Mary travelled to the bedroom.
> Sandra went to the office.
> John picked up the football.
> Mary went to the office.
> Mary went to the hallway.
> John returned to the hallway.
> Mary returned to the bathroom.
> Sandra went to the bedroom.
> John returned to the garden.
> Sandra travelled to the office.
> Mary returned to the hallway.
> John put down the milk.
> Sandra went to the hallway.

</details>

## Question

> Where was the milk before the hallway? 

## Answer choices

- **A.** hallway
- **B.** office
- **C.** bedroom
- **D.** bathroom
- **E.** garden
- **F.** kitchen

**Reference answer:** `B`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Daniel went to the office.\nSandra went to the garden.\nMary journeyed to the office.\nMary returned to the hallway.\nMary went to the garden.\nJohn journeyed to the bedroom.\nDaniel took the milk there.\nDaniel left the milk.\nDaniel picked up the milk.\nJohn went to the hallway.\nSandra journeyed to the kitchen.\nDaniel discarded the milk.\nMary returned to the bathroom.\nDaniel got the milk.\nMary picked up the football.\nDaniel put down the milk.\nMary went to the office.\nDaniel journeyed to the bathroom.\nMary grabbed the milk.\nMary went to the garden.\nJohn returned to the bedroom.\nMary travelled to the bedroom.\nJohn picked up the apple.\nMary returned to the kitchen.\nDaniel travelled to the bedroom.\nSandra journeyed to the bedroom.\nJohn left the apple there.\nJohn got the apple.\nJohn discarded the apple.\nSandra picked up the apple.\nMary returned to the office.\nJohn returned to the kitchen.\nSandra discarded the apple.\nDaniel grabbed the apple.\nDaniel went to the hallway.\nSandra went to the garden.\nJohn went to the office.\nMary dropped the football.\nDaniel went to the garden.\nSandra went to the kitchen.\nSandra went to the garden.\nDaniel put down the apple there.\nSandra took the apple.\nMary travelled to the garden.\nJohn went to the garden.\nSandra returned to the bedroom.\nMary journeyed to the bedroom.\nJohn went to the bedroom.\nSandra put down the apple.\nDaniel returned to the office.\nSandra took the apple.\nDaniel took the football.\nMary put down the milk there.\nJohn picked up the milk there.\nJohn put down the milk.\nMary grabbed the milk.\nMary dropped the milk there.\nDaniel left the football.\nDaniel went to the kitchen.\nSandra left the apple.\nSandra went to the kitchen.\nMary took the milk.\nJohn picked up the apple.\nJohn discarded the apple.\nJohn grabbed the apple.\nMary left the milk.\nJohn picked up the milk there.\nDaniel went to the bedroom.\nMary went to the hallway.\nJohn discarded the apple.\nSandra went to the bathroom.\nJohn took the apple there.\nSandra travelled to the hallway.\nDaniel went to the hallway.\nDaniel went to the bathroom.\nDaniel went to the hallway.\nJohn went to the office.\nMary travelled to the bedroom.\nSandra went to the office.\nJohn picked up the football.\nMary went to the office.\nMary went to the hallway.\nJohn returned to the hallway.\nMary returned to the bathroom.\nSandra went to the bedroom.\nJohn returned to the garden.\nSandra travelled to the office.\nMary returned to the hallway.\nJohn put down the milk.\nSandra went to the hallway.",
  "question": "Where was the milk before the hallway? ",
  "choices": {
    "A": "hallway",
    "B": "office",
    "C": "bedroom",
    "D": "bathroom",
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
| Jev | `C` — bedroom | `C` — bedroom | Same answer |
| Microsoft Decision-1 | `C` — bedroom | `C` — bedroom | Same answer |
| Clef | `D` — bathroom | `C` — bedroom | Different answer |
| Luna Decisions | `D` — bathroom | `C` — bedroom | Different answer |
| Clef Flash | `D` — bathroom | `D` — bathroom | Same answer |
| Strands Decider | `F` — kitchen | `F` — kitchen | Same answer |
| GLiNER2.5 Decide | `A` — hallway | `A` — hallway | Same answer |
| Laya | `B` — office | `B` — office | Same answer |
| CalDec v1 | `C` — bedroom | `B` — office | Different answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `babi/a1f6c6ac025c82548034/paraphrasing/surface`

**Input fingerprint:** `ed77458fd3ba04aee1b64bdd9bc02aaa5948db6b39e23766916be9164fb22e08`

| Change | Recorded version |
| --- | --- |
| Paraphrasing | Change individual words and phrases |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/state-tracking-and-updating/babi-a1f6c6ac025c82548034.md).
