# Evidence order · Present the evidence in a shuffled order variant

[Original question](../../../questions/causal-reasoning/cladder-a1f341b7c52630c0b7a3.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Wibl has a direct effect on uvzi. For those who are zuph, the probability of uvzi is 73%. Zuph has a direct effect on wibl. For those who are not zuph, the probability of uvzi is 70%.

## Question

> For those who are zuph, would it be less likely to see uvzi if the individual was not zuph?

## Answer choices

- **yes.** Yes
- **no.** No

**Reference answer:** `yes`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Wibl has a direct effect on uvzi. For those who are zuph, the probability of uvzi is 73%. Zuph has a direct effect on wibl. For those who are not zuph, the probability of uvzi is 70%.",
  "question": "For those who are zuph, would it be less likely to see uvzi if the individual was not zuph?",
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
| GLiDE v1.2 | `yes` — Yes | `yes` — Yes | Same answer |
| Decider v1.1 | `yes` — Yes | `yes` — Yes | Same answer |
| Jev | `yes` — Yes | `yes` — Yes | Same answer |
| Microsoft Decision-1 | `yes` — Yes | `yes` — Yes | Same answer |
| Clef | `yes` — Yes | `yes` — Yes | Same answer |
| Luna Decisions | `no` — No | `yes` — Yes | Different answer |
| Clef Flash | `yes` — Yes | `yes` — Yes | Same answer |
| Strands Decider | `no` — No | `no` — No | Same answer |
| GLiNER2.5 Decide | `yes` — Yes | `yes` — Yes | Same answer |
| Laya | `yes` — Yes | `no` — No | Different answer |
| CalDec v1 | `no` — No | `no` — No | Same answer |

**Ordering comparison:** literal units with boundary layout change. Only the exact matched comparison sets contribute to the reported ordering contrasts.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `cladder/a1f341b7c52630c0b7a3/presentation_order/shuffled_presentation/clean-mixed_causal_arithmetic_full_0002`

**Input fingerprint:** `13cbf54e9452c2105c1b4d59e56f45f92fc17db5ffd59db9b9b8771cf577be07`

| Change | Recorded version |
| --- | --- |
| Evidence order | Present the evidence in a shuffled order |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/causal-reasoning/cladder-a1f341b7c52630c0b7a3.md).
