# Spatial cognition · question 56

[Back to Spatial cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `spartqa/e957e04abe5a035ea3a3`  
**Source:** [SPARTQA](https://github.com/HLR/SpartQA_generation)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/spatial-cognition/spartqa-e957e04abe5a035ea3a3/README.md)

## Context

> There are three blocks. We call them A, B and C. Block A is above B. Block B is to the right of C. Block A contains one medium yellow square. Block B contains a medium black square. A medium blue square is below the medium black square. Block C contains two medium yellow squares. Medium yellow square number one is below medium yellow square number two.. A medium blue square is below medium yellow square number one and medium yellow square number two.

## Question

> Which object is to the left of a medium blue square? the medium yellow square that is in block A or medium yellow square number one?

## Answer choices

- **0:** the medium yellow square  that is in block A
- **1:** medium yellow square  number one
- **2:** both of them
- **3:** none of them

**Reference answer:** medium yellow square  number one (`1`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "There are three blocks. We call them A, B and C. Block A is above B. Block B is to the right of C. Block A contains one medium yellow square. Block B contains a medium black square. A medium blue square is below the medium black square. Block C contains two medium yellow squares. Medium yellow square number one is below medium yellow square number two.. A medium blue square is below medium yellow square number one and medium yellow square number two.",
  "question": "Which object is to the left of a medium blue square? the medium yellow square that is in block A or medium yellow square number one?",
  "choices": {
    "0": "the medium yellow square  that is in block A",
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
| Astra | medium yellow square  number one | Correct |
| Opus 5.5 | medium yellow square  number one | Correct |
| GLiDE v1.2 | medium yellow square  number one | Correct |
| Decider v1.1 | medium yellow square  number one | Correct |
| Jev | medium yellow square  number one | Correct |
| Microsoft Decision-1 | medium yellow square  number one | Correct |
| Clef | both of them | Incorrect |
| Luna Decisions | none of them | Incorrect |
| Clef Flash | medium yellow square  number one | Correct |
| Strands Decider | medium yellow square  number one | Correct |
| GLiNER2.5 Decide | medium yellow square  number one | Correct |
| Laya | both of them | Incorrect |
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
    "record": "11769/3",
    "kind": "source_file_record"
  },
  "source_revision": "9892ed1bff9103f5a9103c68bd271b7630ab661e",
  "input_hash": "786924d78fe0ca964de424a8d65af6b76c94db4fe07b7bd5e0adfef72b2b74a2"
}
```

</details>
