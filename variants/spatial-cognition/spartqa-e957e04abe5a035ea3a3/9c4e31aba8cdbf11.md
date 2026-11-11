# Option order · Reverse the answer choices variant

[Original question](../../../questions/spatial-cognition/spartqa-e957e04abe5a035ea3a3.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** answer choices or their order.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> There are three blocks. We call them A, B and C. Block A is above B. Block B is to the right of C. Block A contains one medium yellow square. Block B contains a medium black square. A medium blue square is below the medium black square. Block C contains two medium yellow squares. Medium yellow square number one is below medium yellow square number two.. A medium blue square is below medium yellow square number one and medium yellow square number two.

## Question

> Which object is to the left of a medium blue square? the medium yellow square that is in block A or medium yellow square number one?

## Answer choices

- **3.** none of them
- **2.** both of them
- **1.** medium yellow square  number one
- **0.** the medium yellow square  that is in block A

**Reference answer:** `1`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "There are three blocks. We call them A, B and C. Block A is above B. Block B is to the right of C. Block A contains one medium yellow square. Block B contains a medium black square. A medium blue square is below the medium black square. Block C contains two medium yellow squares. Medium yellow square number one is below medium yellow square number two.. A medium blue square is below medium yellow square number one and medium yellow square number two.",
  "question": "Which object is to the left of a medium blue square? the medium yellow square that is in block A or medium yellow square number one?",
  "choices": {
    "3": "none of them",
    "2": "both of them",
    "1": "medium yellow square  number one",
    "0": "the medium yellow square  that is in block A"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `1` — medium yellow square  number one | `1` — medium yellow square  number one | Same answer |
| Decider v1.1 | `1` — medium yellow square  number one | `1` — medium yellow square  number one | Same answer |
| Jev | `1` — medium yellow square  number one | `1` — medium yellow square  number one | Same answer |
| Microsoft Decision-1 | `1` — medium yellow square  number one | `1` — medium yellow square  number one | Same answer |
| Clef | `2` — both of them | `2` — both of them | Same answer |
| Luna Decisions | `3` — none of them | `3` — none of them | Same answer |
| Clef Flash | `1` — medium yellow square  number one | `1` — medium yellow square  number one | Same answer |
| Strands Decider | `1` — medium yellow square  number one | `1` — medium yellow square  number one | Same answer |
| GLiNER2.5 Decide | `1` — medium yellow square  number one | `1` — medium yellow square  number one | Same answer |
| Laya | `2` — both of them | `2` — both of them | Same answer |
| CalDec v1 | `2` — both of them | `2` — both of them | Same answer |

Clef and Clef Flash sort answer choices in their published input-processing code. Their choice-order results describe that preprocessing.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `spartqa/e957e04abe5a035ea3a3/option_order/reverse`

**Input fingerprint:** `9fa135f44d91bcea90d05f7a7da2acaaf33e918c55cc5286b44b16d18d061ae1`

| Change | Recorded version |
| --- | --- |
| Option order | Reverse the answer choices |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/spatial-cognition/spartqa-e957e04abe5a035ea3a3.md).
