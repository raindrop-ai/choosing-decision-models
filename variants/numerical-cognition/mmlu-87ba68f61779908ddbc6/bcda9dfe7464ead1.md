# Unrelated examples · No worked example (absence-control recipe) variant

[Original question](../../../questions/numerical-cognition/mmlu-87ba68f61779908ddbc6.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> The notebook has a linen cover and stitched binding.

## Question

> A theater collected $6 for each ticket sold to a movie. The theater sold 500 tickets to the movie. The expression below can be used to find how much money the theater collected for the tickets. 6 × 500 Which expression can also be used to find how much money the theater collected for the tickets?

## Answer choices

- **A.** 30 × 10^1
- **B.** 30 × 10^3
- **C.** (6 × 5) × 10^2
- **D.** (6 × 5) × 10^3

**Reference answer:** `C`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "The notebook has a linen cover and stitched binding.",
  "question": "A theater collected $6 for each ticket sold to a movie. The theater sold 500 tickets to the movie. The expression below can be used to find how much money the theater collected for the tickets. 6 × 500 Which expression can also be used to find how much money the theater collected for the tickets?",
  "choices": {
    "A": "30 × 10^1",
    "B": "30 × 10^3",
    "C": "(6 × 5) × 10^2",
    "D": "(6 × 5) × 10^3"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `C` — (6 × 5) × 10^2 | `C` — (6 × 5) × 10^2 | Same answer |
| Decider v1.1 | `C` — (6 × 5) × 10^2 | `C` — (6 × 5) × 10^2 | Same answer |
| Jev | `C` — (6 × 5) × 10^2 | `C` — (6 × 5) × 10^2 | Same answer |
| Microsoft Decision-1 | `C` — (6 × 5) × 10^2 | `C` — (6 × 5) × 10^2 | Same answer |
| Clef | `C` — (6 × 5) × 10^2 | `C` — (6 × 5) × 10^2 | Same answer |
| Luna Decisions | `C` — (6 × 5) × 10^2 | `C` — (6 × 5) × 10^2 | Same answer |
| Clef Flash | `C` — (6 × 5) × 10^2 | `C` — (6 × 5) × 10^2 | Same answer |
| Strands Decider | `C` — (6 × 5) × 10^2 | `C` — (6 × 5) × 10^2 | Same answer |
| GLiNER2.5 Decide | `D` — (6 × 5) × 10^3 | `D` — (6 × 5) × 10^3 | Same answer |
| Laya | `C` — (6 × 5) × 10^2 | `C` — (6 × 5) × 10^2 | Same answer |
| CalDec v1 | `C` — (6 × 5) × 10^2 | `C` — (6 × 5) × 10^2 | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `mmlu/87ba68f61779908ddbc6/examples/absent/clean-source_first_mmlu_quantitative_contexts_full_0098`

**Input fingerprint:** `be53bd3955b206e1ecb590b3db7fb451f064170ccb9e0668fa00d895dc8bcb9b`

| Change | Recorded version |
| --- | --- |
| Unrelated examples | No worked example (absence-control recipe) |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/numerical-cognition/mmlu-87ba68f61779908ddbc6.md).
