# Spatial cognition · question 34

[Back to Spatial cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `spartqa/0d3f975b3e4455fb632e`  
**Source:** [SPARTQA](https://github.com/HLR/SpartQA_generation)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/spatial-cognition/spartqa-0d3f975b3e4455fb632e/README.md)

## Context

> We have three blocks. We call them A, B and C. There is a medium yellow circle in block A. Then, we have block B. It contains one big black square. A big black circle is also in this block. The big black square is far from the big black circle. Block C is above block A and to the right of block B. It has one medium blue square and a small blue circle. The medium blue square is below the small blue circle.

## Question

> Is the medium yellow circle , below a medium shape that is below a small thing?

## Answer choices

- **Yes:** Yes
- **No:** No
- **DK:** DK

**Reference answer:** Yes (`Yes`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "We have three blocks. We call them A, B and C. There is a medium yellow circle in block A. Then, we have block B. It contains one big black square. A big black circle is also in this block. The big black square is far from the big black circle. Block C is above block A and to the right of block B. It has one medium blue square and a small blue circle. The medium blue square is below the small blue circle.",
  "question": "Is the medium yellow circle , below a medium shape that is below a small thing?",
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
| Clef | No | Incorrect |
| Luna Decisions | DK | Incorrect |
| Clef Flash | No | Incorrect |
| Strands Decider | Yes | Correct |
| GLiNER2.5 Decide | No | Incorrect |
| Laya | Yes | Correct |
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
    "path": "extracted/SpartQA_Auto.zip/SpartQA_Auto/train.json",
    "record": "763/1",
    "kind": "source_file_record"
  },
  "source_revision": "9892ed1bff9103f5a9103c68bd271b7630ab661e",
  "input_hash": "8f81d405e15a768df805fc1dbad96eac9d7ee58a2047d759820d970b0df67e5d"
}
```

</details>
