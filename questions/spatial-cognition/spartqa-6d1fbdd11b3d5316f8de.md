# Spatial cognition · question 66

[Back to Spatial cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `spartqa/6d1fbdd11b3d5316f8de`  
**Source:** [SPARTQA](https://github.com/HLR/SpartQA_generation)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/spatial-cognition/spartqa-6d1fbdd11b3d5316f8de/README.md)

## Context

> We have three blocks. We call them A, B and C. Block B is to the left of C and block C is above A. Block A contains one medium yellow circle, one big yellow triangle and one small blue circle. Above a big blue square there is the medium yellow circle. The big yellow triangle is above the small blue circle and the big blue square. Near to the big blue square there is the small blue circle. The medium yellow circle is to the left of the yellow object which is above the small blue circle. The small blue circle is touching the bottom edge of this block. Block B contains one small blue circle. Block C contains two big yellow triangles. Big yellow triangle number one is touching the right edge of this block. Big yellow triangle number two is touching the right edge of this block. There is also one big blue square in this block. It is near to big yellow triangle number two. Below big yellow triangle number two and the big blue square there is big yellow triangle number one.

## Question

> What is the relation between the square which is above big yellow triangle number one and the yellow triangle that is above a big yellow triangle that is touching the right edge of a block?

## Answer choices

- **0:** left
- **1:** right
- **2:** above
- **3:** below
- **4:** near to
- **5:** far from
- **6:** touching
- **7:** DK

**Reference answer:** near to (`4`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "We have three blocks. We call them A, B and C. Block B is to the left of C and block C is above A. Block A contains one medium yellow circle, one big yellow triangle and one small blue circle. Above a big blue square there is the medium yellow circle. The big yellow triangle is above the small blue circle and the big blue square. Near to the big blue square there is the small blue circle. The medium yellow circle is to the left of the yellow object which is above the small blue circle. The small blue circle is touching the bottom edge of this block. Block B contains one small blue circle. Block C contains two big yellow triangles. Big yellow triangle number one is touching the right edge of this block. Big yellow triangle number two is touching the right edge of this block. There is also one big blue square in this block. It is near to big yellow triangle number two. Below big yellow triangle number two and the big blue square there is big yellow triangle number one.",
  "question": "What is the relation between the square which is above big yellow triangle number one and the yellow triangle that is above a big yellow triangle that is touching the right edge of a block?",
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
| Astra | near to | Correct |
| Opus 5.5 | near to | Correct |
| GLiDE v1.2 | near to | Correct |
| Decider v1.1 | near to | Correct |
| Jev | near to | Correct |
| Microsoft Decision-1 | near to | Correct |
| Clef | near to | Correct |
| Luna Decisions | DK | Incorrect |
| Clef Flash | right | Incorrect |
| Strands Decider | near to | Correct |
| GLiNER2.5 Decide | touching | Incorrect |
| Laya | below | Incorrect |
| CalDec v1 | below | Incorrect |

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
    "record": "4467/5",
    "kind": "source_file_record"
  },
  "source_revision": "9892ed1bff9103f5a9103c68bd271b7630ab661e",
  "input_hash": "0b5c8ee97b14771058f96b3187c42b475cfd5442b3e4d27c21f9141fb21d2b6d"
}
```

</details>
