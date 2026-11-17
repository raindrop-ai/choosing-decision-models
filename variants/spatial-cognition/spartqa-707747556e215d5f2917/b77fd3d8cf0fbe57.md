# Invented names · Use familiar names variant

[Original question](../../../questions/spatial-cognition/spartqa-707747556e215d5f2917.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> There are three blocks, Apple, Bridge and Castle. Block Castle is to the right of and Bridge is to the left of Apple. Block Apple has a medium black circle. Block Bridge has a medium blue square. Block Castle has one medium blue circle, one small black triangle and a small yellow triangle. The medium blue circle is touching the right edge of this block. To the left of and below the small yellow triangle is the small black triangle. The medium blue circle is to the right of the small yellow triangle. It is above the small black triangle.

## Question

> Which object is to the right of a square? the small yellow triangle or the small black triangle?

## Answer choices

- **0.** the small yellow triangle
- **1.** the small black triangle
- **2.** both of them
- **3.** none of them

**Reference answer:** `2`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "There are three blocks, Apple, Bridge and Castle. Block Castle is to the right of and Bridge is to the left of Apple. Block Apple has a medium black circle. Block Bridge has a medium blue square. Block Castle has one medium blue circle, one small black triangle and a small yellow triangle. The medium blue circle is touching the right edge of this block. To the left of and below the small yellow triangle is the small black triangle. The medium blue circle is to the right of the small yellow triangle. It is above the small black triangle.",
  "question": "Which object is to the right of a square? the small yellow triangle or the small black triangle?",
  "choices": {
    "0": "the small yellow triangle ",
    "1": "the small black triangle ",
    "2": "both of them",
    "3": "none of them"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `2` — both of them | `2` — both of them | Same answer |
| Decider v1.1 | `2` — both of them | `2` — both of them | Same answer |
| Jev | `2` — both of them | `2` — both of them | Same answer |
| Microsoft Decision-1 | `2` — both of them | `2` — both of them | Same answer |
| Clef | `2` — both of them | `2` — both of them | Same answer |
| Luna Decisions | `0` — the small yellow triangle  | `3` — none of them | Different answer |
| Clef Flash | `2` — both of them | `2` — both of them | Same answer |
| Strands Decider | `2` — both of them | `0` — the small yellow triangle  | Different answer |
| GLiNER2.5 Decide | `1` — the small black triangle  | `1` — the small black triangle  | Same answer |
| Laya | `2` — both of them | `2` — both of them | Same answer |
| CalDec v1 | `1` — the small black triangle  | `2` — both of them | Different answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `spartqa/707747556e215d5f2917/unfamiliar_names/familiar`

**Input fingerprint:** `4b69a97bec856063a0d0772a44e24a849d948d47975d897f0bfb3ffb5b525699`

| Change | Recorded version |
| --- | --- |
| Invented names | Use familiar names |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/spatial-cognition/spartqa-707747556e215d5f2917.md).
