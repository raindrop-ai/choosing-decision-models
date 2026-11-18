# Spatial cognition · question 27

[Back to Spatial cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `babi/aaf87651bddcd409df1e`  
**Source:** [bAbI](https://s3.amazonaws.com/text-datasets/babi_tasks_1-20_v1-2.tar.gz)  
**Input format:** adapted choices

[Explore this question’s altered versions](../../variants/spatial-cognition/babi-aaf87651bddcd409df1e/README.md)

## Context

> The kitchen is west of the bathroom.
> The office is east of the bathroom.
> The hallway is north of the garden.
> The bedroom is south of the bathroom.
> The garden is west of the bedroom.

## Question

> How do you go from the garden to the bathroom?

## Answer choices

- **A:** n,s
- **B:** e,n
- **C:** w,s
- **D:** s,e

**Reference answer:** e,n (`B`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "The kitchen is west of the bathroom.\nThe office is east of the bathroom.\nThe hallway is north of the garden.\nThe bedroom is south of the bathroom.\nThe garden is west of the bedroom.",
  "question": "How do you go from the garden to the bathroom?",
  "choices": {
    "A": "n,s",
    "B": "e,n",
    "C": "w,s",
    "D": "s,e"
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
| Jev | e,n | Correct |
| Microsoft Decision-1 | e,n | Correct |
| Clef | s,e | Incorrect |
| Luna Decisions | e,n | Correct |
| Clef Flash | n,s | Incorrect |
| Strands Decider | s,e | Incorrect |
| GLiNER2.5 Decide | w,s | Incorrect |
| Laya | w,s | Incorrect |
| CalDec v1 | n,s | Incorrect |

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
    "record": "3443",
    "kind": "source_file_record"
  },
  "source_revision": null,
  "input_hash": "5f34983461f373fec1625ac2cafba3d1eae3ba3ca940e673ab87cc5fbb68b736"
}
```

</details>
