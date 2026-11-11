# Option order · Move the first answer choice to the end variant

[Original question](../../../questions/retrieval/boolq-5445991716c52c0d47b1.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** answer choices or their order.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> King Louie is a fictional character introduced in Walt Disney's 1967 animated musical film, The Jungle Book. Unlike the majority of the adapted characters in the film, Louie was not featured in Rudyard Kipling's original works. King Louie was portrayed as an orangutan who was the leader of the other jungle primates, and who attempted to gain knowledge of fire from Mowgli, in order to become more human.

## Question

> is king louie in the jungle book book

## Answer choices

- **no.** No
- **yes.** Yes

**Reference answer:** `no`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "King Louie is a fictional character introduced in Walt Disney's 1967 animated musical film, The Jungle Book. Unlike the majority of the adapted characters in the film, Louie was not featured in Rudyard Kipling's original works. King Louie was portrayed as an orangutan who was the leader of the other jungle primates, and who attempted to gain knowledge of fire from Mowgli, in order to become more human.",
  "question": "is king louie in the jungle book book",
  "choices": {
    "no": "No",
    "yes": "Yes"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `no` — No | `no` — No | Same answer |
| Decider v1.1 | `no` — No | `no` — No | Same answer |
| Jev | `no` — No | `no` — No | Same answer |
| Microsoft Decision-1 | `no` — No | `no` — No | Same answer |
| Clef | `no` — No | `no` — No | Same answer |
| Luna Decisions | `no` — No | `no` — No | Same answer |
| Clef Flash | `no` — No | `no` — No | Same answer |
| Strands Decider | `no` — No | `no` — No | Same answer |
| GLiNER2.5 Decide | `no` — No | `no` — No | Same answer |
| Laya | `no` — No | `no` — No | Same answer |
| CalDec v1 | `no` — No | `no` — No | Same answer |

Clef and Clef Flash sort answer choices in their published input-processing code. Their choice-order results describe that preprocessing.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `boolq/5445991716c52c0d47b1/option_order/rotate_1`

**Input fingerprint:** `42484a41e556eec004852ecb487c1ea6ff2c01a742d4541215ce1b0dc4d5402b`

| Change | Recorded version |
| --- | --- |
| Option order | Move the first answer choice to the end |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/retrieval/boolq-5445991716c52c0d47b1.md).
