# Spatial cognition · question 38

[Back to Spatial cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `spartqa/9c777e3fec6ea7fbad98`  
**Source:** [SPARTQA](https://github.com/HLR/SpartQA_generation)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/spatial-cognition/spartqa-9c777e3fec6ea7fbad98/README.md)

## Context

> We have two blocks, A and B. There are a medium black square, one big yellow square and a medium blue triangle in block A. Below the medium blue triangle and the big yellow square is the medium black square. The big yellow square is to the left of and above the medium blue triangle. Block B is above block A. It contains one big black triangle, a big yellow square and one medium blue triangle. To the left of the big yellow square there is the big black triangle. The medium blue triangle is to the left of and near to a big blue square which is below a medium yellow triangle. The medium yellow triangle is touching the right edge of this block. The big black triangle is touching the left edge of this block. This object is below the medium yellow triangle.

## Question

> What is above the medium black square? a big yellow square or a thing that is touching the left edge of a block?

## Answer choices

- **0:** big yellow square 
- **1:** thing that is touching the left edge of a block 
- **2:** both of them
- **3:** none of them

**Reference answer:** both of them (`2`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "We have two blocks, A and B. There are a medium black square, one big yellow square and a medium blue triangle in block A. Below the medium blue triangle and the big yellow square is the medium black square. The big yellow square is to the left of and above the medium blue triangle. Block B is above block A. It contains one big black triangle, a big yellow square and one medium blue triangle. To the left of the big yellow square there is the big black triangle. The medium blue triangle is to the left of and near to a big blue square which is below a medium yellow triangle. The medium yellow triangle is touching the right edge of this block. The big black triangle is touching the left edge of this block. This object is below the medium yellow triangle.",
  "question": "What is above the medium black square? a big yellow square or a thing that is touching the left edge of a block?",
  "choices": {
    "0": "big yellow square ",
    "1": "thing that is touching the left edge of a block ",
    "2": "both of them",
    "3": "none of them"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | both of them | Correct |
| Opus 5.5 | both of them | Correct |
| GLiDE v1.2 | both of them | Correct |
| Decider v1.1 | both of them | Correct |
| Jev | big yellow square  | Incorrect |
| Microsoft Decision-1 | both of them | Correct |
| Clef | big yellow square  | Incorrect |
| Luna Decisions | big yellow square  | Incorrect |
| Clef Flash | big yellow square  | Incorrect |
| Strands Decider | both of them | Correct |
| GLiNER2.5 Decide | thing that is touching the left edge of a block  | Incorrect |
| Laya | thing that is touching the left edge of a block  | Incorrect |
| CalDec v1 | thing that is touching the left edge of a block  | Incorrect |

## Source and sharing

Attribution: HLR / Roshanak Mirzaee et al..  
Terms: **[MIT](https://opensource.org/license/mit)**. [Source sharing decision](../../docs/data-sharing.md).  
The capability assignment and choice-format normalization are part of this experiment. Source data retain their own terms.

<details>
<summary>Exact source locator and input fingerprint</summary>

```json
{
  "source_locator": {
    "path": "extracted/SpartQA_Auto.zip/SpartQA_Auto/train.json",
    "record": "9332/3",
    "kind": "source_file_record"
  },
  "source_revision": "9892ed1bff9103f5a9103c68bd271b7630ab661e",
  "input_hash": "236a309eb0367036808bf5386fe0c46948fcf457498d6818e104ec201a25be93"
}
```

</details>
