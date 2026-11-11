# Evidence order · Present the evidence in reverse order variant

[Original question](../../../questions/communication/pub-af91d0e3d83ed05469bf.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> X: Can you afford an apartment?
> Y: I've been saving for a long time.
> Context: Y has just told X that he/she is thinking of buying a flat in New York.

## Question

> Choose the interpretation or answer requested by the text.

## Answer choices

- **A.** Yes
- **B.** No
- **C.** Yes, subject to some conditions
- **D.** In the middle, neither yes nor no
- **E.** Other

**Reference answer:** `A`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "X: Can you afford an apartment?\nY: I've been saving for a long time.\nContext: Y has just told X that he/she is thinking of buying a flat in New York.\n",
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
| GLiDE v1.2 | `A` — Yes | `A` — Yes | Same answer |
| Decider v1.1 | `A` — Yes | `A` — Yes | Same answer |
| Jev | `A` — Yes | `A` — Yes | Same answer |
| Microsoft Decision-1 | `A` — Yes | `A` — Yes | Same answer |
| Clef | `A` — Yes | `A` — Yes | Same answer |
| Luna Decisions | `C` — Yes, subject to some conditions | `E` — Other | Different answer |
| Clef Flash | `A` — Yes | `A` — Yes | Same answer |
| Strands Decider | `A` — Yes | `A` — Yes | Same answer |
| GLiNER2.5 Decide | `E` — Other | `E` — Other | Same answer |
| Laya | `A` — Yes | `C` — Yes, subject to some conditions | Different answer |
| CalDec v1 | `A` — Yes | `A` — Yes | Same answer |

**Ordering comparison:** literal requested source unit permutation. Only the exact matched comparison sets contribute to the reported ordering contrasts.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `pub/af91d0e3d83ed05469bf/presentation_order/reverse_presentation/clean-source_first_order_name_completion_contexts_full_0242`

**Input fingerprint:** `dc0308ba74c60dcde3f2cf23fbe481ad09b83a9d95930751e157b5012afd17f7`

| Change | Recorded version |
| --- | --- |
| Evidence order | Present the evidence in reverse order |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/communication/pub-af91d0e3d83ed05469bf.md).
