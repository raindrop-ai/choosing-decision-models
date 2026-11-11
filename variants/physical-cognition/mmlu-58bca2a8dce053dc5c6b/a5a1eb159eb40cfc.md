# Similar distractors · Add fewer similar but irrelevant items variant

[Original question](../../../questions/physical-cognition/mmlu-58bca2a8dce053dc5c6b.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> «A separate fictional mission record places a probe near a small moon and records a curved trajectory on its navigation chart.»

## Question

> A simple and correct way to comprehend satellites orbiting Earth is to view them as

## Answer choices

- **A.** balanced between gravitational and centripetal forces.
- **B.** beyond the main pull of Earth gravity.
- **C.** in mechanical equilibrium with a net force of zero.
- **D.** having sufficient tangential velocities to fall around rather than into Earth.

**Reference answer:** `D`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "«A separate fictional mission record places a probe near a small moon and records a curved trajectory on its navigation chart.»",
  "question": "A simple and correct way to comprehend satellites orbiting Earth is to view them as",
  "choices": {
    "A": "balanced between gravitational and centripetal forces.",
    "B": "beyond the main pull of Earth gravity.",
    "C": "in mechanical equilibrium with a net force of zero.",
    "D": "having sufficient tangential velocities to fall around rather than into Earth."
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `D` — having sufficient tangential velocities to fall around rather than into Earth. | `D` — having sufficient tangential velocities to fall around rather than into Earth. | Same answer |
| Decider v1.1 | `D` — having sufficient tangential velocities to fall around rather than into Earth. | `D` — having sufficient tangential velocities to fall around rather than into Earth. | Same answer |
| Jev | `D` — having sufficient tangential velocities to fall around rather than into Earth. | `D` — having sufficient tangential velocities to fall around rather than into Earth. | Same answer |
| Microsoft Decision-1 | `D` — having sufficient tangential velocities to fall around rather than into Earth. | `D` — having sufficient tangential velocities to fall around rather than into Earth. | Same answer |
| Clef | `D` — having sufficient tangential velocities to fall around rather than into Earth. | `D` — having sufficient tangential velocities to fall around rather than into Earth. | Same answer |
| Luna Decisions | `D` — having sufficient tangential velocities to fall around rather than into Earth. | `D` — having sufficient tangential velocities to fall around rather than into Earth. | Same answer |
| Clef Flash | `D` — having sufficient tangential velocities to fall around rather than into Earth. | `D` — having sufficient tangential velocities to fall around rather than into Earth. | Same answer |
| Strands Decider | `D` — having sufficient tangential velocities to fall around rather than into Earth. | `D` — having sufficient tangential velocities to fall around rather than into Earth. | Same answer |
| GLiNER2.5 Decide | `D` — having sufficient tangential velocities to fall around rather than into Earth. | `D` — having sufficient tangential velocities to fall around rather than into Earth. | Same answer |
| Laya | `C` — in mechanical equilibrium with a net force of zero. | `A` — balanced between gravitational and centripetal forces. | Different answer |
| CalDec v1 | `A` — balanced between gravitational and centripetal forces. | `B` — beyond the main pull of Earth gravity. | Different answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `mmlu/58bca2a8dce053dc5c6b/similar_distractors/low/clean-source_first_parallel_b_near_accounts_0301`

**Input fingerprint:** `91e97a212be2e75042d3c391fe3391216208ab546ca1d564bc2e59b8a0e41fa9`

| Change | Recorded version |
| --- | --- |
| Similar distractors | Add fewer similar but irrelevant items |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/physical-cognition/mmlu-58bca2a8dce053dc5c6b.md).
