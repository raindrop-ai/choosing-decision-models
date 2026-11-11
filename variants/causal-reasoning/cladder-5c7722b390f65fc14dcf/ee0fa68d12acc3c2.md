# Unrelated examples · No worked example (absence-control recipe) variant

[Original question](../../../questions/causal-reasoning/cladder-5c7722b390f65fc14dcf.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> The notebook's cover has a stitched border and an embossed title.
>
> Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Yupt has a direct effect on zupj and muvq. Zupj has a direct effect on muvq.
> For those who are not yupt and are not zupj, the probability of muvq is 54%. For those who are not yupt and are zupj, the probability of muvq is 18%. For those who are yupt and are not zupj, the probability of muvq is 62%. For those who are yupt and are zupj, the probability of muvq is 46%. For those who are not yupt, the probability of zupj is 85%. For those who are yupt, the probability of zupj is 14%.

## Question

> If we disregard the mediation effect through zupj, would yupt positively affect muvq?

## Answer choices

- **yes.** Yes
- **no.** No

**Reference answer:** `yes`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "The notebook's cover has a stitched border and an embossed title.\n\nImagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Yupt has a direct effect on zupj and muvq. Zupj has a direct effect on muvq.\nFor those who are not yupt and are not zupj, the probability of muvq is 54%. For those who are not yupt and are zupj, the probability of muvq is 18%. For those who are yupt and are not zupj, the probability of muvq is 62%. For those who are yupt and are zupj, the probability of muvq is 46%. For those who are not yupt, the probability of zupj is 85%. For those who are yupt, the probability of zupj is 14%.",
  "question": "If we disregard the mediation effect through zupj, would yupt positively affect muvq?",
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
| Laya | `yes` — Yes | `yes` — Yes | Same answer |
| CalDec v1 | `no` — No | `yes` — Yes | Different answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `cladder/5c7722b390f65fc14dcf/examples/absent/clean-source_first_cladder_short_contexts_full_0130`

**Input fingerprint:** `d84d58d740e2630ffd01a0278155e4e58c9f057148a6db87b73bd145026beb73`

| Change | Recorded version |
| --- | --- |
| Unrelated examples | No worked example (absence-control recipe) |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/causal-reasoning/cladder-5c7722b390f65fc14dcf.md).
