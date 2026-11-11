# Paraphrasing · Change individual words and phrases variant

[Original question](../../../questions/spatial-cognition/babi-0a48d3b135c90205a4df.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** question instructions.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> The office is west of the bathroom.
> The bedroom is south of the bathroom.
> The kitchen is east of the garden.
> The bathroom is west of the garden.
> The hallway is north of the bathroom.

## Question

> Which route takes you from the bathroom to the kitchen?

## Answer choices

- **A.** n,n
- **B.** e,e
- **C.** e,w
- **D.** s,n

**Reference answer:** `B`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "The office is west of the bathroom.\nThe bedroom is south of the bathroom.\nThe kitchen is east of the garden.\nThe bathroom is west of the garden.\nThe hallway is north of the bathroom.",
  "question": "Which route takes you from the bathroom to the kitchen?",
  "choices": {
    "A": "n,n",
    "B": "e,e",
    "C": "e,w",
    "D": "s,n"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `B` — e,e | `B` — e,e | Same answer |
| Decider v1.1 | `B` — e,e | `B` — e,e | Same answer |
| Jev | `B` — e,e | `B` — e,e | Same answer |
| Microsoft Decision-1 | `B` — e,e | `B` — e,e | Same answer |
| Clef | `B` — e,e | `B` — e,e | Same answer |
| Luna Decisions | `B` — e,e | `B` — e,e | Same answer |
| Clef Flash | `B` — e,e | `B` — e,e | Same answer |
| Strands Decider | `B` — e,e | `B` — e,e | Same answer |
| GLiNER2.5 Decide | `A` — n,n | `A` — n,n | Same answer |
| Laya | `A` — n,n | `B` — e,e | Different answer |
| CalDec v1 | `B` — e,e | `B` — e,e | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `babi/0a48d3b135c90205a4df/paraphrasing/surface`

**Input fingerprint:** `5a8c8e138fa22245331ad07a4a9e7cc2cf70ae14db7b0bc1020d6d8125ddbafc`

| Change | Recorded version |
| --- | --- |
| Paraphrasing | Change individual words and phrases |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/spatial-cognition/babi-0a48d3b135c90205a4df.md).
