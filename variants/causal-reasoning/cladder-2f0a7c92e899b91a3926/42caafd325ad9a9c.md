# Similar distractors · Add more similar but irrelevant items variant

[Original question](../../../questions/causal-reasoning/cladder-2f0a7c92e899b91a3926.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Rovek has a direct effect on tanil. Tanil has a direct effect on dorev.
>
> Kesil has a direct effect on vemak. Vemak has a direct effect on pirun.
>
> Neral has a direct effect on sovik. Sovik has a direct effect on ralen.
>
> Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Eating citrus has a direct effect on vitmain C. Vitmain C has a direct effect on scurvy.
> For patients not consuming citrus, the probability of scurvy is 74%. For patients consuming citrus, the probability of scurvy is 48%.

## Question

> Will citrus intake decrease the chance of scurvy?

## Answer choices

- **yes.** Yes
- **no.** No

**Reference answer:** `yes`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Rovek has a direct effect on tanil. Tanil has a direct effect on dorev.\n\nKesil has a direct effect on vemak. Vemak has a direct effect on pirun.\n\nNeral has a direct effect on sovik. Sovik has a direct effect on ralen.\n\nImagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Eating citrus has a direct effect on vitmain C. Vitmain C has a direct effect on scurvy.\nFor patients not consuming citrus, the probability of scurvy is 74%. For patients consuming citrus, the probability of scurvy is 48%.",
  "question": "Will citrus intake decrease the chance of scurvy?",
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
| Luna Decisions | `yes` — Yes | `yes` — Yes | Same answer |
| Clef Flash | `yes` — Yes | `yes` — Yes | Same answer |
| Strands Decider | `yes` — Yes | `yes` — Yes | Same answer |
| GLiNER2.5 Decide | `yes` — Yes | `yes` — Yes | Same answer |
| Laya | `yes` — Yes | `yes` — Yes | Same answer |
| CalDec v1 | `yes` — Yes | `yes` — Yes | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `cladder/2f0a7c92e899b91a3926/similar_distractors/high/clean-source_first_causal_new_distractors_full_0178`

**Input fingerprint:** `5314bdb16d02a7f26e13d2b0857beca75d4bbfb49985913468547fdd27226587`

| Change | Recorded version |
| --- | --- |
| Similar distractors | Add more similar but irrelevant items |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/causal-reasoning/cladder-2f0a7c92e899b91a3926.md).
