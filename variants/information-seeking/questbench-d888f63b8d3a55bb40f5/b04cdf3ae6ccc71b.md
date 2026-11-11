# Option order · Move the first answer choice to the end variant

[Original question](../../../questions/information-seeking/questbench-d888f63b8d3a55bb40f5.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** answer choices or their order.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Jackie is trying to decide whether to do her taxes herself or hire an accountant. If she does the taxes herself, she'll be able to do 3 fewer hours of freelance work. The accountant charges $90. However, she also has a side hobby of painting. She has paintings ready to sell, but this will not affect her decision about the taxes. How much more money will she have if she hires the accountant?

## Question

> Which missing variable should be asked about to solve this problem?

## Answer choices

- **D.** per painting cost
- **E.** number of paintings
- **B.** freelance rate per hour

**Reference answer:** `B`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Jackie is trying to decide whether to do her taxes herself or hire an accountant. If she does the taxes herself, she'll be able to do 3 fewer hours of freelance work. The accountant charges $90. However, she also has a side hobby of painting. She has paintings ready to sell, but this will not affect her decision about the taxes. How much more money will she have if she hires the accountant?",
  "question": "Which missing variable should be asked about to solve this problem?",
  "choices": {
    "D": "per painting cost",
    "E": "number of paintings",
    "B": "freelance rate per hour"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `B` — freelance rate per hour | `B` — freelance rate per hour | Same answer |
| Decider v1.1 | `B` — freelance rate per hour | `B` — freelance rate per hour | Same answer |
| Jev | `B` — freelance rate per hour | `B` — freelance rate per hour | Same answer |
| Microsoft Decision-1 | `B` — freelance rate per hour | `B` — freelance rate per hour | Same answer |
| Clef | `B` — freelance rate per hour | `B` — freelance rate per hour | Same answer |
| Luna Decisions | `B` — freelance rate per hour | `B` — freelance rate per hour | Same answer |
| Clef Flash | `B` — freelance rate per hour | `B` — freelance rate per hour | Same answer |
| Strands Decider | `B` — freelance rate per hour | `B` — freelance rate per hour | Same answer |
| GLiNER2.5 Decide | `B` — freelance rate per hour | `B` — freelance rate per hour | Same answer |
| Laya | `B` — freelance rate per hour | `B` — freelance rate per hour | Same answer |
| CalDec v1 | `B` — freelance rate per hour | `B` — freelance rate per hour | Same answer |

Clef and Clef Flash sort answer choices in their published input-processing code. Their choice-order results describe that preprocessing.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `questbench/d888f63b8d3a55bb40f5/option_order/rotate_1`

**Input fingerprint:** `d92268f87490ce27fb31f3ddc48915300b6102b524ecab85b38cd3280b148820`

| Change | Recorded version |
| --- | --- |
| Option order | Move the first answer choice to the end |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/information-seeking/questbench-d888f63b8d3a55bb40f5.md).
