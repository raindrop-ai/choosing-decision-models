# Concepts and categorization · question 67

[Back to Concepts and categorization](README.md) · [All capabilities](../README.md)

**Question ID:** `mmlu/8e4e6d77d09ffe6a2d1f`  
**Source:** [MMLU](https://huggingface.co/datasets/cais/mmlu)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/concepts-and-categorization/mmlu-8e4e6d77d09ffe6a2d1f/README.md)

## Question

> All of the following are modes of asexual reproduction EXCEPT

## Answer choices

- **A:** sporulation
- **B:** fission
- **C:** budding
- **D:** meiosis

**Reference answer:** meiosis (`D`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "",
  "question": "All of the following are modes of asexual reproduction EXCEPT",
  "choices": {
    "A": "sporulation",
    "B": "fission",
    "C": "budding",
    "D": "meiosis"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | meiosis | Correct |
| Opus 5.5 | meiosis | Correct |
| GLiDE v1.2 | meiosis | Correct |
| Decider v1.1 | meiosis | Correct |
| Jev | meiosis | Correct |
| Microsoft Decision-1 | meiosis | Correct |
| Clef | meiosis | Correct |
| Luna Decisions | meiosis | Correct |
| Clef Flash | meiosis | Correct |
| Strands Decider | meiosis | Correct |
| GLiNER2.5 Decide | sporulation | Incorrect |
| Laya | fission | Incorrect |
| CalDec v1 | meiosis | Correct |

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
    "record": "2753",
    "kind": "source_file_record"
  },
  "source_revision": "c30699e8356da336a370243923dbaf21066bb9fe",
  "input_hash": "522af6ea9cf52253f915c5b8e43f703c65ad5a78837844f831c71df430ea612d"
}
```

</details>
