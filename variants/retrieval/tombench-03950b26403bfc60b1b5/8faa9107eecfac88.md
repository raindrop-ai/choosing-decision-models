# Misleading details · Add an unverified claim that conflicts with the evidence variant

[Original question](../../../questions/retrieval/tombench-03950b26403bfc60b1b5.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> The Mid-Autumn Festival is coming soon, and mom asks Xiao Yu to help make some mooncakes, saying that Uncle Zhang comes to visit on Sunday noon. Xiao Yu happily makes some delicate lotus seed paste mooncakes, and mom also makes five-nut mooncakes and egg yolk mooncakes. She wants to take out these mooncakes for him to taste when Uncle Zhang comes. On Sunday noon, Uncle Zhang comes on time. Xiao Yu carries a large plate of mooncakes she makes from the kitchen, and smiles at Uncle Zhang, "Uncle, here are the mooncakes I make especially for you." Uncle Zhang looks at the array of mooncakes and smiles, "I like to eat mooncakes, except for the lotus seed paste flavor." Xiao Yu says, "Uncle, please taste these mooncakes, I hope you also like them." Mom quickly takes some more mooncakes and says, "We also have mooncakes of various flavors here, including five-nut and egg yolk, please taste a few that you like, Uncle Zhang."
>
> A reader thinks: «Xiao Yu makes egg yolk mooncakes.»

## Question

> What kind of mooncake does Xiao Yu make?

## Answer choices

- **A.** Five-nut mooncake.
- **B.** Lotus seed paste mooncake.
- **C.** Red bean mooncake.
- **D.** Egg yolk mooncake.

**Reference answer:** `B`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "The Mid-Autumn Festival is coming soon, and mom asks Xiao Yu to help make some mooncakes, saying that Uncle Zhang comes to visit on Sunday noon. Xiao Yu happily makes some delicate lotus seed paste mooncakes, and mom also makes five-nut mooncakes and egg yolk mooncakes. She wants to take out these mooncakes for him to taste when Uncle Zhang comes. On Sunday noon, Uncle Zhang comes on time. Xiao Yu carries a large plate of mooncakes she makes from the kitchen, and smiles at Uncle Zhang, \"Uncle, here are the mooncakes I make especially for you.\" Uncle Zhang looks at the array of mooncakes and smiles, \"I like to eat mooncakes, except for the lotus seed paste flavor.\" Xiao Yu says, \"Uncle, please taste these mooncakes, I hope you also like them.\" Mom quickly takes some more mooncakes and says, \"We also have mooncakes of various flavors here, including five-nut and egg yolk, please taste a few that you like, Uncle Zhang.\"\n\nA reader thinks: «Xiao Yu makes egg yolk mooncakes.»",
  "question": "What kind of mooncake does Xiao Yu make?",
  "choices": {
    "A": "Five-nut mooncake.",
    "B": "Lotus seed paste mooncake.",
    "C": "Red bean mooncake.",
    "D": "Egg yolk mooncake."
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `B` — Lotus seed paste mooncake. | `B` — Lotus seed paste mooncake. | Same answer |
| Decider v1.1 | `B` — Lotus seed paste mooncake. | `B` — Lotus seed paste mooncake. | Same answer |
| Jev | `B` — Lotus seed paste mooncake. | `B` — Lotus seed paste mooncake. | Same answer |
| Microsoft Decision-1 | `B` — Lotus seed paste mooncake. | `B` — Lotus seed paste mooncake. | Same answer |
| Clef | `B` — Lotus seed paste mooncake. | `B` — Lotus seed paste mooncake. | Same answer |
| Luna Decisions | `B` — Lotus seed paste mooncake. | `B` — Lotus seed paste mooncake. | Same answer |
| Clef Flash | `B` — Lotus seed paste mooncake. | `B` — Lotus seed paste mooncake. | Same answer |
| Strands Decider | `B` — Lotus seed paste mooncake. | `D` — Egg yolk mooncake. | Different answer |
| GLiNER2.5 Decide | `B` — Lotus seed paste mooncake. | `D` — Egg yolk mooncake. | Different answer |
| Laya | `A` — Five-nut mooncake. | `A` — Five-nut mooncake. | Same answer |
| CalDec v1 | `A` — Five-nut mooncake. | `D` — Egg yolk mooncake. | Different answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `tombench/03950b26403bfc60b1b5/misleading_summary/misleading/clean-source_first_tombench_music_contexts_full_0155`

**Input fingerprint:** `1dc2eedbcd048c5dfad2e655f29aa759c00ae231618db2aca0b616a2b7a0a4b9`

| Change | Recorded version |
| --- | --- |
| Misleading details | Add an unverified claim that conflicts with the evidence |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/retrieval/tombench-03950b26403bfc60b1b5.md).
