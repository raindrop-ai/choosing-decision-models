# State tracking and updating · question 2

[Back to State tracking and updating](README.md) · [All capabilities](../README.md)

**Question ID:** `babi/25a8cecfd568bcdf37f2`  
**Source:** [bAbI](https://dl.fbaipublicfiles.com/babi/tasks_1-20_v1-2.tar.gz)  
**Input format:** adapted choices

[Explore this question’s altered versions](../../variants/state-tracking-and-updating/babi-25a8cecfd568bcdf37f2/README.md)

## Context

> Daniel went to the hallway.
> Daniel went to the bedroom.
> John journeyed to the office.
> Mary went back to the bedroom.
> Mary travelled to the office.
> John travelled to the bedroom.
> Mary went to the hallway.
> Mary went back to the kitchen.
> Daniel moved to the hallway.
> Mary moved to the office.

## Question

> Where is Mary? 

## Answer choices

- **A:** office
- **B:** bathroom
- **C:** garden
- **D:** kitchen
- **E:** bedroom
- **F:** hallway

**Reference answer:** office (`A`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Daniel went to the hallway.\nDaniel went to the bedroom.\nJohn journeyed to the office.\nMary went back to the bedroom.\nMary travelled to the office.\nJohn travelled to the bedroom.\nMary went to the hallway.\nMary went back to the kitchen.\nDaniel moved to the hallway.\nMary moved to the office.",
  "question": "Where is Mary? ",
  "choices": {
    "A": "office",
    "B": "bathroom",
    "C": "garden",
    "D": "kitchen",
    "E": "bedroom",
    "F": "hallway"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | office | Correct |
| Opus 5.5 | office | Correct |
| GLiDE v1.2 | office | Correct |
| Decider v1.1 | office | Correct |
| Jev | office | Correct |
| Microsoft Decision-1 | office | Correct |
| Clef | office | Correct |
| Luna Decisions | office | Correct |
| Clef Flash | office | Correct |
| Strands Decider | office | Correct |
| GLiNER2.5 Decide | office | Correct |
| Laya | office | Correct |
| CalDec v1 | office | Correct |

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
    "record": "2579",
    "kind": "source_file_record"
  },
  "source_revision": null,
  "input_hash": "ad37abcb0f1e49117d35c30b1f3c5842d1f5c1ae54bbf78aec182a96d986f137"
}
```

</details>
