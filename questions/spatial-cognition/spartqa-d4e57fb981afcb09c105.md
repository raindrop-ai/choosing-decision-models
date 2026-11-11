# Spatial cognition · question 28

[Back to Spatial cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `spartqa/d4e57fb981afcb09c105`  
**Source:** [SPARTQA](https://github.com/HLR/SpartQA_generation)  
**Input format:** adapted choices

[Explore this question’s altered versions](../../variants/spatial-cognition/spartqa-d4e57fb981afcb09c105/README.md)

## Context

> There are two blocks. We call them A and B. Block A is to the left of B. Block A contains two medium blue squares. Medium blue square number one is below medium blue square number two. Block B has a medium yellow square and a medium black square. The medium yellow square is below the medium black square. There is also a medium blue square in this block. Below the medium black square and the medium yellow square is the medium blue square.

## Question

> Which blocks have a square that is above a medium blue shape?

## Answer choices

- **A:** \[&quot;A&quot;, &quot;B&quot;\]
- **B:** \[&quot;B&quot;\]
- **C:** \[&quot;C&quot;\]
- **D:** \[&quot;A&quot;, &quot;B&quot;, &quot;C&quot;\]
- **E:** \[\]
- **F:** \[&quot;A&quot;\]
- **G:** \[&quot;A&quot;, &quot;C&quot;\]
- **H:** \[&quot;B&quot;, &quot;C&quot;\]

**Reference answer:** \[&quot;A&quot;, &quot;B&quot;\] (`A`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "There are two blocks. We call them A and B. Block A is to the left of B. Block A contains two medium blue squares. Medium blue square number one is below medium blue square number two. Block B has a medium yellow square and a medium black square. The medium yellow square is below the medium black square. There is also a medium blue square in this block. Below the medium black square and the medium yellow square is the medium blue square.",
  "question": "Which blocks have a square that is above a medium blue shape?",
  "choices": {
    "A": "[\"A\", \"B\"]",
    "B": "[\"B\"]",
    "C": "[\"C\"]",
    "D": "[\"A\", \"B\", \"C\"]",
    "E": "[]",
    "F": "[\"A\"]",
    "G": "[\"A\", \"C\"]",
    "H": "[\"B\", \"C\"]"
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
| Microsoft Decision-1 | \[&quot;A&quot;, &quot;B&quot;\] | Correct |
| Clef | \[&quot;A&quot;, &quot;B&quot;\] | Correct |
| Luna Decisions | \[&quot;A&quot;, &quot;B&quot;\] | Correct |
| Clef Flash | \[&quot;A&quot;, &quot;B&quot;\] | Correct |
| Strands Decider | \[&quot;A&quot;, &quot;B&quot;\] | Correct |
| GLiNER2.5 Decide | \[&quot;A&quot;, &quot;B&quot;\] | Correct |
| Laya | \[&quot;B&quot;\] | Incorrect |
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
    "record": "7599/7",
    "kind": "source_file_record"
  },
  "source_revision": "9892ed1bff9103f5a9103c68bd271b7630ab661e",
  "input_hash": "421b3c89a067efdbffa39598c4f44223edbac76ea4775490fbb560e5b0c7fe6a"
}
```

</details>
