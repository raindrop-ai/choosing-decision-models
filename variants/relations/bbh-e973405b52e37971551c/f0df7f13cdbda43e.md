# Text length · 512-token input target variant

[Original question](../../../questions/relations/bbh-e973405b52e37971551c.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

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
> The planting beside the residence wall is dominated by broad leaves and arching stems. Ferns occupy the shaded ground beneath taller foliage, and moss softens the exposed soil around the bed edges. The leaves differ in texture: some are smooth and leathery, others finely divided, with delicate veins visible against the roof light. None of the beds is raised on a stand. The plants emerge directly from a continuous soil surface, which gives the room the feeling of a small sheltered garden rather than a collection of movable containers.

</details>

## Question

> The following paragraphs each describe a set of three objects arranged in a fixed order. The statements are logically consistent within each paragraph. In an antique car show, there are three vehicles: a convertible, a motorcyle, and a truck. The motorcyle is newer than the convertible. The convertible is newer than the truck.

## Answer choices

- **A.** The convertible is the oldest
- **B.** The motorcyle is the oldest
- **C.** The truck is the oldest

**Reference answer:** `C`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "The conservatory occupies a shallow courtyard between a brick residence and a former workshop. Its glazed roof rests on slender iron ribs, while the lower walls retain the texture of old lime plaster. The entrance faces a sheltered gravel court. Through the door, a broad stone path leads toward a recessed bench beneath the far gable. Planting beds lie beside the path, separated from it by low terracotta edging. The interior feels enclosed without feeling cramped: the roof exposes the sky, and the neighboring walls give the planting a sheltered boundary.\n\nThe entrance door has a heavy timber frame and a narrow pane of textured glass. Its handle is polished where hands naturally rest, but the surrounding metal retains a subdued finish. A deep threshold separates the gravel court from the interior paving. Beside the door, a shallow alcove accommodates a brush, a folded cloth, and a rack of garden footwear. The alcove is part of the wall rather than a freestanding cupboard, leaving the entrance passage clear. A slight projection above the doorway shelters the outer face of the timber from direct rain.\n\nThe main path consists of broad limestone slabs with softened edges. Their surface has a faint granular texture, and the joints contain a compact lime mortar. Near the planting beds, the paving has a narrow drainage channel with a removable grating. The channel follows the wall instead of crossing the entrance. The bed edging rises only slightly above the path, making the soil visible from the bench. Along the workshop wall, the slabs meet an older strip of brick paving whose uneven surface gives that side of the room a more domestic character.\n\nThe roof glazing is held in timber glazing bars laid over the iron frame. At the ridge, small ventilation panels sit beneath projecting caps. The caps shelter the opening edges while leaving a passage for air. The roof has a steeper pitch above the central path and a lower profile where it meets the neighboring walls. Narrow gutters follow the eaves. Their supporting brackets are visible from inside, where they form a quiet rhythm against the uninterrupted glass. The metalwork has a muted finish rather than a reflective coating.\n\nThe planting beside the residence wall is dominated by broad leaves and arching stems. Ferns occupy the shaded ground beneath taller foliage, and moss softens the exposed soil around the bed edges. The leaves differ in texture: some are smooth and leathery, others finely divided, with delicate veins visible against the roof light. None of the beds is raised on a stand. The plants emerge directly from a continuous soil surface, which gives the room the feeling of a small sheltered garden rather than a collection of movable containers.",
  "question": "The following paragraphs each describe a set of three objects arranged in a fixed order. The statements are logically consistent within each paragraph. In an antique car show, there are three vehicles: a convertible, a motorcyle, and a truck. The motorcyle is newer than the convertible. The convertible is newer than the truck.",
  "choices": {
    "A": "The convertible is the oldest",
    "B": "The motorcyle is the oldest",
    "C": "The truck is the oldest"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `C` — The truck is the oldest | `C` — The truck is the oldest | Same answer |
| Decider v1.1 | `C` — The truck is the oldest | `C` — The truck is the oldest | Same answer |
| Jev | `C` — The truck is the oldest | `C` — The truck is the oldest | Same answer |
| Microsoft Decision-1 | `C` — The truck is the oldest | `C` — The truck is the oldest | Same answer |
| Clef | `C` — The truck is the oldest | `C` — The truck is the oldest | Same answer |
| Luna Decisions | `C` — The truck is the oldest | `C` — The truck is the oldest | Same answer |
| Clef Flash | `C` — The truck is the oldest | `C` — The truck is the oldest | Same answer |
| Strands Decider | `C` — The truck is the oldest | `C` — The truck is the oldest | Same answer |
| GLiNER2.5 Decide | `A` — The convertible is the oldest | `A` — The convertible is the oldest | Same answer |
| Laya | `A` — The convertible is the oldest | `B` — The motorcyle is the oldest | Different answer |
| CalDec v1 | `A` — The convertible is the oldest | `B` — The motorcyle is the oldest | Different answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `bbh/e973405b52e37971551c/text_length/512/clean-source_first_ordinal_combined_contexts_full_0139`

**Input fingerprint:** `eb1a4eb98a56b308ba244bd4cd3fe250477f38737c7c519fc0f70d14bcefffce`

| Change | Recorded version |
| --- | --- |
| Text length | 512-token input target |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/relations/bbh-e973405b52e37971551c.md).
