# Paraphrasing · Change individual words and phrases variant

[Original question](../../../questions/uncertainty-monitoring/selfaware-fc8794c056e241d0024b.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** question instructions.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> How do vampires dress so fancy if they can’t see their reflections?

## Question

> Is there a determinate answer to this question?

## Answer choices

- **yes.** Answerable
- **no.** Unanswerable

**Reference answer:** `no`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "How do vampires dress so fancy if they can’t see their reflections?",
  "question": "Is there a determinate answer to this question?",
  "choices": {
    "yes": "Answerable",
    "no": "Unanswerable"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `no` — Unanswerable | `no` — Unanswerable | Same answer |
| Decider v1.1 | `no` — Unanswerable | `no` — Unanswerable | Same answer |
| Jev | `no` — Unanswerable | `no` — Unanswerable | Same answer |
| Microsoft Decision-1 | `no` — Unanswerable | `no` — Unanswerable | Same answer |
| Clef | `no` — Unanswerable | `no` — Unanswerable | Same answer |
| Luna Decisions | `yes` — Answerable | `yes` — Answerable | Same answer |
| Clef Flash | `no` — Unanswerable | `no` — Unanswerable | Same answer |
| Strands Decider | `no` — Unanswerable | `no` — Unanswerable | Same answer |
| GLiNER2.5 Decide | `no` — Unanswerable | `no` — Unanswerable | Same answer |
| Laya | `yes` — Answerable | `yes` — Answerable | Same answer |
| CalDec v1 | `no` — Unanswerable | `yes` — Answerable | Different answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `selfaware/fc8794c056e241d0024b/paraphrasing/surface`

**Input fingerprint:** `1f301c6ffcf23118d520b127965eec32af28983fc7cb1acc469fb7b7bfba005f`

| Change | Recorded version |
| --- | --- |
| Paraphrasing | Change individual words and phrases |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/uncertainty-monitoring/selfaware-fc8794c056e241d0024b.md).
