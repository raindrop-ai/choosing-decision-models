# Unrelated examples · Add examples unrelated to the question variant

[Original question](../../../questions/numerical-cognition/bbh-7b7f2169639b9d218188.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Capitalization: blue birds fly. → Blue birds fly.

## Question

> ((-2 \* -8 \* 9 + -5) + (7 - -1 - -4 - 1)) =

## Answer choices

- **A.** 11
- **B.** 16
- **C.** 136
- **D.** 150

**Reference answer:** `D`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Capitalization: blue birds fly. → Blue birds fly.",
  "question": "((-2 * -8 * 9 + -5) + (7 - -1 - -4 - 1)) =",
  "choices": {
    "A": "11",
    "B": "16",
    "C": "136",
    "D": "150"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `C` — 136 | `D` — 150 | Different answer |
| Decider v1.1 | `C` — 136 | `C` — 136 | Same answer |
| Jev | `C` — 136 | `C` — 136 | Same answer |
| Microsoft Decision-1 | `D` — 150 | `D` — 150 | Same answer |
| Clef | `C` — 136 | `C` — 136 | Same answer |
| Luna Decisions | `D` — 150 | `D` — 150 | Same answer |
| Clef Flash | `B` — 16 | `B` — 16 | Same answer |
| Strands Decider | `D` — 150 | `A` — 11 | Different answer |
| GLiNER2.5 Decide | `A` — 11 | `A` — 11 | Same answer |
| Laya | `A` — 11 | `C` — 136 | Different answer |
| CalDec v1 | `A` — 11 | `A` — 11 | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `bbh/7b7f2169639b9d218188/examples/irrelevant/clean-arithmetic_opinions_examples_0004`

**Input fingerprint:** `d49c0461408a0dec9ab5e2d9327cdebeb29efd087406bdf54167440e8098b85e`

| Change | Recorded version |
| --- | --- |
| Unrelated examples | Add examples unrelated to the question |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/numerical-cognition/bbh-7b7f2169639b9d218188.md).
