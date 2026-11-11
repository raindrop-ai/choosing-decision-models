# Misleading details · Add an unverified claim that conflicts with the evidence variant

[Original question](../../../questions/information-seeking/questbench-8ad5ff473674fe4f78fa.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Sally goes to a pizza shop where she buys one small pizza. Sally also buys one family-size pizza that costs 3 times as much as the small pizza she bought. How much does Sally spend in all?
>
> A reader thinks the variable to ask about is «NUMBER OF PEOPLE ENTERED THE SHOP».

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
  "state": "Sally goes to a pizza shop where she buys one small pizza. Sally also buys one family-size pizza that costs 3 times as much as the small pizza she bought. How much does Sally spend in all?\n\nA reader thinks the variable to ask about is «NUMBER OF PEOPLE ENTERED THE SHOP».",
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
| GLiNER2.5 Decide | `A` — COST OF ONE SMALL SIZE PIZZA  SALLY BOUGHT | `P` — NUMBER OF PEOPLE ENTERED THE SHOP | Different answer |
| Laya | `A` — COST OF ONE SMALL SIZE PIZZA  SALLY BOUGHT | `A` — COST OF ONE SMALL SIZE PIZZA  SALLY BOUGHT | Same answer |
| CalDec v1 | `A` — COST OF ONE SMALL SIZE PIZZA  SALLY BOUGHT | `A` — COST OF ONE SMALL SIZE PIZZA  SALLY BOUGHT | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `questbench/8ad5ff473674fe4f78fa/misleading_summary/misleading/clean-source_first_quest_literary_contexts_full_0078`

**Input fingerprint:** `af9f32d81702a052ebbcee6d425a6bfb35d8a16ebf3f6ea2160c0a3f3b74804e`

| Change | Recorded version |
| --- | --- |
| Misleading details | Add an unverified claim that conflicts with the evidence |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/information-seeking/questbench-8ad5ff473674fe4f78fa.md).
