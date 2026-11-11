# Information seeking · question 37

[Back to Information seeking](README.md) · [All capabilities](../README.md)

**Question ID:** `questbench/8ad5ff473674fe4f78fa`  
**Source:** [QuestBench (Google DeepMind)](https://storage.googleapis.com/questbench/questbench_data.tar.gz)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/information-seeking/questbench-8ad5ff473674fe4f78fa/README.md)

## Context

> Sally goes to a pizza shop where she buys one small pizza. Sally also buys one family-size pizza that costs 3 times as much as the small pizza she bought. How much does Sally spend in all?

## Question

> Which missing variable should be asked about to solve this problem?

## Answer choices

- **A:** COST OF ONE SMALL SIZE PIZZA  SALLY BOUGHT
- **P:** NUMBER OF PEOPLE ENTERED THE SHOP
- **Q:** NUMBER OF SMALL PIZZA&#x27;S ORDERED BY THE GROUP

**Reference answer:** COST OF ONE SMALL SIZE PIZZA  SALLY BOUGHT (`A`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Sally goes to a pizza shop where she buys one small pizza. Sally also buys one family-size pizza that costs 3 times as much as the small pizza she bought. How much does Sally spend in all?",
  "question": "Which missing variable should be asked about to solve this problem?",
  "choices": {
    "A": "COST OF ONE SMALL SIZE PIZZA  SALLY BOUGHT",
    "P": "NUMBER OF PEOPLE ENTERED THE SHOP",
    "Q": "NUMBER OF SMALL PIZZA'S ORDERED BY THE GROUP"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | COST OF ONE SMALL SIZE PIZZA  SALLY BOUGHT | Correct |
| Opus 5.5 | COST OF ONE SMALL SIZE PIZZA  SALLY BOUGHT | Correct |
| GLiDE v1.2 | COST OF ONE SMALL SIZE PIZZA  SALLY BOUGHT | Correct |
| Decider v1.1 | COST OF ONE SMALL SIZE PIZZA  SALLY BOUGHT | Correct |
| Jev | COST OF ONE SMALL SIZE PIZZA  SALLY BOUGHT | Correct |
| Microsoft Decision-1 | COST OF ONE SMALL SIZE PIZZA  SALLY BOUGHT | Correct |
| Clef | COST OF ONE SMALL SIZE PIZZA  SALLY BOUGHT | Correct |
| Luna Decisions | COST OF ONE SMALL SIZE PIZZA  SALLY BOUGHT | Correct |
| Clef Flash | COST OF ONE SMALL SIZE PIZZA  SALLY BOUGHT | Correct |
| Strands Decider | COST OF ONE SMALL SIZE PIZZA  SALLY BOUGHT | Correct |
| GLiNER2.5 Decide | COST OF ONE SMALL SIZE PIZZA  SALLY BOUGHT | Correct |
| Laya | COST OF ONE SMALL SIZE PIZZA  SALLY BOUGHT | Correct |
| CalDec v1 | COST OF ONE SMALL SIZE PIZZA  SALLY BOUGHT | Correct |

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
    "record": "21749",
    "kind": "source_file_record"
  },
  "source_revision": null,
  "input_hash": "cb3e506619b0b53369e060e8cc9d4a37566566600080d9cf52b0bdb5ff6ec4b5"
}
```

</details>
