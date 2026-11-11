# Information seeking · question 17

[Back to Information seeking](README.md) · [All capabilities](../README.md)

**Question ID:** `questbench/f9fbe699009e73cd6e45`  
**Source:** [QuestBench (Google DeepMind)](https://storage.googleapis.com/questbench/questbench_data.tar.gz)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/information-seeking/questbench-f9fbe699009e73cd6e45/README.md)

## Context

> Jenna starts out with certain number of sapphires. She trades 3 sapphires for two rubies. She also wanted to trade 2 sapphires for 1 diamond worth a specific amount, but eventually decided against it. If sapphires are worth $800 and rubies are worth $1200, how much money are all her jewels worth?

## Question

> Which missing variable should be asked about to solve this problem?

## Answer choices

- **A:** Number of sapphires initially
- **E:** Price of one diamond

**Reference answer:** Number of sapphires initially (`A`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Jenna starts out with certain number of sapphires. She trades 3 sapphires for two rubies. She also wanted to trade 2 sapphires for 1 diamond worth a specific amount, but eventually decided against it. If sapphires are worth $800 and rubies are worth $1200, how much money are all her jewels worth?",
  "question": "Which missing variable should be asked about to solve this problem?",
  "choices": {
    "A": "Number of sapphires initially",
    "E": "Price of one diamond"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | Number of sapphires initially | Correct |
| Opus 5.5 | Number of sapphires initially | Correct |
| GLiDE v1.2 | Number of sapphires initially | Correct |
| Decider v1.1 | Number of sapphires initially | Correct |
| Jev | Number of sapphires initially | Correct |
| Microsoft Decision-1 | Number of sapphires initially | Correct |
| Clef | Number of sapphires initially | Correct |
| Luna Decisions | Number of sapphires initially | Correct |
| Clef Flash | Number of sapphires initially | Correct |
| Strands Decider | Number of sapphires initially | Correct |
| GLiNER2.5 Decide | Price of one diamond | Incorrect |
| Laya | Price of one diamond | Incorrect |
| CalDec v1 | Number of sapphires initially | Correct |

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
    "record": "23342",
    "kind": "source_file_record"
  },
  "source_revision": null,
  "input_hash": "3bc4cd6f657f72d23d425e1c208f6616bb2656b0d703c17e2e8a860b6b123d87"
}
```

</details>
