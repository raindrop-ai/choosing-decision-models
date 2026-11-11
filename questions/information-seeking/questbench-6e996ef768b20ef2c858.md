# Information seeking · question 64

[Back to Information seeking](README.md) · [All capabilities](../README.md)

**Question ID:** `questbench/6e996ef768b20ef2c858`  
**Source:** [QuestBench (Google DeepMind)](https://storage.googleapis.com/questbench/questbench_data.tar.gz)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/information-seeking/questbench-6e996ef768b20ef2c858/README.md)

## Context

> Jen is planning to sell her root crops at the local farmer's market. She has 6 yams which can be sold at $1.5 each, 10 sweet potatoes that cost $2 each, and  carrots which cost $1.25 each. She also has  beets, but she decides to keep them for her own use, so they won't be sold. If she sells all the yams, sweet potatoes, and carrots, but none of the beets, how much will she earn?

## Question

> Which missing variable should be asked about to solve this problem?

## Answer choices

- **E:** Number of carrots
- **G:** Number of beets

**Reference answer:** Number of carrots (`E`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Jen is planning to sell her root crops at the local farmer's market. She has 6 yams which can be sold at $1.5 each, 10 sweet potatoes that cost $2 each, and  carrots which cost $1.25 each. She also has  beets, but she decides to keep them for her own use, so they won't be sold. If she sells all the yams, sweet potatoes, and carrots, but none of the beets, how much will she earn?",
  "question": "Which missing variable should be asked about to solve this problem?",
  "choices": {
    "E": "Number of carrots",
    "G": "Number of beets"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | Number of carrots | Correct |
| Opus 5.5 | Number of carrots | Correct |
| GLiDE v1.2 | Number of carrots | Correct |
| Decider v1.1 | Number of carrots | Correct |
| Jev | Number of carrots | Correct |
| Microsoft Decision-1 | Number of carrots | Correct |
| Clef | Number of carrots | Correct |
| Luna Decisions | Number of carrots | Correct |
| Clef Flash | Number of carrots | Correct |
| Strands Decider | Number of carrots | Correct |
| GLiNER2.5 Decide | Number of beets | Incorrect |
| Laya | Number of carrots | Correct |
| CalDec v1 | Number of beets | Incorrect |

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
    "record": "14391",
    "kind": "source_file_record"
  },
  "source_revision": null,
  "input_hash": "b5aebd1e4005d6fb584b78a0dc5aa475705ee52adafcd3dfdeb4a145b71e55ac"
}
```

</details>
