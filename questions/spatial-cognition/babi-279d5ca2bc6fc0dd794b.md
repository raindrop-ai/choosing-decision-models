# Spatial cognition · question 31

[Back to Spatial cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `babi/279d5ca2bc6fc0dd794b`  
**Source:** [bAbI](https://dl.fbaipublicfiles.com/babi/tasks_1-20_v1-2.tar.gz)  
**Input format:** adapted choices

[Explore this question’s altered versions](../../variants/spatial-cognition/babi-279d5ca2bc6fc0dd794b/README.md)

## Context

> The office is south of the kitchen.
> The bedroom is south of the bathroom.
> The hallway is west of the office.
> The garden is north of the bathroom.
> The office is west of the bathroom.

## Question

> How do you go from the bedroom to the office?

## Answer choices

- **A:** n,w
- **B:** s,w
- **C:** w,w
- **D:** w,n

**Reference answer:** n,w (`A`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "The office is south of the kitchen.\nThe bedroom is south of the bathroom.\nThe hallway is west of the office.\nThe garden is north of the bathroom.\nThe office is west of the bathroom.",
  "question": "How do you go from the bedroom to the office?",
  "choices": {
    "A": "n,w",
    "B": "s,w",
    "C": "w,w",
    "D": "w,n"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | n,w | Correct |
| Opus 5.5 | n,w | Correct |
| GLiDE v1.2 | n,w | Correct |
| Decider v1.1 | n,w | Correct |
| Jev | w,w | Incorrect |
| Microsoft Decision-1 | n,w | Correct |
| Clef | n,w | Correct |
| Luna Decisions | n,w | Correct |
| Clef Flash | n,w | Correct |
| Strands Decider | n,w | Correct |
| GLiNER2.5 Decide | s,w | Incorrect |
| Laya | s,w | Incorrect |
| CalDec v1 | s,w | Incorrect |

## Source and sharing

Attribution: Facebook, Inc.; bAbI authors.  
Terms: **[CC-BY-3.0](https://creativecommons.org/licenses/by/3.0/)**. [Source sharing decision](../../docs/data-sharing.md).  
The capability assignment and choice-format normalization are part of this experiment. Source data retain their own terms.

<details>
<summary>Exact source locator and input fingerprint</summary>

```json
{
  "source_locator": {
    "path": "extracted/tasks.tar.gz/tasks_1-20_v1-2/en/qa19_path-finding_test.txt",
    "record": "2729",
    "kind": "source_file_record"
  },
  "source_revision": null,
  "input_hash": "de8626047bf59568105d7586ce2af74bd55298e4b8d377d5b510282fdb37ac40"
}
```

</details>
