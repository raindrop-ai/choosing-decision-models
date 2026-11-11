# Extra events · Add 6 unrelated events variant

[Original question](../../../questions/spatial-cognition/babi-bac48ca11edbaf4f5a6f.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Nolan is the editor of a poetry catalog. Its entries are Virel, Zorven, Kesil, Nereth, Pavrel, and Sovrin.
> Nolan classifies Virel as a dialogue. Nolan classifies Zorven as a monologue. Nolan classifies Kesil as an elegy. Nolan classifies Nereth as a satire. Nolan classifies Pavrel as a fable. Nolan classifies Sovrin as a ballad.
>
> The hallway is west of the office.
> The bathroom is east of the kitchen.
> The office is north of the garden.
> The kitchen is south of the bedroom.
> The bedroom is east of the office.

## Question

> How do you go from the kitchen to the office?

## Answer choices

- **A.** w,n
- **B.** w,s
- **C.** n,w
- **D.** e,w

**Reference answer:** `C`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Nolan is the editor of a poetry catalog. Its entries are Virel, Zorven, Kesil, Nereth, Pavrel, and Sovrin.\nNolan classifies Virel as a dialogue. Nolan classifies Zorven as a monologue. Nolan classifies Kesil as an elegy. Nolan classifies Nereth as a satire. Nolan classifies Pavrel as a fable. Nolan classifies Sovrin as a ballad.\n\nThe hallway is west of the office.\nThe bathroom is east of the kitchen.\nThe office is north of the garden.\nThe kitchen is south of the bedroom.\nThe bedroom is east of the office.",
  "question": "How do you go from the kitchen to the office?",
  "choices": {
    "A": "w,n",
    "B": "w,s",
    "C": "n,w",
    "D": "e,w"
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
| Clef | `C` — n,w | `D` — e,w | Different answer |
| Luna Decisions | `C` — n,w | `C` — n,w | Same answer |
| Clef Flash | `A` — w,n | `A` — w,n | Same answer |
| Strands Decider | `C` — n,w | `C` — n,w | Same answer |
| GLiNER2.5 Decide | `A` — w,n | `A` — w,n | Same answer |
| Laya | `A` — w,n | `A` — w,n | Same answer |
| CalDec v1 | `A` — w,n | `A` — w,n | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `babi/bac48ca11edbaf4f5a6f/event_count/6/clean-source_first_babi_route_worlds_full_0090`

**Input fingerprint:** `34bae18150f46b04a9ae18d36dfab3e1994d88e1847c76ea180af70c42cc7b0f`

| Change | Recorded version |
| --- | --- |
| Extra events | Add 6 unrelated events |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/spatial-cognition/babi-bac48ca11edbaf4f5a6f.md).
