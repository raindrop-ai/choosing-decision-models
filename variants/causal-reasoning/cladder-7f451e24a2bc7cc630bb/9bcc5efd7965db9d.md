# Evidence order · Present the evidence in a shuffled order variant

[Original question](../../../questions/causal-reasoning/cladder-7f451e24a2bc7cc630bb.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Other unobserved factors has a direct effect on parents' social status and child's intelligence. Other unobserved factors is unobserved. liking spicy food or confounder active or high parental social status causes intelligent child. Liking spicy food has a direct effect on parents' social status and child's intelligence.
> Parents' social status has a direct effect on child's intelligence. We know that liking spicy food and confounder active causes high parental social status. We observed confounder inactive.

## Question

> Would the child is intelligent if not liking spicy food instead of liking spicy food?

## Answer choices

- **yes.** Yes
- **no.** No

**Reference answer:** `no`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Other unobserved factors has a direct effect on parents' social status and child's intelligence. Other unobserved factors is unobserved. liking spicy food or confounder active or high parental social status causes intelligent child. Liking spicy food has a direct effect on parents' social status and child's intelligence.\nParents' social status has a direct effect on child's intelligence. We know that liking spicy food and confounder active causes high parental social status. We observed confounder inactive.",
  "question": "Would the child is intelligent if not liking spicy food instead of liking spicy food?",
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
| Clef | `yes` — Yes | `no` — No | Different answer |
| Luna Decisions | `no` — No | `no` — No | Same answer |
| Clef Flash | `no` — No | `no` — No | Same answer |
| Strands Decider | `yes` — Yes | `yes` — Yes | Same answer |
| GLiNER2.5 Decide | `yes` — Yes | `yes` — Yes | Same answer |
| Laya | `no` — No | `no` — No | Same answer |
| CalDec v1 | `yes` — Yes | `yes` — Yes | Same answer |

**Ordering comparison:** literal requested source unit permutation. Only the exact matched comparison sets contribute to the reported ordering contrasts.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `cladder/7f451e24a2bc7cc630bb/presentation_order/shuffled_presentation/clean-bare_causal_premise_order_full_0053`

**Input fingerprint:** `2b984ac946984d63dcd548d5dc0bcf7bffb2593c2d106cb38f5ec3f234db0a0a`

| Change | Recorded version |
| --- | --- |
| Evidence order | Present the evidence in a shuffled order |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/causal-reasoning/cladder-7f451e24a2bc7cc630bb.md).
