# Spatial cognition · question 48

[Back to Spatial cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `spartqa/c1596942e6f6fbff9be2`  
**Source:** [SPARTQA](https://github.com/HLR/SpartQA_generation)  
**Input format:** adapted choices

[Explore this question’s altered versions](../../variants/spatial-cognition/spartqa-c1596942e6f6fbff9be2/README.md)

## Context

> There are three blocks, A, B and C. There is one medium yellow square in block A. To the right of block A is block B with one medium black square in it. There is also a medium blue square touching the bottom edge of this block. Below the medium black square is the medium blue square. Finally, we have block C to the right of block A. It has two medium yellow squares. There is also one medium black square in this block. It is below medium yellow square number two. Medium yellow square number one is touching the bottom edge of this block. This object is below medium yellow square number two and the medium black square.

## Question

> Which blocks don't have any medium square which is to the right of a yellow square?

## Answer choices

- **A:** \[&quot;A&quot;, &quot;B&quot;\]
- **B:** \[&quot;A&quot;, &quot;B&quot;, &quot;C&quot;\]
- **C:** \[&quot;A&quot;\]
- **D:** \[&quot;B&quot;, &quot;C&quot;\]
- **E:** \[&quot;C&quot;\]
- **F:** \[\]
- **G:** \[&quot;B&quot;\]
- **H:** \[&quot;A&quot;, &quot;C&quot;\]

**Reference answer:** \[&quot;A&quot;\] (`C`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "There are three blocks, A, B and C. There is one medium yellow square in block A. To the right of block A is block B with one medium black square in it. There is also a medium blue square touching the bottom edge of this block. Below the medium black square is the medium blue square. Finally, we have block C to the right of block A. It has two medium yellow squares. There is also one medium black square in this block. It is below medium yellow square number two. Medium yellow square number one is touching the bottom edge of this block. This object is below medium yellow square number two and the medium black square.",
  "question": "Which blocks don't have any medium square which is to the right of a yellow square?",
  "choices": {
    "A": "[\"A\", \"B\"]",
    "B": "[\"A\", \"B\", \"C\"]",
    "C": "[\"A\"]",
    "D": "[\"B\", \"C\"]",
    "E": "[\"C\"]",
    "F": "[]",
    "G": "[\"B\"]",
    "H": "[\"A\", \"C\"]"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | \[&quot;A&quot;\] | Correct |
| Opus 5.5 | \[&quot;A&quot;\] | Correct |
| GLiDE v1.2 | \[&quot;A&quot;\] | Correct |
| Decider v1.1 | \[&quot;A&quot;\] | Correct |
| Jev | \[&quot;A&quot;, &quot;B&quot;\] | Incorrect |
| Microsoft Decision-1 | \[&quot;A&quot;\] | Correct |
| Clef | \[&quot;A&quot;, &quot;B&quot;\] | Incorrect |
| Luna Decisions | \[&quot;A&quot;, &quot;B&quot;\] | Incorrect |
| Clef Flash | \[&quot;A&quot;, &quot;B&quot;\] | Incorrect |
| Strands Decider | \[&quot;A&quot;\] | Correct |
| GLiNER2.5 Decide | \[&quot;A&quot;, &quot;C&quot;\] | Incorrect |
| Laya | \[&quot;A&quot;, &quot;B&quot;\] | Incorrect |
| CalDec v1 | \[&quot;A&quot;, &quot;B&quot;\] | Incorrect |

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
    "record": "9778/6",
    "kind": "source_file_record"
  },
  "source_revision": "9892ed1bff9103f5a9103c68bd271b7630ab661e",
  "input_hash": "1b994e7162e4b4a3bf2dbbda763b3cb882271a0bdc5a6fe9c3a1dd35c7f27b1d"
}
```

</details>
