# Information seeking · question 41

[Back to Information seeking](README.md) · [All capabilities](../README.md)

**Question ID:** `questbench/b34b77658c5be5e9f757`  
**Source:** [QuestBench (Google DeepMind)](https://storage.googleapis.com/questbench/questbench_data.tar.gz)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/information-seeking/questbench-b34b77658c5be5e9f757/README.md)

## Context

> There are forty apples in one box. Uncle Franky ordered two boxes of apples and some boxes of oranges. He is planning to pack the apples with few apples in one pack. How many packs of apples can he make with the two boxes of apples?

## Question

> Which missing variable should be asked about to solve this problem?

## Answer choices

- **E:** number of apples uncle franky packed in one pack
- **C:** number of boxes of oranges ordered by uncle franky

**Reference answer:** number of apples uncle franky packed in one pack (`E`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "There are forty apples in one box. Uncle Franky ordered two boxes of apples and some boxes of oranges. He is planning to pack the apples with few apples in one pack. How many packs of apples can he make with the two boxes of apples?",
  "question": "Which missing variable should be asked about to solve this problem?",
  "choices": {
    "E": "number of apples uncle franky packed in one pack",
    "C": "number of boxes of oranges ordered by uncle franky"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | number of apples uncle franky packed in one pack | Correct |
| Opus 5.5 | number of apples uncle franky packed in one pack | Correct |
| GLiDE v1.2 | number of apples uncle franky packed in one pack | Correct |
| Decider v1.1 | number of apples uncle franky packed in one pack | Correct |
| Jev | number of apples uncle franky packed in one pack | Correct |
| Microsoft Decision-1 | number of apples uncle franky packed in one pack | Correct |
| Clef | number of apples uncle franky packed in one pack | Correct |
| Luna Decisions | number of apples uncle franky packed in one pack | Correct |
| Clef Flash | number of apples uncle franky packed in one pack | Correct |
| Strands Decider | number of apples uncle franky packed in one pack | Correct |
| GLiNER2.5 Decide | number of apples uncle franky packed in one pack | Correct |
| Laya | number of apples uncle franky packed in one pack | Correct |
| CalDec v1 | number of apples uncle franky packed in one pack | Correct |

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
    "record": "10811",
    "kind": "source_file_record"
  },
  "source_revision": null,
  "input_hash": "b3bf2cca3ee25c71320ef7d4adbe0bb98311771a75b8b556617952171f148760"
}
```

</details>
