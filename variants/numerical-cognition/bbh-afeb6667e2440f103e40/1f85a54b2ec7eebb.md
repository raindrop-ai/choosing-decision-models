# Unrelated examples · Add examples unrelated to the question variant

[Original question](../../../questions/numerical-cognition/bbh-afeb6667e2440f103e40.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Capitalization: blue birds fly. → Blue birds fly.

## Question

> ((0 \* -4 - -7 \* 5) + (-4 \* 0 + 6 + 0)) =

## Answer choices

- **A.** 0
- **B.** 1
- **C.** 41
- **D.** -35

**Reference answer:** `C`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Capitalization: blue birds fly. → Blue birds fly.",
  "question": "((0 * -4 - -7 * 5) + (-4 * 0 + 6 + 0)) =",
  "choices": {
    "A": "0",
    "B": "1",
    "C": "41",
    "D": "-35"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `C` — 41 | `C` — 41 | Same answer |
| Decider v1.1 | `C` — 41 | `C` — 41 | Same answer |
| Jev | `C` — 41 | `C` — 41 | Same answer |
| Microsoft Decision-1 | `C` — 41 | `C` — 41 | Same answer |
| Clef | `C` — 41 | `C` — 41 | Same answer |
| Luna Decisions | `C` — 41 | `C` — 41 | Same answer |
| Clef Flash | `B` — 1 | `B` — 1 | Same answer |
| Strands Decider | `C` — 41 | `A` — 0 | Different answer |
| GLiNER2.5 Decide | `A` — 0 | `A` — 0 | Same answer |
| Laya | `A` — 0 | `A` — 0 | Same answer |
| CalDec v1 | `A` — 0 | `A` — 0 | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `bbh/afeb6667e2440f103e40/examples/irrelevant/clean-arithmetic_opinions_examples_0004`

**Input fingerprint:** `57c0dcc8e8ac1f9929d6b52e82d400085b0fcd4c6e73b02612e9a8e45d4c2f6e`

| Change | Recorded version |
| --- | --- |
| Unrelated examples | Add examples unrelated to the question |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/numerical-cognition/bbh-afeb6667e2440f103e40.md).
