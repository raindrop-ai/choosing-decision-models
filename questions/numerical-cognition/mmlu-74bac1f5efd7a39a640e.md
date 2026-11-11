# Numerical cognition · question 19

[Back to Numerical cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `mmlu/74bac1f5efd7a39a640e`  
**Source:** [MMLU](https://huggingface.co/datasets/cais/mmlu)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/numerical-cognition/mmlu-74bac1f5efd7a39a640e/README.md)

## Question

> In a group of 10 scores, the largest score is increased by 40 points. What will happen to the mean?

## Answer choices

- **A:** It will remain the same.
- **B:** It will increase by 4 points.
- **C:** It will increase by 10 points.
- **D:** It will increase by 40 points.

**Reference answer:** It will increase by 4 points. (`B`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "",
  "question": "In a group of 10 scores, the largest score is increased by 40 points. What will happen to the mean?",
  "choices": {
    "A": "It will remain the same.",
    "B": "It will increase by 4 points.",
    "C": "It will increase by 10 points.",
    "D": "It will increase by 40 points."
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | It will increase by 4 points. | Correct |
| Opus 5.5 | It will increase by 4 points. | Correct |
| GLiDE v1.2 | It will increase by 4 points. | Correct |
| Decider v1.1 | It will increase by 4 points. | Correct |
| Jev | It will increase by 4 points. | Correct |
| Microsoft Decision-1 | It will increase by 4 points. | Correct |
| Clef | It will increase by 4 points. | Correct |
| Luna Decisions | It will increase by 4 points. | Correct |
| Clef Flash | It will increase by 4 points. | Correct |
| Strands Decider | It will increase by 4 points. | Correct |
| GLiNER2.5 Decide | It will increase by 40 points. | Incorrect |
| Laya | It will increase by 10 points. | Incorrect |
| CalDec v1 | It will increase by 10 points. | Incorrect |

## Source and sharing

Attribution: Dan Hendrycks et al.; MMLU authors.  
Terms: **[MIT](https://opensource.org/license/mit)**. [Source sharing decision](../../docs/data-sharing.md).  
The capability assignment and choice-format normalization are part of this experiment. Source data retain their own terms.

<details>
<summary>Exact source locator and input fingerprint</summary>

```json
{
  "source_locator": {
    "path": "all/test-00000-of-00001.parquet",
    "record": "5612",
    "kind": "source_file_record"
  },
  "source_revision": "c30699e8356da336a370243923dbaf21066bb9fe",
  "input_hash": "fad0f20e9c3b9697430629554e4685e475f5c16762447ca9e65b05a1d8912d82"
}
```

</details>
