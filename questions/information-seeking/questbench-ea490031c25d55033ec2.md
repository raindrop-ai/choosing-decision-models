# Information seeking · question 31

[Back to Information seeking](README.md) · [All capabilities](../README.md)

**Question ID:** `questbench/ea490031c25d55033ec2`  
**Source:** [QuestBench (Google DeepMind)](https://storage.googleapis.com/questbench/questbench_data.tar.gz)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/information-seeking/questbench-ea490031c25d55033ec2/README.md)

## Context

> Martha is knitting winter wear for her 3 grandchildren. They're triplets, so they're all the same size. She wants to make a hat, scarf, sweater, mittens, and socks for each of them. It takes 2 skeins of wool to make a hat, 4 for a scarf, 12 for a sweater, and 1 for a pair of mittens. How many skeins of wool will Martha need to buy?

## Question

> Which missing variable should be asked about to solve this problem?

## Answer choices

- **F:** Number of skeins used of wool to make socks
- **G:** Number of wools her cat uses to play

**Reference answer:** Number of skeins used of wool to make socks (`F`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Martha is knitting winter wear for her 3 grandchildren. They're triplets, so they're all the same size. She wants to make a hat, scarf, sweater, mittens, and socks for each of them. It takes 2 skeins of wool to make a hat, 4 for a scarf, 12 for a sweater, and 1 for a pair of mittens. How many skeins of wool will Martha need to buy?\n",
  "question": "Which missing variable should be asked about to solve this problem?",
  "choices": {
    "F": "Number of skeins used of wool to make socks",
    "G": "Number of wools her cat uses to play"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | Number of skeins used of wool to make socks | Correct |
| Opus 5.5 | Number of skeins used of wool to make socks | Correct |
| GLiDE v1.2 | Number of skeins used of wool to make socks | Correct |
| Decider v1.1 | Number of skeins used of wool to make socks | Correct |
| Jev | Number of skeins used of wool to make socks | Correct |
| Microsoft Decision-1 | Number of skeins used of wool to make socks | Correct |
| Clef | Number of skeins used of wool to make socks | Correct |
| Luna Decisions | Number of skeins used of wool to make socks | Correct |
| Clef Flash | Number of skeins used of wool to make socks | Correct |
| Strands Decider | Number of skeins used of wool to make socks | Correct |
| GLiNER2.5 Decide | Number of skeins used of wool to make socks | Correct |
| Laya | Number of skeins used of wool to make socks | Correct |
| CalDec v1 | Number of skeins used of wool to make socks | Correct |

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
    "record": "19494",
    "kind": "source_file_record"
  },
  "source_revision": null,
  "input_hash": "f419040e352b565c52462686f42b98bba71cbf9bd7435766ee3e4a43a2b1ef14"
}
```

</details>
