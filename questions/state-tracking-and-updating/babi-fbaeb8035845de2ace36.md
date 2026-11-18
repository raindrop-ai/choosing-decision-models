# State tracking and updating · question 11

[Back to State tracking and updating](README.md) · [All capabilities](../README.md)

**Question ID:** `babi/fbaeb8035845de2ace36`  
**Source:** [bAbI](https://s3.amazonaws.com/text-datasets/babi_tasks_1-20_v1-2.tar.gz)  
**Input format:** adapted choices

[Explore this question’s altered versions](../../variants/state-tracking-and-updating/babi-fbaeb8035845de2ace36/README.md)

## Context

> John took the football there.
> John left the football.
> Mary went back to the bathroom.
> Sandra got the football there.
> Daniel journeyed to the kitchen.
> John journeyed to the bedroom.
> Sandra dropped the football.
> Mary moved to the kitchen.
> Daniel grabbed the apple there.
> Mary went to the bathroom.
> Mary moved to the bedroom.
> John went back to the bathroom.
> Daniel discarded the apple there.
> Mary travelled to the kitchen.
> Sandra picked up the football there.
> Sandra left the football there.
> Mary went to the hallway.
> Daniel got the apple there.
> Daniel travelled to the hallway.
> Mary took the football there.
> John travelled to the hallway.
> Mary put down the football.

## Question

> Where is the football? 

## Answer choices

- **A:** bathroom
- **B:** kitchen
- **C:** garden
- **D:** hallway
- **E:** office
- **F:** bedroom

**Reference answer:** hallway (`D`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "John took the football there.\nJohn left the football.\nMary went back to the bathroom.\nSandra got the football there.\nDaniel journeyed to the kitchen.\nJohn journeyed to the bedroom.\nSandra dropped the football.\nMary moved to the kitchen.\nDaniel grabbed the apple there.\nMary went to the bathroom.\nMary moved to the bedroom.\nJohn went back to the bathroom.\nDaniel discarded the apple there.\nMary travelled to the kitchen.\nSandra picked up the football there.\nSandra left the football there.\nMary went to the hallway.\nDaniel got the apple there.\nDaniel travelled to the hallway.\nMary took the football there.\nJohn travelled to the hallway.\nMary put down the football.",
  "question": "Where is the football? ",
  "choices": {
    "A": "bathroom",
    "B": "kitchen",
    "C": "garden",
    "D": "hallway",
    "E": "office",
    "F": "bedroom"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | hallway | Correct |
| Opus 5.5 | hallway | Correct |
| GLiDE v1.2 | hallway | Correct |
| Decider v1.1 | hallway | Correct |
| Jev | hallway | Correct |
| Microsoft Decision-1 | hallway | Correct |
| Clef | hallway | Correct |
| Luna Decisions | hallway | Correct |
| Clef Flash | hallway | Correct |
| Strands Decider | hallway | Correct |
| GLiNER2.5 Decide | hallway | Correct |
| Laya | kitchen | Incorrect |
| CalDec v1 | hallway | Correct |

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
    "record": "5394",
    "kind": "source_file_record"
  },
  "source_revision": null,
  "input_hash": "4dc94c63d50f24ef30f73f562e8142d79aeb01bae852426d6251747f40c627ba"
}
```

</details>
