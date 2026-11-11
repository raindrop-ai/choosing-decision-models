# Information seeking · question 15

[Back to Information seeking](README.md) · [All capabilities](../README.md)

**Question ID:** `questbench/37d1accf7e249644f05d`  
**Source:** [QuestBench (Google DeepMind)](https://storage.googleapis.com/questbench/questbench_data.tar.gz)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/information-seeking/questbench-37d1accf7e249644f05d/README.md)

## Context

> Tyson decided to make muffaletta sandwiches for the big game. Each sandwich required 1 pound of meat and cheese and would serve 4 people. There would be 20 people in total watching the game. The meat cost $7.00 per pound and the cheese cost $3.00 per pound. Tyson also decided to buy some pickles and olives for the sandwiches, which cost $2.00 per pound. How much money would he spend on the meat and cheese to make enough sandwiches to serve 20 people?

## Question

> Which missing variable should be asked about to solve this problem?

## Answer choices

- **D:** Pounds of cheese required per sandwich
- **P:** Cost of pickles and olives per pound

**Reference answer:** Pounds of cheese required per sandwich (`D`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Tyson decided to make muffaletta sandwiches for the big game. Each sandwich required 1 pound of meat and cheese and would serve 4 people. There would be 20 people in total watching the game. The meat cost $7.00 per pound and the cheese cost $3.00 per pound. Tyson also decided to buy some pickles and olives for the sandwiches, which cost $2.00 per pound. How much money would he spend on the meat and cheese to make enough sandwiches to serve 20 people?",
  "question": "Which missing variable should be asked about to solve this problem?",
  "choices": {
    "D": "Pounds of cheese required per sandwich",
    "P": "Cost of pickles and olives per pound"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | Pounds of cheese required per sandwich | Correct |
| Opus 5.5 | Pounds of cheese required per sandwich | Correct |
| GLiDE v1.2 | Pounds of cheese required per sandwich | Correct |
| Decider v1.1 | Pounds of cheese required per sandwich | Correct |
| Jev | Pounds of cheese required per sandwich | Correct |
| Microsoft Decision-1 | Pounds of cheese required per sandwich | Correct |
| Clef | Pounds of cheese required per sandwich | Correct |
| Luna Decisions | Pounds of cheese required per sandwich | Correct |
| Clef Flash | Pounds of cheese required per sandwich | Correct |
| Strands Decider | Pounds of cheese required per sandwich | Correct |
| GLiNER2.5 Decide | Cost of pickles and olives per pound | Incorrect |
| Laya | Pounds of cheese required per sandwich | Correct |
| CalDec v1 | Cost of pickles and olives per pound | Incorrect |

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
    "record": "15215",
    "kind": "source_file_record"
  },
  "source_revision": null,
  "input_hash": "38280e3571ed971796d51e0e61f4693cb8171f3633971cbb864e89e149bd9cf9"
}
```

</details>
