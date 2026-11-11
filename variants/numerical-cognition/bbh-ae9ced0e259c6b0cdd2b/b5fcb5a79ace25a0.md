# Option order · Move the first answer choice to the end variant

[Original question](../../../questions/numerical-cognition/bbh-ae9ced0e259c6b0cdd2b.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** answer choices or their order.

[How the edits were constructed](../../../docs/variant-methods.md)

## Question

> ((-8 - -6 \* 7 \* 0) \* (0 + -5 \* -8 - 0)) =

## Answer choices

- **B.** -320
- **C.** 40
- **D.** 1
- **A.** -1

**Reference answer:** `B`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "",
  "question": "((-8 - -6 * 7 * 0) * (0 + -5 * -8 - 0)) =",
  "choices": {
    "B": "-320",
    "C": "40",
    "D": "1",
    "A": "-1"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `B` — -320 | `B` — -320 | Same answer |
| Decider v1.1 | `B` — -320 | `B` — -320 | Same answer |
| Jev | `B` — -320 | `B` — -320 | Same answer |
| Microsoft Decision-1 | `B` — -320 | `B` — -320 | Same answer |
| Clef | `B` — -320 | `B` — -320 | Same answer |
| Luna Decisions | `B` — -320 | `B` — -320 | Same answer |
| Clef Flash | `C` — 40 | `C` — 40 | Same answer |
| Strands Decider | `B` — -320 | `B` — -320 | Same answer |
| GLiNER2.5 Decide | `A` — -1 | `B` — -320 | Different answer |
| Laya | `A` — -1 | `A` — -1 | Same answer |
| CalDec v1 | `A` — -1 | `A` — -1 | Same answer |

Clef and Clef Flash sort answer choices in their published input-processing code. Their choice-order results describe that preprocessing.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `bbh/ae9ced0e259c6b0cdd2b/option_order/rotate_1`

**Input fingerprint:** `08dee012b815168bdd880024a797717cc5699f6499cd5116385909cea720da78`

| Change | Recorded version |
| --- | --- |
| Option order | Move the first answer choice to the end |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/numerical-cognition/bbh-ae9ced0e259c6b0cdd2b.md).
