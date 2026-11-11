# Evidence order · Present the evidence in a shuffled order variant

[Original question](../../../questions/relations/bbh-bd7dbece61ab36c21988.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** question instructions.

[How the edits were constructed](../../../docs/variant-methods.md)

## Question

> The following paragraphs each describe a set of five objects arranged in a fixed order. The statements are logically consistent within each paragraph. A fruit stand sells five fruits: apples, mangoes, oranges, plums, and pears. The plums are the cheapest. The pears are more expensive than the oranges. The oranges are more expensive than the mangoes. The apples are less expensive than the mangoes.

## Answer choices

- **A.** The apples are the second-cheapest
- **B.** The mangoes are the second-cheapest
- **C.** The oranges are the second-cheapest
- **D.** The plums are the second-cheapest
- **E.** The pears are the second-cheapest

**Reference answer:** `A`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "",
  "question": "The following paragraphs each describe a set of five objects arranged in a fixed order. The statements are logically consistent within each paragraph. A fruit stand sells five fruits: apples, mangoes, oranges, plums, and pears. The plums are the cheapest. The pears are more expensive than the oranges. The oranges are more expensive than the mangoes. The apples are less expensive than the mangoes.",
  "choices": {
    "A": "The apples are the second-cheapest",
    "B": "The mangoes are the second-cheapest",
    "C": "The oranges are the second-cheapest",
    "D": "The plums are the second-cheapest",
    "E": "The pears are the second-cheapest"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `A` — The apples are the second-cheapest | `A` — The apples are the second-cheapest | Same answer |
| Decider v1.1 | `A` — The apples are the second-cheapest | `A` — The apples are the second-cheapest | Same answer |
| Jev | `A` — The apples are the second-cheapest | `A` — The apples are the second-cheapest | Same answer |
| Microsoft Decision-1 | `A` — The apples are the second-cheapest | `A` — The apples are the second-cheapest | Same answer |
| Clef | `A` — The apples are the second-cheapest | `B` — The mangoes are the second-cheapest | Different answer |
| Luna Decisions | `A` — The apples are the second-cheapest | `A` — The apples are the second-cheapest | Same answer |
| Clef Flash | `B` — The mangoes are the second-cheapest | `B` — The mangoes are the second-cheapest | Same answer |
| Strands Decider | `B` — The mangoes are the second-cheapest | `B` — The mangoes are the second-cheapest | Same answer |
| GLiNER2.5 Decide | `E` — The pears are the second-cheapest | `D` — The plums are the second-cheapest | Different answer |
| Laya | `A` — The apples are the second-cheapest | `D` — The plums are the second-cheapest | Different answer |
| CalDec v1 | `A` — The apples are the second-cheapest | `D` — The plums are the second-cheapest | Different answer |

**Ordering comparison:** literal requested source unit permutation. Only the exact matched comparison sets contribute to the reported ordering contrasts.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `bbh/bd7dbece61ab36c21988/presentation_order/shuffled_presentation/clean-bare_ordinal_fact_order_full_0050`

**Input fingerprint:** `e1fe8199556def6c1cd3cb9ea52a3e7ae83946ba467a1e2bc95df39ed1521af4`

| Change | Recorded version |
| --- | --- |
| Evidence order | Present the evidence in a shuffled order |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/relations/bbh-bd7dbece61ab36c21988.md).
