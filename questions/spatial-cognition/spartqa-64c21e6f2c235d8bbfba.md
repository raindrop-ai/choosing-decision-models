# Spatial cognition · question 46

[Back to Spatial cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `spartqa/64c21e6f2c235d8bbfba`  
**Source:** [SPARTQA](https://github.com/HLR/SpartQA_generation)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/spatial-cognition/spartqa-64c21e6f2c235d8bbfba/README.md)

## Context

> We have three blocks, A, B and C. Block A has a small black circle and a big blue circle. Below the big blue circle there is the small black circle. Block B is to the right of block A. It contains one big black triangle. There is also one medium black circle touching the right edge of this block. A big blue triangle is also in this block. Above the medium black circle and the big blue triangle there is the big black triangle. Above block B there is block C which has one small yellow circle. One medium blue triangle is also in this block. It is far from a big black circle. Above the medium blue triangle there is the small yellow circle. The big black circle is touching the right edge of this block. To the left of the big black circle there is the small yellow circle.

## Question

> What is to the right of the big blue circle? a big blue triangle or a small black circle?

## Answer choices

- **0:** big blue triangle 
- **1:** small black circle 
- **2:** both of them
- **3:** none of them

**Reference answer:** big blue triangle  (`0`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "We have three blocks, A, B and C. Block A has a small black circle and a big blue circle. Below the big blue circle there is the small black circle. Block B is to the right of block A. It contains one big black triangle. There is also one medium black circle touching the right edge of this block. A big blue triangle is also in this block. Above the medium black circle and the big blue triangle there is the big black triangle. Above block B there is block C which has one small yellow circle. One medium blue triangle is also in this block. It is far from a big black circle. Above the medium blue triangle there is the small yellow circle. The big black circle is touching the right edge of this block. To the left of the big black circle there is the small yellow circle.",
  "question": "What is to the right of the big blue circle? a big blue triangle or a small black circle?",
  "choices": {
    "0": "big blue triangle ",
    "1": "small black circle ",
    "2": "both of them",
    "3": "none of them"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | big blue triangle  | Correct |
| Opus 5.5 | big blue triangle  | Correct |
| GLiDE v1.2 | big blue triangle  | Correct |
| Decider v1.1 | big blue triangle  | Correct |
| Jev | big blue triangle  | Correct |
| Microsoft Decision-1 | big blue triangle  | Correct |
| Clef | big blue triangle  | Correct |
| Luna Decisions | big blue triangle  | Correct |
| Clef Flash | none of them | Incorrect |
| Strands Decider | big blue triangle  | Correct |
| GLiNER2.5 Decide | small black circle  | Incorrect |
| Laya | none of them | Incorrect |
| CalDec v1 | both of them | Incorrect |

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
    "record": "1152/2",
    "kind": "source_file_record"
  },
  "source_revision": "9892ed1bff9103f5a9103c68bd271b7630ab661e",
  "input_hash": "b614d56bbe98c3ab7a57cc94064a447349698d01751ddef9b3f950826153e9db"
}
```

</details>
