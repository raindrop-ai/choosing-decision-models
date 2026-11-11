# Unrelated examples · Add examples unrelated to the question variant

[Original question](../../../questions/causal-reasoning/cladder-a7a7d38034363c059bd7.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Capitalization: “winter has arrived.” → “Winter has arrived.”
>
> Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Kwox has a direct effect on swoq and kwoz. Swoq has a direct effect on kwoz.
> For those who are not kwox and are not swoq, the probability of kwoz is 60%. For those who are not kwox and are swoq, the probability of kwoz is 94%. For those who are kwox and are not swoq, the probability of kwoz is 15%. For those who are kwox and are swoq, the probability of kwoz is 30%. For those who are not kwox, the probability of swoq is 9%. For those who are kwox, the probability of swoq is 37%.

## Question

> If we disregard the mediation effect through swoq, would kwox negatively affect kwoz?

## Answer choices

- **yes.** Yes
- **no.** No

**Reference answer:** `yes`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Capitalization: “winter has arrived.” → “Winter has arrived.”\n\nImagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Kwox has a direct effect on swoq and kwoz. Swoq has a direct effect on kwoz.\nFor those who are not kwox and are not swoq, the probability of kwoz is 60%. For those who are not kwox and are swoq, the probability of kwoz is 94%. For those who are kwox and are not swoq, the probability of kwoz is 15%. For those who are kwox and are swoq, the probability of kwoz is 30%. For those who are not kwox, the probability of swoq is 9%. For those who are kwox, the probability of swoq is 37%.",
  "question": "If we disregard the mediation effect through swoq, would kwox negatively affect kwoz?",
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
| GLiNER2.5 Decide | `no` — No | `no` — No | Same answer |
| Laya | `no` — No | `no` — No | Same answer |
| CalDec v1 | `yes` — Yes | `yes` — Yes | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `cladder/a7a7d38034363c059bd7/examples/irrelevant/clean-source_first_cladder_short_contexts_full_0129`

**Input fingerprint:** `fb0a5c143d24b571e388939228705c87005ada3f73ff23dfba834794ddad9661`

| Change | Recorded version |
| --- | --- |
| Unrelated examples | Add examples unrelated to the question |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/causal-reasoning/cladder-a7a7d38034363c059bd7.md).
