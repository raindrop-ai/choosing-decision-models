# Extra events · Add 2 unrelated events variant

[Original question](../../../questions/spatial-cognition/babi-56cc78bd32b8ba76af0d.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Nolan is the editor of a poetry catalog. Its entries are Virel, Zorven, Kesil, Nereth, Pavrel, and Sovrin.
> Nolan classifies Virel as a dialogue. Nolan classifies Zorven as a monologue.
>
> The garden is north of the kitchen.
> The bathroom is north of the hallway.
> The garden is east of the bedroom.
> The kitchen is west of the office.
> The kitchen is east of the hallway.

## Question

> How do you go from the hallway to the garden?

## Answer choices

- **A.** n,s
- **B.** w,s
- **C.** e,s
- **D.** e,n

**Reference answer:** `D`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Nolan is the editor of a poetry catalog. Its entries are Virel, Zorven, Kesil, Nereth, Pavrel, and Sovrin.\nNolan classifies Virel as a dialogue. Nolan classifies Zorven as a monologue.\n\nThe garden is north of the kitchen.\nThe bathroom is north of the hallway.\nThe garden is east of the bedroom.\nThe kitchen is west of the office.\nThe kitchen is east of the hallway.",
  "question": "How do you go from the hallway to the garden?",
  "choices": {
    "A": "n,s",
    "B": "w,s",
    "C": "e,s",
    "D": "e,n"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `D` — e,n | `D` — e,n | Same answer |
| Decider v1.1 | `D` — e,n | `D` — e,n | Same answer |
| Jev | `D` — e,n | `D` — e,n | Same answer |
| Microsoft Decision-1 | `D` — e,n | `D` — e,n | Same answer |
| Clef | `D` — e,n | `D` — e,n | Same answer |
| Luna Decisions | `D` — e,n | `D` — e,n | Same answer |
| Clef Flash | `D` — e,n | `D` — e,n | Same answer |
| Strands Decider | `D` — e,n | `D` — e,n | Same answer |
| GLiNER2.5 Decide | `A` — n,s | `A` — n,s | Same answer |
| Laya | `B` — w,s | `A` — n,s | Different answer |
| CalDec v1 | `A` — n,s | `A` — n,s | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `babi/56cc78bd32b8ba76af0d/event_count/2/clean-source_first_babi_route_worlds_full_0090`

**Input fingerprint:** `1747dbd19d541c12c6548cc7bce08d09e697f64150349463049cab6383457b79`

| Change | Recorded version |
| --- | --- |
| Extra events | Add 2 unrelated events |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/spatial-cognition/babi-56cc78bd32b8ba76af0d.md).
