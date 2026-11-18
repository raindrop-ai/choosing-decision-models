# Spatial cognition · question 11

[Back to Spatial cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `babi/80d2a9dfbea2ad192d5e`  
**Source:** [bAbI](https://s3.amazonaws.com/text-datasets/babi_tasks_1-20_v1-2.tar.gz)  
**Input format:** adapted choices

[Explore this question’s altered versions](../../variants/spatial-cognition/babi-80d2a9dfbea2ad192d5e/README.md)

## Context

> The hallway is east of the office.
> The garden is north of the hallway.
> The kitchen is east of the garden.
> The bedroom is east of the bathroom.
> The bathroom is east of the hallway.

## Question

> How do you go from the garden to the bathroom?

## Answer choices

- **A:** s,s
- **B:** w,n
- **C:** s,e
- **D:** e,w

**Reference answer:** s,e (`C`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "The hallway is east of the office.\nThe garden is north of the hallway.\nThe kitchen is east of the garden.\nThe bedroom is east of the bathroom.\nThe bathroom is east of the hallway.",
  "question": "How do you go from the garden to the bathroom?",
  "choices": {
    "A": "s,s",
    "B": "w,n",
    "C": "s,e",
    "D": "e,w"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | s,e | Correct |
| Opus 5.5 | s,e | Correct |
| GLiDE v1.2 | s,e | Correct |
| Decider v1.1 | s,e | Correct |
| Jev | s,e | Correct |
| Microsoft Decision-1 | s,e | Correct |
| Clef | s,e | Correct |
| Luna Decisions | s,s | Incorrect |
| Clef Flash | s,s | Incorrect |
| Strands Decider | s,e | Correct |
| GLiNER2.5 Decide | s,s | Incorrect |
| Laya | s,e | Correct |
| CalDec v1 | s,s | Incorrect |

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
    "record": "5801",
    "kind": "source_file_record"
  },
  "source_revision": null,
  "input_hash": "ca8e30d9e57b13b30aa83a9e19ad42c350aae232b2cc135b4f69dc526e47f209"
}
```

</details>
