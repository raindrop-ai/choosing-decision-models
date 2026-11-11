# Evidence order · Present the evidence in reverse order variant

[Original question](../../../questions/causal-reasoning/cladder-2e442b0d6902c7d200e7.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: For those who are yupt, the correlation between jyka and kwox is -0.15. Kwox has a direct effect on yupt. Jyka has a direct effect on yupt.

## Question

> If we look at those who are yupt, does it mean that jyka affects kwox?

## Answer choices

- **yes.** Yes
- **no.** No

**Reference answer:** `no`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: For those who are yupt, the correlation between jyka and kwox is -0.15. Kwox has a direct effect on yupt. Jyka has a direct effect on yupt.",
  "question": "If we look at those who are yupt, does it mean that jyka affects kwox?",
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
| Strands Decider | `no` — No | `yes` — Yes | Different answer |
| GLiNER2.5 Decide | `no` — No | `yes` — Yes | Different answer |
| Laya | `no` — No | `no` — No | Same answer |
| CalDec v1 | `yes` — Yes | `yes` — Yes | Same answer |

**Ordering comparison:** literal units with boundary layout change. Only the exact matched comparison sets contribute to the reported ordering contrasts.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `cladder/2e442b0d6902c7d200e7/presentation_order/reverse_presentation/clean-mixed_causal_arithmetic_full_0002`

**Input fingerprint:** `34b859b03fbf739d0e56bf5c76229a544edc57cc81d83e0863110625b7e2af39`

| Change | Recorded version |
| --- | --- |
| Evidence order | Present the evidence in reverse order |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/causal-reasoning/cladder-2e442b0d6902c7d200e7.md).
