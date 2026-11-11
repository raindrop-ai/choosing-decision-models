# Evidence order · Present the evidence in reverse order variant

[Original question](../../../questions/spatial-cognition/spartqa-48eef2d2dbdde48bc27d.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> There are three blocks, A, B and C. Block C is to the left of B and block B is below A. And block C has two medium yellow squares. Medium yellow square number one is below medium yellow square number two.. One medium blue square is also touching the bottom edge of this block. Below medium yellow square number one and medium yellow square number two is the medium blue square. Block B contains a medium yellow square and a medium blue square. The medium yellow square is touching the bottom edge of this block. It is below the medium blue square. Block A contains a medium blue square. The medium blue square is below a medium black square.

## Question

> What is the relation between the medium object that is below medium yellow object number one and the yellow square which is above a yellow square?

## Answer choices

- **0.** left
- **1.** right
- **2.** above
- **3.** below
- **4.** near to
- **5.** far from
- **6.** touching
- **7.** DK

**Reference answer:** `3`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "There are three blocks, A, B and C. Block C is to the left of B and block B is below A. And block C has two medium yellow squares. Medium yellow square number one is below medium yellow square number two.. One medium blue square is also touching the bottom edge of this block. Below medium yellow square number one and medium yellow square number two is the medium blue square. Block B contains a medium yellow square and a medium blue square. The medium yellow square is touching the bottom edge of this block. It is below the medium blue square. Block A contains a medium blue square. The medium blue square is below a medium black square.",
  "question": "What is the relation between the medium object that is below medium yellow object number one and the yellow square which is above a yellow square?",
  "choices": {
    "0": "left",
    "1": "right",
    "2": "above",
    "3": "below",
    "4": "near to",
    "5": "far from",
    "6": "touching",
    "7": "DK"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `3` — below | `3` — below | Same answer |
| Decider v1.1 | `3` — below | `3` — below | Same answer |
| Jev | `3` — below | `3` — below | Same answer |
| Microsoft Decision-1 | `3` — below | `3` — below | Same answer |
| Clef | `3` — below | `3` — below | Same answer |
| Luna Decisions | `0` — left | `6` — touching | Different answer |
| Clef Flash | `3` — below | `3` — below | Same answer |
| Strands Decider | `3` — below | `3` — below | Same answer |
| GLiNER2.5 Decide | `3` — below | `3` — below | Same answer |
| Laya | `3` — below | `3` — below | Same answer |
| CalDec v1 | `3` — below | `3` — below | Same answer |

**Ordering comparison:** literal requested source unit permutation. Only the exact matched comparison sets contribute to the reported ordering contrasts.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `spartqa/48eef2d2dbdde48bc27d/presentation_order/reverse_presentation/clean-source_first_spartqa_block_bundle_orders_full_0147`

**Input fingerprint:** `72c5865432aee85eacae37d1706e9166520282848f162e0c1201da9dcde2053e`

| Change | Recorded version |
| --- | --- |
| Evidence order | Present the evidence in reverse order |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/spatial-cognition/spartqa-48eef2d2dbdde48bc27d.md).
