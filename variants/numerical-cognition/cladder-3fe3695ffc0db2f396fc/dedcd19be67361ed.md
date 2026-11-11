# Evidence order · Present the evidence in a shuffled order variant

[Original question](../../../questions/numerical-cognition/cladder-3fe3695ffc0db2f396fc.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Yupt has a direct effect on kwox. For those who are not jyka, the probability of kwox is 66%.
> Jyka has a direct effect on yupt. The overall probability of jyka is 59%. For those who are jyka, the probability of kwox is 77%.

## Question

> Is kwox more likely than not kwox overall?

## Answer choices

- **yes.** Yes
- **no.** No

**Reference answer:** `yes`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Yupt has a direct effect on kwox. For those who are not jyka, the probability of kwox is 66%.\nJyka has a direct effect on yupt. The overall probability of jyka is 59%. For those who are jyka, the probability of kwox is 77%.",
  "question": "Is kwox more likely than not kwox overall?",
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
| Laya | `yes` — Yes | `no` — No | Different answer |
| CalDec v1 | `no` — No | `yes` — Yes | Different answer |

**Ordering comparison:** literal requested source unit permutation. Only the exact matched comparison sets contribute to the reported ordering contrasts.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `cladder/3fe3695ffc0db2f396fc/presentation_order/shuffled_presentation/clean-bare_causal_premise_order_full_0034`

**Input fingerprint:** `45fe68549e6f9742c02c9b72ef6485f64c2817b300e0b45445eb9dadfa276c08`

| Change | Recorded version |
| --- | --- |
| Evidence order | Present the evidence in a shuffled order |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/numerical-cognition/cladder-3fe3695ffc0db2f396fc.md).
