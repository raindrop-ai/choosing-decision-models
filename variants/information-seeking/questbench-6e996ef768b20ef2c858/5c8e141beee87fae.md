# Evidence order · Shuffle the list of given items variant

[Original question](../../../questions/information-seeking/questbench-6e996ef768b20ef2c858.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Jen is planning to sell her root crops at the local farmer's market. She has 10 sweet potatoes that cost $2 each, 6 yams which can be sold at $1.5 each, and  carrots which cost $1.25 each. She also has  beets, but she decides to keep them for her own use, so they won't be sold. If she sells all the yams, sweet potatoes, and carrots, but none of the beets, how much will she earn?

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
  "state": "Jen is planning to sell her root crops at the local farmer's market. She has 10 sweet potatoes that cost $2 each, 6 yams which can be sold at $1.5 each, and  carrots which cost $1.25 each. She also has  beets, but she decides to keep them for her own use, so they won't be sold. If she sells all the yams, sweet potatoes, and carrots, but none of the beets, how much will she earn?",
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

**Ordering comparison:** literal local or custom unit permutation. Only the exact matched comparison sets contribute to the reported ordering contrasts.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `questbench/6e996ef768b20ef2c858/presentation_order/shuffle_given_inventory/clean-source_first_parallel_b_financial_orders_0305`

**Input fingerprint:** `c375c909781dcd40c8c803d0570bc66f8b2a2f2299f4fee29717eada8a8d2c1a`

| Change | Recorded version |
| --- | --- |
| Evidence order | Shuffle the list of given items |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/information-seeking/questbench-6e996ef768b20ef2c858.md).
