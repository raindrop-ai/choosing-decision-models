# Retrieval · question 37

[Back to Retrieval](README.md) · [All capabilities](../README.md)

**Question ID:** `boolq/bd166e1008ee2e61a4b3`  
**Source:** [BoolQ](https://huggingface.co/datasets/google/boolq)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/retrieval/boolq-bd166e1008ee2e61a4b3/README.md)

## Context

> Principal photography for The Lord of the Rings film trilogy was conducted concurrently in New Zealand for 438 days from October 11, 1999 through to December 22, 2000. Pick-up shoots were conducted annually from 2001 to 2003. The trilogy was shot at over 150 different locations, with seven different units shooting, as well as soundstages around Wellington and Queenstown. Peter Jackson directed the whole production, while other unit directors included Alun Bollinger, John Mahaffie, Geoff Murphy, Fran Walsh, Barrie Osborne, and Rick Porras. Jackson monitored these units with live satellite feeds, and with the added pressure of constant script re-writes and the multiple units handling his vision, he only got around 4 hours of sleep a night.

## Question

> did they film the lord of the rings all at once

## Answer choices

- **yes:** Yes
- **no:** No

**Reference answer:** Yes (`yes`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Principal photography for The Lord of the Rings film trilogy was conducted concurrently in New Zealand for 438 days from October 11, 1999 through to December 22, 2000. Pick-up shoots were conducted annually from 2001 to 2003. The trilogy was shot at over 150 different locations, with seven different units shooting, as well as soundstages around Wellington and Queenstown. Peter Jackson directed the whole production, while other unit directors included Alun Bollinger, John Mahaffie, Geoff Murphy, Fran Walsh, Barrie Osborne, and Rick Porras. Jackson monitored these units with live satellite feeds, and with the added pressure of constant script re-writes and the multiple units handling his vision, he only got around 4 hours of sleep a night.",
  "question": "did they film the lord of the rings all at once",
  "choices": {
    "yes": "Yes",
    "no": "No"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | Yes | Correct |
| Opus 5.5 | Yes | Correct |
| GLiDE v1.2 | Yes | Correct |
| Decider v1.1 | Yes | Correct |
| Jev | No | Incorrect |
| Microsoft Decision-1 | Yes | Correct |
| Clef | Yes | Correct |
| Luna Decisions | Yes | Correct |
| Clef Flash | Yes | Correct |
| Strands Decider | Yes | Correct |
| GLiNER2.5 Decide | No | Incorrect |
| Laya | Yes | Correct |
| CalDec v1 | No | Incorrect |

## Source and sharing

Original Wikipedia passage: [Principal photography of The Lord of the Rings film series](https://en.wikipedia.org/wiki/Principal_photography_of_The_Lord_of_the_Rings_film_series); [contributor history](https://en.wikipedia.org/w/index.php?title=Principal_photography_of_The_Lord_of_the_Rings_film_series&action=history). The BoolQ excerpt is unchanged. This question material retains CC BY-SA 3.0.

Attribution: Wikipedia contributors; Christopher Clark, Kenton Lee, Ming-Wei Chang, Tom Kwiatkowski, Michael Collins, Kristina Toutanova (BoolQ).  
Terms: **[CC-BY-SA-3.0](https://creativecommons.org/licenses/by-sa/3.0/)**. [Source sharing decision](../../docs/data-sharing.md).  
The capability assignment and choice-format normalization are part of this experiment. Source data retain their own terms.

<details>
<summary>Exact source locator and input fingerprint</summary>

```json
{
  "source_locator": {
    "path": "data/train-00000-of-00001.parquet",
    "record": "3969",
    "kind": "source_file_record"
  },
  "source_revision": "35b264d03638db9f4ce671b711558bf7ff0f80d5",
  "input_hash": "7fc5a62d61a01fd8cc6126754cd311b5f96a1414bc1285f46803031ad7ce9f18"
}
```

</details>
