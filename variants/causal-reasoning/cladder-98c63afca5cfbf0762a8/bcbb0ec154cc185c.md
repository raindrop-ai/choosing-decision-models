# Evidence order · Present the evidence in a shuffled order variant

[Original question](../../../questions/causal-reasoning/cladder-98c63afca5cfbf0762a8.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Tijw has a direct effect on tijv and gyzp. Tijw is unobserved. For those who are xevo, the probability of gyzp is 74%. Xevo has a direct effect on tijv and gyzp.
> Tijv has a direct effect on gyzp. For those who are not xevo, the probability of gyzp is 69%.

## Question

> Will xevo decrease the chance of gyzp?

## Answer choices

- **yes.** Yes
- **no.** No

**Reference answer:** `no`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Tijw has a direct effect on tijv and gyzp. Tijw is unobserved. For those who are xevo, the probability of gyzp is 74%. Xevo has a direct effect on tijv and gyzp.\nTijv has a direct effect on gyzp. For those who are not xevo, the probability of gyzp is 69%.",
  "question": "Will xevo decrease the chance of gyzp?",
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
| Laya | `yes` — Yes | `no` — No | Different answer |
| CalDec v1 | `no` — No | `no` — No | Same answer |

**Ordering comparison:** literal requested source unit permutation. Only the exact matched comparison sets contribute to the reported ordering contrasts.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `cladder/98c63afca5cfbf0762a8/presentation_order/shuffled_presentation/clean-bare_causal_premise_order_full_0053`

**Input fingerprint:** `1fc4114db6af7dedd9edc44331bdcef60d23021e656d933d8019d5300f6fd7d8`

| Change | Recorded version |
| --- | --- |
| Evidence order | Present the evidence in a shuffled order |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/causal-reasoning/cladder-98c63afca5cfbf0762a8.md).
