# Spatial cognition · question 44

[Back to Spatial cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `spartqa/f89e4bd006f3703dc33c`  
**Source:** [SPARTQA](https://github.com/HLR/SpartQA_generation)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/spatial-cognition/spartqa-f89e4bd006f3703dc33c/README.md)

## Context

> We have two blocks. We call them A and B. There are two medium blue squares in block A. Below medium blue square number two which is below a medium yellow square there is medium blue square number one. It is below the medium yellow square. Block B is to the right of block A. It contains two medium black squares. There is also a medium blue square in this block. This shape is below medium black square number two. Medium black square number one is below medium black square number two and the medium blue square.

## Question

> What is the relation between the medium black object that is below a blue square and the black thing that is above a medium square?

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
  "state": "We have two blocks. We call them A and B. There are two medium blue squares in block A. Below medium blue square number two which is below a medium yellow square there is medium blue square number one. It is below the medium yellow square. Block B is to the right of block A. It contains two medium black squares. There is also a medium blue square in this block. This shape is below medium black square number two. Medium black square number one is below medium black square number two and the medium blue square.",
  "question": "What is the relation between the medium black object that is below a blue square and the black thing that is above a medium square?",
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
| Luna Decisions | DK | Incorrect |
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
    "record": "2191/5",
    "kind": "source_file_record"
  },
  "source_revision": "9892ed1bff9103f5a9103c68bd271b7630ab661e",
  "input_hash": "e7cddf9a8ed145548fa6cff304955325556dbfbb3c2f36a764f63aee1011f983"
}
```

</details>
