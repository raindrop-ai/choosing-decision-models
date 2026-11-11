# Option order · Reverse the answer choices variant

[Original question](../../../questions/spatial-cognition/babi-bac48ca11edbaf4f5a6f.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** answer choices or their order.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> The hallway is west of the office.
> The bathroom is east of the kitchen.
> The office is north of the garden.
> The kitchen is south of the bedroom.
> The bedroom is east of the office.

## Question

> How do you go from the kitchen to the office?

## Answer choices

- **D.** e,w
- **C.** n,w
- **B.** w,s
- **A.** w,n

**Reference answer:** `C`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "The hallway is west of the office.\nThe bathroom is east of the kitchen.\nThe office is north of the garden.\nThe kitchen is south of the bedroom.\nThe bedroom is east of the office.",
  "question": "How do you go from the kitchen to the office?",
  "choices": {
    "D": "e,w",
    "C": "n,w",
    "B": "w,s",
    "A": "w,n"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `C` — n,w | `C` — n,w | Same answer |
| Decider v1.1 | `C` — n,w | `C` — n,w | Same answer |
| Jev | `A` — w,n | `C` — n,w | Different answer |
| Microsoft Decision-1 | `C` — n,w | `C` — n,w | Same answer |
| Clef | `C` — n,w | `C` — n,w | Same answer |
| Luna Decisions | `C` — n,w | `C` — n,w | Same answer |
| Clef Flash | `A` — w,n | `A` — w,n | Same answer |
| Strands Decider | `C` — n,w | `A` — w,n | Different answer |
| GLiNER2.5 Decide | `A` — w,n | `A` — w,n | Same answer |
| Laya | `A` — w,n | `A` — w,n | Same answer |
| CalDec v1 | `A` — w,n | `D` — e,w | Different answer |

Clef and Clef Flash sort answer choices in their published input-processing code. Their choice-order results describe that preprocessing.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `babi/bac48ca11edbaf4f5a6f/option_order/reverse`

**Input fingerprint:** `9fcf21ec3f2266262c3fd38bc30695808452f0da14a602402ee4171d0f4759d8`

| Change | Recorded version |
| --- | --- |
| Option order | Reverse the answer choices |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/spatial-cognition/babi-bac48ca11edbaf4f5a6f.md).
