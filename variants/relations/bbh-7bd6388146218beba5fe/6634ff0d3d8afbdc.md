# Paraphrasing · Change the sentence structure variant

[Original question](../../../questions/relations/bbh-7bd6388146218beba5fe.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** question instructions.

[How the edits were constructed](../../../docs/variant-methods.md)

## Question

> The following paragraphs each describe a set of seven objects arranged in a fixed order. The statements are logically consistent within each paragraph. A fruit stand sells seven fruits: loquats, cantaloupes, watermelons, apples, oranges, pears, and mangoes. The oranges are the second-cheapest. The pears are more expensive than the apples. The cantaloupes are less expensive than the mangoes. The mangoes are the third-cheapest. The watermelons are the second-most expensive. The loquats are the third-most expensive.

## Answer choices

- **A.** The loquats are the fourth-most expensive
- **B.** The cantaloupes are the fourth-most expensive
- **C.** The watermelons are the fourth-most expensive
- **D.** The apples are the fourth-most expensive
- **E.** The oranges are the fourth-most expensive
- **F.** The pears are the fourth-most expensive
- **G.** The mangoes are the fourth-most expensive

**Reference answer:** `D`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "",
  "question": "The following paragraphs each describe a set of seven objects arranged in a fixed order. The statements are logically consistent within each paragraph. A fruit stand sells seven fruits: loquats, cantaloupes, watermelons, apples, oranges, pears, and mangoes. The oranges are the second-cheapest. The pears are more expensive than the apples. The cantaloupes are less expensive than the mangoes. The mangoes are the third-cheapest. The watermelons are the second-most expensive. The loquats are the third-most expensive.",
  "choices": {
    "A": "The loquats are the fourth-most expensive",
    "B": "The cantaloupes are the fourth-most expensive",
    "C": "The watermelons are the fourth-most expensive",
    "D": "The apples are the fourth-most expensive",
    "E": "The oranges are the fourth-most expensive",
    "F": "The pears are the fourth-most expensive",
    "G": "The mangoes are the fourth-most expensive"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `D` — The apples are the fourth-most expensive | `D` — The apples are the fourth-most expensive | Same answer |
| Decider v1.1 | `D` — The apples are the fourth-most expensive | `G` — The mangoes are the fourth-most expensive | Different answer |
| Jev | `D` — The apples are the fourth-most expensive | `F` — The pears are the fourth-most expensive | Different answer |
| Microsoft Decision-1 | `D` — The apples are the fourth-most expensive | `F` — The pears are the fourth-most expensive | Different answer |
| Clef | `F` — The pears are the fourth-most expensive | `D` — The apples are the fourth-most expensive | Different answer |
| Luna Decisions | `D` — The apples are the fourth-most expensive | `D` — The apples are the fourth-most expensive | Same answer |
| Clef Flash | `F` — The pears are the fourth-most expensive | `F` — The pears are the fourth-most expensive | Same answer |
| Strands Decider | `D` — The apples are the fourth-most expensive | `F` — The pears are the fourth-most expensive | Different answer |
| GLiNER2.5 Decide | `G` — The mangoes are the fourth-most expensive | `G` — The mangoes are the fourth-most expensive | Same answer |
| Laya | `A` — The loquats are the fourth-most expensive | `A` — The loquats are the fourth-most expensive | Same answer |
| CalDec v1 | `E` — The oranges are the fourth-most expensive | `E` — The oranges are the fourth-most expensive | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `bbh/7bd6388146218beba5fe/paraphrasing/structural`

**Input fingerprint:** `576428d660e448390e523750f093863aeda7779ad66febb1b4cfd2b64d610242`

| Change | Recorded version |
| --- | --- |
| Paraphrasing | Change the sentence structure |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/relations/bbh-7bd6388146218beba5fe.md).
