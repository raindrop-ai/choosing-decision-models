# Extra events · Add 2 unrelated events variant

[Original question](../../../questions/uncertainty-monitoring/selfaware-a84fd3aac838986e9bc9.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Nolan is the editor of a poetry catalog. Its entries are Virel, Zorven, Kesil, Nereth, Pavrel, and Sovrin.
> Nolan classifies Virel as a dialogue. Nolan classifies Zorven as a monologue.
>
> What restaurant chain with over 15,000 locations is a sister franchise to Wing Street?

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
  "state": "Nolan is the editor of a poetry catalog. Its entries are Virel, Zorven, Kesil, Nereth, Pavrel, and Sovrin.\nNolan classifies Virel as a dialogue. Nolan classifies Zorven as a monologue.\n\nWhat restaurant chain with over 15,000 locations is a sister franchise to Wing Street?",
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
| Decider v1.1 | `yes` — Answerable | `no` — Unanswerable | Different answer |
| Jev | `yes` — Answerable | `yes` — Answerable | Same answer |
| Microsoft Decision-1 | `yes` — Answerable | `no` — Unanswerable | Different answer |
| Clef | `yes` — Answerable | `no` — Unanswerable | Different answer |
| Luna Decisions | `yes` — Answerable | `yes` — Answerable | Same answer |
| Clef Flash | `yes` — Answerable | `yes` — Answerable | Same answer |
| Strands Decider | `no` — Unanswerable | `no` — Unanswerable | Same answer |
| GLiNER2.5 Decide | `yes` — Answerable | `no` — Unanswerable | Different answer |
| Laya | `no` — Unanswerable | `no` — Unanswerable | Same answer |
| CalDec v1 | `no` — Unanswerable | `no` — Unanswerable | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `selfaware/a84fd3aac838986e9bc9/event_count/2/clean-source_first_selfaware_short_contexts_full_0127`

**Input fingerprint:** `cf71730f0850ceebed6662f6bc6a19e2364b65b5258cdbacd49b058f9beaa480`

| Change | Recorded version |
| --- | --- |
| Extra events | Add 2 unrelated events |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/uncertainty-monitoring/selfaware-a84fd3aac838986e9bc9.md).
