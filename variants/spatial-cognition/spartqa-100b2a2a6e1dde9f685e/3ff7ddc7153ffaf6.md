# Text length · 512-token input target variant

[Original question](../../../questions/spatial-cognition/spartqa-100b2a2a6e1dde9f685e.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

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
> There are three blocks called A, B, and C. B is to the right of A and C is to the right of B. In A, there is a small black triangle near and below a large yellow circle. Far to the right of the yellow circle is a small blue square. In B, there is a large black triangle far below a small blue circle. The small blue circle is near and below a small blue triangle. In C, there is a small blue circle.

</details>

## Question

> Is the small blue circle in B below a large black thing?

## Answer choices

- **Yes.** Yes
- **No.** No
- **DK.** DK

**Reference answer:** `No`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "The conservatory occupies a shallow courtyard between a brick residence and a former workshop. Its glazed roof rests on slender iron ribs, while the lower walls retain the texture of old lime plaster. The entrance faces a sheltered gravel court. Through the door, a broad stone path leads toward a recessed bench beneath the far gable. Planting beds lie beside the path, separated from it by low terracotta edging. The interior feels enclosed without feeling cramped: the roof exposes the sky, and the neighboring walls give the planting a sheltered boundary.\n\nThe entrance door has a heavy timber frame and a narrow pane of textured glass. Its handle is polished where hands naturally rest, but the surrounding metal retains a subdued finish. A deep threshold separates the gravel court from the interior paving. Beside the door, a shallow alcove accommodates a brush, a folded cloth, and a rack of garden footwear. The alcove is part of the wall rather than a freestanding cupboard, leaving the entrance passage clear. A slight projection above the doorway shelters the outer face of the timber from direct rain.\n\nThe main path consists of broad limestone slabs with softened edges. Their surface has a faint granular texture, and the joints contain a compact lime mortar. Near the planting beds, the paving has a narrow drainage channel with a removable grating. The channel follows the wall instead of crossing the entrance. The bed edging rises only slightly above the path, making the soil visible from the bench. Along the workshop wall, the slabs meet an older strip of brick paving whose uneven surface gives that side of the room a more domestic character.\n\nThe roof glazing is held in timber glazing bars laid over the iron frame. At the ridge, small ventilation panels sit beneath projecting caps. The caps shelter the opening edges while leaving a passage for air. The roof has a steeper pitch above the central path and a lower profile where it meets the neighboring walls. Narrow gutters follow the eaves. Their supporting brackets are visible from inside, where they form a quiet rhythm against the uninterrupted glass. The metalwork has a muted finish rather than a reflective coating.\n\nThere are three blocks called A, B, and C. B is to the right of A and C is to the right of B. In A, there is a small black triangle near and below a large yellow circle. Far to the right of the yellow circle is a small blue square. In B, there is a large black triangle far below a small blue circle. The small blue circle is near and below a small blue triangle. In C, there is a small blue circle.",
  "question": "Is the small blue circle in B below a large black thing?",
  "choices": {
    "Yes": "Yes",
    "No": "No",
    "DK": "DK"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `No` — No | `No` — No | Same answer |
| Decider v1.1 | `No` — No | `No` — No | Same answer |
| Jev | `No` — No | `No` — No | Same answer |
| Microsoft Decision-1 | `No` — No | `No` — No | Same answer |
| Clef | `Yes` — Yes | `Yes` — Yes | Same answer |
| Luna Decisions | `Yes` — Yes | `Yes` — Yes | Same answer |
| Clef Flash | `No` — No | `Yes` — Yes | Different answer |
| Strands Decider | `Yes` — Yes | `Yes` — Yes | Same answer |
| GLiNER2.5 Decide | `No` — No | `Yes` — Yes | Different answer |
| Laya | `Yes` — Yes | `No` — No | Different answer |
| CalDec v1 | `Yes` — Yes | `No` — No | Different answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `spartqa/100b2a2a6e1dde9f685e/text_length/512/clean-source_first_spartqa_combined_contexts_full_0138`

**Input fingerprint:** `71ea56b9b117c397c6a1a6f8149b95f1bd1555ba762e7e35b368658d4ef26896`

| Change | Recorded version |
| --- | --- |
| Text length | 512-token input target |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/spatial-cognition/spartqa-100b2a2a6e1dde9f685e.md).
