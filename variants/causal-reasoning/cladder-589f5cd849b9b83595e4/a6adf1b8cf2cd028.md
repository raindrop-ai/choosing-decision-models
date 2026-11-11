# Similar distractors · Add fewer similar but irrelevant items variant

[Original question](../../../questions/causal-reasoning/cladder-589f5cd849b9b83595e4.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Rovek has a direct effect on tanil. Tanil has a direct effect on dorev.
>
> Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Tanning salon treatment has a direct effect on black hair. Going to the beach has a direct effect on black hair.
> For people not using tanning salon treatments, the probability of black hair is 76%. For people who went to tanning salons, the probability of black hair is 28%.

## Question

> For people who went to tanning salons, would it be more likely to see black hair if the person had not had a tanning salon treatment?

## Answer choices

- **yes.** Yes
- **no.** No

**Reference answer:** `yes`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Rovek has a direct effect on tanil. Tanil has a direct effect on dorev.\n\nImagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Tanning salon treatment has a direct effect on black hair. Going to the beach has a direct effect on black hair.\nFor people not using tanning salon treatments, the probability of black hair is 76%. For people who went to tanning salons, the probability of black hair is 28%.",
  "question": "For people who went to tanning salons, would it be more likely to see black hair if the person had not had a tanning salon treatment?",
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
| Strands Decider | `no` — No | `no` — No | Same answer |
| GLiNER2.5 Decide | `yes` — Yes | `yes` — Yes | Same answer |
| Laya | `no` — No | `no` — No | Same answer |
| CalDec v1 | `no` — No | `no` — No | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `cladder/589f5cd849b9b83595e4/similar_distractors/low/clean-source_first_causal_new_distractors_full_0178`

**Input fingerprint:** `177c13a2d858778c6e7813f37cddf574032e785d69f92cad8eabce19dbc67a09`

| Change | Recorded version |
| --- | --- |
| Similar distractors | Add fewer similar but irrelevant items |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/causal-reasoning/cladder-589f5cd849b9b83595e4.md).
