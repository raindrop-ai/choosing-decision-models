# Misleading details · Add an unverified claim that agrees with the evidence variant

[Original question](../../../questions/communication/isarcasmeval-6012a8260570a330f0af.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** question instructions.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> After the two years we’ve just had, the loss of twenty shows just before Christmas…if we lose our Union Chapel show too it’ll be devastating. But I’d rather be safe than dead

## Question

> Is this message intended to be sarcastic?
>
> A reader thinks the classification of «After the two years we’ve just had, the loss of twenty shows just before Christmas…if we lose our Union Chapel show too it’ll be devastating. But I’d rather be safe than dead» is «Not sarcastic».

## Answer choices

- **no.** Not sarcastic
- **yes.** Sarcastic

**Reference answer:** `no`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "After the two years we’ve just had, the loss of twenty shows just before Christmas…if we lose our Union Chapel show too it’ll be devastating. But I’d rather be safe than dead",
  "question": "Is this message intended to be sarcastic?\n\nA reader thinks the classification of «After the two years we’ve just had, the loss of twenty shows just before Christmas…if we lose our Union Chapel show too it’ll be devastating. But I’d rather be safe than dead» is «Not sarcastic».",
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
| Luna Decisions | `no` — Not sarcastic | `no` — Not sarcastic | Same answer |
| Clef Flash | `no` — Not sarcastic | `no` — Not sarcastic | Same answer |
| Strands Decider | `no` — Not sarcastic | `no` — Not sarcastic | Same answer |
| GLiNER2.5 Decide | `no` — Not sarcastic | `no` — Not sarcastic | Same answer |
| Laya | `no` — Not sarcastic | `no` — Not sarcastic | Same answer |
| CalDec v1 | `no` — Not sarcastic | `no` — Not sarcastic | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `isarcasmeval/6012a8260570a330f0af/misleading_summary/accurate/clean-source_first_sarcasm_question_contexts_full_0182`

**Input fingerprint:** `5a81212861335a79ec55e984d101b5a7888f8f40b491655c3875ce9d01836de9`

| Change | Recorded version |
| --- | --- |
| Misleading details | Add an unverified claim that agrees with the evidence |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/communication/isarcasmeval-6012a8260570a330f0af.md).
