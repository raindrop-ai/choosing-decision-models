# Information seeking · question 21

[Back to Information seeking](README.md) · [All capabilities](../README.md)

**Question ID:** `questbench/d888f63b8d3a55bb40f5`  
**Source:** [QuestBench (Google DeepMind)](https://storage.googleapis.com/questbench/questbench_data.tar.gz)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/information-seeking/questbench-d888f63b8d3a55bb40f5/README.md)

## Context

> Jackie is trying to decide whether to do her taxes herself or hire an accountant. If she does the taxes herself, she'll be able to do 3 fewer hours of freelance work. The accountant charges $90. However, she also has a side hobby of painting. She has paintings ready to sell, but this will not affect her decision about the taxes. How much more money will she have if she hires the accountant?

## Question

> Which missing variable should be asked about to solve this problem?

## Answer choices

- **B:** freelance rate per hour
- **D:** per painting cost
- **E:** number of paintings

**Reference answer:** freelance rate per hour (`B`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Jackie is trying to decide whether to do her taxes herself or hire an accountant. If she does the taxes herself, she'll be able to do 3 fewer hours of freelance work. The accountant charges $90. However, she also has a side hobby of painting. She has paintings ready to sell, but this will not affect her decision about the taxes. How much more money will she have if she hires the accountant?",
  "question": "Which missing variable should be asked about to solve this problem?",
  "choices": {
    "B": "freelance rate per hour",
    "D": "per painting cost",
    "E": "number of paintings"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | freelance rate per hour | Correct |
| Opus 5.5 | freelance rate per hour | Correct |
| GLiDE v1.2 | freelance rate per hour | Correct |
| Decider v1.1 | freelance rate per hour | Correct |
| Jev | freelance rate per hour | Correct |
| Microsoft Decision-1 | freelance rate per hour | Correct |
| Clef | freelance rate per hour | Correct |
| Luna Decisions | freelance rate per hour | Correct |
| Clef Flash | freelance rate per hour | Correct |
| Strands Decider | freelance rate per hour | Correct |
| GLiNER2.5 Decide | freelance rate per hour | Correct |
| Laya | freelance rate per hour | Correct |
| CalDec v1 | freelance rate per hour | Correct |

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
    "record": "16498",
    "kind": "source_file_record"
  },
  "source_revision": null,
  "input_hash": "6aa7f970cf89904350075f34a53c1dc37e7efd82cced09c3f70afd9a3248e197"
}
```

</details>
