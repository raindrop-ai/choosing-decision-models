# Information seeking · question 66

[Back to Information seeking](README.md) · [All capabilities](../README.md)

**Question ID:** `questbench/2aca787a0073ef02e8d7`  
**Source:** [QuestBench (Google DeepMind)](https://storage.googleapis.com/questbench/questbench_data.tar.gz)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/information-seeking/questbench-2aca787a0073ef02e8d7/README.md)

## Context

> There are penguins sunbathing in the snow. One-third of them jump in and swim in the ocean, where the water temperature is a chilly degrees Celsius. Another one-third go inside the cave to eat their dinner, where the temperature is a cozy degrees Celsius. Despite these temperature differences, how many penguins are still left sunbathing in the snow?

## Question

> Which missing variable should be asked about to solve this problem?

## Answer choices

- **P:** Total number of penguins
- **X1:** Temperature of the ocean in degrees Celsius
- **X2:** Temperature of the cave in degrees Celsius

**Reference answer:** Total number of penguins (`P`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "There are penguins sunbathing in the snow. One-third of them jump in and swim in the ocean, where the water temperature is a chilly degrees Celsius. Another one-third go inside the cave to eat their dinner, where the temperature is a cozy degrees Celsius. Despite these temperature differences, how many penguins are still left sunbathing in the snow?",
  "question": "Which missing variable should be asked about to solve this problem?",
  "choices": {
    "P": "Total number of penguins",
    "X1": "Temperature of the ocean in degrees Celsius",
    "X2": "Temperature of the cave in degrees Celsius"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | Total number of penguins | Correct |
| Opus 5.5 | Total number of penguins | Correct |
| GLiDE v1.2 | Total number of penguins | Correct |
| Decider v1.1 | Total number of penguins | Correct |
| Jev | Total number of penguins | Correct |
| Microsoft Decision-1 | Total number of penguins | Correct |
| Clef | Total number of penguins | Correct |
| Luna Decisions | Total number of penguins | Correct |
| Clef Flash | Total number of penguins | Correct |
| Strands Decider | Total number of penguins | Correct |
| GLiNER2.5 Decide | Temperature of the cave in degrees Celsius | Incorrect |
| Laya | Total number of penguins | Correct |
| CalDec v1 | Total number of penguins | Correct |

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
    "record": "19524",
    "kind": "source_file_record"
  },
  "source_revision": null,
  "input_hash": "412fee972e8be079300e501140fc707d086e3591df5944eab831155db3d25e68"
}
```

</details>
