# Similar distractors · Add more similar but irrelevant items variant

[Original question](../../../questions/information-seeking/questbench-4c0ac3cf132611a92c6f.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> «Varelin packs three boxes with four marbles in each box. How many marbles does Varelin pack?»
>
> «Zorven begins with nine counters and gives away two counters. How many counters remain with Zorven?»
>
> «Nerava divides twelve shells into three equal groups. How many shells are in each group?»
>
> Katina has money in her savings account. If she removes $100 from the account every month to buy shoes, how much money will remain in the account after 2 years?

## Question

> Which missing variable should be asked about to solve this problem?

## Answer choices

- **A.** Total amount of money in the account
- **H.** Price of each pair of shoes

**Reference answer:** `A`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "«Varelin packs three boxes with four marbles in each box. How many marbles does Varelin pack?»\n\n«Zorven begins with nine counters and gives away two counters. How many counters remain with Zorven?»\n\n«Nerava divides twelve shells into three equal groups. How many shells are in each group?»\n\nKatina has money in her savings account. If she removes $100 from the account every month to buy shoes, how much money will remain in the account after 2 years?",
  "question": "Which missing variable should be asked about to solve this problem?",
  "choices": {
    "A": "Total amount of money in the account",
    "H": "Price of each pair of shoes"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `A` — Total amount of money in the account | `A` — Total amount of money in the account | Same answer |
| Decider v1.1 | `A` — Total amount of money in the account | `A` — Total amount of money in the account | Same answer |
| Jev | `A` — Total amount of money in the account | `A` — Total amount of money in the account | Same answer |
| Microsoft Decision-1 | `A` — Total amount of money in the account | `A` — Total amount of money in the account | Same answer |
| Clef | `A` — Total amount of money in the account | `A` — Total amount of money in the account | Same answer |
| Luna Decisions | `A` — Total amount of money in the account | `A` — Total amount of money in the account | Same answer |
| Clef Flash | `A` — Total amount of money in the account | `A` — Total amount of money in the account | Same answer |
| Strands Decider | `A` — Total amount of money in the account | `A` — Total amount of money in the account | Same answer |
| GLiNER2.5 Decide | `A` — Total amount of money in the account | `A` — Total amount of money in the account | Same answer |
| Laya | `A` — Total amount of money in the account | `A` — Total amount of money in the account | Same answer |
| CalDec v1 | `A` — Total amount of money in the account | `A` — Total amount of money in the account | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `questbench/4c0ac3cf132611a92c6f/similar_distractors/high/clean-source_first_quest_near_problems_full_0212`

**Input fingerprint:** `4fc25dfb77a8b011ec60229a74b5b1aa7b2579e8ee09b7511cc1b2b1abc1750f`

| Change | Recorded version |
| --- | --- |
| Similar distractors | Add more similar but irrelevant items |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/information-seeking/questbench-4c0ac3cf132611a92c6f.md).
