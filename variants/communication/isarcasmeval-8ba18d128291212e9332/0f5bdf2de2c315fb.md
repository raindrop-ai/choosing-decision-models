# Evidence position · Move the article's source within the sentence variant

[Original question](../../../questions/communication/isarcasmeval-8ba18d128291212e9332.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> @futboIjacob @LFC @Thiago6 It, in the article, literally says that he’s expected back next week.

## Question

> Is this message intended to be sarcastic?

## Answer choices

- **yes.** Sarcastic
- **no.** Not sarcastic

**Reference answer:** `no`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "@futboIjacob @LFC @Thiago6 It, in the article, literally says that he’s expected back next week.",
  "question": "Is this message intended to be sarcastic?",
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
| Luna Decisions | `no` — Not sarcastic | `yes` — Sarcastic | Different answer |
| Clef Flash | `no` — Not sarcastic | `no` — Not sarcastic | Same answer |
| Strands Decider | `no` — Not sarcastic | `no` — Not sarcastic | Same answer |
| GLiNER2.5 Decide | `no` — Not sarcastic | `no` — Not sarcastic | Same answer |
| Laya | `no` — Not sarcastic | `no` — Not sarcastic | Same answer |
| CalDec v1 | `no` — Not sarcastic | `no` — Not sarcastic | Same answer |

**Ordering comparison:** coupled wording reference chronology or representation. Only the exact matched comparison sets contribute to the reported ordering contrasts.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `isarcasmeval/8ba18d128291212e9332/evidence_position/native_article_source_internal/clean-source_first_native_unit_roles_strong_shuffle_full_0380`

**Input fingerprint:** `77159d3113cea055b606aa0adbdea8488ac154989236aa966041ff7440bd6c1b`

| Change | Recorded version |
| --- | --- |
| Evidence position | Move the article&#x27;s source within the sentence |
| Evidence order | Reorder parts of an original expression or statement |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/communication/isarcasmeval-8ba18d128291212e9332.md).
