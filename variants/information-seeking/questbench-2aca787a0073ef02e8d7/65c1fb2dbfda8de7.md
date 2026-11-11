# Option order · Reverse the answer choices variant

[Original question](../../../questions/information-seeking/questbench-2aca787a0073ef02e8d7.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** answer choices or their order.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> There are penguins sunbathing in the snow. One-third of them jump in and swim in the ocean, where the water temperature is a chilly degrees Celsius. Another one-third go inside the cave to eat their dinner, where the temperature is a cozy degrees Celsius. Despite these temperature differences, how many penguins are still left sunbathing in the snow?

## Question

> Which missing variable should be asked about to solve this problem?

## Answer choices

- **X2.** Temperature of the cave in degrees Celsius
- **X1.** Temperature of the ocean in degrees Celsius
- **P.** Total number of penguins

**Reference answer:** `P`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "There are penguins sunbathing in the snow. One-third of them jump in and swim in the ocean, where the water temperature is a chilly degrees Celsius. Another one-third go inside the cave to eat their dinner, where the temperature is a cozy degrees Celsius. Despite these temperature differences, how many penguins are still left sunbathing in the snow?",
  "question": "Which missing variable should be asked about to solve this problem?",
  "choices": {
    "X2": "Temperature of the cave in degrees Celsius",
    "X1": "Temperature of the ocean in degrees Celsius",
    "P": "Total number of penguins"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `P` — Total number of penguins | `P` — Total number of penguins | Same answer |
| Decider v1.1 | `P` — Total number of penguins | `P` — Total number of penguins | Same answer |
| Jev | `P` — Total number of penguins | `P` — Total number of penguins | Same answer |
| Microsoft Decision-1 | `P` — Total number of penguins | `P` — Total number of penguins | Same answer |
| Clef | `P` — Total number of penguins | `P` — Total number of penguins | Same answer |
| Luna Decisions | `P` — Total number of penguins | `P` — Total number of penguins | Same answer |
| Clef Flash | `P` — Total number of penguins | `P` — Total number of penguins | Same answer |
| Strands Decider | `P` — Total number of penguins | `P` — Total number of penguins | Same answer |
| GLiNER2.5 Decide | `X2` — Temperature of the cave in degrees Celsius | `X1` — Temperature of the ocean in degrees Celsius | Different answer |
| Laya | `P` — Total number of penguins | `P` — Total number of penguins | Same answer |
| CalDec v1 | `P` — Total number of penguins | `P` — Total number of penguins | Same answer |

Clef and Clef Flash sort answer choices in their published input-processing code. Their choice-order results describe that preprocessing.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `questbench/2aca787a0073ef02e8d7/option_order/reverse`

**Input fingerprint:** `652495e8a1f64806f3aab6890c4acbeae78cc1751a1833e089593b368e0095fd`

| Change | Recorded version |
| --- | --- |
| Option order | Reverse the answer choices |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/information-seeking/questbench-2aca787a0073ef02e8d7.md).
