# Option order · Move the first answer choice to the end variant

[Original question](../../../questions/numerical-cognition/bbh-a2cf02e5372b6d6b00a3.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** answer choices or their order.

[How the edits were constructed](../../../docs/variant-methods.md)

## Question

> ((-5 + 1 - 2 - -3) \* (-9 \* 3 + 9 + -1)) =

## Answer choices

- **B.** -19
- **C.** 57
- **D.** 175
- **A.** -57

**Reference answer:** `C`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "",
  "question": "((-5 + 1 - 2 - -3) * (-9 * 3 + 9 + -1)) =",
  "choices": {
    "B": "-19",
    "C": "57",
    "D": "175",
    "A": "-57"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `C` — 57 | `C` — 57 | Same answer |
| Decider v1.1 | `C` — 57 | `A` — -57 | Different answer |
| Jev | `C` — 57 | `C` — 57 | Same answer |
| Microsoft Decision-1 | `A` — -57 | `A` — -57 | Same answer |
| Clef | `C` — 57 | `C` — 57 | Same answer |
| Luna Decisions | `A` — -57 | `B` — -19 | Different answer |
| Clef Flash | `A` — -57 | `A` — -57 | Same answer |
| Strands Decider | `C` — 57 | `A` — -57 | Different answer |
| GLiNER2.5 Decide | `A` — -57 | `B` — -19 | Different answer |
| Laya | `A` — -57 | `B` — -19 | Different answer |
| CalDec v1 | `A` — -57 | `B` — -19 | Different answer |

Clef and Clef Flash sort answer choices in their published input-processing code. Their choice-order results describe that preprocessing.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `bbh/a2cf02e5372b6d6b00a3/option_order/rotate_1`

**Input fingerprint:** `d67776f0ada331d29ae8171356d33ea55a36e51e4cec3e5fae442a2e0482961c`

| Change | Recorded version |
| --- | --- |
| Option order | Move the first answer choice to the end |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/numerical-cognition/bbh-a2cf02e5372b6d6b00a3.md).
