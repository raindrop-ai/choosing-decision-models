# Option order · Reverse the answer choices variant

[Original question](../../../questions/numerical-cognition/bbh-2af04cddb08f4d9edc57.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** answer choices or their order.

[How the edits were constructed](../../../docs/variant-methods.md)

## Question

> ((-1 - -9 \* 8 - -9) + (-9 - 2 \* -6 + -6)) =

## Answer choices

- **D.** -3
- **C.** 77
- **B.** -12
- **A.** -77

**Reference answer:** `C`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "",
  "question": "((-1 - -9 * 8 - -9) + (-9 - 2 * -6 + -6)) =",
  "choices": {
    "D": "-3",
    "C": "77",
    "B": "-12",
    "A": "-77"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `C` — 77 | `C` — 77 | Same answer |
| Decider v1.1 | `C` — 77 | `C` — 77 | Same answer |
| Jev | `C` — 77 | `C` — 77 | Same answer |
| Microsoft Decision-1 | `C` — 77 | `C` — 77 | Same answer |
| Clef | `B` — -12 | `B` — -12 | Same answer |
| Luna Decisions | `C` — 77 | `C` — 77 | Same answer |
| Clef Flash | `B` — -12 | `B` — -12 | Same answer |
| Strands Decider | `A` — -77 | `A` — -77 | Same answer |
| GLiNER2.5 Decide | `A` — -77 | `D` — -3 | Different answer |
| Laya | `A` — -77 | `A` — -77 | Same answer |
| CalDec v1 | `A` — -77 | `A` — -77 | Same answer |

Clef and Clef Flash sort answer choices in their published input-processing code. Their choice-order results describe that preprocessing.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `bbh/2af04cddb08f4d9edc57/option_order/reverse`

**Input fingerprint:** `bfc9278ca3c288b47563a0f83f040d536f5207df95afad298c440790b6e52553`

| Change | Recorded version |
| --- | --- |
| Option order | Reverse the answer choices |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/numerical-cognition/bbh-2af04cddb08f4d9edc57.md).
