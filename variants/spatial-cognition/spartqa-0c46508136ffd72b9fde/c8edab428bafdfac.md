# Unrelated examples · Add examples unrelated to the question variant

[Original question](../../../questions/spatial-cognition/spartqa-0c46508136ffd72b9fde.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Capitalization: harbor → Harbor
>
> We have two blocks. Lets call them A and B. Block A contains one small black circle, a small black triangle and a medium black circle. The small black circle is to the left of the medium black circle. Near to the medium black circle there is the small black triangle. To the left of the black shape which is near to the medium black circle is the small black circle. To the left of block A there is block B. It contains one big yellow circle, a medium black triangle and one big yellow triangle. The big yellow circle is below the big yellow triangle. The medium black triangle is above and to the left of the big yellow triangle.

## Question

> Which object is to the left of a small black circle? the big yellow circle or the medium black triangle?

## Answer choices

- **0.** the big yellow circle
- **1.** the medium black triangle
- **2.** both of them
- **3.** none of them

**Reference answer:** `2`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Capitalization: harbor → Harbor\n\nWe have two blocks. Lets call them A and B. Block A contains one small black circle, a small black triangle and a medium black circle. The small black circle is to the left of the medium black circle. Near to the medium black circle there is the small black triangle. To the left of the black shape which is near to the medium black circle is the small black circle. To the left of block A there is block B. It contains one big yellow circle, a medium black triangle and one big yellow triangle. The big yellow circle is below the big yellow triangle. The medium black triangle is above and to the left of the big yellow triangle.",
  "question": "Which object is to the left of a small black circle? the big yellow circle or the medium black triangle?",
  "choices": {
    "0": "the big yellow circle ",
    "1": "the medium black triangle ",
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
| Luna Decisions | `3` — none of them | `3` — none of them | Same answer |
| Clef Flash | `0` — the big yellow circle  | `0` — the big yellow circle  | Same answer |
| Strands Decider | `0` — the big yellow circle  | `2` — both of them | Different answer |
| GLiNER2.5 Decide | `1` — the medium black triangle  | `1` — the medium black triangle  | Same answer |
| Laya | `0` — the big yellow circle  | `2` — both of them | Different answer |
| CalDec v1 | `1` — the medium black triangle  | `1` — the medium black triangle  | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `spartqa/0c46508136ffd72b9fde/examples/irrelevant/clean-source_first_spartqa_short_contexts_full_0136`

**Input fingerprint:** `ae334e183a0d6b61196b39459fe26d7bdb5bf0629f6ac17ef8a6b6bc5120c9f9`

| Change | Recorded version |
| --- | --- |
| Unrelated examples | Add examples unrelated to the question |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/spatial-cognition/spartqa-0c46508136ffd72b9fde.md).
