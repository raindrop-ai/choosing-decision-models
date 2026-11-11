# Misleading details · Add an unverified claim that conflicts with the evidence variant

[Original question](../../../questions/spatial-cognition/babi-279d5ca2bc6fc0dd794b.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> The office is south of the kitchen.
> The bedroom is south of the bathroom.
> The hallway is west of the office.
> The garden is north of the bathroom.
> The office is west of the bathroom.
>
> A reader thinks: «The proposed route from the bedroom to the office is south, then west.»

## Question

> How do you go from the bedroom to the office?

## Answer choices

- **A.** n,w
- **B.** s,w
- **C.** w,w
- **D.** w,n

**Reference answer:** `A`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "The office is south of the kitchen.\nThe bedroom is south of the bathroom.\nThe hallway is west of the office.\nThe garden is north of the bathroom.\nThe office is west of the bathroom.\n\nA reader thinks: «The proposed route from the bedroom to the office is south, then west.»",
  "question": "How do you go from the bedroom to the office?",
  "choices": {
    "A": "n,w",
    "B": "s,w",
    "C": "w,w",
    "D": "w,n"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `A` — n,w | `A` — n,w | Same answer |
| Decider v1.1 | `A` — n,w | `A` — n,w | Same answer |
| Jev | `C` — w,w | `D` — w,n | Different answer |
| Microsoft Decision-1 | `A` — n,w | `A` — n,w | Same answer |
| Clef | `A` — n,w | `A` — n,w | Same answer |
| Luna Decisions | `A` — n,w | `B` — s,w | Different answer |
| Clef Flash | `A` — n,w | `A` — n,w | Same answer |
| Strands Decider | `A` — n,w | `B` — s,w | Different answer |
| GLiNER2.5 Decide | `B` — s,w | `B` — s,w | Same answer |
| Laya | `B` — s,w | `B` — s,w | Same answer |
| CalDec v1 | `B` — s,w | `B` — s,w | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `babi/279d5ca2bc6fc0dd794b/misleading_summary/misleading/clean-source_first_babi_route_worlds_full_0090`

**Input fingerprint:** `af067f4536fca9933ae408f46b01378204b266b8b7cbb38809300c043e3b57b0`

| Change | Recorded version |
| --- | --- |
| Misleading details | Add an unverified claim that conflicts with the evidence |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/spatial-cognition/babi-279d5ca2bc6fc0dd794b.md).
