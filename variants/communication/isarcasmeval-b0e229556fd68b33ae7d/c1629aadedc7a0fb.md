# Paraphrasing · Change individual words and phrases variant

[Original question](../../../questions/communication/isarcasmeval-b0e229556fd68b33ae7d.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** question instructions.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> It's beggars belief that the MET Police suggest they can't, or won't, investigate crimes that have already been committed.

## Question

> Is sarcasm intended in this message?

## Answer choices

- **no.** Not sarcastic
- **yes.** Sarcastic

**Reference answer:** `no`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "It's beggars belief that the MET Police suggest they can't, or won't, investigate crimes that have already been committed.",
  "question": "Is sarcasm intended in this message?",
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
| Microsoft Decision-1 | `no` — Not sarcastic | `no` — Not sarcastic | Same answer |
| Clef | `no` — Not sarcastic | `no` — Not sarcastic | Same answer |
| Luna Decisions | `yes` — Sarcastic | `yes` — Sarcastic | Same answer |
| Clef Flash | `no` — Not sarcastic | `no` — Not sarcastic | Same answer |
| Strands Decider | `no` — Not sarcastic | `yes` — Sarcastic | Different answer |
| GLiNER2.5 Decide | `yes` — Sarcastic | `yes` — Sarcastic | Same answer |
| Laya | `no` — Not sarcastic | `no` — Not sarcastic | Same answer |
| CalDec v1 | `no` — Not sarcastic | `no` — Not sarcastic | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `isarcasmeval/b0e229556fd68b33ae7d/paraphrasing/surface`

**Input fingerprint:** `cdab855cc4a0092ea18aa289eb96bafe4d1d720a28a8073e257d3fb3847cb16e`

| Change | Recorded version |
| --- | --- |
| Paraphrasing | Change individual words and phrases |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/communication/isarcasmeval-b0e229556fd68b33ae7d.md).
