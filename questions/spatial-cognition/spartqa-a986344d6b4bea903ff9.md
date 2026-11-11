# Spatial cognition · question 18

[Back to Spatial cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `spartqa/a986344d6b4bea903ff9`  
**Source:** [SPARTQA](https://github.com/HLR/SpartQA_generation)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/spatial-cognition/spartqa-a986344d6b4bea903ff9/README.md)

## Context

> We have two blocks. Lets call them A and B. Block A is to the left of B. Block A contains a small black triangle. Block B has a medium blue square, a medium black square and one small yellow triangle. The medium blue square is above and to the right of the medium black square which is near to a small black square and the small yellow triangle.

## Question

> Is the small black triangle , to the left of all black squares that are near to a black square?

## Answer choices

- **Yes:** Yes
- **No:** No
- **DK:** DK

**Reference answer:** Yes (`Yes`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "We have two blocks. Lets call them A and B. Block A is to the left of B. Block A contains a small black triangle. Block B has a medium blue square, a medium black square and one small yellow triangle. The medium blue square is above and to the right of the medium black square which is near to a small black square and the small yellow triangle.",
  "question": "Is the small black triangle , to the left of all black squares that are near to a black square?",
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
    "record": "12841/0",
    "kind": "source_file_record"
  },
  "source_revision": "9892ed1bff9103f5a9103c68bd271b7630ab661e",
  "input_hash": "77677490595fce474b48711ac4350397c83fbbcc5bf732d6b92ab93e40aa3ffb"
}
```

</details>
