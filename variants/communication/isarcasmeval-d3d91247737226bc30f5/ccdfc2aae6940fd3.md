# Unrelated examples · No worked example (prose-control recipe) variant

[Original question](../../../questions/communication/isarcasmeval-d3d91247737226bc30f5.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** question instructions.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Boy, I sure do love being constantly misgendered by my cis relatives at family gatherings 🙃

## Question

> Is this message intended to be sarcastic?
>
> The notebook has a linen cover and stitched binding.

## Answer choices

- **yes.** Sarcastic
- **no.** Not sarcastic

**Reference answer:** `yes`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Boy, I sure do love being constantly misgendered by my cis relatives at family gatherings 🙃",
  "question": "Is this message intended to be sarcastic?\n\nThe notebook has a linen cover and stitched binding.",
  "choices": {
    "yes": "Sarcastic",
    "no": "Not sarcastic"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `yes` — Sarcastic | `yes` — Sarcastic | Same answer |
| Decider v1.1 | `yes` — Sarcastic | `yes` — Sarcastic | Same answer |
| Jev | `yes` — Sarcastic | `yes` — Sarcastic | Same answer |
| Microsoft Decision-1 | `yes` — Sarcastic | `no` — Not sarcastic | Different answer |
| Clef | `no` — Not sarcastic | `no` — Not sarcastic | Same answer |
| Luna Decisions | `yes` — Sarcastic | `no` — Not sarcastic | Different answer |
| Clef Flash | `no` — Not sarcastic | `no` — Not sarcastic | Same answer |
| Strands Decider | `yes` — Sarcastic | `yes` — Sarcastic | Same answer |
| GLiNER2.5 Decide | `yes` — Sarcastic | `yes` — Sarcastic | Same answer |
| Laya | `yes` — Sarcastic | `yes` — Sarcastic | Same answer |
| CalDec v1 | `yes` — Sarcastic | `yes` — Sarcastic | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `isarcasmeval/d3d91247737226bc30f5/examples/prose_control/clean-source_first_sarcasm_question_contexts_full_0182`

**Input fingerprint:** `b72b0219204608ccbd10f2d06fcb6461d20ec7a27d6b4586ee8e748a5b90283d`

| Change | Recorded version |
| --- | --- |
| Unrelated examples | No worked example (prose-control recipe) |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/communication/isarcasmeval-d3d91247737226bc30f5.md).
