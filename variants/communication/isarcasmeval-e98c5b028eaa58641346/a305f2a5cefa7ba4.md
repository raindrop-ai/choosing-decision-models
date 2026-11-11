# Unrelated examples · No worked example (prose-control recipe) variant

[Original question](../../../questions/communication/isarcasmeval-e98c5b028eaa58641346.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** question instructions.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> New years resolution this year is to pick up some more self distinctive habits.

## Question

> Is this message intended to be sarcastic?
>
> The notebook has a linen cover and stitched binding.

## Answer choices

- **no.** Not sarcastic
- **yes.** Sarcastic

**Reference answer:** `no`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "New years resolution this year is to pick up some more self distinctive habits.",
  "question": "Is this message intended to be sarcastic?\n\nThe notebook has a linen cover and stitched binding.",
  "choices": {
    "no": "Not sarcastic",
    "yes": "Sarcastic"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `no` — Not sarcastic | `no` — Not sarcastic | Same answer |
| Decider v1.1 | `no` — Not sarcastic | `no` — Not sarcastic | Same answer |
| Jev | `no` — Not sarcastic | `no` — Not sarcastic | Same answer |
| Microsoft Decision-1 | `yes` — Sarcastic | `no` — Not sarcastic | Different answer |
| Clef | `no` — Not sarcastic | `no` — Not sarcastic | Same answer |
| Luna Decisions | `no` — Not sarcastic | `no` — Not sarcastic | Same answer |
| Clef Flash | `no` — Not sarcastic | `no` — Not sarcastic | Same answer |
| Strands Decider | `no` — Not sarcastic | `no` — Not sarcastic | Same answer |
| GLiNER2.5 Decide | `no` — Not sarcastic | `no` — Not sarcastic | Same answer |
| Laya | `no` — Not sarcastic | `no` — Not sarcastic | Same answer |
| CalDec v1 | `no` — Not sarcastic | `no` — Not sarcastic | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `isarcasmeval/e98c5b028eaa58641346/examples/prose_control/clean-source_first_sarcasm_question_contexts_full_0182`

**Input fingerprint:** `ddde687fd534f946b88f3928190e609e581d951f58bc0954cd8e1a91f092749f`

| Change | Recorded version |
| --- | --- |
| Unrelated examples | No worked example (prose-control recipe) |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/communication/isarcasmeval-e98c5b028eaa58641346.md).
