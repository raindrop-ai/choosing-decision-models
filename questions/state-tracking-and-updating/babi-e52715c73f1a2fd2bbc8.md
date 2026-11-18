# State tracking and updating · question 15

[Back to State tracking and updating](README.md) · [All capabilities](../README.md)

**Question ID:** `babi/e52715c73f1a2fd2bbc8`  
**Source:** [bAbI](https://s3.amazonaws.com/text-datasets/babi_tasks_1-20_v1-2.tar.gz)  
**Input format:** adapted choices

[Explore this question’s altered versions](../../variants/state-tracking-and-updating/babi-e52715c73f1a2fd2bbc8/README.md)

## Context

> John travelled to the garden.
> Mary journeyed to the office.
> Sandra went to the garden.
> John went back to the office.
> John moved to the bedroom.
> John moved to the garden.

## Question

> Where is John? 

## Answer choices

- **A:** bedroom
- **B:** hallway
- **C:** bathroom
- **D:** office
- **E:** garden
- **F:** kitchen

**Reference answer:** garden (`E`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "John travelled to the garden.\nMary journeyed to the office.\nSandra went to the garden.\nJohn went back to the office.\nJohn moved to the bedroom.\nJohn moved to the garden.",
  "question": "Where is John? ",
  "choices": {
    "A": "bedroom",
    "B": "hallway",
    "C": "bathroom",
    "D": "office",
    "E": "garden",
    "F": "kitchen"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | garden | Correct |
| Opus 5.5 | garden | Correct |
| GLiDE v1.2 | garden | Correct |
| Decider v1.1 | garden | Correct |
| Jev | garden | Correct |
| Microsoft Decision-1 | garden | Correct |
| Clef | garden | Correct |
| Luna Decisions | garden | Correct |
| Clef Flash | garden | Correct |
| Strands Decider | garden | Correct |
| GLiNER2.5 Decide | garden | Correct |
| Laya | bedroom | Incorrect |
| CalDec v1 | garden | Correct |

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
    "record": "2678",
    "kind": "source_file_record"
  },
  "source_revision": null,
  "input_hash": "4132cee0f5ea063bcb248432a0b36e9ddb144cf1156ead400fcf7540a354ad8b"
}
```

</details>
