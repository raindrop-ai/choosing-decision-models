# Spatial cognition · question 24

[Back to Spatial cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `spartqa/0c46508136ffd72b9fde`  
**Source:** [SPARTQA](https://github.com/HLR/SpartQA_generation)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/spatial-cognition/spartqa-0c46508136ffd72b9fde/README.md)

## Context

> We have two blocks. Lets call them A and B. Block A contains one small black circle, a small black triangle and a medium black circle. The small black circle is to the left of the medium black circle. Near to the medium black circle there is the small black triangle. To the left of the black shape which is near to the medium black circle is the small black circle. To the left of block A there is block B. It contains one big yellow circle, a medium black triangle and one big yellow triangle. The big yellow circle is below the big yellow triangle. The medium black triangle is above and to the left of the big yellow triangle.

## Question

> Which object is to the left of a small black circle? the big yellow circle or the medium black triangle?

## Answer choices

- **0:** the big yellow circle 
- **1:** the medium black triangle 
- **2:** both of them
- **3:** none of them

**Reference answer:** both of them (`2`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "We have two blocks. Lets call them A and B. Block A contains one small black circle, a small black triangle and a medium black circle. The small black circle is to the left of the medium black circle. Near to the medium black circle there is the small black triangle. To the left of the black shape which is near to the medium black circle is the small black circle. To the left of block A there is block B. It contains one big yellow circle, a medium black triangle and one big yellow triangle. The big yellow circle is below the big yellow triangle. The medium black triangle is above and to the left of the big yellow triangle.",
  "question": "Which object is to the left of a small black circle? the big yellow circle or the medium black triangle?",
  "choices": {
    "0": "the big yellow circle ",
    "1": "the medium black triangle ",
    "2": "both of them",
    "3": "none of them"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | both of them | Correct |
| Opus 5.5 | both of them | Correct |
| GLiDE v1.2 | both of them | Correct |
| Decider v1.1 | both of them | Correct |
| Jev | both of them | Correct |
| Microsoft Decision-1 | both of them | Correct |
| Clef | both of them | Correct |
| Luna Decisions | none of them | Incorrect |
| Clef Flash | the big yellow circle  | Incorrect |
| Strands Decider | the big yellow circle  | Incorrect |
| GLiNER2.5 Decide | the medium black triangle  | Incorrect |
| Laya | the big yellow circle  | Incorrect |
| CalDec v1 | the medium black triangle  | Incorrect |

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
    "record": "8170/2",
    "kind": "source_file_record"
  },
  "source_revision": "9892ed1bff9103f5a9103c68bd271b7630ab661e",
  "input_hash": "f0d4415aabd1134eeab4df26429a92b427712bd6d49d3250f0f4136aedef3b0d"
}
```

</details>
