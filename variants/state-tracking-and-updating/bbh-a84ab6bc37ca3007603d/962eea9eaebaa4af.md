# Unrelated examples · No worked example (absence-control recipe) variant

[Original question](../../../questions/state-tracking-and-updating/bbh-a84ab6bc37ca3007603d.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> The notebook cover is linen.

## Question

> Alice, Bob, Claire, Dave, and Eve are playing a game. At the start of the game, they are each holding a ball: Alice has a brown ball, Bob has a black ball, Claire has a white ball, Dave has a yellow ball, and Eve has a purple ball.
> As the game progresses, pairs of players trade balls. First, Claire and Dave swap balls. Then, Alice and Eve swap balls. Then, Dave and Bob swap balls. Then, Alice and Eve swap balls. Finally, Claire and Eve swap balls. At the end of the game, Alice has the

## Answer choices

- **A.** brown ball
- **B.** black ball
- **C.** white ball
- **D.** yellow ball
- **E.** purple ball

**Reference answer:** `A`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "The notebook cover is linen.",
  "question": "Alice, Bob, Claire, Dave, and Eve are playing a game. At the start of the game, they are each holding a ball: Alice has a brown ball, Bob has a black ball, Claire has a white ball, Dave has a yellow ball, and Eve has a purple ball.\nAs the game progresses, pairs of players trade balls. First, Claire and Dave swap balls. Then, Alice and Eve swap balls. Then, Dave and Bob swap balls. Then, Alice and Eve swap balls. Finally, Claire and Eve swap balls. At the end of the game, Alice has the",
  "choices": {
    "A": "brown ball",
    "B": "black ball",
    "C": "white ball",
    "D": "yellow ball",
    "E": "purple ball"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `A` — brown ball | `A` — brown ball | Same answer |
| Decider v1.1 | `A` — brown ball | `A` — brown ball | Same answer |
| Jev | `E` — purple ball | `A` — brown ball | Different answer |
| Microsoft Decision-1 | `A` — brown ball | `A` — brown ball | Same answer |
| Clef | `A` — brown ball | `A` — brown ball | Same answer |
| Luna Decisions | `A` — brown ball | `A` — brown ball | Same answer |
| Clef Flash | `E` — purple ball | `A` — brown ball | Different answer |
| Strands Decider | `E` — purple ball | `E` — purple ball | Same answer |
| GLiNER2.5 Decide | `A` — brown ball | `A` — brown ball | Same answer |
| Laya | `A` — brown ball | `A` — brown ball | Same answer |
| CalDec v1 | `A` — brown ball | `A` — brown ball | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `bbh/a84ab6bc37ca3007603d/examples/absent/clean-source_first_tracking_short_contexts_full_0121`

**Input fingerprint:** `1df155f7429b50885138e0ada51eb24c7b37e6dd00d3f0a9f5b4bfa7221ac194`

| Change | Recorded version |
| --- | --- |
| Unrelated examples | No worked example (absence-control recipe) |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/state-tracking-and-updating/bbh-a84ab6bc37ca3007603d.md).
