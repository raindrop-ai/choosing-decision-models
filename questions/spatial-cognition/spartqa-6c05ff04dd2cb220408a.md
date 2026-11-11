# Spatial cognition · question 60

[Back to Spatial cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `spartqa/6c05ff04dd2cb220408a`  
**Source:** [SPARTQA](https://github.com/HLR/SpartQA_generation)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/spatial-cognition/spartqa-6c05ff04dd2cb220408a/README.md)

## Context

> We have three blocks. We call them A, B and C. Block A is below and C is to the left of B. Block A has one big blue triangle. Block B contains a small black square and a small blue square. One small blue triangle is also touching the right edge of this block. Below the small blue triangle is the small black square. To the left of and above the small blue triangle there is the small blue square. Block C has one small blue square.

## Question

> What is the relation between the small blue triangle that is below a small blue shape and the big thing?

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
  "state": "We have three blocks. We call them A, B and C. Block A is below and C is to the left of B. Block A has one big blue triangle. Block B contains a small black square and a small blue square. One small blue triangle is also touching the right edge of this block. Below the small blue triangle is the small black square. To the left of and above the small blue triangle there is the small blue square. Block C has one small blue square.",
  "question": "What is the relation between the small blue triangle that is below a small blue shape and the big thing?",
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
| Jev | right | Incorrect |
| Microsoft Decision-1 | above | Correct |
| Clef | far from | Incorrect |
| Luna Decisions | below | Incorrect |
| Clef Flash | far from | Incorrect |
| Strands Decider | below | Incorrect |
| GLiNER2.5 Decide | touching | Incorrect |
| Laya | above | Correct |
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
    "record": "7914/4",
    "kind": "source_file_record"
  },
  "source_revision": "9892ed1bff9103f5a9103c68bd271b7630ab661e",
  "input_hash": "6b846c5fe8f650cdcba840411452fbfcf9af003916ca61d67380373b6c9cd309"
}
```

</details>
