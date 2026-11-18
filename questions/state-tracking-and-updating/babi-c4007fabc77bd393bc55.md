# State tracking and updating · question 32

[Back to State tracking and updating](README.md) · [All capabilities](../README.md)

**Question ID:** `babi/c4007fabc77bd393bc55`  
**Source:** [bAbI](https://s3.amazonaws.com/text-datasets/babi_tasks_1-20_v1-2.tar.gz)  
**Input format:** adapted choices

[Explore this question’s altered versions](../../variants/state-tracking-and-updating/babi-c4007fabc77bd393bc55/README.md)

## Context

> John got the football there.
> John left the football.
> Daniel went back to the bathroom.
> Mary went back to the bathroom.
> Sandra travelled to the office.
> Daniel got the apple there.
> John got the football there.
> John left the football.
> Daniel journeyed to the kitchen.
> John moved to the bathroom.
> John went to the office.
> Mary took the milk there.
> John journeyed to the garden.
> Sandra went to the garden.
> Daniel grabbed the football there.
> Mary discarded the milk.
> Sandra moved to the office.
> Mary got the milk there.
> Mary moved to the garden.
> Mary left the milk.
> Daniel dropped the apple.
> Sandra went back to the bathroom.

## Question

> Where is the apple? 

## Answer choices

- **A:** garden
- **B:** kitchen
- **C:** bedroom
- **D:** hallway
- **E:** bathroom
- **F:** office

**Reference answer:** kitchen (`B`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "John got the football there.\nJohn left the football.\nDaniel went back to the bathroom.\nMary went back to the bathroom.\nSandra travelled to the office.\nDaniel got the apple there.\nJohn got the football there.\nJohn left the football.\nDaniel journeyed to the kitchen.\nJohn moved to the bathroom.\nJohn went to the office.\nMary took the milk there.\nJohn journeyed to the garden.\nSandra went to the garden.\nDaniel grabbed the football there.\nMary discarded the milk.\nSandra moved to the office.\nMary got the milk there.\nMary moved to the garden.\nMary left the milk.\nDaniel dropped the apple.\nSandra went back to the bathroom.",
  "question": "Where is the apple? ",
  "choices": {
    "A": "garden",
    "B": "kitchen",
    "C": "bedroom",
    "D": "hallway",
    "E": "bathroom",
    "F": "office"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | kitchen | Correct |
| Opus 5.5 | kitchen | Correct |
| GLiDE v1.2 | kitchen | Correct |
| Decider v1.1 | kitchen | Correct |
| Jev | kitchen | Correct |
| Microsoft Decision-1 | kitchen | Correct |
| Clef | kitchen | Correct |
| Luna Decisions | kitchen | Correct |
| Clef Flash | kitchen | Correct |
| Strands Decider | kitchen | Correct |
| GLiNER2.5 Decide | bathroom | Incorrect |
| Laya | office | Incorrect |
| CalDec v1 | garden | Incorrect |

## Source and sharing

Attribution: Facebook, Inc.; bAbI authors.  
Terms: **[CC-BY-3.0](https://creativecommons.org/licenses/by/3.0/)**. [Source sharing decision](../../docs/data-sharing.md).  
The capability assignment and choice-format normalization are part of this experiment. Source data retain their own terms.

<details>
<summary>Exact source locator and input fingerprint</summary>

```json
{
  "source_locator": {
    "path": "extracted/tasks.tar.gz/tasks_1-20_v1-2/en/qa2_two-supporting-facts_test.txt",
    "record": "806",
    "kind": "source_file_record"
  },
  "source_revision": null,
  "input_hash": "8b7c70d529f240622775cbc58a529d145da5b3fcc9cedc42481ca609e9323d13"
}
```

</details>
