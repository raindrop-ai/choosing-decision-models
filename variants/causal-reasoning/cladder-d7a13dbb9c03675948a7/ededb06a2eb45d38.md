# Evidence position · Place the relevant information in the middle variant

[Original question](../../../questions/causal-reasoning/cladder-d7a13dbb9c03675948a7.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> The notebook has a linen cover.
>
> The notebook's title is embossed.
>
> Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Education level has a direct effect on skill. Skill has a direct effect on salary.
> For people without a college degree, the probability of high salary is 19%. For people with a college degree or higher, the probability of high salary is 69%.
>
> The notebook's page edges are uneven.
>
> The notebook's binding is stitched.

## Question

> Does education level positively affect salary through skill?

## Answer choices

- **yes.** Yes
- **no.** No

**Reference answer:** `yes`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "The notebook has a linen cover.\n\nThe notebook's title is embossed.\n\nImagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Education level has a direct effect on skill. Skill has a direct effect on salary.\nFor people without a college degree, the probability of high salary is 19%. For people with a college degree or higher, the probability of high salary is 69%.\n\nThe notebook's page edges are uneven.\n\nThe notebook's binding is stitched.",
  "question": "Does education level positively affect salary through skill?",
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
| GLiNER2.5 Decide | `yes` — Yes | `no` — No | Different answer |
| Laya | `yes` — Yes | `yes` — Yes | Same answer |
| CalDec v1 | `yes` — Yes | `yes` — Yes | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `cladder/d7a13dbb9c03675948a7/evidence_position/middle/clean-source_first_cladder_position_full_0133`

**Input fingerprint:** `43b94e52ca8beedd92baa5864dcf27e29e381ee417caf9b85b64acc9ed22a473`

| Change | Recorded version |
| --- | --- |
| Evidence position | Place the relevant information in the middle |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/causal-reasoning/cladder-d7a13dbb9c03675948a7.md).
