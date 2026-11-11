# Information seeking · question 29

[Back to Information seeking](README.md) · [All capabilities](../README.md)

**Question ID:** `questbench/29b30e92691cd8d676ca`  
**Source:** [QuestBench (Google DeepMind)](https://storage.googleapis.com/questbench/questbench_data.tar.gz)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/information-seeking/questbench-29b30e92691cd8d676ca/README.md)

## Context

> Peter went to the store with few $ in his pocket. He purchased 20 popsicles at and decided to buy 4 ice cream bars at $0.50 each. He also saw a pack of gum but decided not to buy it. How much did he spend in total in dollars?

## Question

> Which missing variable should be asked about to solve this problem?

## Answer choices

- **C:** cost of each popsicle
- **A:** amount he had with him
- **F:** cost of a pack of gum

**Reference answer:** cost of each popsicle (`C`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Peter went to the store with few $ in his pocket. He purchased 20 popsicles at and decided to buy 4 ice cream bars at $0.50 each. He also saw a pack of gum but decided not to buy it. How much did he spend in total in dollars?",
  "question": "Which missing variable should be asked about to solve this problem?",
  "choices": {
    "C": "cost of each popsicle",
    "A": "amount he had with him",
    "F": "cost of a pack of gum"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | cost of each popsicle | Correct |
| Opus 5.5 | cost of each popsicle | Correct |
| GLiDE v1.2 | cost of each popsicle | Correct |
| Decider v1.1 | cost of each popsicle | Correct |
| Jev | cost of each popsicle | Correct |
| Microsoft Decision-1 | cost of each popsicle | Correct |
| Clef | cost of each popsicle | Correct |
| Luna Decisions | cost of each popsicle | Correct |
| Clef Flash | cost of each popsicle | Correct |
| Strands Decider | cost of each popsicle | Correct |
| GLiNER2.5 Decide | amount he had with him | Incorrect |
| Laya | amount he had with him | Incorrect |
| CalDec v1 | amount he had with him | Incorrect |

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
    "record": "15722",
    "kind": "source_file_record"
  },
  "source_revision": null,
  "input_hash": "c9d6c9811650492fcafba535d609cd0743636dad69fa0e218d667c9041c08264"
}
```

</details>
