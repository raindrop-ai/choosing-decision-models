# Option order · Reverse the answer choices variant

[Original question](../../../questions/spatial-cognition/babi-ce484dba76a710dca15b.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** answer choices or their order.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> The garden is south of the kitchen.
> The bathroom is west of the office.
> The bathroom is east of the bedroom.
> The hallway is south of the bathroom.
> The garden is north of the office.

## Question

> How do you go from the bathroom to the garden?

## Answer choices

- **D.** w,s
- **C.** e,e
- **B.** s,s
- **A.** e,n

**Reference answer:** `A`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "The garden is south of the kitchen.\nThe bathroom is west of the office.\nThe bathroom is east of the bedroom.\nThe hallway is south of the bathroom.\nThe garden is north of the office.",
  "question": "How do you go from the bathroom to the garden?",
  "choices": {
    "D": "w,s",
    "C": "e,e",
    "B": "s,s",
    "A": "e,n"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `A` — e,n | `A` — e,n | Same answer |
| Decider v1.1 | `A` — e,n | `A` — e,n | Same answer |
| Jev | `C` — e,e | `A` — e,n | Different answer |
| Microsoft Decision-1 | `A` — e,n | `A` — e,n | Same answer |
| Clef | `B` — s,s | `B` — s,s | Same answer |
| Luna Decisions | `A` — e,n | `A` — e,n | Same answer |
| Clef Flash | `B` — s,s | `B` — s,s | Same answer |
| Strands Decider | `A` — e,n | `A` — e,n | Same answer |
| GLiNER2.5 Decide | `A` — e,n | `A` — e,n | Same answer |
| Laya | `C` — e,e | `D` — w,s | Different answer |
| CalDec v1 | `A` — e,n | `D` — w,s | Different answer |

Clef and Clef Flash sort answer choices in their published input-processing code. Their choice-order results describe that preprocessing.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `babi/ce484dba76a710dca15b/option_order/reverse`

**Input fingerprint:** `6d51eb56a25fa7df375d298c13f81df84728a618488d062298f2382de6e12a3f`

| Change | Recorded version |
| --- | --- |
| Option order | Reverse the answer choices |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/spatial-cognition/babi-ce484dba76a710dca15b.md).
