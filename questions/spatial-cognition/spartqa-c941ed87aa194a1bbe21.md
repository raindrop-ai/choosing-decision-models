# Spatial cognition · question 2

[Back to Spatial cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `spartqa/c941ed87aa194a1bbe21`  
**Source:** [SPARTQA](https://github.com/HLR/SpartQA_generation)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/spatial-cognition/spartqa-c941ed87aa194a1bbe21/README.md)

## Context

> There are three blocks, A, B and C. Block A is to the left of C and block B is below A. Block A contains two small blue squares. There is also a medium blue circle in this block. To the right of small blue square number two there is the medium blue circle. A medium yellow square is above a big yellow triangle. The big yellow triangle is to the right of small blue square number two. Small blue square number one is touching the right edge of this block. The medium yellow square is near to and above small blue square number one. Block B contains a big yellow circle. The big yellow circle is to the right of a big yellow triangle. And block C has a small blue triangle and a medium blue circle. The small blue triangle is touching the right edge of this block. The medium blue circle is touching the bottom edge of this block. Above and to the right of the medium blue circle there is the small blue triangle.

## Question

> Are all medium blue circles that are to the left of a small blue triangle that is touching the right edge of a block , near to all yellow objects that are below a medium circle that is in block A?

## Answer choices

- **Yes:** Yes
- **No:** No
- **DK:** DK

**Reference answer:** DK (`DK`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "There are three blocks, A, B and C. Block A is to the left of C and block B is below A. Block A contains two small blue squares. There is also a medium blue circle in this block. To the right of small blue square number two there is the medium blue circle. A medium yellow square is above a big yellow triangle. The big yellow triangle is to the right of small blue square number two. Small blue square number one is touching the right edge of this block. The medium yellow square is near to and above small blue square number one. Block B contains a big yellow circle. The big yellow circle is to the right of a big yellow triangle. And block C has a small blue triangle and a medium blue circle. The small blue triangle is touching the right edge of this block. The medium blue circle is touching the bottom edge of this block. Above and to the right of the medium blue circle there is the small blue triangle.",
  "question": "Are all medium blue circles that are to the left of a small blue triangle that is touching the right edge of a block , near to all yellow objects that are below a medium circle that is in block A?",
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
| Astra | DK | Correct |
| Opus 5.5 | DK | Correct |
| GLiDE v1.2 | DK | Correct |
| Decider v1.1 | DK | Correct |
| Jev | No | Incorrect |
| Microsoft Decision-1 | No | Incorrect |
| Clef | Yes | Incorrect |
| Luna Decisions | Yes | Incorrect |
| Clef Flash | No | Incorrect |
| Strands Decider | No | Incorrect |
| GLiNER2.5 Decide | Yes | Incorrect |
| Laya | Yes | Incorrect |
| CalDec v1 | Yes | Incorrect |

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
    "record": "7521/1",
    "kind": "source_file_record"
  },
  "source_revision": "9892ed1bff9103f5a9103c68bd271b7630ab661e",
  "input_hash": "aecd42d841fb9f2095051d5bdaa62f3a9f28e9cf78baba83ee0fc49a2963ea41"
}
```

</details>
