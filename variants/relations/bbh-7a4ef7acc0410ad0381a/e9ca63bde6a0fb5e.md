# Option order · Reverse the answer choices variant

[Original question](../../../questions/relations/bbh-7a4ef7acc0410ad0381a.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** answer choices or their order.

[How the edits were constructed](../../../docs/variant-methods.md)

## Question

> The following paragraphs each describe a set of three objects arranged in a fixed order. The statements are logically consistent within each paragraph. In a golf tournament, there were three golfers: Mel, Ada, and Ana. Mel finished last. Ana finished second.

## Answer choices

- **C.** Ana finished first
- **B.** Ada finished first
- **A.** Mel finished first

**Reference answer:** `B`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "",
  "question": "The following paragraphs each describe a set of three objects arranged in a fixed order. The statements are logically consistent within each paragraph. In a golf tournament, there were three golfers: Mel, Ada, and Ana. Mel finished last. Ana finished second.",
  "choices": {
    "C": "Ana finished first",
    "B": "Ada finished first",
    "A": "Mel finished first"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `B` — Ada finished first | `B` — Ada finished first | Same answer |
| Decider v1.1 | `B` — Ada finished first | `B` — Ada finished first | Same answer |
| Jev | `B` — Ada finished first | `B` — Ada finished first | Same answer |
| Microsoft Decision-1 | `B` — Ada finished first | `B` — Ada finished first | Same answer |
| Clef | `B` — Ada finished first | `B` — Ada finished first | Same answer |
| Luna Decisions | `B` — Ada finished first | `B` — Ada finished first | Same answer |
| Clef Flash | `B` — Ada finished first | `B` — Ada finished first | Same answer |
| Strands Decider | `B` — Ada finished first | `B` — Ada finished first | Same answer |
| GLiNER2.5 Decide | `C` — Ana finished first | `A` — Mel finished first | Different answer |
| Laya | `C` — Ana finished first | `A` — Mel finished first | Different answer |
| CalDec v1 | `A` — Mel finished first | `A` — Mel finished first | Same answer |

Clef and Clef Flash sort answer choices in their published input-processing code. Their choice-order results describe that preprocessing.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `bbh/7a4ef7acc0410ad0381a/option_order/reverse`

**Input fingerprint:** `c933b61cbc92a84bc99c8d56355871082bb2caefd60179659d4c46cd14a276bb`

| Change | Recorded version |
| --- | --- |
| Option order | Reverse the answer choices |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/relations/bbh-7a4ef7acc0410ad0381a.md).
