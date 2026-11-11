# Evidence order · Swap a qualifying phrase and the question variant

[Original question](../../../questions/uncertainty-monitoring/selfaware-a84fd3aac838986e9bc9.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> With over 15,000 locations, what restaurant chain is a sister franchise to Wing Street?

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
  "state": "With over 15,000 locations, what restaurant chain is a sister franchise to Wing Street?",
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
| GLiDE v1.2 | `yes` — Answerable | `no` — Unanswerable | Different answer |
| Decider v1.1 | `yes` — Answerable | `yes` — Answerable | Same answer |
| Jev | `yes` — Answerable | `yes` — Answerable | Same answer |
| Microsoft Decision-1 | `yes` — Answerable | `yes` — Answerable | Same answer |
| Clef | `yes` — Answerable | `yes` — Answerable | Same answer |
| Luna Decisions | `yes` — Answerable | `yes` — Answerable | Same answer |
| Clef Flash | `yes` — Answerable | `yes` — Answerable | Same answer |
| Strands Decider | `no` — Unanswerable | `no` — Unanswerable | Same answer |
| GLiNER2.5 Decide | `yes` — Answerable | `no` — Unanswerable | Different answer |
| Laya | `no` — Unanswerable | `yes` — Answerable | Different answer |
| CalDec v1 | `no` — Unanswerable | `yes` — Answerable | Different answer |

**Ordering comparison:** coupled wording reference chronology or representation. Only the exact matched comparison sets contribute to the reported ordering contrasts.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `selfaware/a84fd3aac838986e9bc9/presentation_order/swap_native_qualifier_query_units/clean-source_first_scoped_qualifier_given_operand_orders_full_0314`

**Input fingerprint:** `1975a85e4bcf4bf3951293d6549bb5d123177861ad2776489b067ecdacebfeea`

| Change | Recorded version |
| --- | --- |
| Evidence order | Swap a qualifying phrase and the question |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/uncertainty-monitoring/selfaware-a84fd3aac838986e9bc9.md).
