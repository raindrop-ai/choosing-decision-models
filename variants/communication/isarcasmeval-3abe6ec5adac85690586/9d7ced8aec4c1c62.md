# Similar distractors · Add fewer similar but irrelevant items variant

[Original question](../../../questions/communication/isarcasmeval-3abe6ec5adac85690586.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** question instructions.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> So Boris has made a hash of Brexit, let 150,000 people die and lied through his teeth but still thinks he deserves a boozy bash! Nothing surprises me about him any more sadly.

## Question

> Is this message intended to be sarcastic?
>
> Varelin writes, "Wonderful, the bus left just before I reached the stop."

## Answer choices

- **yes.** Sarcastic
- **no.** Not sarcastic

**Reference answer:** `no`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "So Boris has made a hash of Brexit, let 150,000 people die and lied through his teeth but still thinks he deserves a boozy bash! Nothing surprises me about him any more sadly.",
  "question": "Is this message intended to be sarcastic?\n\nVarelin writes, \"Wonderful, the bus left just before I reached the stop.\"",
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
| GLiDE v1.2 | `no` — Not sarcastic | `yes` — Sarcastic | Different answer |
| Decider v1.1 | `no` — Not sarcastic | `yes` — Sarcastic | Different answer |
| Jev | `no` — Not sarcastic | `yes` — Sarcastic | Different answer |
| Microsoft Decision-1 | `no` — Not sarcastic | `yes` — Sarcastic | Different answer |
| Clef | `no` — Not sarcastic | `no` — Not sarcastic | Same answer |
| Luna Decisions | `yes` — Sarcastic | `yes` — Sarcastic | Same answer |
| Clef Flash | `no` — Not sarcastic | `no` — Not sarcastic | Same answer |
| Strands Decider | `yes` — Sarcastic | `yes` — Sarcastic | Same answer |
| GLiNER2.5 Decide | `yes` — Sarcastic | `yes` — Sarcastic | Same answer |
| Laya | `yes` — Sarcastic | `no` — Not sarcastic | Different answer |
| CalDec v1 | `yes` — Sarcastic | `no` — Not sarcastic | Different answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `isarcasmeval/3abe6ec5adac85690586/similar_distractors/low/clean-source_first_sarcasm_near_posts_full_0213`

**Input fingerprint:** `18d3948d4c9aa7809a2adfaf7c2efcafbec5fa72f2cdbbbbbe4c3d67917078df`

| Change | Recorded version |
| --- | --- |
| Similar distractors | Add fewer similar but irrelevant items |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/communication/isarcasmeval-3abe6ec5adac85690586.md).
