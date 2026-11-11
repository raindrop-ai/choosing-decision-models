# Information seeking · question 25

[Back to Information seeking](README.md) · [All capabilities](../README.md)

**Question ID:** `questbench/4c0ac3cf132611a92c6f`  
**Source:** [QuestBench (Google DeepMind)](https://storage.googleapis.com/questbench/questbench_data.tar.gz)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/information-seeking/questbench-4c0ac3cf132611a92c6f/README.md)

## Context

> Katina has money in her savings account. If she removes $100 from the account every month to buy shoes, how much money will remain in the account after 2 years?

## Question

> Which missing variable should be asked about to solve this problem?

## Answer choices

- **A:** Total amount of money in the account
- **H:** Price of each pair of shoes

**Reference answer:** Total amount of money in the account (`A`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Katina has money in her savings account. If she removes $100 from the account every month to buy shoes, how much money will remain in the account after 2 years?",
  "question": "Which missing variable should be asked about to solve this problem?",
  "choices": {
    "A": "Total amount of money in the account",
    "H": "Price of each pair of shoes"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | Total amount of money in the account | Correct |
| Opus 5.5 | Total amount of money in the account | Correct |
| GLiDE v1.2 | Total amount of money in the account | Correct |
| Decider v1.1 | Total amount of money in the account | Correct |
| Jev | Total amount of money in the account | Correct |
| Microsoft Decision-1 | Total amount of money in the account | Correct |
| Clef | Total amount of money in the account | Correct |
| Luna Decisions | Total amount of money in the account | Correct |
| Clef Flash | Total amount of money in the account | Correct |
| Strands Decider | Total amount of money in the account | Correct |
| GLiNER2.5 Decide | Total amount of money in the account | Correct |
| Laya | Total amount of money in the account | Correct |
| CalDec v1 | Total amount of money in the account | Correct |

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
    "record": "15094",
    "kind": "source_file_record"
  },
  "source_revision": null,
  "input_hash": "6897238ac46d6d8208e0e995f8f1c229c4a0395e578e1c275af64a057fb0b3e4"
}
```

</details>
