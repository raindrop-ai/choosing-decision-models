# Information seeking · question 3

[Back to Information seeking](README.md) · [All capabilities](../README.md)

**Question ID:** `questbench/180dba734e7174c941e0`  
**Source:** [QuestBench (Google DeepMind)](https://storage.googleapis.com/questbench/questbench_data.tar.gz)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/information-seeking/questbench-180dba734e7174c941e0/README.md)

## Context

> Johnny, on the other hand, bought 2 more face masks than thrice the number of face masks Mike bought. How many face masks did Johnny buy?

## Question

> Which missing variable should be asked about to solve this problem?

## Answer choices

- **M:** Number of face masks Mike bought
- **X1:** Number of gloves Johnny bought
- **X2:** Number of hand sanitizers Mike bought

**Reference answer:** Number of face masks Mike bought (`M`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Johnny, on the other hand, bought 2 more face masks than thrice the number of face masks Mike bought. How many face masks did Johnny buy?",
  "question": "Which missing variable should be asked about to solve this problem?",
  "choices": {
    "M": "Number of face masks Mike bought",
    "X1": "Number of gloves Johnny bought",
    "X2": "Number of hand sanitizers Mike bought"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | Number of face masks Mike bought | Correct |
| Opus 5.5 | Number of face masks Mike bought | Correct |
| GLiDE v1.2 | Number of face masks Mike bought | Correct |
| Decider v1.1 | Number of face masks Mike bought | Correct |
| Jev | Number of face masks Mike bought | Correct |
| Microsoft Decision-1 | Number of face masks Mike bought | Correct |
| Clef | Number of face masks Mike bought | Correct |
| Luna Decisions | Number of face masks Mike bought | Correct |
| Clef Flash | Number of face masks Mike bought | Correct |
| Strands Decider | Number of face masks Mike bought | Correct |
| GLiNER2.5 Decide | Number of face masks Mike bought | Correct |
| Laya | Number of face masks Mike bought | Correct |
| CalDec v1 | Number of face masks Mike bought | Correct |

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
    "record": "20412",
    "kind": "source_file_record"
  },
  "source_revision": null,
  "input_hash": "0a41cc078bb082d6d4b7b22a75de83bbb1d1b8dfb5cabf8b52811640cd8b3a1d"
}
```

</details>
