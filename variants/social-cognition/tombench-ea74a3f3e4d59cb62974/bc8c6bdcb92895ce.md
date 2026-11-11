# Option order · Move the first answer choice to the end variant

[Original question](../../../questions/social-cognition/tombench-ea74a3f3e4d59cb62974.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** answer choices or their order.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Liu Jing finds that her best friend Zhang Hong does not invite her to the birthday party.

## Question

> What emotion does Liu Jing possibly have?

## Answer choices

- **B.** Disappointed
- **C.** Ashamed
- **D.** Contempt
- **A.** Embarrassed

**Reference answer:** `B`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Liu Jing finds that her best friend Zhang Hong does not invite her to the birthday party.",
  "question": "What emotion does Liu Jing possibly have?",
  "choices": {
    "B": "Disappointed",
    "C": "Ashamed",
    "D": "Contempt",
    "A": "Embarrassed"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `B` — Disappointed | `B` — Disappointed | Same answer |
| Decider v1.1 | `B` — Disappointed | `B` — Disappointed | Same answer |
| Jev | `B` — Disappointed | `B` — Disappointed | Same answer |
| Microsoft Decision-1 | `B` — Disappointed | `B` — Disappointed | Same answer |
| Clef | `B` — Disappointed | `B` — Disappointed | Same answer |
| Luna Decisions | `B` — Disappointed | `B` — Disappointed | Same answer |
| Clef Flash | `B` — Disappointed | `B` — Disappointed | Same answer |
| Strands Decider | `B` — Disappointed | `B` — Disappointed | Same answer |
| GLiNER2.5 Decide | `B` — Disappointed | `B` — Disappointed | Same answer |
| Laya | `A` — Embarrassed | `B` — Disappointed | Different answer |
| CalDec v1 | `B` — Disappointed | `B` — Disappointed | Same answer |

Clef and Clef Flash sort answer choices in their published input-processing code. Their choice-order results describe that preprocessing.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `tombench/ea74a3f3e4d59cb62974/option_order/rotate_1`

**Input fingerprint:** `1069764a7db74ae6c2055d7164b38cab3c00db8f1cbb1cee085af739ef2879d8`

| Change | Recorded version |
| --- | --- |
| Option order | Move the first answer choice to the end |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/social-cognition/tombench-ea74a3f3e4d59cb62974.md).
