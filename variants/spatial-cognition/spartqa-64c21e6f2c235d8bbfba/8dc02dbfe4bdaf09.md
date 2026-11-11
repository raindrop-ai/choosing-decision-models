# Text length · 512-token input target variant

[Original question](../../../questions/spatial-cognition/spartqa-64c21e6f2c235d8bbfba.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

<details>
<summary>Read the full context</summary>

> The conservatory occupies a shallow courtyard between a brick residence and a former workshop. Its glazed roof rests on slender iron ribs, while the lower walls retain the texture of old lime plaster. The entrance faces a sheltered gravel court. Through the door, a broad stone path leads toward a recessed bench beneath the far gable. Planting beds lie beside the path, separated from it by low terracotta edging. The interior feels enclosed without feeling cramped: the roof exposes the sky, and the neighboring walls give the planting a sheltered boundary.
>
> The entrance door has a heavy timber frame and a narrow pane of textured glass. Its handle is polished where hands naturally rest, but the surrounding metal retains a subdued finish. A deep threshold separates the gravel court from the interior paving. Beside the door, a shallow alcove accommodates a brush, a folded cloth, and a rack of garden footwear. The alcove is part of the wall rather than a freestanding cupboard, leaving the entrance passage clear. A slight projection above the doorway shelters the outer face of the timber from direct rain.
>
> The main path consists of broad limestone slabs with softened edges. Their surface has a faint granular texture, and the joints contain a compact lime mortar. Near the planting beds, the paving has a narrow drainage channel with a removable grating. The channel follows the wall instead of crossing the entrance. The bed edging rises only slightly above the path, making the soil visible from the bench. Along the workshop wall, the slabs meet an older strip of brick paving whose uneven surface gives that side of the room a more domestic character.
>
> The roof glazing is held in timber glazing bars laid over the iron frame. At the ridge, small ventilation panels sit beneath projecting caps. The caps shelter the opening edges while leaving a passage for air. The roof has a steeper pitch above the central path and a lower profile where it meets the neighboring walls. Narrow gutters follow the eaves. Their supporting brackets are visible from inside, where they form a quiet rhythm against the uninterrupted glass. The metalwork has a muted finish rather than a reflective coating.
>
> We have three blocks, A, B and C. Block A has a small black circle and a big blue circle. Below the big blue circle there is the small black circle. Block B is to the right of block A. It contains one big black triangle. There is also one medium black circle touching the right edge of this block. A big blue triangle is also in this block. Above the medium black circle and the big blue triangle there is the big black triangle. Above block B there is block C which has one small yellow circle. One medium blue triangle is also in this block. It is far from a big black circle. Above the medium blue triangle there is the small yellow circle. The big black circle is touching the right edge of this block. To the left of the big black circle there is the small yellow circle.

</details>

## Question

> What is to the right of the big blue circle? a big blue triangle or a small black circle?

## Answer choices

- **0.** big blue triangle 
- **1.** small black circle 
- **2.** both of them
- **3.** none of them

**Reference answer:** `0`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "The conservatory occupies a shallow courtyard between a brick residence and a former workshop. Its glazed roof rests on slender iron ribs, while the lower walls retain the texture of old lime plaster. The entrance faces a sheltered gravel court. Through the door, a broad stone path leads toward a recessed bench beneath the far gable. Planting beds lie beside the path, separated from it by low terracotta edging. The interior feels enclosed without feeling cramped: the roof exposes the sky, and the neighboring walls give the planting a sheltered boundary.\n\nThe entrance door has a heavy timber frame and a narrow pane of textured glass. Its handle is polished where hands naturally rest, but the surrounding metal retains a subdued finish. A deep threshold separates the gravel court from the interior paving. Beside the door, a shallow alcove accommodates a brush, a folded cloth, and a rack of garden footwear. The alcove is part of the wall rather than a freestanding cupboard, leaving the entrance passage clear. A slight projection above the doorway shelters the outer face of the timber from direct rain.\n\nThe main path consists of broad limestone slabs with softened edges. Their surface has a faint granular texture, and the joints contain a compact lime mortar. Near the planting beds, the paving has a narrow drainage channel with a removable grating. The channel follows the wall instead of crossing the entrance. The bed edging rises only slightly above the path, making the soil visible from the bench. Along the workshop wall, the slabs meet an older strip of brick paving whose uneven surface gives that side of the room a more domestic character.\n\nThe roof glazing is held in timber glazing bars laid over the iron frame. At the ridge, small ventilation panels sit beneath projecting caps. The caps shelter the opening edges while leaving a passage for air. The roof has a steeper pitch above the central path and a lower profile where it meets the neighboring walls. Narrow gutters follow the eaves. Their supporting brackets are visible from inside, where they form a quiet rhythm against the uninterrupted glass. The metalwork has a muted finish rather than a reflective coating.\n\nWe have three blocks, A, B and C. Block A has a small black circle and a big blue circle. Below the big blue circle there is the small black circle. Block B is to the right of block A. It contains one big black triangle. There is also one medium black circle touching the right edge of this block. A big blue triangle is also in this block. Above the medium black circle and the big blue triangle there is the big black triangle. Above block B there is block C which has one small yellow circle. One medium blue triangle is also in this block. It is far from a big black circle. Above the medium blue triangle there is the small yellow circle. The big black circle is touching the right edge of this block. To the left of the big black circle there is the small yellow circle.",
  "question": "What is to the right of the big blue circle? a big blue triangle or a small black circle?",
  "choices": {
    "0": "big blue triangle ",
    "1": "small black circle ",
    "2": "both of them",
    "3": "none of them"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `0` — big blue triangle  | `0` — big blue triangle  | Same answer |
| Decider v1.1 | `0` — big blue triangle  | `0` — big blue triangle  | Same answer |
| Jev | `0` — big blue triangle  | `0` — big blue triangle  | Same answer |
| Microsoft Decision-1 | `0` — big blue triangle  | `0` — big blue triangle  | Same answer |
| Clef | `0` — big blue triangle  | `0` — big blue triangle  | Same answer |
| Luna Decisions | `0` — big blue triangle  | `1` — small black circle  | Different answer |
| Clef Flash | `3` — none of them | `1` — small black circle  | Different answer |
| Strands Decider | `0` — big blue triangle  | `0` — big blue triangle  | Same answer |
| GLiNER2.5 Decide | `1` — small black circle  | `1` — small black circle  | Same answer |
| Laya | `3` — none of them | `3` — none of them | Same answer |
| CalDec v1 | `2` — both of them | `2` — both of them | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `spartqa/64c21e6f2c235d8bbfba/text_length/512/clean-source_first_spartqa_combined_contexts_full_0138`

**Input fingerprint:** `60962c292f30bcc4630d1b0272f2a7ec7f592c2d5a1b818656014a203901caaf`

| Change | Recorded version |
| --- | --- |
| Text length | 512-token input target |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/spatial-cognition/spartqa-64c21e6f2c235d8bbfba.md).
