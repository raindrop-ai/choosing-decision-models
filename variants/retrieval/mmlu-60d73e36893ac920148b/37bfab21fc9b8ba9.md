# Option order · Move the first answer choice to the end variant

[Original question](../../../questions/retrieval/mmlu-60d73e36893ac920148b.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** answer choices or their order.

[How the edits were constructed](../../../docs/variant-methods.md)

## Question

>  When customers assess prices, they estimate value using \_\_\_\_\_\_\_\_\_\_, because they do not always know the true cost and price of the item that they are purchasing. These pricing cues include: sale signs; odd-number pricing; the purchase context; and price bundling and rebates.

## Answer choices

- **B.** Sale price.
- **C.** Pricing cues.
- **D.** Pricing bundles.
- **A.** Pricing strategies.

**Reference answer:** `C`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "",
  "question": " When customers assess prices, they estimate value using __________, because they do not always know the true cost and price of the item that they are purchasing. These pricing cues include: sale signs; odd-number pricing; the purchase context; and price bundling and rebates.",
  "choices": {
    "B": "Sale price.",
    "C": "Pricing cues.",
    "D": "Pricing bundles.",
    "A": "Pricing strategies."
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `C` — Pricing cues. | `C` — Pricing cues. | Same answer |
| Decider v1.1 | `C` — Pricing cues. | `C` — Pricing cues. | Same answer |
| Jev | `C` — Pricing cues. | `C` — Pricing cues. | Same answer |
| Microsoft Decision-1 | `C` — Pricing cues. | `C` — Pricing cues. | Same answer |
| Clef | `C` — Pricing cues. | `C` — Pricing cues. | Same answer |
| Luna Decisions | `C` — Pricing cues. | `C` — Pricing cues. | Same answer |
| Clef Flash | `C` — Pricing cues. | `C` — Pricing cues. | Same answer |
| Strands Decider | `C` — Pricing cues. | `C` — Pricing cues. | Same answer |
| GLiNER2.5 Decide | `C` — Pricing cues. | `C` — Pricing cues. | Same answer |
| Laya | `C` — Pricing cues. | `C` — Pricing cues. | Same answer |
| CalDec v1 | `C` — Pricing cues. | `C` — Pricing cues. | Same answer |

Clef and Clef Flash sort answer choices in their published input-processing code. Their choice-order results describe that preprocessing.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `mmlu/60d73e36893ac920148b/option_order/rotate_1`

**Input fingerprint:** `70d8cc55951cdad9e601d4ec85993db5ab2ee1121c5520a3063a219763fc29ed`

| Change | Recorded version |
| --- | --- |
| Option order | Move the first answer choice to the end |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/retrieval/mmlu-60d73e36893ac920148b.md).
