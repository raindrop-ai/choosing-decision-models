# Paraphrasing · Change individual words and phrases variant

[Original question](../../../questions/state-tracking-and-updating/bbh-a84ab6bc37ca3007603d.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** question instructions.

[How the edits were constructed](../../../docs/variant-methods.md)

## Question

> Alice, Bob, Claire, Dave, and Eve are playing a game. At the start of the game, they are each holding a ball: Alice has a brown ball, Bob has a black ball, Claire has a white ball, Dave has a yellow ball, and Eve has a purple ball.
> As the game progresses, pairs of players trade balls. First, Claire and Dave swap balls. Then, Alice and Eve swap balls. Then, Dave and Bob swap balls. Then, Alice and Eve swap balls. Finally, Claire and Eve swap balls. At the end of the game, which ball does Alice have?

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
  "state": "",
  "question": "Alice, Bob, Claire, Dave, and Eve are playing a game. At the start of the game, they are each holding a ball: Alice has a brown ball, Bob has a black ball, Claire has a white ball, Dave has a yellow ball, and Eve has a purple ball.\nAs the game progresses, pairs of players trade balls. First, Claire and Dave swap balls. Then, Alice and Eve swap balls. Then, Dave and Bob swap balls. Then, Alice and Eve swap balls. Finally, Claire and Eve swap balls. At the end of the game, which ball does Alice have?",
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
| Clef Flash | `E` — purple ball | `E` — purple ball | Same answer |
| Strands Decider | `E` — purple ball | `E` — purple ball | Same answer |
| GLiNER2.5 Decide | `A` — brown ball | `A` — brown ball | Same answer |
| Laya | `A` — brown ball | `A` — brown ball | Same answer |
| CalDec v1 | `A` — brown ball | `A` — brown ball | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `bbh/a84ab6bc37ca3007603d/paraphrasing/surface`

**Input fingerprint:** `431415222c84075bca7753b45e9956bc3a51a081ef0528818c086f7eac76a3a4`

| Change | Recorded version |
| --- | --- |
| Paraphrasing | Change individual words and phrases |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/state-tracking-and-updating/bbh-a84ab6bc37ca3007603d.md).
