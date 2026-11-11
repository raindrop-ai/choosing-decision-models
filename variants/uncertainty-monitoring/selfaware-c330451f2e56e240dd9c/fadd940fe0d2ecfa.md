# Unrelated examples · No worked example (absence-control recipe) variant

[Original question](../../../questions/uncertainty-monitoring/selfaware-c330451f2e56e240dd9c.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> The notebook's cover is linen.
>
> Is the Higgs-Boson machine a good or bad thing for our universe?

## Question

> Does this question have a determinate answer?

## Answer choices

- **yes.** Answerable
- **no.** Unanswerable

**Reference answer:** `no`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "The notebook's cover is linen.\n\nIs the Higgs-Boson machine a good or bad thing for our universe?",
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
| GLiDE v1.2 | `no` — Unanswerable | `no` — Unanswerable | Same answer |
| Decider v1.1 | `no` — Unanswerable | `no` — Unanswerable | Same answer |
| Jev | `no` — Unanswerable | `no` — Unanswerable | Same answer |
| Microsoft Decision-1 | `no` — Unanswerable | `no` — Unanswerable | Same answer |
| Clef | `no` — Unanswerable | `no` — Unanswerable | Same answer |
| Luna Decisions | `yes` — Answerable | `no` — Unanswerable | Different answer |
| Clef Flash | `no` — Unanswerable | `yes` — Answerable | Different answer |
| Strands Decider | `yes` — Answerable | `no` — Unanswerable | Different answer |
| GLiNER2.5 Decide | `no` — Unanswerable | `no` — Unanswerable | Same answer |
| Laya | `yes` — Answerable | `yes` — Answerable | Same answer |
| CalDec v1 | `no` — Unanswerable | `no` — Unanswerable | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `selfaware/c330451f2e56e240dd9c/examples/absent/clean-source_first_selfaware_short_contexts_full_0128`

**Input fingerprint:** `23e420fdaafa71321de9101fe910a8e29e5a61d795693218d961f587b5a0d9f1`

| Change | Recorded version |
| --- | --- |
| Unrelated examples | No worked example (absence-control recipe) |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/uncertainty-monitoring/selfaware-c330451f2e56e240dd9c.md).
