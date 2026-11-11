# Option order · Move the first answer choice to the end variant

[Original question](../../../questions/concepts-and-categorization/mmlu-444ad26b7aa6304eed26.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** answer choices or their order.

[How the edits were constructed](../../../docs/variant-methods.md)

## Question

> Once a train pulls out of a station, or an aeroplane takes off or a film starts, those seats are lost and can never be sold. This is referred to as:

## Answer choices

- **B.** Variability.
- **C.** Intangibility.
- **D.** Perishability.
- **A.** Inseparability.

**Reference answer:** `D`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "",
  "question": "Once a train pulls out of a station, or an aeroplane takes off or a film starts, those seats are lost and can never be sold. This is referred to as:",
  "choices": {
    "B": "Variability.",
    "C": "Intangibility.",
    "D": "Perishability.",
    "A": "Inseparability."
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
| GLiNER2.5 Decide | `D` — Perishability. | `D` — Perishability. | Same answer |
| Laya | `A` — Inseparability. | `A` — Inseparability. | Same answer |
| CalDec v1 | `A` — Inseparability. | `A` — Inseparability. | Same answer |

Clef and Clef Flash sort answer choices in their published input-processing code. Their choice-order results describe that preprocessing.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `mmlu/444ad26b7aa6304eed26/option_order/rotate_1`

**Input fingerprint:** `3f3b0bdde0f567147e778233e777be51aa1aaaf47970ea1fa972b7a90fa66b67`

| Change | Recorded version |
| --- | --- |
| Option order | Move the first answer choice to the end |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/concepts-and-categorization/mmlu-444ad26b7aa6304eed26.md).
