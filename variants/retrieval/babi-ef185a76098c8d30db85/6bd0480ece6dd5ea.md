# Option order · Move the first answer choice to the end variant

[Original question](../../../questions/retrieval/babi-ef185a76098c8d30db85.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** answer choices or their order.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Daniel went to the hallway.
> John travelled to the bathroom.
> Daniel moved to the bedroom.
> Daniel went to the bathroom.

## Question

> Where is John? 

## Answer choices

- **B.** hallway
- **C.** bedroom
- **D.** office
- **E.** garden
- **F.** kitchen
- **A.** bathroom

**Reference answer:** `A`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Daniel went to the hallway.\nJohn travelled to the bathroom.\nDaniel moved to the bedroom.\nDaniel went to the bathroom.",
  "question": "Where is John? ",
  "choices": {
    "B": "hallway",
    "C": "bedroom",
    "D": "office",
    "E": "garden",
    "F": "kitchen",
    "A": "bathroom"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `A` — bathroom | `A` — bathroom | Same answer |
| Decider v1.1 | `A` — bathroom | `A` — bathroom | Same answer |
| Jev | `A` — bathroom | `A` — bathroom | Same answer |
| Microsoft Decision-1 | `A` — bathroom | `A` — bathroom | Same answer |
| Clef | `A` — bathroom | `A` — bathroom | Same answer |
| Luna Decisions | `A` — bathroom | `A` — bathroom | Same answer |
| Clef Flash | `A` — bathroom | `A` — bathroom | Same answer |
| Strands Decider | `A` — bathroom | `A` — bathroom | Same answer |
| GLiNER2.5 Decide | `B` — hallway | `B` — hallway | Same answer |
| Laya | `A` — bathroom | `A` — bathroom | Same answer |
| CalDec v1 | `A` — bathroom | `A` — bathroom | Same answer |

Clef and Clef Flash sort answer choices in their published input-processing code. Their choice-order results describe that preprocessing.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `babi/ef185a76098c8d30db85/option_order/rotate_1`

**Input fingerprint:** `f47f014d16af5c26b2534c24630a75b44a73f05e8197b68cba507fbe62ec2ec7`

| Change | Recorded version |
| --- | --- |
| Option order | Move the first answer choice to the end |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/retrieval/babi-ef185a76098c8d30db85.md).
