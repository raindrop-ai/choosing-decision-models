# Unrelated examples · No worked example (absence-control recipe) variant

[Original question](../../../questions/state-tracking-and-updating/babi-6d3842d1971d4be98e73.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

<details>
<summary>Read the full context</summary>

> Daniel went to the hallway.
> Daniel went to the kitchen.
> Mary went back to the hallway.
> John picked up the apple.
> John went to the garden.
> Daniel journeyed to the hallway.
> John journeyed to the hallway.
> Mary moved to the office.
> Daniel went back to the kitchen.
> John discarded the apple there.
> John picked up the apple.
> John left the apple there.
> Mary went to the bedroom.
> Mary moved to the kitchen.
> John grabbed the apple.
> Daniel went to the garden.
> Mary moved to the office.
> Daniel went to the bedroom.
> Mary went back to the bedroom.
> Daniel journeyed to the hallway.
> Daniel went to the bedroom.
> John put down the apple.
> John moved to the bedroom.
> Mary moved to the bathroom.
> John moved to the bathroom.
> Mary travelled to the garden.
> Mary journeyed to the kitchen.
> Sandra journeyed to the hallway.
> Sandra travelled to the office.
> Mary travelled to the garden.
> John got the milk.
> John went back to the garden.
> Mary went back to the bedroom.
> John went back to the kitchen.
> Mary travelled to the garden.
> Daniel moved to the kitchen.
> Sandra journeyed to the bathroom.
> Sandra grabbed the football.
> John went back to the office.
> John moved to the kitchen.
> John travelled to the office.
> Sandra went back to the hallway.
> John discarded the milk.
> John took the milk.
> Sandra dropped the football.
> Daniel journeyed to the garden.
> John discarded the milk.
> John got the milk.
> John left the milk.
> Sandra grabbed the football.
> Daniel travelled to the bathroom.
> Sandra discarded the football.
> John went to the bedroom.
> John moved to the kitchen.
> Sandra picked up the football there.
> Sandra dropped the football.
> Daniel travelled to the bedroom.
> Sandra moved to the office.
> Sandra went back to the bathroom.
> Mary went to the bathroom.
> Daniel moved to the garden.
> John went to the bedroom.
> Sandra went back to the hallway.
> Sandra took the apple.
> Sandra grabbed the football.
> Sandra dropped the apple.
> Daniel travelled to the bathroom.
> Mary went back to the office.
> Sandra dropped the football there.
> Daniel travelled to the office.
> John travelled to the kitchen.
> Sandra got the apple.
> Daniel picked up the milk.
> Sandra grabbed the football there.
> Sandra put down the football.
> Sandra moved to the garden.
> John moved to the office.
> Mary moved to the bedroom.
> Daniel dropped the milk.
> John grabbed the milk.
> Daniel moved to the bedroom.
> Mary travelled to the office.
> Sandra went back to the bathroom.
> John went back to the hallway.
> Sandra went to the office.
> Mary journeyed to the bedroom.
> Daniel went back to the garden.
> Daniel went to the kitchen.
> John picked up the football.
> John put down the football.
> John discarded the milk.
> Daniel moved to the bathroom.
> Sandra went back to the garden.
> John took the milk.
> Sandra moved to the bathroom.
> Mary moved to the garden.
> Daniel moved to the garden.
> Sandra put down the apple.
>
> The poem has a refrain and an anonymous narrator.

</details>

## Question

> Where was the apple before the office? 

## Answer choices

- **A.** office
- **B.** bedroom
- **C.** hallway
- **D.** kitchen
- **E.** bathroom
- **F.** garden

**Reference answer:** `E`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Daniel went to the hallway.\nDaniel went to the kitchen.\nMary went back to the hallway.\nJohn picked up the apple.\nJohn went to the garden.\nDaniel journeyed to the hallway.\nJohn journeyed to the hallway.\nMary moved to the office.\nDaniel went back to the kitchen.\nJohn discarded the apple there.\nJohn picked up the apple.\nJohn left the apple there.\nMary went to the bedroom.\nMary moved to the kitchen.\nJohn grabbed the apple.\nDaniel went to the garden.\nMary moved to the office.\nDaniel went to the bedroom.\nMary went back to the bedroom.\nDaniel journeyed to the hallway.\nDaniel went to the bedroom.\nJohn put down the apple.\nJohn moved to the bedroom.\nMary moved to the bathroom.\nJohn moved to the bathroom.\nMary travelled to the garden.\nMary journeyed to the kitchen.\nSandra journeyed to the hallway.\nSandra travelled to the office.\nMary travelled to the garden.\nJohn got the milk.\nJohn went back to the garden.\nMary went back to the bedroom.\nJohn went back to the kitchen.\nMary travelled to the garden.\nDaniel moved to the kitchen.\nSandra journeyed to the bathroom.\nSandra grabbed the football.\nJohn went back to the office.\nJohn moved to the kitchen.\nJohn travelled to the office.\nSandra went back to the hallway.\nJohn discarded the milk.\nJohn took the milk.\nSandra dropped the football.\nDaniel journeyed to the garden.\nJohn discarded the milk.\nJohn got the milk.\nJohn left the milk.\nSandra grabbed the football.\nDaniel travelled to the bathroom.\nSandra discarded the football.\nJohn went to the bedroom.\nJohn moved to the kitchen.\nSandra picked up the football there.\nSandra dropped the football.\nDaniel travelled to the bedroom.\nSandra moved to the office.\nSandra went back to the bathroom.\nMary went to the bathroom.\nDaniel moved to the garden.\nJohn went to the bedroom.\nSandra went back to the hallway.\nSandra took the apple.\nSandra grabbed the football.\nSandra dropped the apple.\nDaniel travelled to the bathroom.\nMary went back to the office.\nSandra dropped the football there.\nDaniel travelled to the office.\nJohn travelled to the kitchen.\nSandra got the apple.\nDaniel picked up the milk.\nSandra grabbed the football there.\nSandra put down the football.\nSandra moved to the garden.\nJohn moved to the office.\nMary moved to the bedroom.\nDaniel dropped the milk.\nJohn grabbed the milk.\nDaniel moved to the bedroom.\nMary travelled to the office.\nSandra went back to the bathroom.\nJohn went back to the hallway.\nSandra went to the office.\nMary journeyed to the bedroom.\nDaniel went back to the garden.\nDaniel went to the kitchen.\nJohn picked up the football.\nJohn put down the football.\nJohn discarded the milk.\nDaniel moved to the bathroom.\nSandra went back to the garden.\nJohn took the milk.\nSandra moved to the bathroom.\nMary moved to the garden.\nDaniel moved to the garden.\nSandra put down the apple.\n\nThe poem has a refrain and an anonymous narrator.",
  "question": "Where was the apple before the office? ",
  "choices": {
    "A": "office",
    "B": "bedroom",
    "C": "hallway",
    "D": "kitchen",
    "E": "bathroom",
    "F": "garden"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `E` — bathroom | `E` — bathroom | Same answer |
| Decider v1.1 | `E` — bathroom | `E` — bathroom | Same answer |
| Jev | `E` — bathroom | `C` — hallway | Different answer |
| Microsoft Decision-1 | `E` — bathroom | `E` — bathroom | Same answer |
| Clef | `E` — bathroom | `C` — hallway | Different answer |
| Luna Decisions | `C` — hallway | `C` — hallway | Same answer |
| Clef Flash | `F` — garden | `F` — garden | Same answer |
| Strands Decider | `F` — garden | `F` — garden | Same answer |
| GLiNER2.5 Decide | `F` — garden | `F` — garden | Same answer |
| Laya | `A` — office | `A` — office | Same answer |
| CalDec v1 | `A` — office | `A` — office | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `babi/6d3842d1971d4be98e73/examples/absent/clean-source_first_babi_object_contexts_full_0088`

**Input fingerprint:** `02417589241b7122c3fa3e2aea8b22e966f24995a5ffbb51415d627115bd023e`

| Change | Recorded version |
| --- | --- |
| Unrelated examples | No worked example (absence-control recipe) |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/state-tracking-and-updating/babi-6d3842d1971d4be98e73.md).
