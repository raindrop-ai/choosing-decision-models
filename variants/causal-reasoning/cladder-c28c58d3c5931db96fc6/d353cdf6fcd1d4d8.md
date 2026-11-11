# Paraphrasing · Change the sentence structure variant

[Original question](../../../questions/causal-reasoning/cladder-c28c58d3c5931db96fc6.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: There is a direct causal effect from Full moon to sprinkler. There is a direct causal effect from Full moon to weather. There is a direct causal effect from Weather to ground. There is a direct causal effect from Sprinkler to ground.
> For situations where there is no full moon, the probability of wet ground is 37%. For situations where there is a full moon, the probability of wet ground is 42%.

## Question

> Will full moon increase the chance of wet ground?

## Answer choices

- **yes.** Yes
- **no.** No

**Reference answer:** `yes`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: There is a direct causal effect from Full moon to sprinkler. There is a direct causal effect from Full moon to weather. There is a direct causal effect from Weather to ground. There is a direct causal effect from Sprinkler to ground.\nFor situations where there is no full moon, the probability of wet ground is 37%. For situations where there is a full moon, the probability of wet ground is 42%.",
  "question": "Will full moon increase the chance of wet ground?",
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
| CalDec v1 | `yes` — Yes | `yes` — Yes | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `cladder/c28c58d3c5931db96fc6/paraphrasing/structural`

**Input fingerprint:** `b3b91e15a72f9020fac9be3721712e7d9d4c9dd6765180a580e7f96abfc7d94d`

| Change | Recorded version |
| --- | --- |
| Paraphrasing | Change the sentence structure |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/causal-reasoning/cladder-c28c58d3c5931db96fc6.md).
