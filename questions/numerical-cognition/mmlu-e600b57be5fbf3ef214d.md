# Numerical cognition · question 2

[Back to Numerical cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `mmlu/e600b57be5fbf3ef214d`  
**Source:** [MMLU](https://huggingface.co/datasets/cais/mmlu)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/numerical-cognition/mmlu-e600b57be5fbf3ef214d/README.md)

## Question

> A number’s prime factors are 2, 5, 7, 13, and 31. Which of the following must be a factor of the number?

## Answer choices

- **A:** 4
- **B:** 6
- **C:** 10
- **D:** 15

**Reference answer:** 10 (`C`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "",
  "question": "A number’s prime factors are 2, 5, 7, 13, and 31. Which of the following must be a factor of the number?",
  "choices": {
    "A": "4",
    "B": "6",
    "C": "10",
    "D": "15"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | 10 | Correct |
| Opus 5.5 | 10 | Correct |
| GLiDE v1.2 | 10 | Correct |
| Decider v1.1 | 10 | Correct |
| Jev | 10 | Correct |
| Microsoft Decision-1 | 10 | Correct |
| Clef | 10 | Correct |
| Luna Decisions | 10 | Correct |
| Clef Flash | 10 | Correct |
| Strands Decider | 10 | Correct |
| GLiNER2.5 Decide | 4 | Incorrect |
| Laya | 4 | Incorrect |
| CalDec v1 | 4 | Incorrect |

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
    "record": "4269",
    "kind": "source_file_record"
  },
  "source_revision": "c30699e8356da336a370243923dbaf21066bb9fe",
  "input_hash": "ea86df935dd8f9dcb16205631899d35be53d612deeefc082a46737aa64ffd539"
}
```

</details>
