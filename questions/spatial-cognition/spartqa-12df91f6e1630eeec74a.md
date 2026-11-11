# Spatial cognition · question 54

[Back to Spatial cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `spartqa/12df91f6e1630eeec74a`  
**Source:** [SPARTQA](https://github.com/HLR/SpartQA_generation)  
**Input format:** adapted choices

[Explore this question’s altered versions](../../variants/spatial-cognition/spartqa-12df91f6e1630eeec74a/README.md)

## Context

> We have three blocks, A, B and C. Block A is below block C and above block B. Block A has two medium yellow squares. Medium yellow square number one is touching the bottom edge of this block. This shape is below medium yellow square number two. Block B contains one medium blue square. One medium yellow square is also in this block. The medium blue square is below the medium yellow square. And block C contains one medium blue square.

## Question

> Which blocks don't have any medium square that is below a medium square?

## Answer choices

- **A:** \[&quot;A&quot;, &quot;C&quot;\]
- **B:** \[&quot;A&quot;, &quot;B&quot;, &quot;C&quot;\]
- **C:** \[&quot;B&quot;, &quot;C&quot;\]
- **D:** \[&quot;A&quot;\]
- **E:** \[&quot;C&quot;\]
- **F:** \[&quot;B&quot;\]
- **G:** \[&quot;A&quot;, &quot;B&quot;\]
- **H:** \[\]

**Reference answer:** \[&quot;C&quot;\] (`E`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "We have three blocks, A, B and C. Block A is below block C and above block B. Block A has two medium yellow squares. Medium yellow square number one is touching the bottom edge of this block. This shape is below medium yellow square number two. Block B contains one medium blue square. One medium yellow square is also in this block. The medium blue square is below the medium yellow square. And block C contains one medium blue square.",
  "question": "Which blocks don't have any medium square that is below a medium square?",
  "choices": {
    "A": "[\"A\", \"C\"]",
    "B": "[\"A\", \"B\", \"C\"]",
    "C": "[\"B\", \"C\"]",
    "D": "[\"A\"]",
    "E": "[\"C\"]",
    "F": "[\"B\"]",
    "G": "[\"A\", \"B\"]",
    "H": "[]"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | \[&quot;C&quot;\] | Correct |
| Opus 5.5 | \[&quot;C&quot;\] | Correct |
| GLiDE v1.2 | \[&quot;C&quot;\] | Correct |
| Decider v1.1 | \[&quot;C&quot;\] | Correct |
| Jev | \[&quot;C&quot;\] | Correct |
| Microsoft Decision-1 | \[&quot;C&quot;\] | Correct |
| Clef | \[&quot;C&quot;\] | Correct |
| Luna Decisions | \[&quot;A&quot;, &quot;C&quot;\] | Incorrect |
| Clef Flash | \[&quot;C&quot;\] | Correct |
| Strands Decider | \[&quot;A&quot;, &quot;C&quot;\] | Incorrect |
| GLiNER2.5 Decide | \[&quot;A&quot;, &quot;C&quot;\] | Incorrect |
| Laya | \[&quot;A&quot;, &quot;B&quot;, &quot;C&quot;\] | Incorrect |
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
    "path": "extracted/SpartQA_Auto.zip/SpartQA_Auto/dev.json",
    "record": "29/6",
    "kind": "source_file_record"
  },
  "source_revision": "9892ed1bff9103f5a9103c68bd271b7630ab661e",
  "input_hash": "f95adad07f626deff421237e34a1bcaa330d12d84f9eef517aff1da3e8ccdca3"
}
```

</details>
