# Unrelated examples · No worked example (absence-control recipe) variant

[Original question](../../../questions/uncertainty-monitoring/selfaware-48c2f213861e852409bd.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> The notebook's cover is linen.
>
> Carol and her mom were picking carrots from their garden. Carol picked 29 and her mother picked 16. If only less than 38 of the carrots were good, how many bad carrots did they have?

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
  "state": "The notebook's cover is linen.\n\nCarol and her mom were picking carrots from their garden. Carol picked 29 and her mother picked 16. If only less than 38 of the carrots were good, how many bad carrots did they have?",
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
| Jev | `no` — Unanswerable | `yes` — Answerable | Different answer |
| Microsoft Decision-1 | `no` — Unanswerable | `no` — Unanswerable | Same answer |
| Clef | `no` — Unanswerable | `no` — Unanswerable | Same answer |
| Luna Decisions | `no` — Unanswerable | `no` — Unanswerable | Same answer |
| Clef Flash | `yes` — Answerable | `yes` — Answerable | Same answer |
| Strands Decider | `yes` — Answerable | `no` — Unanswerable | Different answer |
| GLiNER2.5 Decide | `no` — Unanswerable | `no` — Unanswerable | Same answer |
| Laya | `yes` — Answerable | `yes` — Answerable | Same answer |
| CalDec v1 | `yes` — Answerable | `yes` — Answerable | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `selfaware/48c2f213861e852409bd/examples/absent/clean-source_first_selfaware_short_contexts_full_0127`

**Input fingerprint:** `5dedb31a43e0c4f7d6687b25e812cd05a6e4fb7c1a67e0e01f5ef83e0944d27e`

| Change | Recorded version |
| --- | --- |
| Unrelated examples | No worked example (absence-control recipe) |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/uncertainty-monitoring/selfaware-48c2f213861e852409bd.md).
