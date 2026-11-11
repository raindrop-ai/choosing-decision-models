# State tracking and updating · question 38

[Back to State tracking and updating](README.md) · [All capabilities](../README.md)

**Question ID:** `babi/d8b4cc8682faee0edd89`  
**Source:** [bAbI](https://dl.fbaipublicfiles.com/babi/tasks_1-20_v1-2.tar.gz)  
**Input format:** adapted choices

[Explore this question’s altered versions](../../variants/state-tracking-and-updating/babi-d8b4cc8682faee0edd89/README.md)

## Context

> Sandra went to the garden.
> Sandra picked up the apple there.
> Daniel went back to the office.
> Sandra put down the apple.
> Mary travelled to the hallway.
> Sandra travelled to the kitchen.
> Mary went back to the bedroom.
> John moved to the hallway.
> Mary went to the office.
> Daniel went to the bedroom.
> Sandra journeyed to the bedroom.
> Mary journeyed to the hallway.
> Mary journeyed to the bedroom.
> John went to the bathroom.
> Sandra grabbed the football there.
> John took the milk there.
> Daniel travelled to the kitchen.
> Mary went to the garden.
> John discarded the milk.
> Daniel journeyed to the bathroom.
> Daniel went back to the office.
> Mary grabbed the apple there.

## Question

> Where is the milk? 

## Answer choices

- **A:** bathroom
- **B:** hallway
- **C:** office
- **D:** bedroom
- **E:** kitchen
- **F:** garden

**Reference answer:** bathroom (`A`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Sandra went to the garden.\nSandra picked up the apple there.\nDaniel went back to the office.\nSandra put down the apple.\nMary travelled to the hallway.\nSandra travelled to the kitchen.\nMary went back to the bedroom.\nJohn moved to the hallway.\nMary went to the office.\nDaniel went to the bedroom.\nSandra journeyed to the bedroom.\nMary journeyed to the hallway.\nMary journeyed to the bedroom.\nJohn went to the bathroom.\nSandra grabbed the football there.\nJohn took the milk there.\nDaniel travelled to the kitchen.\nMary went to the garden.\nJohn discarded the milk.\nDaniel journeyed to the bathroom.\nDaniel went back to the office.\nMary grabbed the apple there.",
  "question": "Where is the milk? ",
  "choices": {
    "A": "bathroom",
    "B": "hallway",
    "C": "office",
    "D": "bedroom",
    "E": "kitchen",
    "F": "garden"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | bathroom | Correct |
| Opus 5.5 | bathroom | Correct |
| GLiDE v1.2 | bathroom | Correct |
| Decider v1.1 | bathroom | Correct |
| Jev | bathroom | Correct |
| Microsoft Decision-1 | bathroom | Correct |
| Clef | bathroom | Correct |
| Luna Decisions | bathroom | Correct |
| Clef Flash | bathroom | Correct |
| Strands Decider | hallway | Incorrect |
| GLiNER2.5 Decide | office | Incorrect |
| Laya | bathroom | Correct |
| CalDec v1 | bathroom | Correct |

## Source and sharing

Attribution: Facebook, Inc.; bAbI authors.  
Terms: **[CC-BY-3.0](https://creativecommons.org/licenses/by/3.0/)**. [Source sharing decision](../../docs/data-sharing.md).  
The capability assignment and choice-format normalization are part of this experiment. Source data retain their own terms.

<details>
<summary>Exact source locator and input fingerprint</summary>

```json
{
  "source_locator": {
    "path": "extracted/tasks.tar.gz/tasks_1-20_v1-2/en/qa2_two-supporting-facts_train.txt",
    "record": "2665",
    "kind": "source_file_record"
  },
  "source_revision": null,
  "input_hash": "43a9376506c4c90160eef822de752cb0fccf42fba3e1e664dd888d372303cb81"
}
```

</details>
