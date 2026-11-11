# Option order · Move the first answer choice to the end variant

[Original question](../../../questions/retrieval/babi-9402ed5547bab520026c.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** answer choices or their order.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> John travelled to the bathroom.
> Daniel went to the hallway.
> John moved to the kitchen.
> Mary journeyed to the kitchen.
> Daniel travelled to the bathroom.
> John travelled to the bathroom.
> Daniel went to the garden.
> Sandra travelled to the hallway.

## Question

> Where is Sandra? 

## Answer choices

- **B.** garden
- **C.** hallway
- **D.** bathroom
- **E.** kitchen
- **F.** bedroom
- **A.** office

**Reference answer:** `C`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "John travelled to the bathroom.\nDaniel went to the hallway.\nJohn moved to the kitchen.\nMary journeyed to the kitchen.\nDaniel travelled to the bathroom.\nJohn travelled to the bathroom.\nDaniel went to the garden.\nSandra travelled to the hallway.",
  "question": "Where is Sandra? ",
  "choices": {
    "B": "garden",
    "C": "hallway",
    "D": "bathroom",
    "E": "kitchen",
    "F": "bedroom",
    "A": "office"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `C` — hallway | `C` — hallway | Same answer |
| Decider v1.1 | `C` — hallway | `C` — hallway | Same answer |
| Jev | `C` — hallway | `C` — hallway | Same answer |
| Microsoft Decision-1 | `C` — hallway | `C` — hallway | Same answer |
| Clef | `C` — hallway | `C` — hallway | Same answer |
| Luna Decisions | `C` — hallway | `C` — hallway | Same answer |
| Clef Flash | `C` — hallway | `C` — hallway | Same answer |
| Strands Decider | `C` — hallway | `C` — hallway | Same answer |
| GLiNER2.5 Decide | `C` — hallway | `C` — hallway | Same answer |
| Laya | `C` — hallway | `C` — hallway | Same answer |
| CalDec v1 | `C` — hallway | `C` — hallway | Same answer |

Clef and Clef Flash sort answer choices in their published input-processing code. Their choice-order results describe that preprocessing.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `babi/9402ed5547bab520026c/option_order/rotate_1`

**Input fingerprint:** `3a1d240ff74b67d90a0761c1963eb9dc25347fb504bbb40431d8ae11f0c68037`

| Change | Recorded version |
| --- | --- |
| Option order | Move the first answer choice to the end |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/retrieval/babi-9402ed5547bab520026c.md).
