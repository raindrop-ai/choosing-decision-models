# Irrelevant details · Add a small amount of irrelevant detail variant

[Original question](../../../questions/causal-reasoning/cladder-8bb7bc8217de7fa40d2a.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> The notebook has a linen cover.
>
> Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Jyka has a direct effect on hwax and lirg. Gyzp has a direct effect on hwax and lirg. Hwax has a direct effect on lirg. Gyzp is unobserved.
> For those who are not jyka, the probability of lirg is 97%. For those who are jyka, the probability of lirg is 51%.

## Question

> For those who are jyka, would it be less likely to see lirg if the individual was not jyka?

## Answer choices

- **yes.** Yes
- **no.** No

**Reference answer:** `no`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "The notebook has a linen cover.\n\nImagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Jyka has a direct effect on hwax and lirg. Gyzp has a direct effect on hwax and lirg. Hwax has a direct effect on lirg. Gyzp is unobserved.\nFor those who are not jyka, the probability of lirg is 97%. For those who are jyka, the probability of lirg is 51%.",
  "question": "For those who are jyka, would it be less likely to see lirg if the individual was not jyka?",
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
| Luna Decisions | `no` — No | `yes` — Yes | Different answer |
| Clef Flash | `no` — No | `no` — No | Same answer |
| Strands Decider | `yes` — Yes | `yes` — Yes | Same answer |
| GLiNER2.5 Decide | `yes` — Yes | `yes` — Yes | Same answer |
| Laya | `no` — No | `yes` — Yes | Different answer |
| CalDec v1 | `no` — No | `no` — No | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `cladder/8bb7bc8217de7fa40d2a/irrelevant_details/low/clean-source_first_cladder_short_contexts_full_0129`

**Input fingerprint:** `1f10cf8e932fec4bf2903129e4fdf6272dfe2c6290af46c3cbcb9af8981caec8`

| Change | Recorded version |
| --- | --- |
| Irrelevant details | Add a small amount of irrelevant detail |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/causal-reasoning/cladder-8bb7bc8217de7fa40d2a.md).
