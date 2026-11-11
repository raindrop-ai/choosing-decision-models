# Information seeking · question 13

[Back to Information seeking](README.md) · [All capabilities](../README.md)

**Question ID:** `questbench/f3d3fec034c5da8bf67e`  
**Source:** [QuestBench (Google DeepMind)](https://storage.googleapis.com/questbench/questbench_data.tar.gz)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/information-seeking/questbench-f3d3fec034c5da8bf67e/README.md)

## Context

> In a board game, four students scored a sum of points. Naomi scored 68 points, while Yuri, who was wearing a blue shirt and had just eaten several slices of pizza, scored 10 more than half as many points as Naomi. Brianna, who was sitting next to a window and had a couple  cups of water during the game, scored 17 points more than Naomi. If Jojo, who was wearing a red hat and had to take a break during the game, scored the remaining points, how many points did Jojo score?

## Question

> Which missing variable should be asked about to solve this problem?

## Answer choices

- **T:** Total points scored by all students
- **X1:** Number of slices of pizza Yuri ate
- **X2:** Number of cups of water Brianna drank
- **X3:** Duration of Jojo&#x27;s break in minutes

**Reference answer:** Total points scored by all students (`T`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "In a board game, four students scored a sum of points. Naomi scored 68 points, while Yuri, who was wearing a blue shirt and had just eaten several slices of pizza, scored 10 more than half as many points as Naomi. Brianna, who was sitting next to a window and had a couple  cups of water during the game, scored 17 points more than Naomi. If Jojo, who was wearing a red hat and had to take a break during the game, scored the remaining points, how many points did Jojo score?",
  "question": "Which missing variable should be asked about to solve this problem?",
  "choices": {
    "T": "Total points scored by all students",
    "X1": "Number of slices of pizza Yuri ate",
    "X2": "Number of cups of water Brianna drank",
    "X3": "Duration of Jojo's break in minutes"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | Total points scored by all students | Correct |
| Opus 5.5 | Total points scored by all students | Correct |
| GLiDE v1.2 | Total points scored by all students | Correct |
| Decider v1.1 | Total points scored by all students | Correct |
| Jev | Total points scored by all students | Correct |
| Microsoft Decision-1 | Total points scored by all students | Correct |
| Clef | Total points scored by all students | Correct |
| Luna Decisions | Total points scored by all students | Correct |
| Clef Flash | Total points scored by all students | Correct |
| Strands Decider | Total points scored by all students | Correct |
| GLiNER2.5 Decide | Duration of Jojo&#x27;s break in minutes | Incorrect |
| Laya | Total points scored by all students | Correct |
| CalDec v1 | Total points scored by all students | Correct |

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
    "record": "20789",
    "kind": "source_file_record"
  },
  "source_revision": null,
  "input_hash": "edaec25e6eeec757ec5f414d4c9b0a4d6e10227e3fabadd7b2ae695120110706"
}
```

</details>
