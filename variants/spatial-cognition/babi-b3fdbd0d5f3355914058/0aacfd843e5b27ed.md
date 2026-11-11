# Extra events · Add 2 unrelated events variant

[Original question](../../../questions/spatial-cognition/babi-b3fdbd0d5f3355914058.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Nolan is the editor of a poetry catalog. Its entries are Virel, Zorven, Kesil, Nereth, Pavrel, and Sovrin.
> Nolan classifies Virel as a dialogue. Nolan classifies Zorven as a monologue.
>
> The bedroom is north of the hallway.
> The kitchen is east of the hallway.
> The hallway is north of the office.
> The garden is north of the bedroom.
> The bathroom is west of the hallway.

## Question

> How do you go from the bedroom to the bathroom?

## Answer choices

- **A.** n,n
- **B.** n,w
- **C.** s,w
- **D.** s,n

**Reference answer:** `C`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Nolan is the editor of a poetry catalog. Its entries are Virel, Zorven, Kesil, Nereth, Pavrel, and Sovrin.\nNolan classifies Virel as a dialogue. Nolan classifies Zorven as a monologue.\n\nThe bedroom is north of the hallway.\nThe kitchen is east of the hallway.\nThe hallway is north of the office.\nThe garden is north of the bedroom.\nThe bathroom is west of the hallway.",
  "question": "How do you go from the bedroom to the bathroom?",
  "choices": {
    "A": "n,n",
    "B": "n,w",
    "C": "s,w",
    "D": "s,n"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `C` — s,w | `C` — s,w | Same answer |
| Decider v1.1 | `C` — s,w | `C` — s,w | Same answer |
| Jev | `C` — s,w | `C` — s,w | Same answer |
| Microsoft Decision-1 | `C` — s,w | `C` — s,w | Same answer |
| Clef | `C` — s,w | `C` — s,w | Same answer |
| Luna Decisions | `C` — s,w | `C` — s,w | Same answer |
| Clef Flash | `C` — s,w | `C` — s,w | Same answer |
| Strands Decider | `C` — s,w | `B` — n,w | Different answer |
| GLiNER2.5 Decide | `A` — n,n | `C` — s,w | Different answer |
| Laya | `A` — n,n | `A` — n,n | Same answer |
| CalDec v1 | `A` — n,n | `A` — n,n | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `babi/b3fdbd0d5f3355914058/event_count/2/clean-source_first_babi_route_worlds_full_0090`

**Input fingerprint:** `a6af89332bcb42b9d567c5dc9b6c82a9fe2b55f576968e4aa60fc8400caa8254`

| Change | Recorded version |
| --- | --- |
| Extra events | Add 2 unrelated events |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/spatial-cognition/babi-b3fdbd0d5f3355914058.md).
