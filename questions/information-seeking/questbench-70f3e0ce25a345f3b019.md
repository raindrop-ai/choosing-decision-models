# Information seeking · question 60

[Back to Information seeking](README.md) · [All capabilities](../README.md)

**Question ID:** `questbench/70f3e0ce25a345f3b019`  
**Source:** [QuestBench (Google DeepMind)](https://storage.googleapis.com/questbench/questbench_data.tar.gz)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/information-seeking/questbench-70f3e0ce25a345f3b019/README.md)

## Context

> In a family, there are 2 brothers and 3 sisters. All sisters are the same age. One of the brothers is 12 years old, which is half the age of the older brother. The family also has a pet dog that is years old and a pet parrot that is years old. What is the total age of all these siblings, not including the ages of the pets?

## Question

> Which missing variable should be asked about to solve this problem?

## Answer choices

- **B:** SECOND SISTER&#x27;S AGE
- **F:** PET DOG&#x27;S AGE
- **G:** PET PARROT&#x27;S AGE

**Reference answer:** SECOND SISTER&#x27;S AGE (`B`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "In a family, there are 2 brothers and 3 sisters. All sisters are the same age. One of the brothers is 12 years old, which is half the age of the older brother. The family also has a pet dog that is years old and a pet parrot that is years old. What is the total age of all these siblings, not including the ages of the pets?",
  "question": "Which missing variable should be asked about to solve this problem?",
  "choices": {
    "B": "SECOND SISTER'S AGE",
    "F": "PET DOG'S AGE",
    "G": "PET PARROT'S AGE"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | SECOND SISTER&#x27;S AGE | Correct |
| Opus 5.5 | SECOND SISTER&#x27;S AGE | Correct |
| GLiDE v1.2 | SECOND SISTER&#x27;S AGE | Correct |
| Decider v1.1 | SECOND SISTER&#x27;S AGE | Correct |
| Jev | SECOND SISTER&#x27;S AGE | Correct |
| Microsoft Decision-1 | SECOND SISTER&#x27;S AGE | Correct |
| Clef | SECOND SISTER&#x27;S AGE | Correct |
| Luna Decisions | SECOND SISTER&#x27;S AGE | Correct |
| Clef Flash | SECOND SISTER&#x27;S AGE | Correct |
| Strands Decider | SECOND SISTER&#x27;S AGE | Correct |
| GLiNER2.5 Decide | PET DOG&#x27;S AGE | Incorrect |
| Laya | PET DOG&#x27;S AGE | Incorrect |
| CalDec v1 | SECOND SISTER&#x27;S AGE | Correct |

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
    "record": "8369",
    "kind": "source_file_record"
  },
  "source_revision": null,
  "input_hash": "d4f2b5b8635d6d09577a245da1eb96a93ab865ecfa2f43ffedb4e0a936dad6d3"
}
```

</details>
