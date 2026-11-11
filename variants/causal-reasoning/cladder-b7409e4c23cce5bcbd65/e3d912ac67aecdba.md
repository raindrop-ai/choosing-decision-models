# Evidence order · Present the evidence in a shuffled order variant

[Original question](../../../questions/causal-reasoning/cladder-b7409e4c23cce5bcbd65.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Hwax has a direct effect on rukz. For those who are pexu, the probability of rukz is 52%. Pexu has a direct effect on hwax. For those who are not pexu, the probability of rukz is 52%.

## Question

> Does pexu positively affect rukz through hwax?

## Answer choices

- **yes.** Yes
- **no.** No

**Reference answer:** `no`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Hwax has a direct effect on rukz. For those who are pexu, the probability of rukz is 52%. Pexu has a direct effect on hwax. For those who are not pexu, the probability of rukz is 52%.",
  "question": "Does pexu positively affect rukz through hwax?",
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
| Microsoft Decision-1 | `no` — No | `no` — No | Same answer |
| Clef | `no` — No | `no` — No | Same answer |
| Luna Decisions | `no` — No | `no` — No | Same answer |
| Clef Flash | `no` — No | `no` — No | Same answer |
| Strands Decider | `yes` — Yes | `yes` — Yes | Same answer |
| GLiNER2.5 Decide | `yes` — Yes | `yes` — Yes | Same answer |
| Laya | `yes` — Yes | `yes` — Yes | Same answer |
| CalDec v1 | `yes` — Yes | `yes` — Yes | Same answer |

**Ordering comparison:** literal units with boundary layout change. Only the exact matched comparison sets contribute to the reported ordering contrasts.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `cladder/b7409e4c23cce5bcbd65/presentation_order/shuffled_presentation/clean-mixed_causal_arithmetic_full_0002`

**Input fingerprint:** `9eeca2cb21852c59e1eda49ef182a242b1d9c1cf80c6e068bb60fff543e545f7`

| Change | Recorded version |
| --- | --- |
| Evidence order | Present the evidence in a shuffled order |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/causal-reasoning/cladder-b7409e4c23cce5bcbd65.md).
