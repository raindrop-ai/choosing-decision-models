# Spatial cognition · question 35

[Back to Spatial cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `babi/ce484dba76a710dca15b`  
**Source:** [bAbI](https://s3.amazonaws.com/text-datasets/babi_tasks_1-20_v1-2.tar.gz)  
**Input format:** adapted choices

[Explore this question’s altered versions](../../variants/spatial-cognition/babi-ce484dba76a710dca15b/README.md)

## Context

> The garden is south of the kitchen.
> The bathroom is west of the office.
> The bathroom is east of the bedroom.
> The hallway is south of the bathroom.
> The garden is north of the office.

## Question

> How do you go from the bathroom to the garden?

## Answer choices

- **A:** e,n
- **B:** s,s
- **C:** e,e
- **D:** w,s

**Reference answer:** e,n (`A`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "The garden is south of the kitchen.\nThe bathroom is west of the office.\nThe bathroom is east of the bedroom.\nThe hallway is south of the bathroom.\nThe garden is north of the office.",
  "question": "How do you go from the bathroom to the garden?",
  "choices": {
    "A": "e,n",
    "B": "s,s",
    "C": "e,e",
    "D": "w,s"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | e,n | Correct |
| Opus 5.5 | e,n | Correct |
| GLiDE v1.2 | e,n | Correct |
| Decider v1.1 | e,n | Correct |
| Jev | e,e | Incorrect |
| Microsoft Decision-1 | e,n | Correct |
| Clef | s,s | Incorrect |
| Luna Decisions | e,n | Correct |
| Clef Flash | s,s | Incorrect |
| Strands Decider | e,n | Correct |
| GLiNER2.5 Decide | e,n | Correct |
| Laya | e,e | Incorrect |
| CalDec v1 | e,n | Correct |

## Source and sharing

Attribution: Facebook, Inc.; bAbI authors.  
Terms: **[CC-BY-3.0](https://creativecommons.org/licenses/by/3.0/)**. [Source sharing decision](../../docs/data-sharing.md).  
The capability assignment and choice-format normalization are part of this experiment. Source data retain their own terms.

<details>
<summary>Exact source locator and input fingerprint</summary>

```json
{
  "source_locator": {
    "path": "extracted/tasks.tar.gz/tasks_1-20_v1-2/en/qa19_path-finding_train.txt",
    "record": "4763",
    "kind": "source_file_record"
  },
  "source_revision": null,
  "input_hash": "24fabcba7b1af7ea41f2ce5efb35bc4aac601d3086bc8120f1b6bd7e3a419ade"
}
```

</details>
