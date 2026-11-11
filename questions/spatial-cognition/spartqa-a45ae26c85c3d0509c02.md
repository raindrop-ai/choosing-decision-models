# Spatial cognition · question 22

[Back to Spatial cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `spartqa/a45ae26c85c3d0509c02`  
**Source:** [SPARTQA](https://github.com/HLR/SpartQA_generation)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/spatial-cognition/spartqa-a45ae26c85c3d0509c02/README.md)

## Context

> There are three blocks. We call them A, B and C. Block B is to the left of A and block A is below C. Block A has a big blue triangle, one big yellow square and a medium blue triangle. The big blue triangle is below the big yellow square which is above, near to and to the left of the medium blue triangle. This block also has a big black square. This object is touching the right edge of this block. To the left of the medium blue triangle there is the big blue triangle. The big yellow square is touching the top edge of this block. Block B contains a small yellow circle, a small yellow square and a medium black circle. The small yellow circle is to the left of the medium black circle. The small yellow square is to the right of the medium black circle. It is touching the bottom edge of this block. The small yellow circle is above the small yellow square. The medium black circle is touching the bottom edge of this block. And block C contains one small blue circle.

## Question

> What is the relation between the small blue circle and the big triangle that is to the right of a small yellow square that is touching the bottom edge of a block?

## Answer choices

- **0:** left
- **1:** right
- **2:** above
- **3:** below
- **4:** near to
- **5:** far from
- **6:** touching
- **7:** DK

**Reference answer:** above (`2`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "There are three blocks. We call them A, B and C. Block B is to the left of A and block A is below C. Block A has a big blue triangle, one big yellow square and a medium blue triangle. The big blue triangle is below the big yellow square which is above, near to and to the left of the medium blue triangle. This block also has a big black square. This object is touching the right edge of this block. To the left of the medium blue triangle there is the big blue triangle. The big yellow square is touching the top edge of this block. Block B contains a small yellow circle, a small yellow square and a medium black circle. The small yellow circle is to the left of the medium black circle. The small yellow square is to the right of the medium black circle. It is touching the bottom edge of this block. The small yellow circle is above the small yellow square. The medium black circle is touching the bottom edge of this block. And block C contains one small blue circle.",
  "question": "What is the relation between the small blue circle and the big triangle that is to the right of a small yellow square that is touching the bottom edge of a block?",
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
| Astra | above | Correct |
| Opus 5.5 | above | Correct |
| GLiDE v1.2 | above | Correct |
| Decider v1.1 | above | Correct |
| Jev | DK | Incorrect |
| Microsoft Decision-1 | above | Correct |
| Clef | far from | Incorrect |
| Luna Decisions | DK | Incorrect |
| Clef Flash | far from | Incorrect |
| Strands Decider | left | Incorrect |
| GLiNER2.5 Decide | touching | Incorrect |
| Laya | below | Incorrect |
| CalDec v1 | above | Correct |

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
    "record": "6625/4",
    "kind": "source_file_record"
  },
  "source_revision": "9892ed1bff9103f5a9103c68bd271b7630ab661e",
  "input_hash": "44bc95b1b7d28494cab4c882dd05d698f74094a0e2fa5cb1d544b6c6d7190bfd"
}
```

</details>
