# Unrelated examples · No worked example (absence-control recipe) variant

[Original question](../../../questions/causal-reasoning/cladder-a90b85ab6575b0fd6603.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> The notebook's cover has a stitched border and an embossed title.
>
> Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Kraz has a direct effect on pexu and rukz. Pexu has a direct effect on hwax. Hwax has a direct effect on rukz. Kraz is unobserved.
> For those who are not pexu, the probability of hwax is 43%. For those who are pexu, the probability of hwax is 92%. For those who are not pexu and are not hwax, the probability of rukz is 0%. For those who are not pexu and are hwax, the probability of rukz is 34%. For those who are pexu and are not hwax, the probability of rukz is 1%. For those who are pexu and are hwax, the probability of rukz is 33%. The overall probability of pexu is 17%.

## Question

> Does pexu negatively affect rukz through hwax?

## Answer choices

- **yes.** Yes
- **no.** No

**Reference answer:** `no`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "The notebook's cover has a stitched border and an embossed title.\n\nImagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Kraz has a direct effect on pexu and rukz. Pexu has a direct effect on hwax. Hwax has a direct effect on rukz. Kraz is unobserved.\nFor those who are not pexu, the probability of hwax is 43%. For those who are pexu, the probability of hwax is 92%. For those who are not pexu and are not hwax, the probability of rukz is 0%. For those who are not pexu and are hwax, the probability of rukz is 34%. For those who are pexu and are not hwax, the probability of rukz is 1%. For those who are pexu and are hwax, the probability of rukz is 33%. The overall probability of pexu is 17%.",
  "question": "Does pexu negatively affect rukz through hwax?",
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
| Strands Decider | `yes` — Yes | `no` — No | Different answer |
| GLiNER2.5 Decide | `no` — No | `no` — No | Same answer |
| Laya | `no` — No | `no` — No | Same answer |
| CalDec v1 | `yes` — Yes | `yes` — Yes | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `cladder/a90b85ab6575b0fd6603/examples/absent/clean-source_first_cladder_short_contexts_full_0129`

**Input fingerprint:** `076c67c87c41712874e947c9cbf7578ce5bedb78745f36213781b66bbe1a34d6`

| Change | Recorded version |
| --- | --- |
| Unrelated examples | No worked example (absence-control recipe) |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/causal-reasoning/cladder-a90b85ab6575b0fd6603.md).
