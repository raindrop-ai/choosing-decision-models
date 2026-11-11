# Paraphrasing · Change individual words and phrases variant

[Original question](../../../questions/communication/pub-d86468fb97d0eb54e717.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Speaker\_1: The mountain range had a very rounded shape
> Speaker\_2: Yes, The mountain range was As soft as hills

## Question

> Choose the interpretation or answer requested by the text.

## Answer choices

- **A.** Agrees
- **B.** Sarcastic

**Reference answer:** `A`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Speaker_1: The mountain range had a very rounded shape\nSpeaker_2: Yes, The mountain range was As soft as hills",
  "question": "Choose the interpretation or answer requested by the text.",
  "choices": {
    "A": "Agrees",
    "B": "Sarcastic"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `A` — Agrees | `A` — Agrees | Same answer |
| Decider v1.1 | `A` — Agrees | `A` — Agrees | Same answer |
| Jev | `A` — Agrees | `A` — Agrees | Same answer |
| Microsoft Decision-1 | `A` — Agrees | `A` — Agrees | Same answer |
| Clef | `A` — Agrees | `A` — Agrees | Same answer |
| Luna Decisions | `A` — Agrees | `A` — Agrees | Same answer |
| Clef Flash | `A` — Agrees | `A` — Agrees | Same answer |
| Strands Decider | `B` — Sarcastic | `A` — Agrees | Different answer |
| GLiNER2.5 Decide | `B` — Sarcastic | `B` — Sarcastic | Same answer |
| Laya | `B` — Sarcastic | `B` — Sarcastic | Same answer |
| CalDec v1 | `A` — Agrees | `A` — Agrees | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `pub/d86468fb97d0eb54e717/paraphrasing/surface`

**Input fingerprint:** `7703e21ce265e915390ecd8175bcf4839a30f900106a49250954c34ce79fb8ad`

| Change | Recorded version |
| --- | --- |
| Paraphrasing | Change individual words and phrases |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/communication/pub-d86468fb97d0eb54e717.md).
