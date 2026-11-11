# Option order · Move the first answer choice to the end variant

[Original question](../../../questions/numerical-cognition/bbh-afeb6667e2440f103e40.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** answer choices or their order.

[How the edits were constructed](../../../docs/variant-methods.md)

## Question

> ((0 \* -4 - -7 \* 5) + (-4 \* 0 + 6 + 0)) =

## Answer choices

- **B.** 1
- **C.** 41
- **D.** -35
- **A.** 0

**Reference answer:** `C`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "",
  "question": "((0 * -4 - -7 * 5) + (-4 * 0 + 6 + 0)) =",
  "choices": {
    "B": "1",
    "C": "41",
    "D": "-35",
    "A": "0"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `C` — 41 | `C` — 41 | Same answer |
| Decider v1.1 | `C` — 41 | `C` — 41 | Same answer |
| Jev | `C` — 41 | `C` — 41 | Same answer |
| Microsoft Decision-1 | `C` — 41 | `C` — 41 | Same answer |
| Clef | `C` — 41 | `C` — 41 | Same answer |
| Luna Decisions | `C` — 41 | `C` — 41 | Same answer |
| Clef Flash | `B` — 1 | `B` — 1 | Same answer |
| Strands Decider | `C` — 41 | `C` — 41 | Same answer |
| GLiNER2.5 Decide | `A` — 0 | `B` — 1 | Different answer |
| Laya | `A` — 0 | `A` — 0 | Same answer |
| CalDec v1 | `A` — 0 | `A` — 0 | Same answer |

Clef and Clef Flash sort answer choices in their published input-processing code. Their choice-order results describe that preprocessing.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `bbh/afeb6667e2440f103e40/option_order/rotate_1`

**Input fingerprint:** `41e3e76e677f67568818886894277e798fa1752408aac219de9bdbb5ca02e9ec`

| Change | Recorded version |
| --- | --- |
| Option order | Move the first answer choice to the end |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/numerical-cognition/bbh-afeb6667e2440f103e40.md).
