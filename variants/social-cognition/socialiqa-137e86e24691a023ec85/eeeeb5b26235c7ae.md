# Option order · Move the first answer choice to the end variant

[Original question](../../../questions/social-cognition/socialiqa-137e86e24691a023ec85.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** answer choices or their order.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Addison's fish died recently and Addison wanted to buy a replacement.

## Question

> Why did Addison do this?

## Answer choices

- **B.** get a frog
- **C.** discover that their fish was dead
- **A.** fill her aquarium

**Reference answer:** `A`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Addison's fish died recently and Addison wanted to buy a replacement.",
  "question": "Why did Addison do this?",
  "choices": {
    "B": "get a frog",
    "C": "discover that their fish was dead",
    "A": "fill her aquarium"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `A` — fill her aquarium | `A` — fill her aquarium | Same answer |
| Decider v1.1 | `A` — fill her aquarium | `A` — fill her aquarium | Same answer |
| Jev | `A` — fill her aquarium | `A` — fill her aquarium | Same answer |
| Microsoft Decision-1 | `C` — discover that their fish was dead | `C` — discover that their fish was dead | Same answer |
| Clef | `A` — fill her aquarium | `A` — fill her aquarium | Same answer |
| Luna Decisions | `A` — fill her aquarium | `A` — fill her aquarium | Same answer |
| Clef Flash | `A` — fill her aquarium | `A` — fill her aquarium | Same answer |
| Strands Decider | `C` — discover that their fish was dead | `C` — discover that their fish was dead | Same answer |
| GLiNER2.5 Decide | `C` — discover that their fish was dead | `C` — discover that their fish was dead | Same answer |
| Laya | `A` — fill her aquarium | `C` — discover that their fish was dead | Different answer |
| CalDec v1 | `C` — discover that their fish was dead | `C` — discover that their fish was dead | Same answer |

Clef and Clef Flash sort answer choices in their published input-processing code. Their choice-order results describe that preprocessing.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `socialiqa/137e86e24691a023ec85/option_order/rotate_1`

**Input fingerprint:** `c75c49a96069bad2bd15ce9ac90eb589ee6ded8c92d5df1d998697e77e9df7c6`

| Change | Recorded version |
| --- | --- |
| Option order | Move the first answer choice to the end |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/social-cognition/socialiqa-137e86e24691a023ec85.md).
