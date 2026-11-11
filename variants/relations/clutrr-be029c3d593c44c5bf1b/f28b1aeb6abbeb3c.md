# Text length · 512-token input target variant

[Original question](../../../questions/relations/clutrr-be029c3d593c44c5bf1b.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

<details>
<summary>Read the full context</summary>

> \[William\] took his sister \[Sheila\] out to lunch after learning that she got accepted into her first choice for university. \[Seth\] and his daughter \[Ruth\] took a day off school to go to the zoo. \[Jonathan\] took his sister \[Ruth\] out to lunch after learning that she got accepted into her first choice for university. \[Jonathan\] is proud that his daughter is such a good student. Her name is \[Diana\]. \[Sheila\], who is the sister of \[Diana\], is a lovely girl.
>
> The conservatory occupies a shallow courtyard between a brick residence and a former workshop. Its glazed roof rests on slender iron ribs, while the lower walls retain the texture of old lime plaster. The entrance faces a sheltered gravel court. Through the door, a broad stone path leads toward a recessed bench beneath the far gable. Planting beds lie beside the path, separated from it by low terracotta edging. The interior feels enclosed without feeling cramped: the roof exposes the sky, and the neighboring walls give the planting a sheltered boundary.
>
> The entrance door has a heavy timber frame and a narrow pane of textured glass. Its handle is polished where hands naturally rest, but the surrounding metal retains a subdued finish. A deep threshold separates the gravel court from the interior paving. Beside the door, a shallow alcove accommodates a brush, a folded cloth, and a rack of garden footwear. The alcove is part of the wall rather than a freestanding cupboard, leaving the entrance passage clear. A slight projection above the doorway shelters the outer face of the timber from direct rain.
>
> The main path consists of broad limestone slabs with softened edges. Their surface has a faint granular texture, and the joints contain a compact lime mortar. Near the planting beds, the paving has a narrow drainage channel with a removable grating. The channel follows the wall instead of crossing the entrance. The bed edging rises only slightly above the path, making the soil visible from the bench. Along the workshop wall, the slabs meet an older strip of brick paving whose uneven surface gives that side of the room a more domestic character.
>
> The roof glazing is held in timber glazing bars laid over the iron frame. At the ridge, small ventilation panels sit beneath projecting caps. The caps shelter the opening edges while leaving a passage for air. The roof has a steeper pitch above the central path and a lower profile where it meets the neighboring walls. Narrow gutters follow the eaves. Their supporting brackets are visible from inside, where they form a quiet rhythm against the uninterrupted glass. The metalwork has a muted finish rather than a reflective coating.

</details>

## Question

> What is William’s relationship to Seth?

## Answer choices

- **aunt.** aunt
- **brother.** brother
- **daughter.** daughter
- **daughter-in-law.** daughter-in-law
- **father.** father
- **father-in-law.** father-in-law
- **granddaughter.** granddaughter
- **grandfather.** grandfather
- **grandmother.** grandmother
- **grandson.** grandson
- **mother.** mother
- **mother-in-law.** mother-in-law
- **nephew.** nephew
- **niece.** niece
- **sister.** sister
- **son.** son
- **son-in-law.** son-in-law
- **uncle.** uncle

**Reference answer:** `grandson`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "[William] took his sister [Sheila] out to lunch after learning that she got accepted into her first choice for university. [Seth] and his daughter [Ruth] took a day off school to go to the zoo. [Jonathan] took his sister [Ruth] out to lunch after learning that she got accepted into her first choice for university. [Jonathan] is proud that his daughter is such a good student. Her name is [Diana]. [Sheila], who is the sister of [Diana], is a lovely girl.\n\nThe conservatory occupies a shallow courtyard between a brick residence and a former workshop. Its glazed roof rests on slender iron ribs, while the lower walls retain the texture of old lime plaster. The entrance faces a sheltered gravel court. Through the door, a broad stone path leads toward a recessed bench beneath the far gable. Planting beds lie beside the path, separated from it by low terracotta edging. The interior feels enclosed without feeling cramped: the roof exposes the sky, and the neighboring walls give the planting a sheltered boundary.\n\nThe entrance door has a heavy timber frame and a narrow pane of textured glass. Its handle is polished where hands naturally rest, but the surrounding metal retains a subdued finish. A deep threshold separates the gravel court from the interior paving. Beside the door, a shallow alcove accommodates a brush, a folded cloth, and a rack of garden footwear. The alcove is part of the wall rather than a freestanding cupboard, leaving the entrance passage clear. A slight projection above the doorway shelters the outer face of the timber from direct rain.\n\nThe main path consists of broad limestone slabs with softened edges. Their surface has a faint granular texture, and the joints contain a compact lime mortar. Near the planting beds, the paving has a narrow drainage channel with a removable grating. The channel follows the wall instead of crossing the entrance. The bed edging rises only slightly above the path, making the soil visible from the bench. Along the workshop wall, the slabs meet an older strip of brick paving whose uneven surface gives that side of the room a more domestic character.\n\nThe roof glazing is held in timber glazing bars laid over the iron frame. At the ridge, small ventilation panels sit beneath projecting caps. The caps shelter the opening edges while leaving a passage for air. The roof has a steeper pitch above the central path and a lower profile where it meets the neighboring walls. Narrow gutters follow the eaves. Their supporting brackets are visible from inside, where they form a quiet rhythm against the uninterrupted glass. The metalwork has a muted finish rather than a reflective coating.",
  "question": "What is William’s relationship to Seth?",
  "choices": {
    "aunt": "aunt",
    "brother": "brother",
    "daughter": "daughter",
    "daughter-in-law": "daughter-in-law",
    "father": "father",
    "father-in-law": "father-in-law",
    "granddaughter": "granddaughter",
    "grandfather": "grandfather",
    "grandmother": "grandmother",
    "grandson": "grandson",
    "mother": "mother",
    "mother-in-law": "mother-in-law",
    "nephew": "nephew",
    "niece": "niece",
    "sister": "sister",
    "son": "son",
    "son-in-law": "son-in-law",
    "uncle": "uncle"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `son-in-law` — son-in-law | `brother` — brother | Different answer |
| Decider v1.1 | `son-in-law` — son-in-law | `uncle` — uncle | Different answer |
| Jev | `brother` — brother | `brother` — brother | Same answer |
| Microsoft Decision-1 | `uncle` — uncle | `uncle` — uncle | Same answer |
| Clef | `uncle` — uncle | `uncle` — uncle | Same answer |
| Luna Decisions | `brother` — brother | Refused | — |
| Clef Flash | `uncle` — uncle | `uncle` — uncle | Same answer |
| Strands Decider | `sister` — sister | `sister` — sister | Same answer |
| GLiNER2.5 Decide | `sister` — sister | `sister` — sister | Same answer |
| Laya | `sister` — sister | `sister` — sister | Same answer |
| CalDec v1 | `sister` — sister | `sister` — sister | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `clutrr/be029c3d593c44c5bf1b/text_length/512/clean-source_first_kinship_length_position_events_full_0103`

**Input fingerprint:** `49a939d84f9a1834b6e515f68d9e24d38310a22529e3096f3a81858bd369a445`

| Change | Recorded version |
| --- | --- |
| Text length | 512-token input target |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/relations/clutrr-be029c3d593c44c5bf1b.md).
