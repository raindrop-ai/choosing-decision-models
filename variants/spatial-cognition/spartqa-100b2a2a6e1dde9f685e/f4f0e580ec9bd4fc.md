# Irrelevant details · Add a small amount of irrelevant detail variant

[Original question](../../../questions/spatial-cognition/spartqa-100b2a2a6e1dde9f685e.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> The notebook has a linen cover.
>
> There are three blocks called A, B, and C. B is to the right of A and C is to the right of B. In A, there is a small black triangle near and below a large yellow circle. Far to the right of the yellow circle is a small blue square. In B, there is a large black triangle far below a small blue circle. The small blue circle is near and below a small blue triangle. In C, there is a small blue circle.

## Question

> Is the small blue circle in B below a large black thing?

## Answer choices

- **Yes.** Yes
- **No.** No
- **DK.** DK

**Reference answer:** `No`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "The notebook has a linen cover.\n\nThere are three blocks called A, B, and C. B is to the right of A and C is to the right of B. In A, there is a small black triangle near and below a large yellow circle. Far to the right of the yellow circle is a small blue square. In B, there is a large black triangle far below a small blue circle. The small blue circle is near and below a small blue triangle. In C, there is a small blue circle.",
  "question": "Is the small blue circle in B below a large black thing?",
  "choices": {
    "Yes": "Yes",
    "No": "No",
    "DK": "DK"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `No` — No | `No` — No | Same answer |
| Decider v1.1 | `No` — No | `No` — No | Same answer |
| Jev | `No` — No | `No` — No | Same answer |
| Microsoft Decision-1 | `No` — No | `No` — No | Same answer |
| Clef | `Yes` — Yes | `Yes` — Yes | Same answer |
| Luna Decisions | `Yes` — Yes | `Yes` — Yes | Same answer |
| Clef Flash | `No` — No | `No` — No | Same answer |
| Strands Decider | `Yes` — Yes | `Yes` — Yes | Same answer |
| GLiNER2.5 Decide | `No` — No | `No` — No | Same answer |
| Laya | `Yes` — Yes | `Yes` — Yes | Same answer |
| CalDec v1 | `Yes` — Yes | `Yes` — Yes | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `spartqa/100b2a2a6e1dde9f685e/irrelevant_details/low/clean-source_first_spartqa_short_contexts_full_0136`

**Input fingerprint:** `9b5ff0793b8977e2a25b4d9c1363f1bba113b3550ebd08d948c4850e8e3cc3b0`

| Change | Recorded version |
| --- | --- |
| Irrelevant details | Add a small amount of irrelevant detail |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/spatial-cognition/spartqa-100b2a2a6e1dde9f685e.md).
