# Similar distractors · Add more similar but irrelevant items variant

[Original question](../../../questions/numerical-cognition/bbh-40eceedeab129fcf9d44.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> ((-8 - -3 \* 5 + 4) \* (2 \* 7 - -3 - -1)) =
> ((-2 \* -1 + 1 \* -3) - (7 \* -7 + -5 \* 6)) =
> ((1 + 1 \* 3 - 2) \* (-8 - -2 - 9 + -9)) =

## Question

> ((3 + 3 - -4 - 2) + (-2 - -7 \* -2 \* 1)) =

## Answer choices

- **A.** 8
- **B.** 14
- **C.** -1
- **D.** -8

**Reference answer:** `D`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "((-8 - -3 * 5 + 4) * (2 * 7 - -3 - -1)) =\n((-2 * -1 + 1 * -3) - (7 * -7 + -5 * 6)) =\n((1 + 1 * 3 - 2) * (-8 - -2 - 9 + -9)) =",
  "question": "((3 + 3 - -4 - 2) + (-2 - -7 * -2 * 1)) =",
  "choices": {
    "A": "8",
    "B": "14",
    "C": "-1",
    "D": "-8"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `D` — -8 | `D` — -8 | Same answer |
| Decider v1.1 | `D` — -8 | `D` — -8 | Same answer |
| Jev | `D` — -8 | `D` — -8 | Same answer |
| Microsoft Decision-1 | `D` — -8 | `D` — -8 | Same answer |
| Clef | `C` — -1 | `C` — -1 | Same answer |
| Luna Decisions | `C` — -1 | `A` — 8 | Different answer |
| Clef Flash | `C` — -1 | `C` — -1 | Same answer |
| Strands Decider | `A` — 8 | `D` — -8 | Different answer |
| GLiNER2.5 Decide | `A` — 8 | `D` — -8 | Different answer |
| Laya | `D` — -8 | `C` — -1 | Different answer |
| CalDec v1 | `C` — -1 | `A` — 8 | Different answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `bbh/40eceedeab129fcf9d44/similar_distractors/high/clean-bare_arithmetic_unsolved_neighbors_full_0057`

**Input fingerprint:** `3d2c202b18dcfa966b321baf588f6cbe27cadd6ae43eb093ff1c64b405a2f0a9`

| Change | Recorded version |
| --- | --- |
| Similar distractors | Add more similar but irrelevant items |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/numerical-cognition/bbh-40eceedeab129fcf9d44.md).
