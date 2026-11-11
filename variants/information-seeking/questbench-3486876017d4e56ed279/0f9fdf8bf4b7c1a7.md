# Option order · Move the first answer choice to the end variant

[Original question](../../../questions/information-seeking/questbench-3486876017d4e56ed279.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** answer choices or their order.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Leah just got a new kitten. Spaying her cost $200, her 3 vaccines costs $20 each, and the kitten broke vases that cost $12 each. Leah also bought a cat bed and a scratching post, but she used a gift card to pay for these items. How much has the kitten cost so far, excluding the items paid for with the gift card?

## Question

> Which missing variable should be asked about to solve this problem?

## Answer choices

- **F.** cat bed
- **G.** scratching post
- **D.** number of vase

**Reference answer:** `D`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Leah just got a new kitten. Spaying her cost $200, her 3 vaccines costs $20 each, and the kitten broke vases that cost $12 each. Leah also bought a cat bed and a scratching post, but she used a gift card to pay for these items. How much has the kitten cost so far, excluding the items paid for with the gift card?",
  "question": "Which missing variable should be asked about to solve this problem?",
  "choices": {
    "F": "cat bed",
    "G": "scratching post",
    "D": "number of vase"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `D` — number of vase | `D` — number of vase | Same answer |
| Decider v1.1 | `D` — number of vase | `D` — number of vase | Same answer |
| Jev | `D` — number of vase | `D` — number of vase | Same answer |
| Microsoft Decision-1 | `D` — number of vase | `D` — number of vase | Same answer |
| Clef | `D` — number of vase | `D` — number of vase | Same answer |
| Luna Decisions | `D` — number of vase | `D` — number of vase | Same answer |
| Clef Flash | `D` — number of vase | `D` — number of vase | Same answer |
| Strands Decider | `D` — number of vase | `D` — number of vase | Same answer |
| GLiNER2.5 Decide | `G` — scratching post | `G` — scratching post | Same answer |
| Laya | `D` — number of vase | `F` — cat bed | Different answer |
| CalDec v1 | `G` — scratching post | `G` — scratching post | Same answer |

Clef and Clef Flash sort answer choices in their published input-processing code. Their choice-order results describe that preprocessing.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `questbench/3486876017d4e56ed279/option_order/rotate_1`

**Input fingerprint:** `930f8493d5d801abdbe931a1ceb9eee9eec5e54f1b948547ad5b2d28d8605bdb`

| Change | Recorded version |
| --- | --- |
| Option order | Move the first answer choice to the end |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/information-seeking/questbench-3486876017d4e56ed279.md).
