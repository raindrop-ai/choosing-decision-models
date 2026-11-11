# Similar distractors · Add fewer similar but irrelevant items variant

[Original question](../../../questions/numerical-cognition/cladder-4ac69ecbb53e1c31b43a.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Rovek has a direct effect on tanil. Tanil has a direct effect on dorev.
>
> Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Jyka has a direct effect on yupt. Kwox has a direct effect on yupt.
> The overall probability of jyka is 77%. For those who are not jyka, the probability of kwox is 67%. For those who are jyka, the probability of kwox is 67%.

## Question

> Is kwox less likely than not kwox overall?

## Answer choices

- **yes.** Yes
- **no.** No

**Reference answer:** `no`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Rovek has a direct effect on tanil. Tanil has a direct effect on dorev.\n\nImagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Jyka has a direct effect on yupt. Kwox has a direct effect on yupt.\nThe overall probability of jyka is 77%. For those who are not jyka, the probability of kwox is 67%. For those who are jyka, the probability of kwox is 67%.",
  "question": "Is kwox less likely than not kwox overall?",
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
| Strands Decider | `no` — No | `no` — No | Same answer |
| GLiNER2.5 Decide | `no` — No | `no` — No | Same answer |
| Laya | `no` — No | `no` — No | Same answer |
| CalDec v1 | `yes` — Yes | `yes` — Yes | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `cladder/4ac69ecbb53e1c31b43a/similar_distractors/low/clean-source_first_causal_new_distractors_full_0178`

**Input fingerprint:** `dcce57eb34a39c9292e317ee99fccd6e4f2c4dc3d36ce01c00e97aac4a92ec0f`

| Change | Recorded version |
| --- | --- |
| Similar distractors | Add fewer similar but irrelevant items |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/numerical-cognition/cladder-4ac69ecbb53e1c31b43a.md).
