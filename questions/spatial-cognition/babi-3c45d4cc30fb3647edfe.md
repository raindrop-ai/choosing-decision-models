# Spatial cognition · question 19

[Back to Spatial cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `babi/3c45d4cc30fb3647edfe`  
**Source:** [bAbI](https://s3.amazonaws.com/text-datasets/babi_tasks_1-20_v1-2.tar.gz)  
**Input format:** adapted choices

[Explore this question’s altered versions](../../variants/spatial-cognition/babi-3c45d4cc30fb3647edfe/README.md)

## Context

> The bathroom is north of the kitchen.
> The kitchen is west of the garden.
> The hallway is north of the office.
> The office is north of the bathroom.
> The bedroom is west of the kitchen.

## Question

> How do you go from the office to the kitchen?

## Answer choices

- **A:** n,w
- **B:** s,s
- **C:** s,n
- **D:** s,w

**Reference answer:** s,s (`B`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "The bathroom is north of the kitchen.\nThe kitchen is west of the garden.\nThe hallway is north of the office.\nThe office is north of the bathroom.\nThe bedroom is west of the kitchen.",
  "question": "How do you go from the office to the kitchen?",
  "choices": {
    "A": "n,w",
    "B": "s,s",
    "C": "s,n",
    "D": "s,w"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | s,s | Correct |
| Opus 5.5 | s,s | Correct |
| GLiDE v1.2 | s,s | Correct |
| Decider v1.1 | s,s | Correct |
| Jev | s,w | Incorrect |
| Microsoft Decision-1 | s,s | Correct |
| Clef | s,s | Correct |
| Luna Decisions | s,w | Incorrect |
| Clef Flash | s,s | Correct |
| Strands Decider | s,w | Incorrect |
| GLiNER2.5 Decide | n,w | Incorrect |
| Laya | n,w | Incorrect |
| CalDec v1 | n,w | Incorrect |

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
    "record": "179",
    "kind": "source_file_record"
  },
  "source_revision": null,
  "input_hash": "5e9f150fc163ebf630cf644a5c13b3cccf49c316be66722cd1f058a0ba7dbd61"
}
```

</details>
