# Evidence order · Present the evidence in reverse order variant

[Original question](../../../questions/causal-reasoning/cladder-c574937d10a7beec03bb.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: For those who are pexu, the probability of rukz is 66%. For those who are not pexu, the probability of rukz is 74%. Kraz has a direct effect on rukz.
> Hwax has a direct effect on rukz. Pexu has a direct effect on kraz and hwax.

## Question

> Does pexu negatively affect rukz through hwax and kraz?

## Answer choices

- **yes.** Yes
- **no.** No

**Reference answer:** `yes`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: For those who are pexu, the probability of rukz is 66%. For those who are not pexu, the probability of rukz is 74%. Kraz has a direct effect on rukz.\nHwax has a direct effect on rukz. Pexu has a direct effect on kraz and hwax.",
  "question": "Does pexu negatively affect rukz through hwax and kraz?",
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
| Microsoft Decision-1 | `yes` — Yes | `no` — No | Different answer |
| Clef | `yes` — Yes | `yes` — Yes | Same answer |
| Luna Decisions | `no` — No | `no` — No | Same answer |
| Clef Flash | `yes` — Yes | `yes` — Yes | Same answer |
| Strands Decider | `yes` — Yes | `yes` — Yes | Same answer |
| GLiNER2.5 Decide | `yes` — Yes | `yes` — Yes | Same answer |
| Laya | `yes` — Yes | `yes` — Yes | Same answer |
| CalDec v1 | `yes` — Yes | `yes` — Yes | Same answer |

**Ordering comparison:** literal requested source unit permutation. Only the exact matched comparison sets contribute to the reported ordering contrasts.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `cladder/c574937d10a7beec03bb/presentation_order/reverse_presentation/clean-bare_causal_premise_order_full_0053`

**Input fingerprint:** `4d7616b86452d458fc9c6e88a4915c8eb1dd9c6a2d89a07ab514f89411870a47`

| Change | Recorded version |
| --- | --- |
| Evidence order | Present the evidence in reverse order |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/causal-reasoning/cladder-c574937d10a7beec03bb.md).
