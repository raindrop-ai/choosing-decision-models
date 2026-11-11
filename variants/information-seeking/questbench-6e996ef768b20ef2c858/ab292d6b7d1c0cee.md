# Unrelated examples · No worked example (absence-control recipe) variant

[Original question](../../../questions/information-seeking/questbench-6e996ef768b20ef2c858.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Jen is planning to sell her root crops at the local farmer's market. She has 6 yams which can be sold at $1.5 each, 10 sweet potatoes that cost $2 each, and  carrots which cost $1.25 each. She also has  beets, but she decides to keep them for her own use, so they won't be sold. If she sells all the yams, sweet potatoes, and carrots, but none of the beets, how much will she earn?
>
> The poem has a refrain and an anonymous narrator.

## Question

> Which missing variable should be asked about to solve this problem?

## Answer choices

- **E.** Number of carrots
- **G.** Number of beets

**Reference answer:** `E`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Jen is planning to sell her root crops at the local farmer's market. She has 6 yams which can be sold at $1.5 each, 10 sweet potatoes that cost $2 each, and  carrots which cost $1.25 each. She also has  beets, but she decides to keep them for her own use, so they won't be sold. If she sells all the yams, sweet potatoes, and carrots, but none of the beets, how much will she earn?\n\nThe poem has a refrain and an anonymous narrator.",
  "question": "Which missing variable should be asked about to solve this problem?",
  "choices": {
    "E": "Number of carrots",
    "G": "Number of beets"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `E` — Number of carrots | `E` — Number of carrots | Same answer |
| Decider v1.1 | `E` — Number of carrots | `E` — Number of carrots | Same answer |
| Jev | `E` — Number of carrots | `E` — Number of carrots | Same answer |
| Microsoft Decision-1 | `E` — Number of carrots | `E` — Number of carrots | Same answer |
| Clef | `E` — Number of carrots | `E` — Number of carrots | Same answer |
| Luna Decisions | `E` — Number of carrots | `E` — Number of carrots | Same answer |
| Clef Flash | `E` — Number of carrots | `E` — Number of carrots | Same answer |
| Strands Decider | `E` — Number of carrots | `E` — Number of carrots | Same answer |
| GLiNER2.5 Decide | `G` — Number of beets | `G` — Number of beets | Same answer |
| Laya | `E` — Number of carrots | `G` — Number of beets | Different answer |
| CalDec v1 | `G` — Number of beets | `G` — Number of beets | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `questbench/6e996ef768b20ef2c858/examples/absent/clean-source_first_quest_literary_contexts_full_0079`

**Input fingerprint:** `1a006363556aaa8b2707a30270ec2773066eb96284484adccbf5f3ad08beb872`

| Change | Recorded version |
| --- | --- |
| Unrelated examples | No worked example (absence-control recipe) |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/information-seeking/questbench-6e996ef768b20ef2c858.md).
