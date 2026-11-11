# Unrelated examples · No worked example (absence-control recipe) variant

[Original question](../../../questions/numerical-cognition/bbh-8b8f4d275ab19baced7e.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> A blue notebook rests on the wooden table beside the window.

## Question

> ((7 - -9 + 0 - 0) + (-9 + 5 - -9 \* -1)) =

## Answer choices

- **A.** -13
- **B.** 3
- **C.** 29
- **D.** 9

**Reference answer:** `B`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "A blue notebook rests on the wooden table beside the window.",
  "question": "((7 - -9 + 0 - 0) + (-9 + 5 - -9 * -1)) =",
  "choices": {
    "A": "-13",
    "B": "3",
    "C": "29",
    "D": "9"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `B` — 3 | `B` — 3 | Same answer |
| Decider v1.1 | `B` — 3 | `B` — 3 | Same answer |
| Jev | `B` — 3 | `B` — 3 | Same answer |
| Microsoft Decision-1 | `B` — 3 | `B` — 3 | Same answer |
| Clef | `D` — 9 | `D` — 9 | Same answer |
| Luna Decisions | `A` — -13 | `A` — -13 | Same answer |
| Clef Flash | `A` — -13 | `D` — 9 | Different answer |
| Strands Decider | `B` — 3 | `B` — 3 | Same answer |
| GLiNER2.5 Decide | `A` — -13 | `A` — -13 | Same answer |
| Laya | `A` — -13 | `D` — 9 | Different answer |
| CalDec v1 | `A` — -13 | `A` — -13 | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `bbh/8b8f4d275ab19baced7e/examples/absent/clean-bare_arithmetic_natural_example_controls_full_0059`

**Input fingerprint:** `fac4ea9113697a6b2f2d7761f5dd9c72657997d52cde2ac418b09ac41abd0b26`

| Change | Recorded version |
| --- | --- |
| Unrelated examples | No worked example (absence-control recipe) |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/numerical-cognition/bbh-8b8f4d275ab19baced7e.md).
