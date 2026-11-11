# Spatial cognition · question 30

[Back to Spatial cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `spartqa/10fcdfb3bfb8885cab25`  
**Source:** [SPARTQA](https://github.com/HLR/SpartQA_generation)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/spatial-cognition/spartqa-10fcdfb3bfb8885cab25/README.md)

## Context

> We have three blocks. We call them A, B and C. There is a medium blue square in block A. A medium black square is also in this block. The medium blue square is below the medium black square. Then, there is block B. It contains one medium black square. Block C is to the right of block B and below block A. It has two medium blue squares. Medium blue square number one is touching the bottom edge of this block. Medium blue square number one is below a medium yellow square and medium blue square number two. Below medium blue square number two there is the medium yellow square.

## Question

> What is the relation between the medium blue square which is below a yellow thing and medium blue square number two?

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
  "state": "We have three blocks. We call them A, B and C. There is a medium blue square in block A. A medium black square is also in this block. The medium blue square is below the medium black square. Then, there is block B. It contains one medium black square. Block C is to the right of block B and below block A. It has two medium blue squares. Medium blue square number one is touching the bottom edge of this block. Medium blue square number one is below a medium yellow square and medium blue square number two. Below medium blue square number two there is the medium yellow square.",
  "question": "What is the relation between the medium blue square which is below a yellow thing and medium blue square number two?",
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
| Luna Decisions | above | Incorrect |
| Clef Flash | below | Correct |
| Strands Decider | below | Correct |
| GLiNER2.5 Decide | touching | Incorrect |
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
    "path": "extracted/SpartQA_Auto.zip/SpartQA_Auto/dev.json",
    "record": "13/5",
    "kind": "source_file_record"
  },
  "source_revision": "9892ed1bff9103f5a9103c68bd271b7630ab661e",
  "input_hash": "bbf5cc21c09738ef73673c22fe31809f07e113c79970e3a0541baca58cd60e7c"
}
```

</details>
