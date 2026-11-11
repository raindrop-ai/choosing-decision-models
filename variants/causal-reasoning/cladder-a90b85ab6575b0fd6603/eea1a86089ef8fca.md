# Text length · 512-token input target variant

[Original question](../../../questions/causal-reasoning/cladder-a90b85ab6575b0fd6603.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

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
> Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Kraz has a direct effect on pexu and rukz. Pexu has a direct effect on hwax. Hwax has a direct effect on rukz. Kraz is unobserved.
> For those who are not pexu, the probability of hwax is 43%. For those who are pexu, the probability of hwax is 92%. For those who are not pexu and are not hwax, the probability of rukz is 0%. For those who are not pexu and are hwax, the probability of rukz is 34%. For those who are pexu and are not hwax, the probability of rukz is 1%. For those who are pexu and are hwax, the probability of rukz is 33%. The overall probability of pexu is 17%.

</details>

## Question

> Does pexu negatively affect rukz through hwax?

## Answer choices

- **yes.** Yes
- **no.** No

**Reference answer:** `no`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "The conservatory occupies a shallow courtyard between a brick residence and a former workshop. Its glazed roof rests on slender iron ribs, while the lower walls retain the texture of old lime plaster. The entrance faces a sheltered gravel court. Through the door, a broad stone path leads toward a recessed bench beneath the far gable. Planting beds lie beside the path, separated from it by low terracotta edging. The interior feels enclosed without feeling cramped: the roof exposes the sky, and the neighboring walls give the planting a sheltered boundary.\n\nThe entrance door has a heavy timber frame and a narrow pane of textured glass. Its handle is polished where hands naturally rest, but the surrounding metal retains a subdued finish. A deep threshold separates the gravel court from the interior paving. Beside the door, a shallow alcove accommodates a brush, a folded cloth, and a rack of garden footwear. The alcove is part of the wall rather than a freestanding cupboard, leaving the entrance passage clear. A slight projection above the doorway shelters the outer face of the timber from direct rain.\n\nThe main path consists of broad limestone slabs with softened edges. Their surface has a faint granular texture, and the joints contain a compact lime mortar. Near the planting beds, the paving has a narrow drainage channel with a removable grating. The channel follows the wall instead of crossing the entrance. The bed edging rises only slightly above the path, making the soil visible from the bench. Along the workshop wall, the slabs meet an older strip of brick paving whose uneven surface gives that side of the room a more domestic character.\n\nImagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Kraz has a direct effect on pexu and rukz. Pexu has a direct effect on hwax. Hwax has a direct effect on rukz. Kraz is unobserved.\nFor those who are not pexu, the probability of hwax is 43%. For those who are pexu, the probability of hwax is 92%. For those who are not pexu and are not hwax, the probability of rukz is 0%. For those who are not pexu and are hwax, the probability of rukz is 34%. For those who are pexu and are not hwax, the probability of rukz is 1%. For those who are pexu and are hwax, the probability of rukz is 33%. The overall probability of pexu is 17%.",
  "question": "Does pexu negatively affect rukz through hwax?",
  "choices": {
    "yes": "Yes",
    "no": "No"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `no` — No | `no` — No | Same answer |
| Decider v1.1 | `no` — No | `no` — No | Same answer |
| Jev | `no` — No | `no` — No | Same answer |
| Microsoft Decision-1 | `no` — No | `no` — No | Same answer |
| Clef | `no` — No | `no` — No | Same answer |
| Luna Decisions | `no` — No | `no` — No | Same answer |
| Clef Flash | `no` — No | `no` — No | Same answer |
| Strands Decider | `yes` — Yes | `no` — No | Different answer |
| GLiNER2.5 Decide | `no` — No | `no` — No | Same answer |
| Laya | `no` — No | `yes` — Yes | Different answer |
| CalDec v1 | `yes` — Yes | `no` — No | Different answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `cladder/a90b85ab6575b0fd6603/text_length/512/clean-source_first_cladder_natural_lengths_full_0131`

**Input fingerprint:** `20297eb64bff9edba7488358cb4033489d7da9c0aa22d57607e18768b32b4b38`

| Change | Recorded version |
| --- | --- |
| Text length | 512-token input target |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/causal-reasoning/cladder-a90b85ab6575b0fd6603.md).
