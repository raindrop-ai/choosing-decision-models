# Irrelevant details · Add a larger amount of irrelevant detail variant

[Original question](../../../questions/uncertainty-monitoring/selfaware-ba57e74868f86e08800b.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> The notebook has a linen cover. The cover has an embossed title. The page edges are uneven. The binding is stitched. A ribbon marks a page. The back cover has a pocket.
>
> Do you think a singularity will happen in this century?

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
  "state": "The notebook has a linen cover. The cover has an embossed title. The page edges are uneven. The binding is stitched. A ribbon marks a page. The back cover has a pocket.\n\nDo you think a singularity will happen in this century?",
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
| Luna Decisions | `yes` — Answerable | `yes` — Answerable | Same answer |
| Clef Flash | `no` — Unanswerable | `no` — Unanswerable | Same answer |
| Strands Decider | `no` — Unanswerable | `no` — Unanswerable | Same answer |
| GLiNER2.5 Decide | `no` — Unanswerable | `no` — Unanswerable | Same answer |
| Laya | `yes` — Answerable | `no` — Unanswerable | Different answer |
| CalDec v1 | `no` — Unanswerable | `no` — Unanswerable | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `selfaware/ba57e74868f86e08800b/irrelevant_details/high/clean-source_first_selfaware_short_contexts_full_0127`

**Input fingerprint:** `056af7d27289e7d5b39bb2063d5319729b09a074ca19e9d0afe117200ed37b48`

| Change | Recorded version |
| --- | --- |
| Irrelevant details | Add a larger amount of irrelevant detail |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/uncertainty-monitoring/selfaware-ba57e74868f86e08800b.md).
