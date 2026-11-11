# Unrelated examples · No worked example (natural-prose recipe) variant

[Original question](../../../questions/communication/isarcasmeval-9bdecb6b9c2d39051c5c.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** question instructions.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Why does Ramish think he can  stop my kitchen rennovation because of the noise? His kids are not exactly quiet or competent when they play their musical instruments, lets just say my dog makes a better sound.

## Question

> Is this message intended to be sarcastic?
>
> The notebook has a linen cover and stitched binding.

## Answer choices

- **no.** Not sarcastic
- **yes.** Sarcastic

**Reference answer:** `yes`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Why does Ramish think he can  stop my kitchen rennovation because of the noise? His kids are not exactly quiet or competent when they play their musical instruments, lets just say my dog makes a better sound.",
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
| Jev | `yes` — Sarcastic | `no` — Not sarcastic | Different answer |
| Microsoft Decision-1 | `no` — Not sarcastic | `no` — Not sarcastic | Same answer |
| Clef | `no` — Not sarcastic | `no` — Not sarcastic | Same answer |
| Luna Decisions | `yes` — Sarcastic | `no` — Not sarcastic | Different answer |
| Clef Flash | `no` — Not sarcastic | `no` — Not sarcastic | Same answer |
| Strands Decider | `yes` — Sarcastic | `yes` — Sarcastic | Same answer |
| GLiNER2.5 Decide | `yes` — Sarcastic | `yes` — Sarcastic | Same answer |
| Laya | `no` — Not sarcastic | `no` — Not sarcastic | Same answer |
| CalDec v1 | `no` — Not sarcastic | `no` — Not sarcastic | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `isarcasmeval/9bdecb6b9c2d39051c5c/examples/natural_prose/clean-source_first_sarcasm_residual_completion_full_0245`

**Input fingerprint:** `e36cb83caa53378136a0ae59e8ff1c1363b56eef1b285f26d4206ef36e301771`

| Change | Recorded version |
| --- | --- |
| Unrelated examples | No worked example (natural-prose recipe) |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/communication/isarcasmeval-9bdecb6b9c2d39051c5c.md).
