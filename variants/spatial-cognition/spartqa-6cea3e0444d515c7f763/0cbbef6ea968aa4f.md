# Invented names · Use invented names variant

[Original question](../../../questions/spatial-cognition/spartqa-6cea3e0444d515c7f763.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> There are two blocks, Varelin and Zorven. Block Varelin is below Zorven. Block Varelin has a medium black diamond. Block Zorven contains one big yellow oval and a little black diamond. There is also one big blue oval touching the bottom edge of this block. A big blue rectangle is to the right side of, close to and on the top of the big blue oval. Below and to the left of the little black diamond there is the big yellow oval. The little black diamond is touching the right side edge of this block.

## Question

> What is the relation between the medium shape and the big blue shape that is on the top of a big blue oval which is touching the bottom edge of a block?

## Answer choices

- **0.** left
- **1.** right
- **2.** top
- **3.** below
- **4.** close to
- **5.** far from
- **6.** touching
- **7.** DK

**Reference answer:** `3`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "There are two blocks, Varelin and Zorven. Block Varelin is below Zorven. Block Varelin has a medium black diamond. Block Zorven contains one big yellow oval and a little black diamond. There is also one big blue oval touching the bottom edge of this block. A big blue rectangle is to the right side of, close to and on the top of the big blue oval. Below and to the left of the little black diamond there is the big yellow oval. The little black diamond is touching the right side edge of this block.",
  "question": "What is the relation between the medium shape and the big blue shape that is on the top of a big blue oval which is touching the bottom edge of a block?",
  "choices": {
    "0": "left",
    "1": "right",
    "2": "top",
    "3": "below",
    "4": "close to",
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
| GLiDE v1.2 | `3` — below | `3` — below | Same answer |
| Decider v1.1 | `3` — below | `3` — below | Same answer |
| Jev | `0` — left | `0` — left | Same answer |
| Microsoft Decision-1 | `3` — below | `3` — below | Same answer |
| Clef | `5` — far from | `5` — far from | Same answer |
| Luna Decisions | `0` — left | `1` — right | Different answer |
| Clef Flash | `5` — far from | `5` — far from | Same answer |
| Strands Decider | `3` — below | `3` — below | Same answer |
| GLiNER2.5 Decide | `6` — touching | `6` — touching | Same answer |
| Laya | `1` — right | `3` — below | Different answer |
| CalDec v1 | `3` — below | `3` — below | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `spartqa/6cea3e0444d515c7f763/unfamiliar_names/invented`

**Input fingerprint:** `af8c49e3bc331e28132a94e154d95984632d57de51783e47014925457b9ecb1b`

| Change | Recorded version |
| --- | --- |
| Invented names | Use invented names |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/spatial-cognition/spartqa-6cea3e0444d515c7f763.md).
