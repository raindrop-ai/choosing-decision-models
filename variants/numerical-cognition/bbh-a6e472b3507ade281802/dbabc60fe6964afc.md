# Similar distractors · Add more similar but irrelevant items variant

[Original question](../../../questions/numerical-cognition/bbh-a6e472b3507ade281802.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> ((6 - 5 + 5 + -9) - (9 + 8 \* -6 \* -1)) =
> ((-9 - -7 + 2 + 2) + (-7 + -9 - -1 - 0)) =
> ((3 \* 8 \* -1 \* -9) - (-2 + 2 \* -8 \* 8)) =

## Question

> ((9 + 7 - 4 - 7) - (-5 + 6 + -1 \* 0)) =

## Answer choices

- **A.** 28
- **B.** 5
- **C.** -1
- **D.** 4

**Reference answer:** `D`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "((6 - 5 + 5 + -9) - (9 + 8 * -6 * -1)) =\n((-9 - -7 + 2 + 2) + (-7 + -9 - -1 - 0)) =\n((3 * 8 * -1 * -9) - (-2 + 2 * -8 * 8)) =",
  "question": "((9 + 7 - 4 - 7) - (-5 + 6 + -1 * 0)) =",
  "choices": {
    "A": "28",
    "B": "5",
    "C": "-1",
    "D": "4"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `D` — 4 | `D` — 4 | Same answer |
| Decider v1.1 | `B` — 5 | `D` — 4 | Different answer |
| Jev | `D` — 4 | `D` — 4 | Same answer |
| Microsoft Decision-1 | `D` — 4 | `D` — 4 | Same answer |
| Clef | `B` — 5 | `B` — 5 | Same answer |
| Luna Decisions | `D` — 4 | `D` — 4 | Same answer |
| Clef Flash | `B` — 5 | `B` — 5 | Same answer |
| Strands Decider | `B` — 5 | `D` — 4 | Different answer |
| GLiNER2.5 Decide | `A` — 28 | `A` — 28 | Same answer |
| Laya | `C` — -1 | `C` — -1 | Same answer |
| CalDec v1 | `C` — -1 | `C` — -1 | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `bbh/a6e472b3507ade281802/similar_distractors/high/clean-bare_arithmetic_unsolved_neighbors_full_0057`

**Input fingerprint:** `540de0f3fe1622176de6a2e3e029b26d9010a76ae3f2242e0a005d33fb92afe1`

| Change | Recorded version |
| --- | --- |
| Similar distractors | Add more similar but irrelevant items |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/numerical-cognition/bbh-a6e472b3507ade281802.md).
