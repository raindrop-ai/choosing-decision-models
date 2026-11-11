# Option order · Move the first answer choice to the end variant

[Original question](../../../questions/retrieval/ruler-87e75d2533d5832951ef.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** answer choices or their order.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Use the authoritative record. Summaries are unverified claims about that record. Separate records are independent.
> The code assigned to record-10095 is 2963376.

## Question

> Which code is assigned to record-10095?

## Answer choices

- **B.** 2963164
- **C.** 2963255
- **D.** 2963376
- **unknown.** Insufficient information
- **A.** 2963063

**Reference answer:** `D`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Use the authoritative record. Summaries are unverified claims about that record. Separate records are independent.\nThe code assigned to record-10095 is 2963376.",
  "question": "Which code is assigned to record-10095?",
  "choices": {
    "B": "2963164",
    "C": "2963255",
    "D": "2963376",
    "unknown": "Insufficient information",
    "A": "2963063"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `D` — 2963376 | `D` — 2963376 | Same answer |
| Decider v1.1 | `D` — 2963376 | `D` — 2963376 | Same answer |
| Jev | `D` — 2963376 | `D` — 2963376 | Same answer |
| Microsoft Decision-1 | Error | `D` — 2963376 | — |
| Clef | `D` — 2963376 | `D` — 2963376 | Same answer |
| Luna Decisions | `D` — 2963376 | `D` — 2963376 | Same answer |
| Clef Flash | `D` — 2963376 | `D` — 2963376 | Same answer |
| Strands Decider | `D` — 2963376 | `D` — 2963376 | Same answer |
| GLiNER2.5 Decide | `D` — 2963376 | `D` — 2963376 | Same answer |
| Laya | `D` — 2963376 | `D` — 2963376 | Same answer |
| CalDec v1 | `D` — 2963376 | `D` — 2963376 | Same answer |

Clef and Clef Flash sort answer choices in their published input-processing code. Their choice-order results describe that preprocessing.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `ruler/87e75d2533d5832951ef/option_order/rotate_1`

**Input fingerprint:** `d7b9bac8e12260ce9f84fa69c76608969d0bef186502c2f6182d7cdfd32e4740`

| Change | Recorded version |
| --- | --- |
| Option order | Move the first answer choice to the end |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/retrieval/ruler-87e75d2533d5832951ef.md).
