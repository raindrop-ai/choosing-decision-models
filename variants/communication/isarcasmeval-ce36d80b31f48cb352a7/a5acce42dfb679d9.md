# Similar distractors · Add more similar but irrelevant items variant

[Original question](../../../questions/communication/isarcasmeval-ce36d80b31f48cb352a7.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** question instructions.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Need a big second half reds

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
  "state": "Need a big second half reds",
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
| Jev | `no` — Not sarcastic | `no` — Not sarcastic | Same answer |
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

**Variant ID:** `isarcasmeval/ce36d80b31f48cb352a7/similar_distractors/high/clean-source_first_sarcasm_near_posts_full_0213`

**Input fingerprint:** `619dc139b61fa17a065a4e7ce63103c6b2d5275c54498d241c6f36cf25ea1afe`

| Change | Recorded version |
| --- | --- |
| Similar distractors | Add more similar but irrelevant items |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/communication/isarcasmeval-ce36d80b31f48cb352a7.md).
