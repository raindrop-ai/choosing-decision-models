# Evidence order · Swap a qualifying phrase and the question variant

[Original question](../../../questions/uncertainty-monitoring/selfaware-c9befb66ce11310c1323.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> In the world, how many undiscovered animals are there?

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
  "state": "In the world, how many undiscovered animals are there?",
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
| Luna Decisions | `no` — Unanswerable | `yes` — Answerable | Different answer |
| Clef Flash | `no` — Unanswerable | `no` — Unanswerable | Same answer |
| Strands Decider | `no` — Unanswerable | `no` — Unanswerable | Same answer |
| GLiNER2.5 Decide | `no` — Unanswerable | `no` — Unanswerable | Same answer |
| Laya | `yes` — Answerable | `yes` — Answerable | Same answer |
| CalDec v1 | `yes` — Answerable | `yes` — Answerable | Same answer |

**Ordering comparison:** coupled wording reference chronology or representation. Only the exact matched comparison sets contribute to the reported ordering contrasts.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `selfaware/c9befb66ce11310c1323/presentation_order/swap_native_qualifier_query_units/clean-source_first_scoped_qualifier_given_operand_orders_full_0314`

**Input fingerprint:** `42e1c4d355a3b4255d7efab3d12456f77ea82c453e259559fb64a67529e0c10c`

| Change | Recorded version |
| --- | --- |
| Evidence order | Swap a qualifying phrase and the question |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/uncertainty-monitoring/selfaware-c9befb66ce11310c1323.md).
