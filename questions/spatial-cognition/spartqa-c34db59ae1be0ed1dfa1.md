# Spatial cognition · question 10

[Back to Spatial cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `spartqa/c34db59ae1be0ed1dfa1`  
**Source:** [SPARTQA](https://github.com/HLR/SpartQA_generation)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/spatial-cognition/spartqa-c34db59ae1be0ed1dfa1/README.md)

## Context

> There are three blocks. Lets call them A, B and C. A medium blue square is in block A. A medium black square is under the medium blue square. Block B is to the right of block A. It has one medium blue square. A medium yellow square is touching the bottom edge of this block. This object is under the medium blue square. To the left side of block B there is block C with two medium blue squares in it. Below medium blue square number two is medium blue square number one. There is also a medium yellow square touching the bottom edge of this block. Below medium blue square number two and medium blue square number one is the medium yellow square.

## Question

> Is there a square that is under a medium square that is in block B, to the right of a blue square that is on the top of a blue square?

## Answer choices

- **Yes:** Yes
- **No:** No
- **DK:** DK

**Reference answer:** Yes (`Yes`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "There are three blocks. Lets call them A, B and C. A medium blue square is in block A. A medium black square is under the medium blue square. Block B is to the right of block A. It has one medium blue square. A medium yellow square is touching the bottom edge of this block. This object is under the medium blue square. To the left side of block B there is block C with two medium blue squares in it. Below medium blue square number two is medium blue square number one. There is also a medium yellow square touching the bottom edge of this block. Below medium blue square number two and medium blue square number one is the medium yellow square.",
  "question": "Is there a square that is under a medium square that is in block B, to the right of a blue square that is on the top of a blue square?",
  "choices": {
    "Yes": "Yes",
    "No": "No",
    "DK": "DK"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | Yes | Correct |
| Opus 5.5 | Yes | Correct |
| GLiDE v1.2 | Yes | Correct |
| Decider v1.1 | Yes | Correct |
| Jev | Yes | Correct |
| Microsoft Decision-1 | Yes | Correct |
| Clef | Yes | Correct |
| Luna Decisions | Yes | Correct |
| Clef Flash | Yes | Correct |
| Strands Decider | Yes | Correct |
| GLiNER2.5 Decide | Yes | Correct |
| Laya | No | Incorrect |
| CalDec v1 | Yes | Correct |

## Source and sharing

Attribution: HLR / Roshanak Mirzaee et al..  
Terms: **[MIT](https://opensource.org/license/mit)**. [Source sharing decision](../../docs/data-sharing.md).  
The capability assignment and choice-format normalization are part of this experiment. Source data retain their own terms.

<details>
<summary>Exact source locator and input fingerprint</summary>

```json
{
  "source_locator": {
    "path": "extracted/SpartQA_Auto.zip/SpartQA_Auto/unseen_test.json",
    "record": "234/1",
    "kind": "source_file_record"
  },
  "source_revision": "9892ed1bff9103f5a9103c68bd271b7630ab661e",
  "input_hash": "d004c16d3fbc89dd9fbb3d4a0d607e265af68b7b8f2f04c2c3cf23006cdc61ef"
}
```

</details>
