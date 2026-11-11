# Evidence order · Reverse the values in the expression variant

[Original question](../../../questions/uncertainty-monitoring/selfaware-a21b560edfa507c432cb.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> If revenge is sweet, and revenge is a dish that’s best served cold, then is revenge ice cream?

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
  "state": "If revenge is sweet, and revenge is a dish that’s best served cold, then is revenge ice cream?",
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
| Jev | `no` — Unanswerable | `no` — Unanswerable | Same answer |
| Microsoft Decision-1 | `no` — Unanswerable | `no` — Unanswerable | Same answer |
| Clef | `no` — Unanswerable | `yes` — Answerable | Different answer |
| Luna Decisions | `yes` — Answerable | `yes` — Answerable | Same answer |
| Clef Flash | `no` — Unanswerable | `no` — Unanswerable | Same answer |
| Strands Decider | `no` — Unanswerable | `no` — Unanswerable | Same answer |
| GLiNER2.5 Decide | `no` — Unanswerable | `no` — Unanswerable | Same answer |
| Laya | `yes` — Answerable | `no` — Unanswerable | Different answer |
| CalDec v1 | `yes` — Answerable | `no` — Unanswerable | Different answer |

**Ordering comparison:** literal local or custom unit permutation. Only the exact matched comparison sets contribute to the reported ordering contrasts.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `selfaware/a21b560edfa507c432cb/presentation_order/reverse_native_operand_list/clean-source_first_operand_process_agnews_full_0269`

**Input fingerprint:** `4706678f234a445652c1f170bec23c24a66e84f1e887dc2cd5789309b53176c3`

| Change | Recorded version |
| --- | --- |
| Evidence order | Reverse the values in the expression |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/uncertainty-monitoring/selfaware-a21b560edfa507c432cb.md).
