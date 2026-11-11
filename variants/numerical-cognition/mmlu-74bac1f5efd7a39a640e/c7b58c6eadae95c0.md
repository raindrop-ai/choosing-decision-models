# Unrelated examples · No worked example (absence-control recipe) variant

[Original question](../../../questions/numerical-cognition/mmlu-74bac1f5efd7a39a640e.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> The notebook has a linen cover and stitched binding.

## Question

> In a group of 10 scores, the largest score is increased by 40 points. What will happen to the mean?

## Answer choices

- **A.** It will remain the same.
- **B.** It will increase by 4 points.
- **C.** It will increase by 10 points.
- **D.** It will increase by 40 points.

**Reference answer:** `B`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "The notebook has a linen cover and stitched binding.",
  "question": "In a group of 10 scores, the largest score is increased by 40 points. What will happen to the mean?",
  "choices": {
    "A": "It will remain the same.",
    "B": "It will increase by 4 points.",
    "C": "It will increase by 10 points.",
    "D": "It will increase by 40 points."
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `B` — It will increase by 4 points. | `B` — It will increase by 4 points. | Same answer |
| Decider v1.1 | `B` — It will increase by 4 points. | `B` — It will increase by 4 points. | Same answer |
| Jev | `B` — It will increase by 4 points. | `B` — It will increase by 4 points. | Same answer |
| Microsoft Decision-1 | `B` — It will increase by 4 points. | `B` — It will increase by 4 points. | Same answer |
| Clef | `B` — It will increase by 4 points. | `B` — It will increase by 4 points. | Same answer |
| Luna Decisions | `B` — It will increase by 4 points. | `B` — It will increase by 4 points. | Same answer |
| Clef Flash | `B` — It will increase by 4 points. | `B` — It will increase by 4 points. | Same answer |
| Strands Decider | `B` — It will increase by 4 points. | `B` — It will increase by 4 points. | Same answer |
| GLiNER2.5 Decide | `D` — It will increase by 40 points. | `D` — It will increase by 40 points. | Same answer |
| Laya | `C` — It will increase by 10 points. | `C` — It will increase by 10 points. | Same answer |
| CalDec v1 | `C` — It will increase by 10 points. | `B` — It will increase by 4 points. | Different answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `mmlu/74bac1f5efd7a39a640e/examples/absent/clean-source_first_mmlu_quantitative_contexts_full_0098`

**Input fingerprint:** `92f0684c9852d15fdf541d39d84724ce5e65b9347664fe548c1be6c6120471a4`

| Change | Recorded version |
| --- | --- |
| Unrelated examples | No worked example (absence-control recipe) |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/numerical-cognition/mmlu-74bac1f5efd7a39a640e.md).
