# Similar distractors · Add more similar but irrelevant items variant

[Original question](../../../questions/communication/isarcasmeval-cb3b0623041aa5e4b431.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** question instructions.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> 3 points for the whites and a curry for tea... Happy Days 😍

## Question

> Is this message intended to be sarcastic?
>
> Varelin writes, "Wonderful, the bus left just before I reached the stop."
>
> Zorven writes, "The picnic starts at noon, and I have packed sandwiches."
>
> Nereth writes, "Exactly what I wanted: another three forms to fill in."

## Answer choices

- **yes.** Sarcastic
- **no.** Not sarcastic

**Reference answer:** `no`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "3 points for the whites and a curry for tea... Happy Days 😍",
  "question": "Is this message intended to be sarcastic?\n\nVarelin writes, \"Wonderful, the bus left just before I reached the stop.\"\n\nZorven writes, \"The picnic starts at noon, and I have packed sandwiches.\"\n\nNereth writes, \"Exactly what I wanted: another three forms to fill in.\"",
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
| Jev | `no` — Not sarcastic | `yes` — Sarcastic | Different answer |
| Microsoft Decision-1 | `no` — Not sarcastic | `no` — Not sarcastic | Same answer |
| Clef | `no` — Not sarcastic | `no` — Not sarcastic | Same answer |
| Luna Decisions | `no` — Not sarcastic | `yes` — Sarcastic | Different answer |
| Clef Flash | `no` — Not sarcastic | `no` — Not sarcastic | Same answer |
| Strands Decider | `no` — Not sarcastic | `no` — Not sarcastic | Same answer |
| GLiNER2.5 Decide | `no` — Not sarcastic | `yes` — Sarcastic | Different answer |
| Laya | `no` — Not sarcastic | `no` — Not sarcastic | Same answer |
| CalDec v1 | `no` — Not sarcastic | `no` — Not sarcastic | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `isarcasmeval/cb3b0623041aa5e4b431/similar_distractors/high/clean-source_first_sarcasm_near_posts_full_0213`

**Input fingerprint:** `7353754f2bad54b0c8aaa730b54a30d1770afa27f5cfc5f1d99016d54d17f156`

| Change | Recorded version |
| --- | --- |
| Similar distractors | Add more similar but irrelevant items |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/communication/isarcasmeval-cb3b0623041aa5e4b431.md).
