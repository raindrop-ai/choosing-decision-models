# Similar distractors · Add fewer similar but irrelevant items variant

[Original question](../../../questions/communication/isarcasmeval-015bc09c82beb2679504.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** question instructions.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Second hand embarrassment for anyone that actually queued to get into a nightclub last night🧐

## Question

> Is this message intended to be sarcastic?
>
> Varelin writes, "Wonderful, the bus left just before I reached the stop."

## Answer choices

- **no.** Not sarcastic
- **yes.** Sarcastic

**Reference answer:** `no`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Second hand embarrassment for anyone that actually queued to get into a nightclub last night🧐",
  "question": "Is this message intended to be sarcastic?\n\nVarelin writes, \"Wonderful, the bus left just before I reached the stop.\"",
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
| Jev | `yes` — Sarcastic | `yes` — Sarcastic | Same answer |
| Microsoft Decision-1 | `no` — Not sarcastic | `yes` — Sarcastic | Different answer |
| Clef | `no` — Not sarcastic | `no` — Not sarcastic | Same answer |
| Luna Decisions | `yes` — Sarcastic | `yes` — Sarcastic | Same answer |
| Clef Flash | `no` — Not sarcastic | `no` — Not sarcastic | Same answer |
| Strands Decider | `yes` — Sarcastic | `yes` — Sarcastic | Same answer |
| GLiNER2.5 Decide | `no` — Not sarcastic | `yes` — Sarcastic | Different answer |
| Laya | `no` — Not sarcastic | `no` — Not sarcastic | Same answer |
| CalDec v1 | `no` — Not sarcastic | `no` — Not sarcastic | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `isarcasmeval/015bc09c82beb2679504/similar_distractors/low/clean-source_first_sarcasm_near_posts_full_0213`

**Input fingerprint:** `018e3751c25ce8d93a5da213e5b792d67183d4ff366946cc95c9ecc4477c6837`

| Change | Recorded version |
| --- | --- |
| Similar distractors | Add fewer similar but irrelevant items |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/communication/isarcasmeval-015bc09c82beb2679504.md).
