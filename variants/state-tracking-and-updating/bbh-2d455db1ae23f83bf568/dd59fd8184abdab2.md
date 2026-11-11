# Similar distractors · Add more similar but irrelevant items variant

[Original question](../../../questions/state-tracking-and-updating/bbh-2d455db1ae23f83bf568.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Varelin holds a flute. Zorven holds a maraca. Nereth holds an oboe. Varelin and Zorven exchange their instruments. Zorven and Nereth exchange their instruments. Nereth and Varelin exchange their instruments.

## Question

> Alice, Bob, and Claire are playing a game. At the start of the game, they are each holding a ball: Alice has a yellow ball, Bob has a green ball, and Claire has a blue ball.
> As the game progresses, pairs of players trade balls. First, Alice and Bob swap balls. Then, Alice and Claire swap balls. Finally, Claire and Bob swap balls. At the end of the game, Alice has the

## Answer choices

- **A.** yellow ball
- **B.** green ball
- **C.** blue ball

**Reference answer:** `C`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Varelin holds a flute. Zorven holds a maraca. Nereth holds an oboe. Varelin and Zorven exchange their instruments. Zorven and Nereth exchange their instruments. Nereth and Varelin exchange their instruments.",
  "question": "Alice, Bob, and Claire are playing a game. At the start of the game, they are each holding a ball: Alice has a yellow ball, Bob has a green ball, and Claire has a blue ball.\nAs the game progresses, pairs of players trade balls. First, Alice and Bob swap balls. Then, Alice and Claire swap balls. Finally, Claire and Bob swap balls. At the end of the game, Alice has the",
  "choices": {
    "A": "yellow ball",
    "B": "green ball",
    "C": "blue ball"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `C` — blue ball | `C` — blue ball | Same answer |
| Decider v1.1 | `C` — blue ball | `C` — blue ball | Same answer |
| Jev | `C` — blue ball | `C` — blue ball | Same answer |
| Microsoft Decision-1 | `B` — green ball | `B` — green ball | Same answer |
| Clef | `C` — blue ball | `C` — blue ball | Same answer |
| Luna Decisions | `B` — green ball | `A` — yellow ball | Different answer |
| Clef Flash | `B` — green ball | `B` — green ball | Same answer |
| Strands Decider | `B` — green ball | `C` — blue ball | Different answer |
| GLiNER2.5 Decide | `A` — yellow ball | `A` — yellow ball | Same answer |
| Laya | `A` — yellow ball | `A` — yellow ball | Same answer |
| CalDec v1 | `A` — yellow ball | `A` — yellow ball | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `bbh/2d455db1ae23f83bf568/similar_distractors/high/clean-source_first_tracking_new_distractors_full_0165`

**Input fingerprint:** `7bc6ca93d62818308ef282627ac9e58c03844ded30b9111703a7c33900a7a8cd`

| Change | Recorded version |
| --- | --- |
| Similar distractors | Add more similar but irrelevant items |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/state-tracking-and-updating/bbh-2d455db1ae23f83bf568.md).
