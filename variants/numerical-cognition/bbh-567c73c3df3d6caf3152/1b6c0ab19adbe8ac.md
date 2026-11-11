# Option order · Reverse the answer choices variant

[Original question](../../../questions/numerical-cognition/bbh-567c73c3df3d6caf3152.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** answer choices or their order.

[How the edits were constructed](../../../docs/variant-methods.md)

## Question

> ((-6 + -2 \* 3 \* 0) + (3 + -4 - 7 - -4)) =

## Answer choices

- **D.** -10
- **C.** 10
- **B.** -9
- **A.** -8

**Reference answer:** `D`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "",
  "question": "((-6 + -2 * 3 * 0) + (3 + -4 - 7 - -4)) =",
  "choices": {
    "D": "-10",
    "C": "10",
    "B": "-9",
    "A": "-8"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `D` — -10 | `D` — -10 | Same answer |
| Decider v1.1 | `D` — -10 | `D` — -10 | Same answer |
| Jev | `A` — -8 | `A` — -8 | Same answer |
| Microsoft Decision-1 | `D` — -10 | `D` — -10 | Same answer |
| Clef | `A` — -8 | `A` — -8 | Same answer |
| Luna Decisions | `A` — -8 | `A` — -8 | Same answer |
| Clef Flash | `A` — -8 | `A` — -8 | Same answer |
| Strands Decider | `D` — -10 | `B` — -9 | Different answer |
| GLiNER2.5 Decide | `A` — -8 | `D` — -10 | Different answer |
| Laya | `A` — -8 | `D` — -10 | Different answer |
| CalDec v1 | `A` — -8 | `A` — -8 | Same answer |

Clef and Clef Flash sort answer choices in their published input-processing code. Their choice-order results describe that preprocessing.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `bbh/567c73c3df3d6caf3152/option_order/reverse`

**Input fingerprint:** `ef0303da5672f98c9b5f1664a95dc8f6410ed87d3cf9d4cc7307912498f88a6a`

| Change | Recorded version |
| --- | --- |
| Option order | Reverse the answer choices |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/numerical-cognition/bbh-567c73c3df3d6caf3152.md).
