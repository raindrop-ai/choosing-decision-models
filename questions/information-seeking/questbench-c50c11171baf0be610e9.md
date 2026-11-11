# Information seeking · question 59

[Back to Information seeking](README.md) · [All capabilities](../README.md)

**Question ID:** `questbench/c50c11171baf0be610e9`  
**Source:** [QuestBench (Google DeepMind)](https://storage.googleapis.com/questbench/questbench_data.tar.gz)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/information-seeking/questbench-c50c11171baf0be610e9/README.md)

## Context

> Vincent is planning a party and wants to buy flowers for decoration. He can buy flowers in packages of 3 or in packages of 2 for $1. He also notices that balloons are sold in packages of 5, but he decides not to buy any balloons. How much money does Vincent save by buying 18 flowers at the better price instead of the more expensive option?

## Question

> Which missing variable should be asked about to solve this problem?

## Answer choices

- **B1:** Cost of the first package option in dollars
- **G:** Cost of the balloons are sold in packages of 5

**Reference answer:** Cost of the first package option in dollars (`B1`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Vincent is planning a party and wants to buy flowers for decoration. He can buy flowers in packages of 3 or in packages of 2 for $1. He also notices that balloons are sold in packages of 5, but he decides not to buy any balloons. How much money does Vincent save by buying 18 flowers at the better price instead of the more expensive option?",
  "question": "Which missing variable should be asked about to solve this problem?",
  "choices": {
    "B1": "Cost of the first package option in dollars",
    "G": "Cost of the balloons are sold in packages of 5"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | Cost of the first package option in dollars | Correct |
| Opus 5.5 | Cost of the first package option in dollars | Correct |
| GLiDE v1.2 | Cost of the first package option in dollars | Correct |
| Decider v1.1 | Cost of the first package option in dollars | Correct |
| Jev | Cost of the first package option in dollars | Correct |
| Microsoft Decision-1 | Cost of the first package option in dollars | Correct |
| Clef | Cost of the first package option in dollars | Correct |
| Luna Decisions | Cost of the first package option in dollars | Correct |
| Clef Flash | Cost of the first package option in dollars | Correct |
| Strands Decider | Cost of the first package option in dollars | Correct |
| GLiNER2.5 Decide | Cost of the balloons are sold in packages of 5 | Incorrect |
| Laya | Cost of the first package option in dollars | Correct |
| CalDec v1 | Cost of the first package option in dollars | Correct |

## Source and sharing

Attribution: Google LLC; QuestBench authors.  
Terms: **[CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)**. [Source sharing decision](../../docs/data-sharing.md).  
The capability assignment and choice-format normalization are part of this experiment. Source data retain their own terms.

<details>
<summary>Exact source locator and input fingerprint</summary>

```json
{
  "source_locator": {
    "path": "extracted/questbench.tar.gz/questbench_data/GSM-Q/gsm_verbal_full.csv",
    "record": "6376",
    "kind": "source_file_record"
  },
  "source_revision": null,
  "input_hash": "1df2bd8cba2d96985c505879d4b84f0b91181fbffc3e5fd6f7b3c1939efbb980"
}
```

</details>
