# Evidence order · Present the evidence in a shuffled order variant

[Original question](../../../questions/information-seeking/questbench-f3d3fec034c5da8bf67e.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Naomi scored 68 points, while Yuri, who was wearing a blue shirt and had just eaten several slices of pizza, scored 10 more than half as many points as Naomi.
> In a board game, four students scored a sum of points.
> Brianna, who was sitting next to a window and had a couple  cups of water during the game, scored 17 points more than Naomi.
> If Jojo, who was wearing a red hat and had to take a break during the game, scored the remaining points, how many points did Jojo score?

## Question

> Which missing variable should be asked about to solve this problem?

## Answer choices

- **T.** Total points scored by all students
- **X1.** Number of slices of pizza Yuri ate
- **X2.** Number of cups of water Brianna drank
- **X3.** Duration of Jojo&#x27;s break in minutes

**Reference answer:** `T`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Naomi scored 68 points, while Yuri, who was wearing a blue shirt and had just eaten several slices of pizza, scored 10 more than half as many points as Naomi.\nIn a board game, four students scored a sum of points.\nBrianna, who was sitting next to a window and had a couple  cups of water during the game, scored 17 points more than Naomi.\nIf Jojo, who was wearing a red hat and had to take a break during the game, scored the remaining points, how many points did Jojo score?",
  "question": "Which missing variable should be asked about to solve this problem?",
  "choices": {
    "T": "Total points scored by all students",
    "X1": "Number of slices of pizza Yuri ate",
    "X2": "Number of cups of water Brianna drank",
    "X3": "Duration of Jojo's break in minutes"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `T` — Total points scored by all students | `T` — Total points scored by all students | Same answer |
| Decider v1.1 | `T` — Total points scored by all students | `T` — Total points scored by all students | Same answer |
| Jev | `T` — Total points scored by all students | `T` — Total points scored by all students | Same answer |
| Microsoft Decision-1 | `T` — Total points scored by all students | `T` — Total points scored by all students | Same answer |
| Clef | `T` — Total points scored by all students | `T` — Total points scored by all students | Same answer |
| Luna Decisions | `T` — Total points scored by all students | `T` — Total points scored by all students | Same answer |
| Clef Flash | `T` — Total points scored by all students | `T` — Total points scored by all students | Same answer |
| Strands Decider | `T` — Total points scored by all students | `T` — Total points scored by all students | Same answer |
| GLiNER2.5 Decide | `X3` — Duration of Jojo&#x27;s break in minutes | `T` — Total points scored by all students | Different answer |
| Laya | `T` — Total points scored by all students | `T` — Total points scored by all students | Same answer |
| CalDec v1 | `T` — Total points scored by all students | `X2` — Number of cups of water Brianna drank | Different answer |

**Ordering comparison:** literal units with boundary layout change. Only the exact matched comparison sets contribute to the reported ordering contrasts.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `questbench/f3d3fec034c5da8bf67e/presentation_order/shuffled_presentation/clean-source_first_parallel_b_quest_global_orders_0390`

**Input fingerprint:** `4b504e5afc454f85a00a371c16f48e69b21f229e0e09826f777656242931e37d`

| Change | Recorded version |
| --- | --- |
| Evidence order | Present the evidence in a shuffled order |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/information-seeking/questbench-f3d3fec034c5da8bf67e.md).
