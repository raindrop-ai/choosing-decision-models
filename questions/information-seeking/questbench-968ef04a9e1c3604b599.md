# Information seeking · question 57

[Back to Information seeking](README.md) · [All capabilities](../README.md)

**Question ID:** `questbench/968ef04a9e1c3604b599`  
**Source:** [QuestBench (Google DeepMind)](https://storage.googleapis.com/questbench/questbench_data.tar.gz)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/information-seeking/questbench-968ef04a9e1c3604b599/README.md)

## Context

> Last night Rick killed ten wolves and 15 cougars while hunting. Today Rick killed three times as many wolves as cougars. How many animals did Rick kill?
>

## Question

> Which missing variable should be asked about to solve this problem?

## Answer choices

- **F1:** Number of fewer cougars killed today compared to yesterday
- **J:** Number of juvenile animals killed

**Reference answer:** Number of fewer cougars killed today compared to yesterday (`F1`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Last night Rick killed ten wolves and 15 cougars while hunting. Today Rick killed three times as many wolves as cougars. How many animals did Rick kill?\n\n",
  "question": "Which missing variable should be asked about to solve this problem?",
  "choices": {
    "F1": "Number of fewer cougars killed today compared to yesterday",
    "J": "Number of juvenile animals killed"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | Number of fewer cougars killed today compared to yesterday | Correct |
| Opus 5.5 | Number of fewer cougars killed today compared to yesterday | Correct |
| GLiDE v1.2 | Number of fewer cougars killed today compared to yesterday | Correct |
| Decider v1.1 | Number of fewer cougars killed today compared to yesterday | Correct |
| Jev | Number of fewer cougars killed today compared to yesterday | Correct |
| Microsoft Decision-1 | Number of fewer cougars killed today compared to yesterday | Correct |
| Clef | Number of fewer cougars killed today compared to yesterday | Correct |
| Luna Decisions | Number of fewer cougars killed today compared to yesterday | Correct |
| Clef Flash | Number of fewer cougars killed today compared to yesterday | Correct |
| Strands Decider | Number of fewer cougars killed today compared to yesterday | Correct |
| GLiNER2.5 Decide | Number of fewer cougars killed today compared to yesterday | Correct |
| Laya | Number of fewer cougars killed today compared to yesterday | Correct |
| CalDec v1 | Number of juvenile animals killed | Incorrect |

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
    "record": "11486",
    "kind": "source_file_record"
  },
  "source_revision": null,
  "input_hash": "77ff94502070386fd6f206f9723b0a6f1b2d6b911d0487746b12262e5ad8ab42"
}
```

</details>
