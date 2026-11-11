# Spatial cognition · question 40

[Back to Spatial cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `spartqa/acacc62dcd74344b8531`  
**Source:** [SPARTQA](https://github.com/HLR/SpartQA_generation)  
**Input format:** adapted choices

[Explore this question’s altered versions](../../variants/spatial-cognition/spartqa-acacc62dcd74344b8531/README.md)

## Context

> We have three blocks. We call them A, B and C. There are two medium blue squares in block A. Medium blue square number one is touching the bottom edge of this block. Medium blue square number two is below a medium black square. Medium blue square number one is below medium blue square number two and the medium black square. Block B is to the left of block A. It has two medium yellow squares. Medium yellow square number one is touching the bottom edge of this block. It is below medium yellow square number two. To the right of block A there is block C. It contains a medium yellow square.

## Question

> Which blocks don't have any medium yellow thing that is to the right of a medium blue shape?

## Answer choices

- **A:** \[\]
- **B:** \[&quot;A&quot;, &quot;C&quot;\]
- **C:** \[&quot;B&quot;, &quot;C&quot;\]
- **D:** \[&quot;A&quot;, &quot;B&quot;\]
- **E:** \[&quot;A&quot;\]
- **F:** \[&quot;A&quot;, &quot;B&quot;, &quot;C&quot;\]
- **G:** \[&quot;C&quot;\]
- **H:** \[&quot;B&quot;\]

**Reference answer:** \[&quot;A&quot;, &quot;B&quot;\] (`D`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "We have three blocks. We call them A, B and C. There are two medium blue squares in block A. Medium blue square number one is touching the bottom edge of this block. Medium blue square number two is below a medium black square. Medium blue square number one is below medium blue square number two and the medium black square. Block B is to the left of block A. It has two medium yellow squares. Medium yellow square number one is touching the bottom edge of this block. It is below medium yellow square number two. To the right of block A there is block C. It contains a medium yellow square.",
  "question": "Which blocks don't have any medium yellow thing that is to the right of a medium blue shape?",
  "choices": {
    "A": "[]",
    "B": "[\"A\", \"C\"]",
    "C": "[\"B\", \"C\"]",
    "D": "[\"A\", \"B\"]",
    "E": "[\"A\"]",
    "F": "[\"A\", \"B\", \"C\"]",
    "G": "[\"C\"]",
    "H": "[\"B\"]"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | \[&quot;A&quot;, &quot;B&quot;\] | Correct |
| Opus 5.5 | \[&quot;A&quot;, &quot;B&quot;\] | Correct |
| GLiDE v1.2 | \[&quot;A&quot;, &quot;B&quot;\] | Correct |
| Decider v1.1 | \[&quot;A&quot;, &quot;B&quot;\] | Correct |
| Jev | \[&quot;A&quot;, &quot;B&quot;\] | Correct |
| Microsoft Decision-1 | \[&quot;B&quot;\] | Incorrect |
| Clef | \[&quot;A&quot;\] | Incorrect |
| Luna Decisions | \[&quot;A&quot;, &quot;B&quot;\] | Correct |
| Clef Flash | \[&quot;A&quot;, &quot;B&quot;\] | Correct |
| Strands Decider | \[&quot;B&quot;\] | Incorrect |
| GLiNER2.5 Decide | \[&quot;B&quot;\] | Incorrect |
| Laya | \[&quot;B&quot;, &quot;C&quot;\] | Incorrect |
| CalDec v1 | \[&quot;A&quot;, &quot;C&quot;\] | Incorrect |

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
    "record": "818/6",
    "kind": "source_file_record"
  },
  "source_revision": "9892ed1bff9103f5a9103c68bd271b7630ab661e",
  "input_hash": "395662700604269658ac9168f4e5c0b6c162e2e68637741b9a88dc177eeaa7d0"
}
```

</details>
