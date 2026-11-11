# Paraphrasing · Change the sentence structure variant

[Original question](../../../questions/information-seeking/questbench-3486876017d4e56ed279.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> What is the kitten's total cost so far, leaving out the cat bed and scratching post paid for by gift card? Leah paid $200 for spaying and $20 for each of 3 vaccines, and the kitten broke vases costing $12 apiece.

## Question

> Which missing variable should be asked about to solve this problem?

## Answer choices

- **D.** number of vase
- **F.** cat bed
- **G.** scratching post

**Reference answer:** `D`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "What is the kitten's total cost so far, leaving out the cat bed and scratching post paid for by gift card? Leah paid $200 for spaying and $20 for each of 3 vaccines, and the kitten broke vases costing $12 apiece.",
  "question": "Which missing variable should be asked about to solve this problem?",
  "choices": {
    "D": "number of vase",
    "F": "cat bed",
    "G": "scratching post"
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
| Strands Decider | `D` — number of vase | `G` — scratching post | Different answer |
| GLiNER2.5 Decide | `G` — scratching post | `G` — scratching post | Same answer |
| Laya | `D` — number of vase | `G` — scratching post | Different answer |
| CalDec v1 | `G` — scratching post | `D` — number of vase | Different answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `questbench/3486876017d4e56ed279/paraphrasing/structural`

**Input fingerprint:** `4f0f1800b7188b2974173190bfaa4ac586730b6185d7a48c24db9091280e3ae6`

| Change | Recorded version |
| --- | --- |
| Paraphrasing | Change the sentence structure |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/information-seeking/questbench-3486876017d4e56ed279.md).
