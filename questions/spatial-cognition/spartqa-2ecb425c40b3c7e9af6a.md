# Spatial cognition · question 6

[Back to Spatial cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `spartqa/2ecb425c40b3c7e9af6a`  
**Source:** [SPARTQA](https://github.com/HLR/SpartQA_generation)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/spatial-cognition/spartqa-2ecb425c40b3c7e9af6a/README.md)

## Context

> There are three blocks, A, B and C. Block A contains a large blue rectangle and one small white diamond. The large blue rectangle is to the right side of the small white diamond. Then, we have block B with a midsize blue diamond and a large white circle in it. The large white circle is touching the bottom edge of this block. The midsize blue diamond is touching the bottom edge of this block. It is to the right side of the large white circle. Block C is to the left side of block A and on the top of block B. It contains one small blue circle. To the left side of and under the small blue circle there is a midsize red rectangle.

## Question

> What is the relation between the large blue rectangle and the small shape that is to the right side of a blue circle?

## Answer choices

- **0:** left
- **1:** right
- **2:** top
- **3:** under
- **4:** close to
- **5:** far from
- **6:** touching
- **7:** DK

**Reference answer:** right (`1`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "There are three blocks, A, B and C. Block A contains a large blue rectangle and one small white diamond. The large blue rectangle is to the right side of the small white diamond. Then, we have block B with a midsize blue diamond and a large white circle in it. The large white circle is touching the bottom edge of this block. The midsize blue diamond is touching the bottom edge of this block. It is to the right side of the large white circle. Block C is to the left side of block A and on the top of block B. It contains one small blue circle. To the left side of and under the small blue circle there is a midsize red rectangle.",
  "question": "What is the relation between the large blue rectangle and the small shape that is to the right side of a blue circle?",
  "choices": {
    "0": "left",
    "1": "right",
    "2": "top",
    "3": "under",
    "4": "close to",
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
| Astra | right | Correct |
| Opus 5.5 | right | Correct |
| GLiDE v1.2 | right | Correct |
| Decider v1.1 | right | Correct |
| Jev | right | Correct |
| Microsoft Decision-1 | right | Correct |
| Clef | far from | Incorrect |
| Luna Decisions | DK | Incorrect |
| Clef Flash | far from | Incorrect |
| Strands Decider | right | Correct |
| GLiNER2.5 Decide | right | Correct |
| Laya | under | Incorrect |
| CalDec v1 | under | Incorrect |

## Source and sharing

Attribution: HLR / Roshanak Mirzaee et al..  
Terms: **[MIT](https://opensource.org/license/mit)**. [Source sharing decision](../../docs/data-sharing.md).  
The capability assignment and choice-format normalization are part of this experiment. Source data retain their own terms.

<details>
<summary>Exact source locator and input fingerprint</summary>

```json
{
  "source_locator": {
    "path": "extracted/SpartQA_Auto.zip/SpartQA_Auto/unseen_test.json",
    "record": "848/5",
    "kind": "source_file_record"
  },
  "source_revision": "9892ed1bff9103f5a9103c68bd271b7630ab661e",
  "input_hash": "29ab9b6a809411d7d9a81c649f131e77c7d6a455ed8540ea18c3c9fe72f167a2"
}
```

</details>
