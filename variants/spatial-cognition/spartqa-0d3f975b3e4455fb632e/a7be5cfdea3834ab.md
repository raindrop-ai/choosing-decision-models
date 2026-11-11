# Text length · 512-token input target variant

[Original question](../../../questions/spatial-cognition/spartqa-0d3f975b3e4455fb632e.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

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
> We have three blocks. We call them A, B and C. There is a medium yellow circle in block A. Then, we have block B. It contains one big black square. A big black circle is also in this block. The big black square is far from the big black circle. Block C is above block A and to the right of block B. It has one medium blue square and a small blue circle. The medium blue square is below the small blue circle.

</details>

## Question

> Is the medium yellow circle , below a medium shape that is below a small thing?

## Answer choices

- **Yes.** Yes
- **No.** No
- **DK.** DK

**Reference answer:** `Yes`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "The conservatory occupies a shallow courtyard between a brick residence and a former workshop. Its glazed roof rests on slender iron ribs, while the lower walls retain the texture of old lime plaster. The entrance faces a sheltered gravel court. Through the door, a broad stone path leads toward a recessed bench beneath the far gable. Planting beds lie beside the path, separated from it by low terracotta edging. The interior feels enclosed without feeling cramped: the roof exposes the sky, and the neighboring walls give the planting a sheltered boundary.\n\nThe entrance door has a heavy timber frame and a narrow pane of textured glass. Its handle is polished where hands naturally rest, but the surrounding metal retains a subdued finish. A deep threshold separates the gravel court from the interior paving. Beside the door, a shallow alcove accommodates a brush, a folded cloth, and a rack of garden footwear. The alcove is part of the wall rather than a freestanding cupboard, leaving the entrance passage clear. A slight projection above the doorway shelters the outer face of the timber from direct rain.\n\nThe main path consists of broad limestone slabs with softened edges. Their surface has a faint granular texture, and the joints contain a compact lime mortar. Near the planting beds, the paving has a narrow drainage channel with a removable grating. The channel follows the wall instead of crossing the entrance. The bed edging rises only slightly above the path, making the soil visible from the bench. Along the workshop wall, the slabs meet an older strip of brick paving whose uneven surface gives that side of the room a more domestic character.\n\nThe roof glazing is held in timber glazing bars laid over the iron frame. At the ridge, small ventilation panels sit beneath projecting caps. The caps shelter the opening edges while leaving a passage for air. The roof has a steeper pitch above the central path and a lower profile where it meets the neighboring walls. Narrow gutters follow the eaves. Their supporting brackets are visible from inside, where they form a quiet rhythm against the uninterrupted glass. The metalwork has a muted finish rather than a reflective coating.\n\nWe have three blocks. We call them A, B and C. There is a medium yellow circle in block A. Then, we have block B. It contains one big black square. A big black circle is also in this block. The big black square is far from the big black circle. Block C is above block A and to the right of block B. It has one medium blue square and a small blue circle. The medium blue square is below the small blue circle.",
  "question": "Is the medium yellow circle , below a medium shape that is below a small thing?",
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
| GLiDE v1.2 | `Yes` — Yes | `Yes` — Yes | Same answer |
| Decider v1.1 | `Yes` — Yes | `Yes` — Yes | Same answer |
| Jev | `Yes` — Yes | `Yes` — Yes | Same answer |
| Microsoft Decision-1 | `Yes` — Yes | `Yes` — Yes | Same answer |
| Clef | `No` — No | `No` — No | Same answer |
| Luna Decisions | `DK` — DK | `DK` — DK | Same answer |
| Clef Flash | `No` — No | `No` — No | Same answer |
| Strands Decider | `Yes` — Yes | `Yes` — Yes | Same answer |
| GLiNER2.5 Decide | `No` — No | `No` — No | Same answer |
| Laya | `Yes` — Yes | `Yes` — Yes | Same answer |
| CalDec v1 | `Yes` — Yes | `Yes` — Yes | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `spartqa/0d3f975b3e4455fb632e/text_length/512/clean-source_first_spartqa_combined_contexts_full_0138`

**Input fingerprint:** `8a08a14550b49518bda68113ffabe62dd913b782199b57e30393e42740fd821e`

| Change | Recorded version |
| --- | --- |
| Text length | 512-token input target |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/spatial-cognition/spartqa-0d3f975b3e4455fb632e.md).
