# Evidence order · Present the evidence in reverse order variant

[Original question](../../../questions/communication/pub-022a4c7f5dee09eaf4b8.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> X: Do you prefer a different career?
> Y: Only if the promotion opportunities are better.
> Context: Y has just told X that he/she is considering switching his/her job.

## Question

> Choose the interpretation or answer requested by the text.

## Answer choices

- **A.** Yes
- **B.** No
- **C.** Yes, subject to some conditions
- **D.** In the middle, neither yes nor no
- **E.** Other

**Reference answer:** `C`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "X: Do you prefer a different career?\nY: Only if the promotion opportunities are better.\nContext: Y has just told X that he/she is considering switching his/her job.\n",
  "question": "Choose the interpretation or answer requested by the text.",
  "choices": {
    "A": "Yes",
    "B": "No",
    "C": "Yes, subject to some conditions",
    "D": "In the middle, neither yes nor no",
    "E": "Other"
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
| Laya | `A` — Yes | `A` — Yes | Same answer |
| CalDec v1 | `A` — Yes | `A` — Yes | Same answer |

**Ordering comparison:** literal requested source unit permutation. Only the exact matched comparison sets contribute to the reported ordering contrasts.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `pub/022a4c7f5dee09eaf4b8/presentation_order/reverse_presentation/clean-source_first_order_name_completion_contexts_full_0242`

**Input fingerprint:** `cbf55729b55874c706abe1a3aa463438f36376298edb5cc1e620fd15fd5d6af7`

| Change | Recorded version |
| --- | --- |
| Evidence order | Present the evidence in reverse order |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/communication/pub-022a4c7f5dee09eaf4b8.md).
