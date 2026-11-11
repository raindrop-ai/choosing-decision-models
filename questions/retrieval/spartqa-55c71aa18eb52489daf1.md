# Retrieval · question 3

[Back to Retrieval](README.md) · [All capabilities](../README.md)

**Question ID:** `spartqa/55c71aa18eb52489daf1`  
**Source:** [SPARTQA](https://github.com/HLR/SpartQA_generation)  
**Input format:** adapted choices

[Explore this question’s altered versions](../../variants/retrieval/spartqa-55c71aa18eb52489daf1/README.md)

## Context

> We have three blocks. Lets call them A, B and C. Block A is below B. Block C is above A. Block A contains one medium blue square. Block B has one medium black square. And block C has two medium blue squares. Medium blue square number one is touching the bottom edge of this block. There is also a medium black square in this block. It is below medium blue square number two. Below the medium black square and medium blue square number two is medium blue square number one.

## Question

> Which blocks have a medium blue square?

## Answer choices

- **A:** \[&quot;A&quot;, &quot;C&quot;\]
- **B:** \[&quot;A&quot;\]
- **C:** \[&quot;C&quot;\]
- **D:** \[\]
- **E:** \[&quot;B&quot;, &quot;C&quot;\]
- **F:** \[&quot;A&quot;, &quot;B&quot;\]
- **G:** \[&quot;B&quot;\]
- **H:** \[&quot;A&quot;, &quot;B&quot;, &quot;C&quot;\]

**Reference answer:** \[&quot;A&quot;, &quot;C&quot;\] (`A`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "We have three blocks. Lets call them A, B and C. Block A is below B. Block C is above A. Block A contains one medium blue square. Block B has one medium black square. And block C has two medium blue squares. Medium blue square number one is touching the bottom edge of this block. There is also a medium black square in this block. It is below medium blue square number two. Below the medium black square and medium blue square number two is medium blue square number one.",
  "question": "Which blocks have a medium blue square?",
  "choices": {
    "A": "[\"A\", \"C\"]",
    "B": "[\"A\"]",
    "C": "[\"C\"]",
    "D": "[]",
    "E": "[\"B\", \"C\"]",
    "F": "[\"A\", \"B\"]",
    "G": "[\"B\"]",
    "H": "[\"A\", \"B\", \"C\"]"
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
| Luna Decisions | \[&quot;A&quot;, &quot;B&quot;, &quot;C&quot;\] | Incorrect |
| Clef Flash | \[&quot;A&quot;, &quot;C&quot;\] | Correct |
| Strands Decider | \[&quot;A&quot;, &quot;C&quot;\] | Correct |
| GLiNER2.5 Decide | \[&quot;A&quot;, &quot;B&quot;, &quot;C&quot;\] | Incorrect |
| Laya | \[&quot;C&quot;\] | Incorrect |
| CalDec v1 | \[&quot;C&quot;\] | Incorrect |

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
    "record": "6711/7",
    "kind": "source_file_record"
  },
  "source_revision": "9892ed1bff9103f5a9103c68bd271b7630ab661e",
  "input_hash": "2cf1e110a706a737afcb301750605c282f9c995e63be1917d9ac7ff22f02343a"
}
```

</details>
