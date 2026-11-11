# Misleading details · Add an unverified claim that conflicts with the evidence variant

[Original question](../../../questions/spatial-cognition/babi-3c45d4cc30fb3647edfe.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> The bathroom is north of the kitchen.
> The kitchen is west of the garden.
> The hallway is north of the office.
> The office is north of the bathroom.
> The bedroom is west of the kitchen.
>
> A reader thinks: «The proposed route from the office to the kitchen is north, then west.»

## Question

> How do you go from the office to the kitchen?

## Answer choices

- **A.** n,w
- **B.** s,s
- **C.** s,n
- **D.** s,w

**Reference answer:** `B`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "The bathroom is north of the kitchen.\nThe kitchen is west of the garden.\nThe hallway is north of the office.\nThe office is north of the bathroom.\nThe bedroom is west of the kitchen.\n\nA reader thinks: «The proposed route from the office to the kitchen is north, then west.»",
  "question": "How do you go from the office to the kitchen?",
  "choices": {
    "A": "n,w",
    "B": "s,s",
    "C": "s,n",
    "D": "s,w"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `B` — s,s | `B` — s,s | Same answer |
| Decider v1.1 | `B` — s,s | `B` — s,s | Same answer |
| Jev | `D` — s,w | `D` — s,w | Same answer |
| Microsoft Decision-1 | `B` — s,s | `B` — s,s | Same answer |
| Clef | `B` — s,s | `D` — s,w | Different answer |
| Luna Decisions | `D` — s,w | `D` — s,w | Same answer |
| Clef Flash | `B` — s,s | `D` — s,w | Different answer |
| Strands Decider | `D` — s,w | `D` — s,w | Same answer |
| GLiNER2.5 Decide | `A` — n,w | `A` — n,w | Same answer |
| Laya | `A` — n,w | `D` — s,w | Different answer |
| CalDec v1 | `A` — n,w | `D` — s,w | Different answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `babi/3c45d4cc30fb3647edfe/misleading_summary/misleading/clean-source_first_babi_route_worlds_full_0090`

**Input fingerprint:** `f51ccb0a31cf5b54e1a3a6f4b01683cd2cc4c5bcf280b7d4e5ae63abbd7271c8`

| Change | Recorded version |
| --- | --- |
| Misleading details | Add an unverified claim that conflicts with the evidence |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/spatial-cognition/babi-3c45d4cc30fb3647edfe.md).
