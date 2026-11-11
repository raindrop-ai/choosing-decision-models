# Misleading details · Add an unverified claim that agrees with the evidence variant

[Original question](../../../questions/communication/isarcasmeval-bfcf69cad7b345fb8301.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** question instructions.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Every break I rediscover my love of reading for pleasure only for it to feel like a chore again when classes starts 😪

## Question

> Is this message intended to be sarcastic?
>
> A reader thinks the classification of «Every break I rediscover my love of reading for pleasure only for it to feel like a chore again when classes starts 😪» is «Not sarcastic».

## Answer choices

- **yes.** Sarcastic
- **no.** Not sarcastic

**Reference answer:** `no`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Every break I rediscover my love of reading for pleasure only for it to feel like a chore again when classes starts 😪",
  "question": "Is this message intended to be sarcastic?\n\nA reader thinks the classification of «Every break I rediscover my love of reading for pleasure only for it to feel like a chore again when classes starts 😪» is «Not sarcastic».",
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
| GLiDE v1.2 | `no` — Not sarcastic | `no` — Not sarcastic | Same answer |
| Decider v1.1 | `no` — Not sarcastic | `no` — Not sarcastic | Same answer |
| Jev | `no` — Not sarcastic | `no` — Not sarcastic | Same answer |
| Microsoft Decision-1 | `no` — Not sarcastic | `no` — Not sarcastic | Same answer |
| Clef | `no` — Not sarcastic | `no` — Not sarcastic | Same answer |
| Luna Decisions | `no` — Not sarcastic | `no` — Not sarcastic | Same answer |
| Clef Flash | `no` — Not sarcastic | `no` — Not sarcastic | Same answer |
| Strands Decider | `no` — Not sarcastic | `yes` — Sarcastic | Different answer |
| GLiNER2.5 Decide | `no` — Not sarcastic | `no` — Not sarcastic | Same answer |
| Laya | `no` — Not sarcastic | `no` — Not sarcastic | Same answer |
| CalDec v1 | `no` — Not sarcastic | `no` — Not sarcastic | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `isarcasmeval/bfcf69cad7b345fb8301/misleading_summary/accurate/clean-source_first_sarcasm_question_contexts_full_0182`

**Input fingerprint:** `ea18db2a0b1beb880d6022610ff5b78249b3d4c66c3ddb12cbd23a6ce29e88f1`

| Change | Recorded version |
| --- | --- |
| Misleading details | Add an unverified claim that agrees with the evidence |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/communication/isarcasmeval-bfcf69cad7b345fb8301.md).
