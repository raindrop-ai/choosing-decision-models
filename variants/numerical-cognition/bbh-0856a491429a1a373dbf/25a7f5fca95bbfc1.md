# Paraphrasing · Change individual words and phrases variant

[Original question](../../../questions/numerical-cognition/bbh-0856a491429a1a373dbf.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** question instructions.

[How the edits were constructed](../../../docs/variant-methods.md)

## Question

> What does ((6 - 5 + 5 + -9) - (9 + 8 \* -6 \* -1)) equal?

## Answer choices

- **A.** 0
- **B.** -60
- **C.** 60
- **D.** -13

**Reference answer:** `B`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "",
  "question": "What does ((6 - 5 + 5 + -9) - (9 + 8 * -6 * -1)) equal?",
  "choices": {
    "A": "0",
    "B": "-60",
    "C": "60",
    "D": "-13"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `B` — -60 | `B` — -60 | Same answer |
| Decider v1.1 | `B` — -60 | `B` — -60 | Same answer |
| Jev | `B` — -60 | `B` — -60 | Same answer |
| Microsoft Decision-1 | `D` — -13 | `D` — -13 | Same answer |
| Clef | `B` — -60 | `B` — -60 | Same answer |
| Luna Decisions | `B` — -60 | `D` — -13 | Different answer |
| Clef Flash | `D` — -13 | `D` — -13 | Same answer |
| Strands Decider | `D` — -13 | `D` — -13 | Same answer |
| GLiNER2.5 Decide | `B` — -60 | `B` — -60 | Same answer |
| Laya | `A` — 0 | `A` — 0 | Same answer |
| CalDec v1 | `B` — -60 | `B` — -60 | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `bbh/0856a491429a1a373dbf/paraphrasing/surface/clean-literal_symbolic_query_repairs_full_0040`

**Input fingerprint:** `c687f20aebf111b0ddee9a9c689c02674f62c15fc9b551c327c2448b44d73f26`

| Change | Recorded version |
| --- | --- |
| Paraphrasing | Change individual words and phrases |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/numerical-cognition/bbh-0856a491429a1a373dbf.md).
