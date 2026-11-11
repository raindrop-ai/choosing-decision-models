# Similar distractors · Add fewer similar but irrelevant items variant

[Original question](../../../questions/uncertainty-monitoring/selfaware-70500a0d24fc6a21b47b.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> “What rhythmic pattern opens the fictional suite Elvarin?”
>
> What are teeth made out of?

## Question

> Does this question have a determinate answer?

## Answer choices

- **yes.** Answerable
- **no.** Unanswerable

**Reference answer:** `yes`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "“What rhythmic pattern opens the fictional suite Elvarin?”\n\nWhat are teeth made out of?",
  "question": "Does this question have a determinate answer?",
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
| GLiDE v1.2 | `yes` — Answerable | `yes` — Answerable | Same answer |
| Decider v1.1 | `yes` — Answerable | `yes` — Answerable | Same answer |
| Jev | `yes` — Answerable | `no` — Unanswerable | Different answer |
| Microsoft Decision-1 | `yes` — Answerable | `yes` — Answerable | Same answer |
| Clef | `yes` — Answerable | `no` — Unanswerable | Different answer |
| Luna Decisions | `yes` — Answerable | `yes` — Answerable | Same answer |
| Clef Flash | `yes` — Answerable | `yes` — Answerable | Same answer |
| Strands Decider | `yes` — Answerable | `no` — Unanswerable | Different answer |
| GLiNER2.5 Decide | `no` — Unanswerable | `no` — Unanswerable | Same answer |
| Laya | `yes` — Answerable | `no` — Unanswerable | Different answer |
| CalDec v1 | `no` — Unanswerable | `no` — Unanswerable | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `selfaware/70500a0d24fc6a21b47b/similar_distractors/low/clean-source_first_selfaware_near_questions_full_0200`

**Input fingerprint:** `b2dcabcd551103cc74e522143141bdb2159f504aad82fffc9e3dd35cc0312bd1`

| Change | Recorded version |
| --- | --- |
| Similar distractors | Add fewer similar but irrelevant items |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/uncertainty-monitoring/selfaware-70500a0d24fc6a21b47b.md).
