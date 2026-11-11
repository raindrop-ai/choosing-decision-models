# Evidence order · Swap qualifying phrases within a larger phrase variant

[Original question](../../../questions/uncertainty-monitoring/selfaware-29334c1ca9df70f176dd.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> "Billy Blaze, an 8-year-old genius who in his backyard constructed a spaceship from old soup cans and other household objects called ""The Bean-with-Bacon Megarocket"" puts on his brother's football helmet and becomes what character in a video game series?"

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
  "state": "\"Billy Blaze, an 8-year-old genius who in his backyard constructed a spaceship from old soup cans and other household objects called \"\"The Bean-with-Bacon Megarocket\"\" puts on his brother's football helmet and becomes what character in a video game series?\"",
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
| Jev | `yes` — Answerable | `yes` — Answerable | Same answer |
| Microsoft Decision-1 | `yes` — Answerable | `yes` — Answerable | Same answer |
| Clef | `yes` — Answerable | `yes` — Answerable | Same answer |
| Luna Decisions | `yes` — Answerable | `yes` — Answerable | Same answer |
| Clef Flash | `yes` — Answerable | `yes` — Answerable | Same answer |
| Strands Decider | `no` — Unanswerable | `yes` — Answerable | Different answer |
| GLiNER2.5 Decide | `yes` — Answerable | `yes` — Answerable | Same answer |
| Laya | `yes` — Answerable | `yes` — Answerable | Same answer |
| CalDec v1 | `no` — Unanswerable | `no` — Unanswerable | Same answer |

**Ordering comparison:** coupled wording reference chronology or representation. Only the exact matched comparison sets contribute to the reported ordering contrasts.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `selfaware/29334c1ca9df70f176dd/presentation_order/swap_nested_native_qualifier_units/clean-source_first_nested_bound_constraint_orders_full_0318`

**Input fingerprint:** `5b7acd9319781c88f58b1f23c0c7a9d43fa750dadc1eb75de1e22da18d99f12f`

| Change | Recorded version |
| --- | --- |
| Evidence order | Swap qualifying phrases within a larger phrase |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/uncertainty-monitoring/selfaware-29334c1ca9df70f176dd.md).
