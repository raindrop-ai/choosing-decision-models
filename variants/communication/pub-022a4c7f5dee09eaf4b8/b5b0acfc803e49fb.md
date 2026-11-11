# Option order · Reverse the answer choices variant

[Original question](../../../questions/communication/pub-022a4c7f5dee09eaf4b8.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** answer choices or their order.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Context: Y has just told X that he/she is considering switching his/her job.
> X: Do you prefer a different career?
> Y: Only if the promotion opportunities are better.

## Question

> Choose the interpretation or answer requested by the text.

## Answer choices

- **E.** Other
- **D.** In the middle, neither yes nor no
- **C.** Yes, subject to some conditions
- **B.** No
- **A.** Yes

**Reference answer:** `C`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Context: Y has just told X that he/she is considering switching his/her job.\nX: Do you prefer a different career?\nY: Only if the promotion opportunities are better.\n",
  "question": "Choose the interpretation or answer requested by the text.",
  "choices": {
    "E": "Other",
    "D": "In the middle, neither yes nor no",
    "C": "Yes, subject to some conditions",
    "B": "No",
    "A": "Yes"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `C` — Yes, subject to some conditions | `C` — Yes, subject to some conditions | Same answer |
| Decider v1.1 | `C` — Yes, subject to some conditions | `C` — Yes, subject to some conditions | Same answer |
| Jev | `C` — Yes, subject to some conditions | `C` — Yes, subject to some conditions | Same answer |
| Microsoft Decision-1 | `C` — Yes, subject to some conditions | `C` — Yes, subject to some conditions | Same answer |
| Clef | `C` — Yes, subject to some conditions | `C` — Yes, subject to some conditions | Same answer |
| Luna Decisions | `C` — Yes, subject to some conditions | `C` — Yes, subject to some conditions | Same answer |
| Clef Flash | `C` — Yes, subject to some conditions | `C` — Yes, subject to some conditions | Same answer |
| Strands Decider | `C` — Yes, subject to some conditions | `C` — Yes, subject to some conditions | Same answer |
| GLiNER2.5 Decide | `E` — Other | `E` — Other | Same answer |
| Laya | `A` — Yes | `C` — Yes, subject to some conditions | Different answer |
| CalDec v1 | `A` — Yes | `A` — Yes | Same answer |

Clef and Clef Flash sort answer choices in their published input-processing code. Their choice-order results describe that preprocessing.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `pub/022a4c7f5dee09eaf4b8/option_order/reverse`

**Input fingerprint:** `efbd832a712153cf3e458caaa60c7c349fe0c5eb0ccd84619d0f93c3c8286bd8`

| Change | Recorded version |
| --- | --- |
| Option order | Reverse the answer choices |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/communication/pub-022a4c7f5dee09eaf4b8.md).
