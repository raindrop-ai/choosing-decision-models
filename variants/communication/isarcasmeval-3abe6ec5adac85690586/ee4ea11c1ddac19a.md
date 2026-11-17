# Evidence position · Place the relevant information at the end variant

[Original question](../../../questions/communication/isarcasmeval-3abe6ec5adac85690586.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> 2 + 3 = 5.
>
> \---
>
> 7 + 8 = 15.
>
> \---
>
> 4 + 5 = 9.
>
> \---
>
> 6 + 7 = 13.
>
> \---
>
> So Boris has made a hash of Brexit, let 150,000 people die and lied through his teeth but still thinks he deserves a boozy bash! Nothing surprises me about him any more sadly.

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
  "state": "2 + 3 = 5.\n\n---\n\n7 + 8 = 15.\n\n---\n\n4 + 5 = 9.\n\n---\n\n6 + 7 = 13.\n\n---\n\nSo Boris has made a hash of Brexit, let 150,000 people die and lied through his teeth but still thinks he deserves a boozy bash! Nothing surprises me about him any more sadly.",
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
| Microsoft Decision-1 | `no` — Not sarcastic | `yes` — Sarcastic | Different answer |
| Clef | `no` — Not sarcastic | `no` — Not sarcastic | Same answer |
| Luna Decisions | `yes` — Sarcastic | `yes` — Sarcastic | Same answer |
| Clef Flash | `no` — Not sarcastic | `no` — Not sarcastic | Same answer |
| Strands Decider | `yes` — Sarcastic | `yes` — Sarcastic | Same answer |
| GLiNER2.5 Decide | `yes` — Sarcastic | `yes` — Sarcastic | Same answer |
| Laya | `yes` — Sarcastic | `no` — Not sarcastic | Different answer |
| CalDec v1 | `yes` — Sarcastic | `yes` — Sarcastic | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `isarcasmeval/3abe6ec5adac85690586/evidence_position/end/clean-source_first_scope0008_sarcasm_position_batch2_full_0423`

**Input fingerprint:** `090676017d1d38994ecaa04be747827c1225f86edbf3beabc252154930c1edc1`

| Change | Recorded version |
| --- | --- |
| Evidence position | Place the relevant information at the end |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/communication/isarcasmeval-3abe6ec5adac85690586.md).
