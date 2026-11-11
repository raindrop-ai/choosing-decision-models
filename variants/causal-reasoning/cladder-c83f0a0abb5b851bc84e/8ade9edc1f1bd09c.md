# Irrelevant details · Add a larger amount of irrelevant detail variant

[Original question](../../../questions/causal-reasoning/cladder-c83f0a0abb5b851bc84e.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> The notebook has a linen cover. The cover has an embossed title. The page edges are uneven. The binding is stitched. A ribbon marks a page. The back cover has a pocket.
>
> Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Smoking has a direct effect on effort and lactose intolerance. Effort has a direct effect on lactose intolerance.
> For nonsmokers and are lazy, the probability of being lactose intolerant is 47%. For nonsmokers and are hard-working, the probability of being lactose intolerant is 88%. For smokers and are lazy, the probability of being lactose intolerant is 23%. For smokers and are hard-working, the probability of being lactose intolerant is 54%. For nonsmokers, the probability of being hard-working is 40%. For smokers, the probability of being hard-working is 61%.

## Question

> Does smoking positively affect lactose intolerance through effort?

## Answer choices

- **yes.** Yes
- **no.** No

**Reference answer:** `yes`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "The notebook has a linen cover. The cover has an embossed title. The page edges are uneven. The binding is stitched. A ribbon marks a page. The back cover has a pocket.\n\nImagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Smoking has a direct effect on effort and lactose intolerance. Effort has a direct effect on lactose intolerance.\nFor nonsmokers and are lazy, the probability of being lactose intolerant is 47%. For nonsmokers and are hard-working, the probability of being lactose intolerant is 88%. For smokers and are lazy, the probability of being lactose intolerant is 23%. For smokers and are hard-working, the probability of being lactose intolerant is 54%. For nonsmokers, the probability of being hard-working is 40%. For smokers, the probability of being hard-working is 61%.",
  "question": "Does smoking positively affect lactose intolerance through effort?",
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
| Microsoft Decision-1 | `no` — No | `no` — No | Same answer |
| Clef | `no` — No | `no` — No | Same answer |
| Luna Decisions | `no` — No | `yes` — Yes | Different answer |
| Clef Flash | `yes` — Yes | `yes` — Yes | Same answer |
| Strands Decider | `yes` — Yes | `yes` — Yes | Same answer |
| GLiNER2.5 Decide | `yes` — Yes | `yes` — Yes | Same answer |
| Laya | `no` — No | `yes` — Yes | Different answer |
| CalDec v1 | `yes` — Yes | `yes` — Yes | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `cladder/c83f0a0abb5b851bc84e/irrelevant_details/high/clean-source_first_cladder_short_contexts_full_0130`

**Input fingerprint:** `dfcbb2eb4c63b0354143e1357bf5f27db4b1492a97ffd8b3aa7ec8e7d568e81e`

| Change | Recorded version |
| --- | --- |
| Irrelevant details | Add a larger amount of irrelevant detail |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/causal-reasoning/cladder-c83f0a0abb5b851bc84e.md).
