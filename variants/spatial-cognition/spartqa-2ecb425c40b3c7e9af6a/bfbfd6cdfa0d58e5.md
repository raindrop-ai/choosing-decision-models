# Invented names · Use familiar names variant

[Original question](../../../questions/spatial-cognition/spartqa-2ecb425c40b3c7e9af6a.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> There are three blocks, Apple, Bridge and Castle. Block Apple contains a large blue rectangle and one small white diamond. The large blue rectangle is to the right side of the small white diamond. Then, we have block Bridge with a midsize blue diamond and a large white circle in it. The large white circle is touching the bottom edge of this block. The midsize blue diamond is touching the bottom edge of this block. It is to the right side of the large white circle. Block Castle is to the left side of block Apple and on the top of block Bridge. It contains one small blue circle. To the left side of and under the small blue circle there is a midsize red rectangle.

## Question

> What is the relation between the large blue rectangle and the small shape that is to the right side of a blue circle?

## Answer choices

- **0.** left
- **1.** right
- **2.** top
- **3.** under
- **4.** close to
- **5.** far from
- **6.** touching
- **7.** DK

**Reference answer:** `1`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "There are three blocks, Apple, Bridge and Castle. Block Apple contains a large blue rectangle and one small white diamond. The large blue rectangle is to the right side of the small white diamond. Then, we have block Bridge with a midsize blue diamond and a large white circle in it. The large white circle is touching the bottom edge of this block. The midsize blue diamond is touching the bottom edge of this block. It is to the right side of the large white circle. Block Castle is to the left side of block Apple and on the top of block Bridge. It contains one small blue circle. To the left side of and under the small blue circle there is a midsize red rectangle.",
  "question": "What is the relation between the large blue rectangle and the small shape that is to the right side of a blue circle?",
  "choices": {
    "0": "left",
    "1": "right",
    "2": "top",
    "3": "under",
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
| GLiDE v1.2 | `1` — right | `1` — right | Same answer |
| Decider v1.1 | `1` — right | `1` — right | Same answer |
| Jev | `1` — right | `1` — right | Same answer |
| Microsoft Decision-1 | `1` — right | `1` — right | Same answer |
| Clef | `5` — far from | `5` — far from | Same answer |
| Luna Decisions | `7` — DK | `7` — DK | Same answer |
| Clef Flash | `5` — far from | `5` — far from | Same answer |
| Strands Decider | `1` — right | `1` — right | Same answer |
| GLiNER2.5 Decide | `1` — right | `1` — right | Same answer |
| Laya | `3` — under | `3` — under | Same answer |
| CalDec v1 | `3` — under | `2` — top | Different answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `spartqa/2ecb425c40b3c7e9af6a/unfamiliar_names/familiar`

**Input fingerprint:** `3ee0ca4bce8312f71bd834f51ea3a11a03979d02bc2a1a3b9330dd65a3eed986`

| Change | Recorded version |
| --- | --- |
| Invented names | Use familiar names |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/spatial-cognition/spartqa-2ecb425c40b3c7e9af6a.md).
