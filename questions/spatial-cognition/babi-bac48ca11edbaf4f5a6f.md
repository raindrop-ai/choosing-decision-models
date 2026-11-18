# Spatial cognition · question 23

[Back to Spatial cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `babi/bac48ca11edbaf4f5a6f`  
**Source:** [bAbI](https://s3.amazonaws.com/text-datasets/babi_tasks_1-20_v1-2.tar.gz)  
**Input format:** adapted choices

[Explore this question’s altered versions](../../variants/spatial-cognition/babi-bac48ca11edbaf4f5a6f/README.md)

## Context

> The hallway is west of the office.
> The bathroom is east of the kitchen.
> The office is north of the garden.
> The kitchen is south of the bedroom.
> The bedroom is east of the office.

## Question

> How do you go from the kitchen to the office?

## Answer choices

- **A:** w,n
- **B:** w,s
- **C:** n,w
- **D:** e,w

**Reference answer:** n,w (`C`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "The hallway is west of the office.\nThe bathroom is east of the kitchen.\nThe office is north of the garden.\nThe kitchen is south of the bedroom.\nThe bedroom is east of the office.",
  "question": "How do you go from the kitchen to the office?",
  "choices": {
    "A": "w,n",
    "B": "w,s",
    "C": "n,w",
    "D": "e,w"
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
| Jev | w,n | Incorrect |
| Microsoft Decision-1 | n,w | Correct |
| Clef | n,w | Correct |
| Luna Decisions | n,w | Correct |
| Clef Flash | w,n | Incorrect |
| Strands Decider | n,w | Correct |
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
    "path": "extracted/tasks.tar.gz/tasks_1-20_v1-2/en/qa19_path-finding_test.txt",
    "record": "4895",
    "kind": "source_file_record"
  },
  "source_revision": null,
  "input_hash": "40dec68e116120213a6a8fe0f9781deece44b3f9dfdf64c8010bbfed11555e51"
}
```

</details>
