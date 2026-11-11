# Spatial cognition · question 36

[Back to Spatial cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `spartqa/48eef2d2dbdde48bc27d`  
**Source:** [SPARTQA](https://github.com/HLR/SpartQA_generation)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/spatial-cognition/spartqa-48eef2d2dbdde48bc27d/README.md)

## Context

> There are three blocks, A, B and C. Block C is to the left of B and block B is below A. Block A contains a medium blue square. The medium blue square is below a medium black square. Block B contains a medium yellow square and a medium blue square. The medium yellow square is touching the bottom edge of this block. It is below the medium blue square. And block C has two medium yellow squares. Medium yellow square number one is below medium yellow square number two.. One medium blue square is also touching the bottom edge of this block. Below medium yellow square number one and medium yellow square number two is the medium blue square.

## Question

> What is the relation between the medium object that is below medium yellow object number one and the yellow square which is above a yellow square?

## Answer choices

- **0:** left
- **1:** right
- **2:** above
- **3:** below
- **4:** near to
- **5:** far from
- **6:** touching
- **7:** DK

**Reference answer:** below (`3`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "There are three blocks, A, B and C. Block C is to the left of B and block B is below A. Block A contains a medium blue square. The medium blue square is below a medium black square. Block B contains a medium yellow square and a medium blue square. The medium yellow square is touching the bottom edge of this block. It is below the medium blue square. And block C has two medium yellow squares. Medium yellow square number one is below medium yellow square number two.. One medium blue square is also touching the bottom edge of this block. Below medium yellow square number one and medium yellow square number two is the medium blue square.",
  "question": "What is the relation between the medium object that is below medium yellow object number one and the yellow square which is above a yellow square?",
  "choices": {
    "0": "left",
    "1": "right",
    "2": "above",
    "3": "below",
    "4": "near to",
    "5": "far from",
    "6": "touching",
    "7": "DK"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | below | Correct |
| Opus 5.5 | below | Correct |
| GLiDE v1.2 | below | Correct |
| Decider v1.1 | below | Correct |
| Jev | below | Correct |
| Microsoft Decision-1 | below | Correct |
| Clef | below | Correct |
| Luna Decisions | left | Incorrect |
| Clef Flash | below | Correct |
| Strands Decider | below | Correct |
| GLiNER2.5 Decide | below | Correct |
| Laya | below | Correct |
| CalDec v1 | below | Correct |

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
    "record": "12153/4",
    "kind": "source_file_record"
  },
  "source_revision": "9892ed1bff9103f5a9103c68bd271b7630ab661e",
  "input_hash": "ad69355d7d385d68f9d1a8d73c6468d8fbb20d091789fecae3a5cc6e6c81fa4e"
}
```

</details>
