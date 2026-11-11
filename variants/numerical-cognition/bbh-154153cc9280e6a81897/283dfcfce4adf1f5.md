# Option order · Move the first answer choice to the end variant

[Original question](../../../questions/numerical-cognition/bbh-154153cc9280e6a81897.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** answer choices or their order.

[How the edits were constructed](../../../docs/variant-methods.md)

## Question

> ((-2 \* -1 + 1 \* -3) - (7 \* -7 + -5 \* 6)) =

## Answer choices

- **B.** -3
- **C.** -1
- **D.** -6
- **A.** 78

**Reference answer:** `A`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "",
  "question": "((-2 * -1 + 1 * -3) - (7 * -7 + -5 * 6)) =",
  "choices": {
    "B": "-3",
    "C": "-1",
    "D": "-6",
    "A": "78"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `A` — 78 | `A` — 78 | Same answer |
| Decider v1.1 | `A` — 78 | `A` — 78 | Same answer |
| Jev | `A` — 78 | `A` — 78 | Same answer |
| Microsoft Decision-1 | `A` — 78 | `A` — 78 | Same answer |
| Clef | `B` — -3 | `B` — -3 | Same answer |
| Luna Decisions | `A` — 78 | `A` — 78 | Same answer |
| Clef Flash | `B` — -3 | `B` — -3 | Same answer |
| Strands Decider | `A` — 78 | `C` — -1 | Different answer |
| GLiNER2.5 Decide | `A` — 78 | `B` — -3 | Different answer |
| Laya | `B` — -3 | `B` — -3 | Same answer |
| CalDec v1 | `B` — -3 | `B` — -3 | Same answer |

Clef and Clef Flash sort answer choices in their published input-processing code. Their choice-order results describe that preprocessing.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `bbh/154153cc9280e6a81897/option_order/rotate_1`

**Input fingerprint:** `7938f1142da93cef0a061fda989611118cfb946369db6023034ddbf4adb1e94d`

| Change | Recorded version |
| --- | --- |
| Option order | Move the first answer choice to the end |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/numerical-cognition/bbh-154153cc9280e6a81897.md).
