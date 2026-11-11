# Spatial cognition · question 12

[Back to Spatial cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `spartqa/6cea3e0444d515c7f763`  
**Source:** [SPARTQA](https://github.com/HLR/SpartQA_generation)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/spatial-cognition/spartqa-6cea3e0444d515c7f763/README.md)

## Context

> There are two blocks, A and B. Block A is below B. Block A has a medium black diamond. Block B contains one big yellow oval and a little black diamond. There is also one big blue oval touching the bottom edge of this block. A big blue rectangle is to the right side of, close to and on the top of the big blue oval. Below and to the left of the little black diamond there is the big yellow oval. The little black diamond is touching the right side edge of this block.

## Question

> What is the relation between the medium shape and the big blue shape that is on the top of a big blue oval which is touching the bottom edge of a block?

## Answer choices

- **0:** left
- **1:** right
- **2:** top
- **3:** below
- **4:** close to
- **5:** far from
- **6:** touching
- **7:** DK

**Reference answer:** below (`3`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "There are two blocks, A and B. Block A is below B. Block A has a medium black diamond. Block B contains one big yellow oval and a little black diamond. There is also one big blue oval touching the bottom edge of this block. A big blue rectangle is to the right side of, close to and on the top of the big blue oval. Below and to the left of the little black diamond there is the big yellow oval. The little black diamond is touching the right side edge of this block.",
  "question": "What is the relation between the medium shape and the big blue shape that is on the top of a big blue oval which is touching the bottom edge of a block?",
  "choices": {
    "0": "left",
    "1": "right",
    "2": "top",
    "3": "below",
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
| Astra | below | Correct |
| Opus 5.5 | below | Correct |
| GLiDE v1.2 | below | Correct |
| Decider v1.1 | below | Correct |
| Jev | left | Incorrect |
| Microsoft Decision-1 | below | Correct |
| Clef | far from | Incorrect |
| Luna Decisions | left | Incorrect |
| Clef Flash | far from | Incorrect |
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
    "path": "extracted/SpartQA_Auto.zip/SpartQA_Auto/unseen_test.json",
    "record": "268/5",
    "kind": "source_file_record"
  },
  "source_revision": "9892ed1bff9103f5a9103c68bd271b7630ab661e",
  "input_hash": "3ae84ccc847ba883a494a4a4b7caa7665b4b758f4107432e0666b208cee56d10"
}
```

</details>
