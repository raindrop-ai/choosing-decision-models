# Information seeking · question 67

[Back to Information seeking](README.md) · [All capabilities](../README.md)

**Question ID:** `questbench/7ee42f4b2058b3907c2f`  
**Source:** [QuestBench (Google DeepMind)](https://storage.googleapis.com/questbench/questbench_data.tar.gz)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/information-seeking/questbench-7ee42f4b2058b3907c2f/README.md)

## Context

> Alisa biked 12 miles per hour while carrying a backpack. Stanley biked at 10 miles per hour for 2.5 hours. How many miles did Alisa and Stanley bike in total, regardless of the weight of Alisa's backpack or the temperature during Stanley's ride?

## Question

> Which missing variable should be asked about to solve this problem?

## Answer choices

- **A2:** Alisa&#x27;s time (hours)
- **X1:** Alisa&#x27;s backpack weight (pounds)
- **X2:** Temperature during Stanley&#x27;s ride (degrees)

**Reference answer:** Alisa&#x27;s time (hours) (`A2`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Alisa biked 12 miles per hour while carrying a backpack. Stanley biked at 10 miles per hour for 2.5 hours. How many miles did Alisa and Stanley bike in total, regardless of the weight of Alisa's backpack or the temperature during Stanley's ride?",
  "question": "Which missing variable should be asked about to solve this problem?",
  "choices": {
    "A2": "Alisa's time (hours)",
    "X1": "Alisa's backpack weight (pounds)",
    "X2": "Temperature during Stanley's ride (degrees)"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | Alisa&#x27;s time (hours) | Correct |
| Opus 5.5 | Alisa&#x27;s time (hours) | Correct |
| GLiDE v1.2 | Alisa&#x27;s time (hours) | Correct |
| Decider v1.1 | Alisa&#x27;s time (hours) | Correct |
| Jev | Alisa&#x27;s time (hours) | Correct |
| Microsoft Decision-1 | Alisa&#x27;s time (hours) | Correct |
| Clef | Alisa&#x27;s time (hours) | Correct |
| Luna Decisions | Alisa&#x27;s time (hours) | Correct |
| Clef Flash | Alisa&#x27;s time (hours) | Correct |
| Strands Decider | Alisa&#x27;s time (hours) | Correct |
| GLiNER2.5 Decide | Temperature during Stanley&#x27;s ride (degrees) | Incorrect |
| Laya | Alisa&#x27;s time (hours) | Correct |
| CalDec v1 | Alisa&#x27;s time (hours) | Correct |

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
    "record": "8551",
    "kind": "source_file_record"
  },
  "source_revision": null,
  "input_hash": "45a1b9d4ff610f781bafd9a9a0e6645327cf73e1c7358e8e8df738c2061740a4"
}
```

</details>
