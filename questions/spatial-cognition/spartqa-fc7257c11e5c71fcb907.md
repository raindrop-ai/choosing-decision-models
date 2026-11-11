# Spatial cognition · question 64

[Back to Spatial cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `spartqa/fc7257c11e5c71fcb907`  
**Source:** [SPARTQA](https://github.com/HLR/SpartQA_generation)  
**Input format:** adapted choices

[Explore this question’s altered versions](../../variants/spatial-cognition/spartqa-fc7257c11e5c71fcb907/README.md)

## Context

> We have three blocks, A, B and C. Block B is below blocks C and A. Block A contains one medium blue square. The medium blue square is below a medium yellow square. Block B has two medium black squares. Below medium black square number two there is medium black square number one. Block C contains a medium black square.

## Question

> Which blocks don't have any medium shape that is below a black square?

## Answer choices

- **A:** \[&quot;A&quot;\]
- **B:** \[\]
- **C:** \[&quot;B&quot;\]
- **D:** \[&quot;B&quot;, &quot;C&quot;\]
- **E:** \[&quot;A&quot;, &quot;B&quot;, &quot;C&quot;\]
- **F:** \[&quot;A&quot;, &quot;C&quot;\]
- **G:** \[&quot;A&quot;, &quot;B&quot;\]
- **H:** \[&quot;C&quot;\]

**Reference answer:** \[&quot;A&quot;, &quot;C&quot;\] (`F`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "We have three blocks, A, B and C. Block B is below blocks C and A. Block A contains one medium blue square. The medium blue square is below a medium yellow square. Block B has two medium black squares. Below medium black square number two there is medium black square number one. Block C contains a medium black square.",
  "question": "Which blocks don't have any medium shape that is below a black square?",
  "choices": {
    "A": "[\"A\"]",
    "B": "[]",
    "C": "[\"B\"]",
    "D": "[\"B\", \"C\"]",
    "E": "[\"A\", \"B\", \"C\"]",
    "F": "[\"A\", \"C\"]",
    "G": "[\"A\", \"B\"]",
    "H": "[\"C\"]"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | \[&quot;A&quot;, &quot;C&quot;\] | Correct |
| Opus 5.5 | \[&quot;A&quot;, &quot;C&quot;\] | Correct |
| GLiDE v1.2 | \[&quot;A&quot;, &quot;C&quot;\] | Correct |
| Decider v1.1 | \[&quot;A&quot;, &quot;C&quot;\] | Correct |
| Jev | \[&quot;A&quot;, &quot;C&quot;\] | Correct |
| Microsoft Decision-1 | \[&quot;A&quot;, &quot;C&quot;\] | Correct |
| Clef | \[&quot;A&quot;, &quot;C&quot;\] | Correct |
| Luna Decisions | \[&quot;A&quot;, &quot;C&quot;\] | Correct |
| Clef Flash | \[&quot;A&quot;, &quot;C&quot;\] | Correct |
| Strands Decider | \[&quot;A&quot;\] | Incorrect |
| GLiNER2.5 Decide | \[&quot;A&quot;\] | Incorrect |
| Laya | \[&quot;B&quot;, &quot;C&quot;\] | Incorrect |
| CalDec v1 | \[&quot;B&quot;\] | Incorrect |

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
    "record": "10509/6",
    "kind": "source_file_record"
  },
  "source_revision": "9892ed1bff9103f5a9103c68bd271b7630ab661e",
  "input_hash": "a8b17309e0b3948b8d3d261961166140ab0c576218e4e346b3675c62f670924a"
}
```

</details>
