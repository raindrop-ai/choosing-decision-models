# Irrelevant details · Add a larger amount of irrelevant detail variant

[Original question](../../../questions/causal-reasoning/cladder-1cb2489995a2e0ea925b.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> The notebook has a linen cover. The cover has an embossed title. The page edges are uneven. The binding is stitched. A ribbon marks a page. The back cover has a pocket.
>
> Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Tanning salon treatment has a direct effect on skin. Going to the beach has a direct effect on skin.
> For people not using tanning salon treatments, the probability of tanned skin is 6%. For people who went to tanning salons, the probability of tanned skin is 57%.

## Question

> Will tanning salon treatment decrease the chance of tanned skin?

## Answer choices

- **yes.** Yes
- **no.** No

**Reference answer:** `no`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "The notebook has a linen cover. The cover has an embossed title. The page edges are uneven. The binding is stitched. A ribbon marks a page. The back cover has a pocket.\n\nImagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Tanning salon treatment has a direct effect on skin. Going to the beach has a direct effect on skin.\nFor people not using tanning salon treatments, the probability of tanned skin is 6%. For people who went to tanning salons, the probability of tanned skin is 57%.",
  "question": "Will tanning salon treatment decrease the chance of tanned skin?",
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
| Strands Decider | `no` — No | `yes` — Yes | Different answer |
| GLiNER2.5 Decide | `no` — No | `no` — No | Same answer |
| Laya | `yes` — Yes | `yes` — Yes | Same answer |
| CalDec v1 | `no` — No | `no` — No | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `cladder/1cb2489995a2e0ea925b/irrelevant_details/high/clean-source_first_cladder_short_contexts_full_0130`

**Input fingerprint:** `17f692633bca09e3da7bddd64f7edcaf2fd2610876a4fd2b127bb21f85869fe6`

| Change | Recorded version |
| --- | --- |
| Irrelevant details | Add a larger amount of irrelevant detail |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/causal-reasoning/cladder-1cb2489995a2e0ea925b.md).
