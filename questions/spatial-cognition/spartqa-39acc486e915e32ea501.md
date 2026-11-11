# Spatial cognition · question 4

[Back to Spatial cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `spartqa/39acc486e915e32ea501`  
**Source:** [SPARTQA](https://github.com/HLR/SpartQA_generation)  
**Input format:** adapted choices

[Explore this question’s altered versions](../../variants/spatial-cognition/spartqa-39acc486e915e32ea501/README.md)

## Context

> We have two blocks, A and B. Two medium blue squares are in block A. One medium black square is also touching the bottom edge of this block. Below medium blue square number one and medium blue square number two there is the medium black square. Below medium blue square number two is medium blue square number one. To the right of block A there is block B which has two medium black squares. Below medium black square number two is medium black square number one.

## Question

> Which blocks have a black shape that is above a black square?

## Answer choices

- **A:** \[&quot;C&quot;\]
- **B:** \[&quot;A&quot;, &quot;B&quot;, &quot;C&quot;\]
- **C:** \[&quot;A&quot;\]
- **D:** \[&quot;B&quot;, &quot;C&quot;\]
- **E:** \[&quot;A&quot;, &quot;C&quot;\]
- **F:** \[\]
- **G:** \[&quot;B&quot;\]
- **H:** \[&quot;A&quot;, &quot;B&quot;\]

**Reference answer:** \[&quot;B&quot;\] (`G`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "We have two blocks, A and B. Two medium blue squares are in block A. One medium black square is also touching the bottom edge of this block. Below medium blue square number one and medium blue square number two there is the medium black square. Below medium blue square number two is medium blue square number one. To the right of block A there is block B which has two medium black squares. Below medium black square number two is medium black square number one.",
  "question": "Which blocks have a black shape that is above a black square?",
  "choices": {
    "A": "[\"C\"]",
    "B": "[\"A\", \"B\", \"C\"]",
    "C": "[\"A\"]",
    "D": "[\"B\", \"C\"]",
    "E": "[\"A\", \"C\"]",
    "F": "[]",
    "G": "[\"B\"]",
    "H": "[\"A\", \"B\"]"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | \[&quot;B&quot;\] | Correct |
| Opus 5.5 | \[&quot;B&quot;\] | Correct |
| GLiDE v1.2 | \[&quot;B&quot;\] | Correct |
| Decider v1.1 | \[&quot;B&quot;\] | Correct |
| Jev | \[&quot;B&quot;\] | Correct |
| Microsoft Decision-1 | \[&quot;B&quot;\] | Correct |
| Clef | \[&quot;B&quot;\] | Correct |
| Luna Decisions | \[\] | Incorrect |
| Clef Flash | \[&quot;A&quot;, &quot;B&quot;\] | Incorrect |
| Strands Decider | \[&quot;A&quot;, &quot;B&quot;\] | Incorrect |
| GLiNER2.5 Decide | \[&quot;A&quot;, &quot;B&quot;\] | Incorrect |
| Laya | \[&quot;A&quot;, &quot;B&quot;, &quot;C&quot;\] | Incorrect |
| CalDec v1 | \[&quot;A&quot;, &quot;B&quot;, &quot;C&quot;\] | Incorrect |

## Source and sharing

Attribution: HLR / Roshanak Mirzaee et al..  
Terms: **[MIT](https://opensource.org/license/mit)**. [Source sharing decision](../../docs/data-sharing.md).  
The capability assignment and choice-format normalization are part of this experiment. Source data retain their own terms.

<details>
<summary>Exact source locator and input fingerprint</summary>

```json
{
  "source_locator": {
    "path": "extracted/SpartQA_Auto.zip/SpartQA_Auto/test.json",
    "record": "258/7",
    "kind": "source_file_record"
  },
  "source_revision": "9892ed1bff9103f5a9103c68bd271b7630ab661e",
  "input_hash": "ca983f0fce6254deb9d0f956e1a709d1634ecda9ef38829cfdbc34aa29cf3747"
}
```

</details>
