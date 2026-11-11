# Unrelated examples · Add examples unrelated to the question variant

[Original question](../../../questions/spatial-cognition/babi-3c62d9757163c5b42d7d.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> The bathroom is east of the kitchen.
> The garden is north of the bedroom.
> The hallway is west of the kitchen.
> The kitchen is south of the bedroom.
> The bathroom is north of the office.
>
> Uppercase: comet → COMET.

## Question

> How do you go from the bedroom to the bathroom?

## Answer choices

- **A.** s,e
- **B.** e,n
- **C.** w,w
- **D.** e,s

**Reference answer:** `A`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "The bathroom is east of the kitchen.\nThe garden is north of the bedroom.\nThe hallway is west of the kitchen.\nThe kitchen is south of the bedroom.\nThe bathroom is north of the office.\n\nUppercase: comet → COMET.",
  "question": "How do you go from the bedroom to the bathroom?",
  "choices": {
    "A": "s,e",
    "B": "e,n",
    "C": "w,w",
    "D": "e,s"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `A` — s,e | `A` — s,e | Same answer |
| Decider v1.1 | `A` — s,e | `A` — s,e | Same answer |
| Jev | `D` — e,s | `A` — s,e | Different answer |
| Microsoft Decision-1 | `A` — s,e | `A` — s,e | Same answer |
| Clef | `A` — s,e | `A` — s,e | Same answer |
| Luna Decisions | `A` — s,e | `D` — e,s | Different answer |
| Clef Flash | `A` — s,e | `A` — s,e | Same answer |
| Strands Decider | `D` — e,s | `D` — e,s | Same answer |
| GLiNER2.5 Decide | `A` — s,e | `A` — s,e | Same answer |
| Laya | `D` — e,s | `D` — e,s | Same answer |
| CalDec v1 | `A` — s,e | `A` — s,e | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `babi/3c62d9757163c5b42d7d/examples/irrelevant/clean-source_first_babi_route_worlds_full_0090`

**Input fingerprint:** `80c32140e0c45bac15a433c95ee3ffdd2aece03740997c292d87be6dbb782794`

| Change | Recorded version |
| --- | --- |
| Unrelated examples | Add examples unrelated to the question |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/spatial-cognition/babi-3c62d9757163c5b42d7d.md).
