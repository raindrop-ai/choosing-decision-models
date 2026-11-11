# Information seeking · question 55

[Back to Information seeking](README.md) · [All capabilities](../README.md)

**Question ID:** `questbench/02c9f7a5d303e4234dfd`  
**Source:** [QuestBench (Google DeepMind)](https://storage.googleapis.com/questbench/questbench_data.tar.gz)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/information-seeking/questbench-02c9f7a5d303e4234dfd/README.md)

## Context

> James is putting together 4 tables. Each table has 4 legs and each leg needs screws. He is also putting chairs, which don't need screws. He has 40 screws. How many screws will he have left over?

## Question

> Which missing variable should be asked about to solve this problem?

## Answer choices

- **C:** Number of screws required per leg.
- **E:** Number of chairs James is assembling.

**Reference answer:** Number of screws required per leg. (`C`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "James is putting together 4 tables. Each table has 4 legs and each leg needs screws. He is also putting chairs, which don't need screws. He has 40 screws. How many screws will he have left over?",
  "question": "Which missing variable should be asked about to solve this problem?",
  "choices": {
    "C": "Number of screws required per leg.",
    "E": "Number of chairs James is assembling."
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | Number of screws required per leg. | Correct |
| Opus 5.5 | Number of screws required per leg. | Correct |
| GLiDE v1.2 | Number of screws required per leg. | Correct |
| Decider v1.1 | Number of screws required per leg. | Correct |
| Jev | Number of screws required per leg. | Correct |
| Microsoft Decision-1 | Number of screws required per leg. | Correct |
| Clef | Number of screws required per leg. | Correct |
| Luna Decisions | Number of screws required per leg. | Correct |
| Clef Flash | Number of screws required per leg. | Correct |
| Strands Decider | Number of chairs James is assembling. | Incorrect |
| GLiNER2.5 Decide | Number of screws required per leg. | Correct |
| Laya | Number of screws required per leg. | Correct |
| CalDec v1 | Number of screws required per leg. | Correct |

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
    "record": "10382",
    "kind": "source_file_record"
  },
  "source_revision": null,
  "input_hash": "6994ba3df25a271a17d774baa4651e264da3d19fe642da7026ad38fa00dd183f"
}
```

</details>
