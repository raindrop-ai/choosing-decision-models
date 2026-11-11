# Unrelated examples · No worked example (absence-control recipe) variant

[Original question](../../../questions/causal-reasoning/cladder-96489cd386a03a35998f.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> The notebook's cover has a stitched border and an embossed title.
>
> Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Encouragement level has a direct effect on studying habit and exam score. Studying habit has a direct effect on exam score.
> For students who are not encouraged, the probability of high exam score is 45%. For students who are encouraged, the probability of high exam score is 89%.

## Question

> Will encouragement decrease the chance of high exam score?

## Answer choices

- **yes.** Yes
- **no.** No

**Reference answer:** `no`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "The notebook's cover has a stitched border and an embossed title.\n\nImagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Encouragement level has a direct effect on studying habit and exam score. Studying habit has a direct effect on exam score.\nFor students who are not encouraged, the probability of high exam score is 45%. For students who are encouraged, the probability of high exam score is 89%.",
  "question": "Will encouragement decrease the chance of high exam score?",
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
| Laya | `no` — No | `yes` — Yes | Different answer |
| CalDec v1 | `yes` — Yes | `yes` — Yes | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `cladder/96489cd386a03a35998f/examples/absent/clean-source_first_cladder_short_contexts_full_0130`

**Input fingerprint:** `ea3bcc6e36bf4df1b8e9d4a0d8a3a62ba61f703c86e7f302b49a77ad18ffa606`

| Change | Recorded version |
| --- | --- |
| Unrelated examples | No worked example (absence-control recipe) |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/causal-reasoning/cladder-96489cd386a03a35998f.md).
