# Spatial cognition · question 49

[Back to Spatial cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `babi/d7ab785ce8d485a8f78c`  
**Source:** [bAbI](https://s3.amazonaws.com/text-datasets/babi_tasks_1-20_v1-2.tar.gz)  
**Input format:** adapted choices

[Explore this question’s altered versions](../../variants/spatial-cognition/babi-d7ab785ce8d485a8f78c/README.md)

## Context

> The triangle is above the blue square.
> The blue square is above the yellow square.

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
  "state": "The triangle is above the blue square.\nThe blue square is above the yellow square.",
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
| Luna Decisions | yes | Correct |
| Clef Flash | yes | Correct |
| Strands Decider | yes | Correct |
| GLiNER2.5 Decide | yes | Correct |
| Laya | no | Incorrect |
| CalDec v1 | no | Incorrect |

## Source and sharing

Attribution: Facebook, Inc.; bAbI authors.  
Terms: **[CC-BY-3.0](https://creativecommons.org/licenses/by/3.0/)**. [Source sharing decision](../../docs/data-sharing.md).  
The capability assignment and choice-format normalization are part of this experiment. Source data retain their own terms.

<details>
<summary>Exact source locator and input fingerprint</summary>

```json
{
  "source_locator": {
    "path": "extracted/tasks.tar.gz/tasks_1-20_v1-2/en/qa17_positional-reasoning_test.txt",
    "record": "416",
    "kind": "source_file_record"
  },
  "source_revision": null,
  "input_hash": "cfd898b1e4631a97dd904e146d8907457af5b486336d77b3f5dace91d7e15d71"
}
```

</details>
