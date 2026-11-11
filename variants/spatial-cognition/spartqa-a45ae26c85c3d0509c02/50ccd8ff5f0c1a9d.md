# Extra events · Add 2 unrelated events variant

[Original question](../../../questions/spatial-cognition/spartqa-a45ae26c85c3d0509c02.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Nolan is the editor of a poetry catalog. Its entries are Virel, Zorven, Kesil, Nereth, Pavrel, and Sovrin.
> Nolan classifies Virel as a dialogue. Nolan classifies Zorven as a monologue.
>
> There are three blocks. We call them A, B and C. Block B is to the left of A and block A is below C. Block A has a big blue triangle, one big yellow square and a medium blue triangle. The big blue triangle is below the big yellow square which is above, near to and to the left of the medium blue triangle. This block also has a big black square. This object is touching the right edge of this block. To the left of the medium blue triangle there is the big blue triangle. The big yellow square is touching the top edge of this block. Block B contains a small yellow circle, a small yellow square and a medium black circle. The small yellow circle is to the left of the medium black circle. The small yellow square is to the right of the medium black circle. It is touching the bottom edge of this block. The small yellow circle is above the small yellow square. The medium black circle is touching the bottom edge of this block. And block C contains one small blue circle.

## Question

> What is the relation between the small blue circle and the big triangle that is to the right of a small yellow square that is touching the bottom edge of a block?

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
  "state": "Nolan is the editor of a poetry catalog. Its entries are Virel, Zorven, Kesil, Nereth, Pavrel, and Sovrin.\nNolan classifies Virel as a dialogue. Nolan classifies Zorven as a monologue.\n\nThere are three blocks. We call them A, B and C. Block B is to the left of A and block A is below C. Block A has a big blue triangle, one big yellow square and a medium blue triangle. The big blue triangle is below the big yellow square which is above, near to and to the left of the medium blue triangle. This block also has a big black square. This object is touching the right edge of this block. To the left of the medium blue triangle there is the big blue triangle. The big yellow square is touching the top edge of this block. Block B contains a small yellow circle, a small yellow square and a medium black circle. The small yellow circle is to the left of the medium black circle. The small yellow square is to the right of the medium black circle. It is touching the bottom edge of this block. The small yellow circle is above the small yellow square. The medium black circle is touching the bottom edge of this block. And block C contains one small blue circle.",
  "question": "What is the relation between the small blue circle and the big triangle that is to the right of a small yellow square that is touching the bottom edge of a block?",
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
| Jev | `7` — DK | `7` — DK | Same answer |
| Microsoft Decision-1 | `2` — above | `2` — above | Same answer |
| Clef | `5` — far from | `2` — above | Different answer |
| Luna Decisions | `7` — DK | `7` — DK | Same answer |
| Clef Flash | `5` — far from | `5` — far from | Same answer |
| Strands Decider | `0` — left | `2` — above | Different answer |
| GLiNER2.5 Decide | `6` — touching | `6` — touching | Same answer |
| Laya | `3` — below | `3` — below | Same answer |
| CalDec v1 | `2` — above | `2` — above | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `spartqa/a45ae26c85c3d0509c02/event_count/2/clean-source_first_spartqa_short_contexts_full_0136`

**Input fingerprint:** `c5dc0bb25d41c7bfe2e8b26bf4614a491b0cc7c3904b02994b56bf5c8d974939`

| Change | Recorded version |
| --- | --- |
| Extra events | Add 2 unrelated events |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/spatial-cognition/spartqa-a45ae26c85c3d0509c02.md).
