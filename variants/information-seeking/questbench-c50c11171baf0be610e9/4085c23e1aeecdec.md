# Unrelated examples · Add examples unrelated to the question variant

[Original question](../../../questions/information-seeking/questbench-c50c11171baf0be610e9.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Vincent is planning a party and wants to buy flowers for decoration. He can buy flowers in packages of 3 or in packages of 2 for $1. He also notices that balloons are sold in packages of 5, but he decides not to buy any balloons. How much money does Vincent save by buying 18 flowers at the better price instead of the more expensive option?
>
> Uppercase: comet → COMET.

## Question

> Which missing variable should be asked about to solve this problem?

## Answer choices

- **B1.** Cost of the first package option in dollars
- **G.** Cost of the balloons are sold in packages of 5

**Reference answer:** `B1`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Vincent is planning a party and wants to buy flowers for decoration. He can buy flowers in packages of 3 or in packages of 2 for $1. He also notices that balloons are sold in packages of 5, but he decides not to buy any balloons. How much money does Vincent save by buying 18 flowers at the better price instead of the more expensive option?\n\nUppercase: comet → COMET.",
  "question": "Which missing variable should be asked about to solve this problem?",
  "choices": {
    "B1": "Cost of the first package option in dollars",
    "G": "Cost of the balloons are sold in packages of 5"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `B1` — Cost of the first package option in dollars | `B1` — Cost of the first package option in dollars | Same answer |
| Decider v1.1 | `B1` — Cost of the first package option in dollars | `B1` — Cost of the first package option in dollars | Same answer |
| Jev | `B1` — Cost of the first package option in dollars | `B1` — Cost of the first package option in dollars | Same answer |
| Microsoft Decision-1 | `B1` — Cost of the first package option in dollars | `B1` — Cost of the first package option in dollars | Same answer |
| Clef | `B1` — Cost of the first package option in dollars | `B1` — Cost of the first package option in dollars | Same answer |
| Luna Decisions | `B1` — Cost of the first package option in dollars | `B1` — Cost of the first package option in dollars | Same answer |
| Clef Flash | `B1` — Cost of the first package option in dollars | `B1` — Cost of the first package option in dollars | Same answer |
| Strands Decider | `B1` — Cost of the first package option in dollars | `B1` — Cost of the first package option in dollars | Same answer |
| GLiNER2.5 Decide | `G` — Cost of the balloons are sold in packages of 5 | `G` — Cost of the balloons are sold in packages of 5 | Same answer |
| Laya | `B1` — Cost of the first package option in dollars | `B1` — Cost of the first package option in dollars | Same answer |
| CalDec v1 | `B1` — Cost of the first package option in dollars | `B1` — Cost of the first package option in dollars | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `questbench/c50c11171baf0be610e9/examples/irrelevant/clean-source_first_quest_literary_contexts_full_0079`

**Input fingerprint:** `5a957837ca2d6cf3180b48920c343bfd9e17455b7522f61ddd5351505dc416f2`

| Change | Recorded version |
| --- | --- |
| Unrelated examples | Add examples unrelated to the question |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/information-seeking/questbench-c50c11171baf0be610e9.md).
