# Unrelated examples · Add examples unrelated to the question variant

[Original question](../../../questions/causal-reasoning/cladder-16bfee89bbdefaaa7cae.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Capitalization: “winter has arrived.” → “Winter has arrived.”
>
> Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Yupt has a direct effect on zupj. Zupj has a direct effect on muvq.
> For those who are not yupt, the probability of muvq is 28%. For those who are yupt, the probability of muvq is 39%.

## Question

> Will yupt decrease the chance of muvq?

## Answer choices

- **yes.** Yes
- **no.** No

**Reference answer:** `no`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Capitalization: “winter has arrived.” → “Winter has arrived.”\n\nImagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Yupt has a direct effect on zupj. Zupj has a direct effect on muvq.\nFor those who are not yupt, the probability of muvq is 28%. For those who are yupt, the probability of muvq is 39%.",
  "question": "Will yupt decrease the chance of muvq?",
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
| GLiNER2.5 Decide | `yes` — Yes | `yes` — Yes | Same answer |
| Laya | `no` — No | `yes` — Yes | Different answer |
| CalDec v1 | `no` — No | `yes` — Yes | Different answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `cladder/16bfee89bbdefaaa7cae/examples/irrelevant/clean-source_first_cladder_short_contexts_full_0129`

**Input fingerprint:** `4159f3511faa4dd3e57e0d1fc57ff761e18fd7f6ab09f7e0d476902beac1935f`

| Change | Recorded version |
| --- | --- |
| Unrelated examples | Add examples unrelated to the question |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/causal-reasoning/cladder-16bfee89bbdefaaa7cae.md).
