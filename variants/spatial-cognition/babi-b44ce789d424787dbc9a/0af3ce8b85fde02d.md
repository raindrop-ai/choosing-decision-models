# Option order · Move the first answer choice to the end variant

[Original question](../../../questions/spatial-cognition/babi-b44ce789d424787dbc9a.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** answer choices or their order.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> The red square is below the yellow square.
> The pink rectangle is above the yellow square.

## Question

> Is the pink rectangle below the red square?

## Answer choices

- **no.** no
- **yes.** yes

**Reference answer:** `no`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "The red square is below the yellow square.\nThe pink rectangle is above the yellow square.",
  "question": "Is the pink rectangle below the red square?",
  "choices": {
    "no": "no",
    "yes": "yes"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `no` — no | `no` — no | Same answer |
| Decider v1.1 | `no` — no | `no` — no | Same answer |
| Jev | `no` — no | `no` — no | Same answer |
| Microsoft Decision-1 | `no` — no | `no` — no | Same answer |
| Clef | `no` — no | `no` — no | Same answer |
| Luna Decisions | `no` — no | `no` — no | Same answer |
| Clef Flash | `no` — no | `no` — no | Same answer |
| Strands Decider | `no` — no | `no` — no | Same answer |
| GLiNER2.5 Decide | `yes` — yes | `yes` — yes | Same answer |
| Laya | `no` — no | `no` — no | Same answer |
| CalDec v1 | `no` — no | `no` — no | Same answer |

Clef and Clef Flash sort answer choices in their published input-processing code. Their choice-order results describe that preprocessing.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `babi/b44ce789d424787dbc9a/option_order/rotate_1`

**Input fingerprint:** `a2cd08993112d56b0d564ef67c223e90c2ebd7010ff1b0d5abb9cf43a5f4149c`

| Change | Recorded version |
| --- | --- |
| Option order | Move the first answer choice to the end |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/spatial-cognition/babi-b44ce789d424787dbc9a.md).
