# Unrelated examples · No worked example (absence-control recipe) variant

[Original question](../../../questions/numerical-cognition/bbh-853cb81439473652bea2.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> A blue notebook rests on the wooden table beside the window.

## Question

> ((-5 - -7 - 4 - 8) - (-4 + 4 + 1 + 0)) =

## Answer choices

- **A.** -11
- **B.** 1
- **C.** -1
- **D.** -2

**Reference answer:** `A`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "A blue notebook rests on the wooden table beside the window.",
  "question": "((-5 - -7 - 4 - 8) - (-4 + 4 + 1 + 0)) =",
  "choices": {
    "A": "-11",
    "B": "1",
    "C": "-1",
    "D": "-2"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `A` — -11 | `A` — -11 | Same answer |
| Decider v1.1 | `A` — -11 | `A` — -11 | Same answer |
| Jev | `A` — -11 | `A` — -11 | Same answer |
| Microsoft Decision-1 | `A` — -11 | `A` — -11 | Same answer |
| Clef | `D` — -2 | `D` — -2 | Same answer |
| Luna Decisions | `A` — -11 | `A` — -11 | Same answer |
| Clef Flash | `D` — -2 | `D` — -2 | Same answer |
| Strands Decider | `D` — -2 | `D` — -2 | Same answer |
| GLiNER2.5 Decide | `A` — -11 | `A` — -11 | Same answer |
| Laya | `A` — -11 | `A` — -11 | Same answer |
| CalDec v1 | `A` — -11 | `C` — -1 | Different answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `bbh/853cb81439473652bea2/examples/absent/clean-bare_arithmetic_natural_example_controls_full_0059`

**Input fingerprint:** `c098e9df323599afa8bc526d868341d62e89c2d37514de8edcbb4c663516628c`

| Change | Recorded version |
| --- | --- |
| Unrelated examples | No worked example (absence-control recipe) |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/numerical-cognition/bbh-853cb81439473652bea2.md).
