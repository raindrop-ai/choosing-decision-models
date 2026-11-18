# Spatial cognition · question 15

[Back to Spatial cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `babi/532c5a16cdb5603bf1ed`  
**Source:** [bAbI](https://s3.amazonaws.com/text-datasets/babi_tasks_1-20_v1-2.tar.gz)  
**Input format:** adapted choices

[Explore this question’s altered versions](../../variants/spatial-cognition/babi-532c5a16cdb5603bf1ed/README.md)

## Context

> The office is west of the bedroom.
> The bathroom is south of the bedroom.
> The hallway is south of the garden.
> The kitchen is south of the office.
> The bedroom is south of the hallway.

## Question

> How do you go from the hallway to the office?

## Answer choices

- **A:** w,n
- **B:** n,w
- **C:** e,w
- **D:** s,w

**Reference answer:** s,w (`D`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "The office is west of the bedroom.\nThe bathroom is south of the bedroom.\nThe hallway is south of the garden.\nThe kitchen is south of the office.\nThe bedroom is south of the hallway.",
  "question": "How do you go from the hallway to the office?",
  "choices": {
    "A": "w,n",
    "B": "n,w",
    "C": "e,w",
    "D": "s,w"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | s,w | Correct |
| Opus 5.5 | s,w | Correct |
| GLiDE v1.2 | s,w | Correct |
| Decider v1.1 | n,w | Incorrect |
| Jev | s,w | Correct |
| Microsoft Decision-1 | s,w | Correct |
| Clef | s,w | Correct |
| Luna Decisions | w,n | Incorrect |
| Clef Flash | n,w | Incorrect |
| Strands Decider | w,n | Incorrect |
| GLiNER2.5 Decide | w,n | Incorrect |
| Laya | w,n | Incorrect |
| CalDec v1 | w,n | Incorrect |

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
    "record": "1997",
    "kind": "source_file_record"
  },
  "source_revision": null,
  "input_hash": "749a6ca59fd0d2c1be96e814e84e7180829957154537716d9781257e8410984a"
}
```

</details>
