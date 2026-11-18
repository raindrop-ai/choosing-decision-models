# Spatial cognition · question 43

[Back to Spatial cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `babi/56cc78bd32b8ba76af0d`  
**Source:** [bAbI](https://s3.amazonaws.com/text-datasets/babi_tasks_1-20_v1-2.tar.gz)  
**Input format:** adapted choices

[Explore this question’s altered versions](../../variants/spatial-cognition/babi-56cc78bd32b8ba76af0d/README.md)

## Context

> The garden is north of the kitchen.
> The bathroom is north of the hallway.
> The garden is east of the bedroom.
> The kitchen is west of the office.
> The kitchen is east of the hallway.

## Question

> How do you go from the hallway to the garden?

## Answer choices

- **A:** n,s
- **B:** w,s
- **C:** e,s
- **D:** e,n

**Reference answer:** e,n (`D`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "The garden is north of the kitchen.\nThe bathroom is north of the hallway.\nThe garden is east of the bedroom.\nThe kitchen is west of the office.\nThe kitchen is east of the hallway.",
  "question": "How do you go from the hallway to the garden?",
  "choices": {
    "A": "n,s",
    "B": "w,s",
    "C": "e,s",
    "D": "e,n"
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
| Clef | e,n | Correct |
| Luna Decisions | e,n | Correct |
| Clef Flash | e,n | Correct |
| Strands Decider | e,n | Correct |
| GLiNER2.5 Decide | n,s | Incorrect |
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
    "record": "5237",
    "kind": "source_file_record"
  },
  "source_revision": null,
  "input_hash": "425d45b1e2db7770bb0eccaef59a9bccba1607a5058a3e3693d7a460990e00b1"
}
```

</details>
