# Information seeking · question 53

[Back to Information seeking](README.md) · [All capabilities](../README.md)

**Question ID:** `questbench/faae3c27fda4e362ce3e`  
**Source:** [QuestBench (Google DeepMind)](https://storage.googleapis.com/questbench/questbench_data.tar.gz)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/information-seeking/questbench-faae3c27fda4e362ce3e/README.md)

## Context

> During her science class study, Brady discovered that each whale in the sea has 40 gallons of blood. She also found out that a shark has three times as much blood as a whale. In the same class, she learned that a dolphin has certain amount of blood volume of a whale, but this information is not relevant to her current calculations. Brady is now curious to find out the total number of gallons of blood that all sharks swimming in the sea would have. Can you help her with this calculation?

## Question

> Which missing variable should be asked about to solve this problem?

## Answer choices

- **T:** Number of sharks swimming in the sea
- **D:** Number of times a dolphin has blood than whale

**Reference answer:** Number of sharks swimming in the sea (`T`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "During her science class study, Brady discovered that each whale in the sea has 40 gallons of blood. She also found out that a shark has three times as much blood as a whale. In the same class, she learned that a dolphin has certain amount of blood volume of a whale, but this information is not relevant to her current calculations. Brady is now curious to find out the total number of gallons of blood that all sharks swimming in the sea would have. Can you help her with this calculation?",
  "question": "Which missing variable should be asked about to solve this problem?",
  "choices": {
    "T": "Number of sharks swimming in the sea",
    "D": "Number of times a dolphin has blood than whale"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | Number of sharks swimming in the sea | Correct |
| Opus 5.5 | Number of sharks swimming in the sea | Correct |
| GLiDE v1.2 | Number of sharks swimming in the sea | Correct |
| Decider v1.1 | Number of sharks swimming in the sea | Correct |
| Jev | Number of sharks swimming in the sea | Correct |
| Microsoft Decision-1 | Number of sharks swimming in the sea | Correct |
| Clef | Number of sharks swimming in the sea | Correct |
| Luna Decisions | Number of sharks swimming in the sea | Correct |
| Clef Flash | Number of sharks swimming in the sea | Correct |
| Strands Decider | Number of sharks swimming in the sea | Correct |
| GLiNER2.5 Decide | Number of sharks swimming in the sea | Correct |
| Laya | Number of times a dolphin has blood than whale | Incorrect |
| CalDec v1 | Number of sharks swimming in the sea | Correct |

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
    "record": "13378",
    "kind": "source_file_record"
  },
  "source_revision": null,
  "input_hash": "5699eb561bd85b209b8bfd2cee02a7037a1de9d7ac26619504c868654930009c"
}
```

</details>
