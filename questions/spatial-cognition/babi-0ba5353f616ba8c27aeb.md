# Spatial cognition · question 13

[Back to Spatial cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `babi/0ba5353f616ba8c27aeb`  
**Source:** [bAbI](https://s3.amazonaws.com/text-datasets/babi_tasks_1-20_v1-2.tar.gz)  
**Input format:** adapted choices

[Explore this question’s altered versions](../../variants/spatial-cognition/babi-0ba5353f616ba8c27aeb/README.md)

## Context

> The yellow square is below the red square.
> The triangle is above the red square.

## Question

> Is the yellow square below the triangle?

## Answer choices

- **no:** no
- **yes:** yes

**Reference answer:** yes (`yes`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "The yellow square is below the red square.\nThe triangle is above the red square.",
  "question": "Is the yellow square below the triangle?",
  "choices": {
    "no": "no",
    "yes": "yes"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | yes | Correct |
| Opus 5.5 | yes | Correct |
| GLiDE v1.2 | yes | Correct |
| Decider v1.1 | yes | Correct |
| Jev | yes | Correct |
| Microsoft Decision-1 | yes | Correct |
| Clef | yes | Correct |
| Luna Decisions | no | Incorrect |
| Clef Flash | yes | Correct |
| Strands Decider | yes | Correct |
| GLiNER2.5 Decide | yes | Correct |
| Laya | yes | Correct |
| CalDec v1 | yes | Correct |

## Source and sharing

Attribution: Facebook, Inc.; bAbI authors.  
Terms: **[CC-BY-3.0](https://creativecommons.org/licenses/by/3.0/)**. [Source sharing decision](../../docs/data-sharing.md).  
The capability assignment and choice-format normalization are part of this experiment. Source data retain their own terms.

<details>
<summary>Exact source locator and input fingerprint</summary>

```json
{
  "source_locator": {
    "path": "extracted/tasks.tar.gz/tasks_1-20_v1-2/en/qa17_positional-reasoning_train.txt",
    "record": "713",
    "kind": "source_file_record"
  },
  "source_revision": null,
  "input_hash": "99d4fba54752880a1d05ba616284f4777c2e2ecab06d3f97dc8c4bf5116ec60b"
}
```

</details>
