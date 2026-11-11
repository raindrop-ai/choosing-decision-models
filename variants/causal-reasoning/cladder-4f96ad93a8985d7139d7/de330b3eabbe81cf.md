# Evidence order · Present the evidence in reverse order variant

[Original question](../../../questions/causal-reasoning/cladder-4f96ad93a8985d7139d7.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: For hospitalized individuals, the correlation between respiratory issues and broken bones is -0.25. Broken bones has a direct effect on hospitalization status.
> Respiratory issues has a direct effect on hospitalization status.

## Question

> If we look at hospitalized individuals, does it mean that respiratory issues affects broken bones?

## Answer choices

- **yes.** Yes
- **no.** No

**Reference answer:** `no`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: For hospitalized individuals, the correlation between respiratory issues and broken bones is -0.25. Broken bones has a direct effect on hospitalization status.\nRespiratory issues has a direct effect on hospitalization status.",
  "question": "If we look at hospitalized individuals, does it mean that respiratory issues affects broken bones?",
  "choices": {
    "yes": "Yes",
    "no": "No"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `no` — No | `no` — No | Same answer |
| Decider v1.1 | `no` — No | `no` — No | Same answer |
| Jev | `no` — No | `no` — No | Same answer |
| Microsoft Decision-1 | `no` — No | `yes` — Yes | Different answer |
| Clef | `no` — No | `no` — No | Same answer |
| Luna Decisions | `no` — No | `no` — No | Same answer |
| Clef Flash | `no` — No | `no` — No | Same answer |
| Strands Decider | `no` — No | `no` — No | Same answer |
| GLiNER2.5 Decide | `no` — No | `yes` — Yes | Different answer |
| Laya | `no` — No | `no` — No | Same answer |
| CalDec v1 | `yes` — Yes | `yes` — Yes | Same answer |

**Ordering comparison:** literal requested source unit permutation. Only the exact matched comparison sets contribute to the reported ordering contrasts.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `cladder/4f96ad93a8985d7139d7/presentation_order/reverse_presentation/clean-bare_causal_premise_order_full_0053`

**Input fingerprint:** `66fb6fae3185066529d067f2db417ea5e7741799a8c2664f119afbaa5df42262`

| Change | Recorded version |
| --- | --- |
| Evidence order | Present the evidence in reverse order |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/causal-reasoning/cladder-4f96ad93a8985d7139d7.md).
