# Information seeking · question 43

[Back to Information seeking](README.md) · [All capabilities](../README.md)

**Question ID:** `questbench/0873cc73dcd2c5d479e5`  
**Source:** [QuestBench (Google DeepMind)](https://storage.googleapis.com/questbench/questbench_data.tar.gz)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/information-seeking/questbench-0873cc73dcd2c5d479e5/README.md)

## Context

> John is a diligent worker who completes cycles of work each day. Each cycle consists of different tasks. Each task pays $1.20. However, John also spends on a cup of coffee after every 10 cycles to keep himself energized, but his employer reimburses him for these coffee breaks. If John works a full 7 day week, how much does he make?

## Question

> Which missing variable should be asked about to solve this problem?

## Answer choices

- **T:** Number of tasks per cycle
- **C1:** Cost of a cup of coffee

**Reference answer:** Number of tasks per cycle (`T`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "John is a diligent worker who completes cycles of work each day. Each cycle consists of different tasks. Each task pays $1.20. However, John also spends on a cup of coffee after every 10 cycles to keep himself energized, but his employer reimburses him for these coffee breaks. If John works a full 7 day week, how much does he make?",
  "question": "Which missing variable should be asked about to solve this problem?",
  "choices": {
    "T": "Number of tasks per cycle",
    "C1": "Cost of a cup of coffee"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | Number of tasks per cycle | Correct |
| Opus 5.5 | Number of tasks per cycle | Correct |
| GLiDE v1.2 | Number of tasks per cycle | Correct |
| Decider v1.1 | Number of tasks per cycle | Correct |
| Jev | Number of tasks per cycle | Correct |
| Microsoft Decision-1 | Number of tasks per cycle | Correct |
| Clef | Number of tasks per cycle | Correct |
| Luna Decisions | Number of tasks per cycle | Correct |
| Clef Flash | Number of tasks per cycle | Correct |
| Strands Decider | Number of tasks per cycle | Correct |
| GLiNER2.5 Decide | Cost of a cup of coffee | Incorrect |
| Laya | Number of tasks per cycle | Correct |
| CalDec v1 | Cost of a cup of coffee | Incorrect |

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
    "record": "18395",
    "kind": "source_file_record"
  },
  "source_revision": null,
  "input_hash": "8b4be82046cabfa6a2e3b7a7e98aef4bb82dc1ddd1307904b6e43b7755e63f1f"
}
```

</details>
