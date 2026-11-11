# Extra events · Add 6 unrelated events variant

[Original question](../../../questions/state-tracking-and-updating/bbh-7e4b9ee7df2a57a444be.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Nolan is the editor of a poetry catalog. Its entries are Virel, Zorven, Kesil, Nereth, Pavrel, and Sovrin.
> Nolan classifies Virel as a dialogue. Nolan classifies Zorven as a monologue. Nolan classifies Kesil as an elegy. Nolan classifies Nereth as a satire. Nolan classifies Pavrel as a fable. Nolan classifies Sovrin as a ballad.

## Question

> Alice, Bob, Claire, Dave, and Eve are friends and avid readers who occasionally trade books. At the start of the semester, they each buy one new book: Alice gets The Great Gatsby, Bob gets Frankenstein, Claire gets Moby Dick, Dave gets The Fellowship of the Ring, and Eve gets Catch-22.
> As the semester proceeds, they start trading around the new books. First, Alice and Bob swap books. Then, Dave and Eve swap books. Then, Eve and Alice swap books. Then, Dave and Eve swap books. Finally, Claire and Dave swap books. At the end of the semester, Dave has

## Answer choices

- **A.** The Great Gatsby
- **B.** Frankenstein
- **C.** Moby Dick
- **D.** The Fellowship of the Ring
- **E.** Catch-22

**Reference answer:** `C`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Nolan is the editor of a poetry catalog. Its entries are Virel, Zorven, Kesil, Nereth, Pavrel, and Sovrin.\nNolan classifies Virel as a dialogue. Nolan classifies Zorven as a monologue. Nolan classifies Kesil as an elegy. Nolan classifies Nereth as a satire. Nolan classifies Pavrel as a fable. Nolan classifies Sovrin as a ballad.",
  "question": "Alice, Bob, Claire, Dave, and Eve are friends and avid readers who occasionally trade books. At the start of the semester, they each buy one new book: Alice gets The Great Gatsby, Bob gets Frankenstein, Claire gets Moby Dick, Dave gets The Fellowship of the Ring, and Eve gets Catch-22.\nAs the semester proceeds, they start trading around the new books. First, Alice and Bob swap books. Then, Dave and Eve swap books. Then, Eve and Alice swap books. Then, Dave and Eve swap books. Finally, Claire and Dave swap books. At the end of the semester, Dave has",
  "choices": {
    "A": "The Great Gatsby",
    "B": "Frankenstein",
    "C": "Moby Dick",
    "D": "The Fellowship of the Ring",
    "E": "Catch-22"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `C` — Moby Dick | `C` — Moby Dick | Same answer |
| Decider v1.1 | `B` — Frankenstein | `C` — Moby Dick | Different answer |
| Jev | `C` — Moby Dick | `C` — Moby Dick | Same answer |
| Microsoft Decision-1 | `C` — Moby Dick | `C` — Moby Dick | Same answer |
| Clef | `C` — Moby Dick | `E` — Catch-22 | Different answer |
| Luna Decisions | `B` — Frankenstein | `B` — Frankenstein | Same answer |
| Clef Flash | `C` — Moby Dick | `C` — Moby Dick | Same answer |
| Strands Decider | `E` — Catch-22 | `E` — Catch-22 | Same answer |
| GLiNER2.5 Decide | `A` — The Great Gatsby | `A` — The Great Gatsby | Same answer |
| Laya | `D` — The Fellowship of the Ring | `E` — Catch-22 | Different answer |
| CalDec v1 | `A` — The Great Gatsby | `C` — Moby Dick | Different answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `bbh/7e4b9ee7df2a57a444be/event_count/6/clean-source_first_tracking_short_contexts_full_0121`

**Input fingerprint:** `598f1c5a0d3b2aad77d8287c14f6a34e513d934e7b36c33c3b67e2a8c49893ea`

| Change | Recorded version |
| --- | --- |
| Extra events | Add 6 unrelated events |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/state-tracking-and-updating/bbh-7e4b9ee7df2a57a444be.md).
