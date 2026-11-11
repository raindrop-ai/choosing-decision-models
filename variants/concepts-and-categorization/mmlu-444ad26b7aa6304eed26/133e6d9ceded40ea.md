# Similar distractors · Add more similar but irrelevant items variant

[Original question](../../../questions/concepts-and-categorization/mmlu-444ad26b7aa6304eed26.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> «In a separate fictional warehouse, unsold metal bolts remain stored on a shelf for sale the following month.»
>
> «In another fictional service record, two visits by a technician differ in the time spent and the equipment used.»
>
> «In a third fictional booking record, an unused appointment ends at noon while a separate physical voucher remains in a drawer.»

## Question

> Once a train pulls out of a station, or an aeroplane takes off or a film starts, those seats are lost and can never be sold. This is referred to as:

## Answer choices

- **A.** Inseparability.
- **B.** Variability.
- **C.** Intangibility.
- **D.** Perishability.

**Reference answer:** `D`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "«In a separate fictional warehouse, unsold metal bolts remain stored on a shelf for sale the following month.»\n\n«In another fictional service record, two visits by a technician differ in the time spent and the equipment used.»\n\n«In a third fictional booking record, an unused appointment ends at noon while a separate physical voucher remains in a drawer.»",
  "question": "Once a train pulls out of a station, or an aeroplane takes off or a film starts, those seats are lost and can never be sold. This is referred to as:",
  "choices": {
    "A": "Inseparability.",
    "B": "Variability.",
    "C": "Intangibility.",
    "D": "Perishability."
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `D` — Perishability. | `D` — Perishability. | Same answer |
| Decider v1.1 | `D` — Perishability. | `D` — Perishability. | Same answer |
| Jev | `D` — Perishability. | `D` — Perishability. | Same answer |
| Microsoft Decision-1 | `D` — Perishability. | `D` — Perishability. | Same answer |
| Clef | `D` — Perishability. | `D` — Perishability. | Same answer |
| Luna Decisions | `D` — Perishability. | `D` — Perishability. | Same answer |
| Clef Flash | `D` — Perishability. | `D` — Perishability. | Same answer |
| Strands Decider | `D` — Perishability. | `D` — Perishability. | Same answer |
| GLiNER2.5 Decide | `D` — Perishability. | `B` — Variability. | Different answer |
| Laya | `A` — Inseparability. | `B` — Variability. | Different answer |
| CalDec v1 | `A` — Inseparability. | `B` — Variability. | Different answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `mmlu/444ad26b7aa6304eed26/similar_distractors/high/clean-source_first_parallel_b_near_accounts_0301`

**Input fingerprint:** `bf60529b722532c583fd63f0006d8f0fe0ac91bff93dc2879e054fb2b5046d36`

| Change | Recorded version |
| --- | --- |
| Similar distractors | Add more similar but irrelevant items |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/concepts-and-categorization/mmlu-444ad26b7aa6304eed26.md).
