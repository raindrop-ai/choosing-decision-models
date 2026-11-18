# State tracking and updating · question 49

[Back to State tracking and updating](README.md) · [All capabilities](../README.md)

**Question ID:** `babi/b397dea8c16faa8a7376`  
**Source:** [bAbI](https://s3.amazonaws.com/text-datasets/babi_tasks_1-20_v1-2.tar.gz)  
**Input format:** adapted choices

[Explore this question’s altered versions](../../variants/state-tracking-and-updating/babi-b397dea8c16faa8a7376/README.md)

## Context

> Sandra went to the bedroom.
> John travelled to the office.
> John travelled to the bedroom.
> Sandra went back to the kitchen.

## Question

> Where is John? 

## Answer choices

- **A:** hallway
- **B:** bedroom
- **C:** office
- **D:** garden
- **E:** bathroom
- **F:** kitchen

**Reference answer:** bedroom (`B`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Sandra went to the bedroom.\nJohn travelled to the office.\nJohn travelled to the bedroom.\nSandra went back to the kitchen.",
  "question": "Where is John? ",
  "choices": {
    "A": "hallway",
    "B": "bedroom",
    "C": "office",
    "D": "garden",
    "E": "bathroom",
    "F": "kitchen"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | bedroom | Correct |
| Opus 5.5 | bedroom | Correct |
| GLiDE v1.2 | bedroom | Correct |
| Decider v1.1 | bedroom | Correct |
| Jev | bedroom | Correct |
| Microsoft Decision-1 | bedroom | Correct |
| Clef | bedroom | Correct |
| Luna Decisions | bedroom | Correct |
| Clef Flash | bedroom | Correct |
| Strands Decider | bedroom | Correct |
| GLiNER2.5 Decide | kitchen | Incorrect |
| Laya | office | Incorrect |
| CalDec v1 | bedroom | Correct |

## Source and sharing

Attribution: Facebook, Inc.; bAbI authors.  
Terms: **[CC-BY-3.0](https://creativecommons.org/licenses/by/3.0/)**. [Source sharing decision](../../docs/data-sharing.md).  
The capability assignment and choice-format normalization are part of this experiment. Source data retain their own terms.

<details>
<summary>Exact source locator and input fingerprint</summary>

```json
{
  "source_locator": {
    "path": "extracted/tasks.tar.gz/tasks_1-20_v1-2/en/qa1_single-supporting-fact_test.txt",
    "record": "2540",
    "kind": "source_file_record"
  },
  "source_revision": null,
  "input_hash": "19161003e86744e5db4a25121b6a0d015bdf02a37627530d0f31ed7b165293d4"
}
```

</details>
