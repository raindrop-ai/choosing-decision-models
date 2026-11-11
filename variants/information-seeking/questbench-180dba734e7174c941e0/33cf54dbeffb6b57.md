# Option order · Move the first answer choice to the end variant

[Original question](../../../questions/information-seeking/questbench-180dba734e7174c941e0.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** answer choices or their order.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Johnny, on the other hand, bought 2 more face masks than thrice the number of face masks Mike bought. How many face masks did Johnny buy?

## Question

> Which missing variable should be asked about to solve this problem?

## Answer choices

- **X1.** Number of gloves Johnny bought
- **X2.** Number of hand sanitizers Mike bought
- **M.** Number of face masks Mike bought

**Reference answer:** `M`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Johnny, on the other hand, bought 2 more face masks than thrice the number of face masks Mike bought. How many face masks did Johnny buy?",
  "question": "Which missing variable should be asked about to solve this problem?",
  "choices": {
    "X1": "Number of gloves Johnny bought",
    "X2": "Number of hand sanitizers Mike bought",
    "M": "Number of face masks Mike bought"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `M` — Number of face masks Mike bought | `M` — Number of face masks Mike bought | Same answer |
| Decider v1.1 | `M` — Number of face masks Mike bought | `M` — Number of face masks Mike bought | Same answer |
| Jev | `M` — Number of face masks Mike bought | `M` — Number of face masks Mike bought | Same answer |
| Microsoft Decision-1 | `M` — Number of face masks Mike bought | `M` — Number of face masks Mike bought | Same answer |
| Clef | `M` — Number of face masks Mike bought | `M` — Number of face masks Mike bought | Same answer |
| Luna Decisions | `M` — Number of face masks Mike bought | `M` — Number of face masks Mike bought | Same answer |
| Clef Flash | `M` — Number of face masks Mike bought | `M` — Number of face masks Mike bought | Same answer |
| Strands Decider | `M` — Number of face masks Mike bought | `M` — Number of face masks Mike bought | Same answer |
| GLiNER2.5 Decide | `M` — Number of face masks Mike bought | `M` — Number of face masks Mike bought | Same answer |
| Laya | `M` — Number of face masks Mike bought | `M` — Number of face masks Mike bought | Same answer |
| CalDec v1 | `M` — Number of face masks Mike bought | `M` — Number of face masks Mike bought | Same answer |

Clef and Clef Flash sort answer choices in their published input-processing code. Their choice-order results describe that preprocessing.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `questbench/180dba734e7174c941e0/option_order/rotate_1`

**Input fingerprint:** `8e85e48531a6fff5e6f4067157c77bf55f8bd5bfe272bd6cb497c3694efe8b1a`

| Change | Recorded version |
| --- | --- |
| Option order | Move the first answer choice to the end |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/information-seeking/questbench-180dba734e7174c941e0.md).
