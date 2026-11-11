# Extra events · Add 6 unrelated events variant

[Original question](../../../questions/spatial-cognition/spartqa-6c05ff04dd2cb220408a.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Nolan is the editor of a poetry catalog. Its entries are Virel, Zorven, Kesil, Nereth, Pavrel, and Sovrin.
> Nolan classifies Virel as a dialogue. Nolan classifies Zorven as a monologue. Nolan classifies Kesil as an elegy. Nolan classifies Nereth as a satire. Nolan classifies Pavrel as a fable. Nolan classifies Sovrin as a ballad.
>
> We have three blocks. We call them A, B and C. Block A is below and C is to the left of B. Block A has one big blue triangle. Block B contains a small black square and a small blue square. One small blue triangle is also touching the right edge of this block. Below the small blue triangle is the small black square. To the left of and above the small blue triangle there is the small blue square. Block C has one small blue square.

## Question

> What is the relation between the small blue triangle that is below a small blue shape and the big thing?

## Answer choices

- **0.** left
- **1.** right
- **2.** above
- **3.** below
- **4.** near to
- **5.** far from
- **6.** touching
- **7.** DK

**Reference answer:** `2`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Nolan is the editor of a poetry catalog. Its entries are Virel, Zorven, Kesil, Nereth, Pavrel, and Sovrin.\nNolan classifies Virel as a dialogue. Nolan classifies Zorven as a monologue. Nolan classifies Kesil as an elegy. Nolan classifies Nereth as a satire. Nolan classifies Pavrel as a fable. Nolan classifies Sovrin as a ballad.\n\nWe have three blocks. We call them A, B and C. Block A is below and C is to the left of B. Block A has one big blue triangle. Block B contains a small black square and a small blue square. One small blue triangle is also touching the right edge of this block. Below the small blue triangle is the small black square. To the left of and above the small blue triangle there is the small blue square. Block C has one small blue square.",
  "question": "What is the relation between the small blue triangle that is below a small blue shape and the big thing?",
  "choices": {
    "0": "left",
    "1": "right",
    "2": "above",
    "3": "below",
    "4": "near to",
    "5": "far from",
    "6": "touching",
    "7": "DK"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `2` — above | `2` — above | Same answer |
| Decider v1.1 | `2` — above | `2` — above | Same answer |
| Jev | `1` — right | `1` — right | Same answer |
| Microsoft Decision-1 | `2` — above | `2` — above | Same answer |
| Clef | `5` — far from | `5` — far from | Same answer |
| Luna Decisions | `3` — below | `3` — below | Same answer |
| Clef Flash | `5` — far from | `5` — far from | Same answer |
| Strands Decider | `3` — below | `3` — below | Same answer |
| GLiNER2.5 Decide | `6` — touching | `6` — touching | Same answer |
| Laya | `2` — above | `6` — touching | Different answer |
| CalDec v1 | `2` — above | `2` — above | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `spartqa/6c05ff04dd2cb220408a/event_count/6/clean-source_first_spartqa_short_contexts_full_0136`

**Input fingerprint:** `af7f69eeae4a8c186365b48a7b83e239c88498a80c371df3117375bbddede9b9`

| Change | Recorded version |
| --- | --- |
| Extra events | Add 6 unrelated events |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/spatial-cognition/spartqa-6c05ff04dd2cb220408a.md).
