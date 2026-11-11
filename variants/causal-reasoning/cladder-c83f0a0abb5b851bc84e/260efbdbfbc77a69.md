# Similar distractors · Add fewer similar but irrelevant items variant

[Original question](../../../questions/causal-reasoning/cladder-c83f0a0abb5b851bc84e.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Rovek has a direct effect on tanil. Tanil has a direct effect on dorev.
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
  "state": "Rovek has a direct effect on tanil. Tanil has a direct effect on dorev.\n\nImagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Smoking has a direct effect on effort and lactose intolerance. Effort has a direct effect on lactose intolerance.\nFor nonsmokers and are lazy, the probability of being lactose intolerant is 47%. For nonsmokers and are hard-working, the probability of being lactose intolerant is 88%. For smokers and are lazy, the probability of being lactose intolerant is 23%. For smokers and are hard-working, the probability of being lactose intolerant is 54%. For nonsmokers, the probability of being hard-working is 40%. For smokers, the probability of being hard-working is 61%.",
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

**Variant ID:** `cladder/c83f0a0abb5b851bc84e/similar_distractors/low/clean-source_first_causal_new_distractors_full_0178`

**Input fingerprint:** `1c1ca477c1a0f783cb58d161d02e92951019e012c437870bb6c6616b7cea7e7b`

| Change | Recorded version |
| --- | --- |
| Similar distractors | Add fewer similar but irrelevant items |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/causal-reasoning/cladder-c83f0a0abb5b851bc84e.md).
