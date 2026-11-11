# Evidence order · Present the evidence in a shuffled order variant

[Original question](../../../questions/spatial-cognition/babi-74ec723cad642281046b.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> The kitchen is west of the hallway.
> The office is east of the bathroom.
> The bedroom is south of the bathroom.
> The bathroom is south of the hallway.
> The hallway is west of the garden.

## Question

> How do you go from the office to the hallway?

## Answer choices

- **A.** e,s
- **B.** w,n
- **C.** s,n
- **D.** w,w

**Reference answer:** `B`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "The kitchen is west of the hallway.\nThe office is east of the bathroom.\nThe bedroom is south of the bathroom.\nThe bathroom is south of the hallway.\nThe hallway is west of the garden.",
  "question": "How do you go from the office to the hallway?",
  "choices": {
    "A": "e,s",
    "B": "w,n",
    "C": "s,n",
    "D": "w,w"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `B` — w,n | `B` — w,n | Same answer |
| Decider v1.1 | `B` — w,n | `B` — w,n | Same answer |
| Jev | `B` — w,n | `B` — w,n | Same answer |
| Microsoft Decision-1 | `B` — w,n | `B` — w,n | Same answer |
| Clef | `D` — w,w | `B` — w,n | Different answer |
| Luna Decisions | `B` — w,n | `B` — w,n | Same answer |
| Clef Flash | `B` — w,n | `B` — w,n | Same answer |
| Strands Decider | `B` — w,n | `B` — w,n | Same answer |
| GLiNER2.5 Decide | `A` — e,s | `A` — e,s | Same answer |
| Laya | `A` — e,s | `A` — e,s | Same answer |
| CalDec v1 | `A` — e,s | `A` — e,s | Same answer |

**Ordering comparison:** literal requested source unit permutation. Only the exact matched comparison sets contribute to the reported ordering contrasts.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `babi/74ec723cad642281046b/presentation_order/shuffled_presentation/clean-source_first_babi_route_worlds_full_0090`

**Input fingerprint:** `27660eb4ca80c687356c929e4ac09ec08baa97b299558eb7c69fef3360b1f31a`

| Change | Recorded version |
| --- | --- |
| Evidence order | Present the evidence in a shuffled order |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/spatial-cognition/babi-74ec723cad642281046b.md).
