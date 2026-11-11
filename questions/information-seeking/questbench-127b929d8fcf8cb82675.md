# Information seeking · question 1

[Back to Information seeking](README.md) · [All capabilities](../README.md)

**Question ID:** `questbench/127b929d8fcf8cb82675`  
**Source:** [QuestBench (Google DeepMind)](https://storage.googleapis.com/questbench/questbench_data.tar.gz)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/information-seeking/questbench-127b929d8fcf8cb82675/README.md)

## Context

> Jill gets paid $20 per hour to teach and $30 to be a cheerleading coach. She also volunteers at a local animal shelter for 5 hours a week, but she doesn't get paid for this. If she works a year, 35 hours a week as a teacher, 15 hours a week as a coach, and volunteers a week at the animal shelter, what's her annual salary?

## Question

> Which missing variable should be asked about to solve this problem?

## Answer choices

- **E:** Total number of weeks
- **H:** Number of hours worked at the animal shelter

**Reference answer:** Total number of weeks (`E`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Jill gets paid $20 per hour to teach and $30 to be a cheerleading coach. She also volunteers at a local animal shelter for 5 hours a week, but she doesn't get paid for this. If she works a year, 35 hours a week as a teacher, 15 hours a week as a coach, and volunteers a week at the animal shelter, what's her annual salary?",
  "question": "Which missing variable should be asked about to solve this problem?",
  "choices": {
    "E": "Total number of weeks",
    "H": "Number of hours worked at the animal shelter"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | Total number of weeks | Correct |
| Opus 5.5 | Total number of weeks | Correct |
| GLiDE v1.2 | Total number of weeks | Correct |
| Decider v1.1 | Total number of weeks | Correct |
| Jev | Total number of weeks | Correct |
| Microsoft Decision-1 | Total number of weeks | Correct |
| Clef | Total number of weeks | Correct |
| Luna Decisions | Total number of weeks | Correct |
| Clef Flash | Total number of weeks | Correct |
| Strands Decider | Total number of weeks | Correct |
| GLiNER2.5 Decide | Number of hours worked at the animal shelter | Incorrect |
| Laya | Total number of weeks | Correct |
| CalDec v1 | Total number of weeks | Correct |

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
    "record": "9985",
    "kind": "source_file_record"
  },
  "source_revision": null,
  "input_hash": "d2ef88c5ba2ade328da115149930f77972bcfddaf9bc423a22c700f12d81dc09"
}
```

</details>
