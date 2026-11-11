# Evidence order · Present the evidence in reverse order variant

[Original question](../../../questions/spatial-cognition/babi-7ba1c069006691a0f1df.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> The hallway is north of the garden.
> The office is south of the garden.
> The kitchen is west of the office.
> The bedroom is east of the office.
> The bathroom is west of the garden.

## Question

> How do you go from the garden to the bedroom?

## Answer choices

- **A.** s,s
- **B.** s,e
- **C.** w,n
- **D.** w,w

**Reference answer:** `B`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "The hallway is north of the garden.\nThe office is south of the garden.\nThe kitchen is west of the office.\nThe bedroom is east of the office.\nThe bathroom is west of the garden.",
  "question": "How do you go from the garden to the bedroom?",
  "choices": {
    "A": "s,s",
    "B": "s,e",
    "C": "w,n",
    "D": "w,w"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `B` — s,e | `B` — s,e | Same answer |
| Decider v1.1 | `B` — s,e | `B` — s,e | Same answer |
| Jev | `B` — s,e | `B` — s,e | Same answer |
| Microsoft Decision-1 | `B` — s,e | `B` — s,e | Same answer |
| Clef | `B` — s,e | `B` — s,e | Same answer |
| Luna Decisions | `B` — s,e | `B` — s,e | Same answer |
| Clef Flash | `B` — s,e | `B` — s,e | Same answer |
| Strands Decider | `B` — s,e | `B` — s,e | Same answer |
| GLiNER2.5 Decide | `A` — s,s | `A` — s,s | Same answer |
| Laya | `B` — s,e | `A` — s,s | Different answer |
| CalDec v1 | `A` — s,s | `A` — s,s | Same answer |

**Ordering comparison:** literal requested source unit permutation. Only the exact matched comparison sets contribute to the reported ordering contrasts.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `babi/7ba1c069006691a0f1df/presentation_order/reverse_presentation/clean-source_first_babi_route_worlds_full_0090`

**Input fingerprint:** `bd990618300da8b53c958694fa903604505ba210bec9181423d939068a040de5`

| Change | Recorded version |
| --- | --- |
| Evidence order | Present the evidence in reverse order |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/spatial-cognition/babi-7ba1c069006691a0f1df.md).
