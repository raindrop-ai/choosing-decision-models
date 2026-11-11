# Information seeking · question 65

[Back to Information seeking](README.md) · [All capabilities](../README.md)

**Question ID:** `questbench/f079973cc91adf9ff01c`  
**Source:** [QuestBench (Google DeepMind)](https://storage.googleapis.com/questbench/questbench_data.tar.gz)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/information-seeking/questbench-f079973cc91adf9ff01c/README.md)

## Context

> Janey and Sally are in a library. Janey has 3 more than twice the number of books that Sally has. How many books does Sally have?

## Question

> Which missing variable should be asked about to solve this problem?

## Answer choices

- **B:** Number of books Janey has
- **A:** Number of books Janey has with respect to Sally
- **C:** Number of books they have not picked up

**Reference answer:** Number of books Janey has (`B`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Janey and Sally are in a library. Janey has 3 more than twice the number of books that Sally has. How many books does Sally have?",
  "question": "Which missing variable should be asked about to solve this problem?",
  "choices": {
    "B": "Number of books Janey has",
    "A": "Number of books Janey has with respect to Sally",
    "C": "Number of books they have not picked up"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | Number of books Janey has | Correct |
| Opus 5.5 | Number of books Janey has | Correct |
| GLiDE v1.2 | Number of books Janey has | Correct |
| Decider v1.1 | Number of books Janey has | Correct |
| Jev | Number of books Janey has | Correct |
| Microsoft Decision-1 | Number of books Janey has | Correct |
| Clef | Number of books Janey has | Correct |
| Luna Decisions | Number of books Janey has | Correct |
| Clef Flash | Number of books Janey has | Correct |
| Strands Decider | Number of books Janey has with respect to Sally | Incorrect |
| GLiNER2.5 Decide | Number of books Janey has with respect to Sally | Incorrect |
| Laya | Number of books Janey has | Correct |
| CalDec v1 | Number of books Janey has | Correct |

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
    "record": "14264",
    "kind": "source_file_record"
  },
  "source_revision": null,
  "input_hash": "a733e968c91483a7880021da24bef665d0e6223ad09234360f87f31720c9f9d5"
}
```

</details>
