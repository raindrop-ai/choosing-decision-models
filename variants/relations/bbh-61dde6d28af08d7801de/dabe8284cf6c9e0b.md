# Option order · Reverse the answer choices variant

[Original question](../../../questions/relations/bbh-61dde6d28af08d7801de.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** answer choices or their order.

[How the edits were constructed](../../../docs/variant-methods.md)

## Question

> The following paragraphs each describe a set of seven objects arranged in a fixed order. The statements are logically consistent within each paragraph. In a golf tournament, there were seven golfers: Ana, Rob, Eve, Mel, Mya, Joe, and Eli. Joe finished second-to-last. Eli finished first. Mya finished below Joe. Mel finished second. Rob finished third-to-last. Ana finished third.

## Answer choices

- **G.** Eli finished fourth
- **F.** Joe finished fourth
- **E.** Mya finished fourth
- **D.** Mel finished fourth
- **C.** Eve finished fourth
- **B.** Rob finished fourth
- **A.** Ana finished fourth

**Reference answer:** `C`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "",
  "question": "The following paragraphs each describe a set of seven objects arranged in a fixed order. The statements are logically consistent within each paragraph. In a golf tournament, there were seven golfers: Ana, Rob, Eve, Mel, Mya, Joe, and Eli. Joe finished second-to-last. Eli finished first. Mya finished below Joe. Mel finished second. Rob finished third-to-last. Ana finished third.",
  "choices": {
    "G": "Eli finished fourth",
    "F": "Joe finished fourth",
    "E": "Mya finished fourth",
    "D": "Mel finished fourth",
    "C": "Eve finished fourth",
    "B": "Rob finished fourth",
    "A": "Ana finished fourth"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `C` — Eve finished fourth | `C` — Eve finished fourth | Same answer |
| Decider v1.1 | `C` — Eve finished fourth | `C` — Eve finished fourth | Same answer |
| Jev | `C` — Eve finished fourth | `C` — Eve finished fourth | Same answer |
| Microsoft Decision-1 | `B` — Rob finished fourth | `C` — Eve finished fourth | Different answer |
| Clef | `C` — Eve finished fourth | `C` — Eve finished fourth | Same answer |
| Luna Decisions | `C` — Eve finished fourth | `C` — Eve finished fourth | Same answer |
| Clef Flash | `C` — Eve finished fourth | `C` — Eve finished fourth | Same answer |
| Strands Decider | `C` — Eve finished fourth | `B` — Rob finished fourth | Different answer |
| GLiNER2.5 Decide | `F` — Joe finished fourth | `A` — Ana finished fourth | Different answer |
| Laya | `F` — Joe finished fourth | `G` — Eli finished fourth | Different answer |
| CalDec v1 | `G` — Eli finished fourth | `G` — Eli finished fourth | Same answer |

Clef and Clef Flash sort answer choices in their published input-processing code. Their choice-order results describe that preprocessing.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `bbh/61dde6d28af08d7801de/option_order/reverse`

**Input fingerprint:** `0b78b5960fed079965895869c3880b8d8f2cbd4388251ba4af9b6f83fc60c2ab`

| Change | Recorded version |
| --- | --- |
| Option order | Reverse the answer choices |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/relations/bbh-61dde6d28af08d7801de.md).
