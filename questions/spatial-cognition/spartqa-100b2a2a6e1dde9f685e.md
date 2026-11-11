# Spatial cognition · question 42

[Back to Spatial cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `spartqa/100b2a2a6e1dde9f685e`  
**Source:** [SPARTQA](https://github.com/HLR/SpartQA_generation)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/spatial-cognition/spartqa-100b2a2a6e1dde9f685e/README.md)

## Context

> There are three blocks called A, B, and C. B is to the right of A and C is to the right of B. In A, there is a small black triangle near and below a large yellow circle. Far to the right of the yellow circle is a small blue square. In B, there is a large black triangle far below a small blue circle. The small blue circle is near and below a small blue triangle. In C, there is a small blue circle.

## Question

> Is the small blue circle in B below a large black thing?

## Answer choices

- **Yes:** Yes
- **No:** No
- **DK:** DK

**Reference answer:** No (`No`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "There are three blocks called A, B, and C. B is to the right of A and C is to the right of B. In A, there is a small black triangle near and below a large yellow circle. Far to the right of the yellow circle is a small blue square. In B, there is a large black triangle far below a small blue circle. The small blue circle is near and below a small blue triangle. In C, there is a small blue circle.",
  "question": "Is the small blue circle in B below a large black thing?",
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
| Astra | No | Correct |
| Opus 5.5 | No | Correct |
| GLiDE v1.2 | No | Correct |
| Decider v1.1 | No | Correct |
| Jev | No | Correct |
| Microsoft Decision-1 | No | Correct |
| Clef | Yes | Incorrect |
| Luna Decisions | Yes | Incorrect |
| Clef Flash | No | Correct |
| Strands Decider | Yes | Incorrect |
| GLiNER2.5 Decide | No | Correct |
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
    "path": "extracted/SpartQA_Human.zip/SpartQA_Human/human_test.json",
    "record": "23/1",
    "kind": "source_file_record"
  },
  "source_revision": "9892ed1bff9103f5a9103c68bd271b7630ab661e",
  "input_hash": "4dff708958db994f9eaf987964b712d2e338bbb29ddcb948282f22cd02bc7221"
}
```

</details>
