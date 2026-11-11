# Spatial cognition · question 14

[Back to Spatial cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `spartqa/1be52e164cba70ab5683`  
**Source:** [SPARTQA](https://github.com/HLR/SpartQA_generation)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/spatial-cognition/spartqa-1be52e164cba70ab5683/README.md)

## Context

> We have two blocks, A and B. Block A contains one medium yellow square. There is also a medium black square in this block. Below the medium yellow square is the medium black square. Block B is to the left of block A. It contains two medium yellow squares. Below medium yellow square number two is medium yellow square number one. A medium black square is touching the bottom edge of this block. It is below medium yellow square number one and medium yellow square number two.

## Question

> Which object is to the left of a medium black square? medium yellow square number two or medium yellow square number one?

## Answer choices

- **0:** medium yellow square  number two
- **1:** medium yellow square  number one
- **2:** both of them
- **3:** none of them

**Reference answer:** both of them (`2`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "We have two blocks, A and B. Block A contains one medium yellow square. There is also a medium black square in this block. Below the medium yellow square is the medium black square. Block B is to the left of block A. It contains two medium yellow squares. Below medium yellow square number two is medium yellow square number one. A medium black square is touching the bottom edge of this block. It is below medium yellow square number one and medium yellow square number two.",
  "question": "Which object is to the left of a medium black square? medium yellow square number two or medium yellow square number one?",
  "choices": {
    "0": "medium yellow square  number two",
    "1": "medium yellow square  number one",
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
| Luna Decisions | both of them | Correct |
| Clef Flash | both of them | Correct |
| Strands Decider | both of them | Correct |
| GLiNER2.5 Decide | medium yellow square  number one | Incorrect |
| Laya | both of them | Correct |
| CalDec v1 | both of them | Correct |

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
    "record": "3587/2",
    "kind": "source_file_record"
  },
  "source_revision": "9892ed1bff9103f5a9103c68bd271b7630ab661e",
  "input_hash": "4a769938cd98b47af4217c3ea2e23c4a29b942c1b460af2ff7a6a5b272139d9b"
}
```

</details>
