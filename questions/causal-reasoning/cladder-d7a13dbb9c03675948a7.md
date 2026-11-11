# Causal reasoning · question 35

[Back to Causal reasoning](README.md) · [All capabilities](../README.md)

**Question ID:** `cladder/d7a13dbb9c03675948a7`  
**Source:** [CLadder](https://github.com/causalNLP/cladder)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/causal-reasoning/cladder-d7a13dbb9c03675948a7/README.md)

## Context

> Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Education level has a direct effect on skill. Skill has a direct effect on salary.
> For people without a college degree, the probability of high salary is 19%. For people with a college degree or higher, the probability of high salary is 69%.

## Question

> Does education level positively affect salary through skill?

## Answer choices

- **yes:** Yes
- **no:** No

**Reference answer:** Yes (`yes`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Education level has a direct effect on skill. Skill has a direct effect on salary.\nFor people without a college degree, the probability of high salary is 19%. For people with a college degree or higher, the probability of high salary is 69%.",
  "question": "Does education level positively affect salary through skill?",
  "choices": {
    "yes": "Yes",
    "no": "No"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | Yes | Correct |
| Opus 5.5 | Yes | Correct |
| GLiDE v1.2 | Yes | Correct |
| Decider v1.1 | Yes | Correct |
| Jev | Yes | Correct |
| Microsoft Decision-1 | Yes | Correct |
| Clef | Yes | Correct |
| Luna Decisions | Yes | Correct |
| Clef Flash | Yes | Correct |
| Strands Decider | Yes | Correct |
| GLiNER2.5 Decide | Yes | Correct |
| Laya | Yes | Correct |
| CalDec v1 | Yes | Correct |

## Source and sharing

Attribution: CLadder original creators; see source.  
Terms: **[MIT](https://opensource.org/license/mit)**. [Source sharing decision](../../docs/data-sharing.md).  
The capability assignment and choice-format normalization are part of this experiment. Source data retain their own terms.

<details>
<summary>Exact source locator and input fingerprint</summary>

```json
{
  "source_locator": {
    "path": "data/cladder-v1-questions.json",
    "record": "836",
    "kind": "source_file_record"
  },
  "source_revision": "3d2d1169b4b939a09048a6a75956c8972a93cc38",
  "input_hash": "93c508b85ddc282dfa2f73e05ee3c459b3a828814741b40cc67f7a0a35d822ab"
}
```

</details>
