# Rule application · question 50

[Back to Rule application](README.md) · [All capabilities](../README.md)

**Question ID:** `cruxeval/0ac3f5256ca2c072c21c`  
**Source:** [CRUXEval](https://github.com/facebookresearch/cruxeval)  
**Input format:** adapted choices

[Explore this question’s altered versions](../../variants/rule-application/cruxeval-0ac3f5256ca2c072c21c/README.md)

## Context

```text
def f(numbers):
    floats = [n % 1 for n in numbers]
    return floats if 1 in floats else []
```

## Question

> What does f(range(100, 120)) return?

## Answer choices

- **A:** \[\]
- **B:** \[2\]
- **C:** \[0\]
- **D:** \[1\]

**Reference answer:** \[\] (`A`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "def f(numbers):\n    floats = [n % 1 for n in numbers]\n    return floats if 1 in floats else []",
  "question": "What does f(range(100, 120)) return?",
  "choices": {
    "A": "[]",
    "B": "[2]",
    "C": "[0]",
    "D": "[1]"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | \[\] | Correct |
| Opus 5.5 | \[\] | Correct |
| GLiDE v1.2 | \[\] | Correct |
| Decider v1.1 | \[\] | Correct |
| Jev | \[\] | Correct |
| Microsoft Decision-1 | \[\] | Correct |
| Clef | \[\] | Correct |
| Luna Decisions | \[0\] | Incorrect |
| Clef Flash | \[\] | Correct |
| Strands Decider | \[1\] | Incorrect |
| GLiNER2.5 Decide | \[\] | Correct |
| Laya | \[\] | Correct |
| CalDec v1 | \[\] | Correct |

## Source and sharing

Attribution: Meta; CRUXEval authors.  
Terms: **[MIT](https://opensource.org/license/mit)**. [Source sharing decision](../../docs/data-sharing.md).  
The capability assignment and choice-format normalization are part of this experiment. Source data retain their own terms.

<details>
<summary>Exact source locator and input fingerprint</summary>

```json
{
  "source_locator": {
    "path": "data/cruxeval.jsonl",
    "record": "522",
    "kind": "source_file_record"
  },
  "source_revision": "190faf16d175b5847b0af05d937872b1fb395942",
  "input_hash": "8550656a11e27734f675246b7266e55ad21ab4a7e85c4cdd5f50f2961692dee5"
}
```

</details>
