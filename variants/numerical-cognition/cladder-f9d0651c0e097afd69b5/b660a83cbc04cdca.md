# Option order · Move the first answer choice to the end variant

[Original question](../../../questions/numerical-cognition/cladder-f9d0651c0e097afd69b5.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** answer choices or their order.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Pexu has a direct effect on hwax. Hwax has a direct effect on rukz.
> The overall probability of pexu is 44%. For those who are not pexu, the probability of rukz is 55%. For those who are pexu, the probability of rukz is 59%.

## Question

> Is rukz less likely than not rukz overall?

## Answer choices

- **no.** No
- **yes.** Yes

**Reference answer:** `no`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Pexu has a direct effect on hwax. Hwax has a direct effect on rukz.\nThe overall probability of pexu is 44%. For those who are not pexu, the probability of rukz is 55%. For those who are pexu, the probability of rukz is 59%.",
  "question": "Is rukz less likely than not rukz overall?",
  "choices": {
    "no": "No",
    "yes": "Yes"
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
| Strands Decider | `no` — No | `no` — No | Same answer |
| GLiNER2.5 Decide | `no` — No | `no` — No | Same answer |
| Laya | `yes` — Yes | `yes` — Yes | Same answer |
| CalDec v1 | `yes` — Yes | `yes` — Yes | Same answer |

Clef and Clef Flash sort answer choices in their published input-processing code. Their choice-order results describe that preprocessing.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `cladder/f9d0651c0e097afd69b5/option_order/rotate_1`

**Input fingerprint:** `4d335212d442a7c7891589ae654a61e39e31f1b5ed7633290a23ffcee3e17111`

| Change | Recorded version |
| --- | --- |
| Option order | Move the first answer choice to the end |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/numerical-cognition/cladder-f9d0651c0e097afd69b5.md).
