# Similar distractors · Add fewer similar but irrelevant items variant

[Original question](../../../questions/information-seeking/questbench-8ad5ff473674fe4f78fa.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> «Varelin packs three boxes with four marbles in each box. How many marbles does Varelin pack?»
>
> Sally goes to a pizza shop where she buys one small pizza. Sally also buys one family-size pizza that costs 3 times as much as the small pizza she bought. How much does Sally spend in all?

## Question

> Which missing variable should be asked about to solve this problem?

## Answer choices

- **A.** COST OF ONE SMALL SIZE PIZZA  SALLY BOUGHT
- **P.** NUMBER OF PEOPLE ENTERED THE SHOP
- **Q.** NUMBER OF SMALL PIZZA&#x27;S ORDERED BY THE GROUP

**Reference answer:** `A`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "«Varelin packs three boxes with four marbles in each box. How many marbles does Varelin pack?»\n\nSally goes to a pizza shop where she buys one small pizza. Sally also buys one family-size pizza that costs 3 times as much as the small pizza she bought. How much does Sally spend in all?",
  "question": "Which missing variable should be asked about to solve this problem?",
  "choices": {
    "A": "COST OF ONE SMALL SIZE PIZZA  SALLY BOUGHT",
    "P": "NUMBER OF PEOPLE ENTERED THE SHOP",
    "Q": "NUMBER OF SMALL PIZZA'S ORDERED BY THE GROUP"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `A` — COST OF ONE SMALL SIZE PIZZA  SALLY BOUGHT | `A` — COST OF ONE SMALL SIZE PIZZA  SALLY BOUGHT | Same answer |
| Decider v1.1 | `A` — COST OF ONE SMALL SIZE PIZZA  SALLY BOUGHT | `A` — COST OF ONE SMALL SIZE PIZZA  SALLY BOUGHT | Same answer |
| Jev | `A` — COST OF ONE SMALL SIZE PIZZA  SALLY BOUGHT | `A` — COST OF ONE SMALL SIZE PIZZA  SALLY BOUGHT | Same answer |
| Microsoft Decision-1 | `A` — COST OF ONE SMALL SIZE PIZZA  SALLY BOUGHT | `A` — COST OF ONE SMALL SIZE PIZZA  SALLY BOUGHT | Same answer |
| Clef | `A` — COST OF ONE SMALL SIZE PIZZA  SALLY BOUGHT | `A` — COST OF ONE SMALL SIZE PIZZA  SALLY BOUGHT | Same answer |
| Luna Decisions | `A` — COST OF ONE SMALL SIZE PIZZA  SALLY BOUGHT | `A` — COST OF ONE SMALL SIZE PIZZA  SALLY BOUGHT | Same answer |
| Clef Flash | `A` — COST OF ONE SMALL SIZE PIZZA  SALLY BOUGHT | `A` — COST OF ONE SMALL SIZE PIZZA  SALLY BOUGHT | Same answer |
| Strands Decider | `A` — COST OF ONE SMALL SIZE PIZZA  SALLY BOUGHT | `A` — COST OF ONE SMALL SIZE PIZZA  SALLY BOUGHT | Same answer |
| GLiNER2.5 Decide | `A` — COST OF ONE SMALL SIZE PIZZA  SALLY BOUGHT | `A` — COST OF ONE SMALL SIZE PIZZA  SALLY BOUGHT | Same answer |
| Laya | `A` — COST OF ONE SMALL SIZE PIZZA  SALLY BOUGHT | `A` — COST OF ONE SMALL SIZE PIZZA  SALLY BOUGHT | Same answer |
| CalDec v1 | `A` — COST OF ONE SMALL SIZE PIZZA  SALLY BOUGHT | `A` — COST OF ONE SMALL SIZE PIZZA  SALLY BOUGHT | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `questbench/8ad5ff473674fe4f78fa/similar_distractors/low/clean-source_first_quest_near_problems_full_0212`

**Input fingerprint:** `00509387e5b7a3050f232d6b5294ea6566694922ef189424e69c58c6dd7c991b`

| Change | Recorded version |
| --- | --- |
| Similar distractors | Add fewer similar but irrelevant items |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/information-seeking/questbench-8ad5ff473674fe4f78fa.md).
