# Information seeking · question 47

[Back to Information seeking](README.md) · [All capabilities](../README.md)

**Question ID:** `questbench/26e575472c7174cae9e3`  
**Source:** [QuestBench (Google DeepMind)](https://storage.googleapis.com/questbench/questbench_data.tar.gz)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/information-seeking/questbench-26e575472c7174cae9e3/README.md)

## Context

> Carlos, Jim, and Carrey were at the beach playing and they decided to gather some seashells. Jim collected 27 seashells, which was more than what Carlos collected. Carlos collected twice as many as Carrey. They gathered all their seashells and divided them equally between themselves. How many did each person get?

## Question

> Which missing variable should be asked about to solve this problem?

## Answer choices

- **F1:** The difference between Jim and Carlos&#x27; seashells
- **X:** The number of seashells the seagull stole and a friendly beachcomber gave back to Jim

**Reference answer:** The difference between Jim and Carlos&#x27; seashells (`F1`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Carlos, Jim, and Carrey were at the beach playing and they decided to gather some seashells. Jim collected 27 seashells, which was more than what Carlos collected. Carlos collected twice as many as Carrey. They gathered all their seashells and divided them equally between themselves. How many did each person get?",
  "question": "Which missing variable should be asked about to solve this problem?",
  "choices": {
    "F1": "The difference between Jim and Carlos' seashells",
    "X": "The number of seashells the seagull stole and a friendly beachcomber gave back to Jim"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | The difference between Jim and Carlos&#x27; seashells | Correct |
| Opus 5.5 | The difference between Jim and Carlos&#x27; seashells | Correct |
| GLiDE v1.2 | The difference between Jim and Carlos&#x27; seashells | Correct |
| Decider v1.1 | The difference between Jim and Carlos&#x27; seashells | Correct |
| Jev | The difference between Jim and Carlos&#x27; seashells | Correct |
| Microsoft Decision-1 | The difference between Jim and Carlos&#x27; seashells | Correct |
| Clef | The difference between Jim and Carlos&#x27; seashells | Correct |
| Luna Decisions | The difference between Jim and Carlos&#x27; seashells | Correct |
| Clef Flash | The difference between Jim and Carlos&#x27; seashells | Correct |
| Strands Decider | The difference between Jim and Carlos&#x27; seashells | Correct |
| GLiNER2.5 Decide | The difference between Jim and Carlos&#x27; seashells | Correct |
| Laya | The difference between Jim and Carlos&#x27; seashells | Correct |
| CalDec v1 | The difference between Jim and Carlos&#x27; seashells | Correct |

## Source and sharing

Attribution: Google LLC; QuestBench authors.  
Terms: **[CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)**. [Source sharing decision](../../docs/data-sharing.md).  
The capability assignment and choice-format normalization are part of this experiment. Source data retain their own terms.

<details>
<summary>Exact source locator and input fingerprint</summary>

```json
{
  "source_locator": {
    "path": "extracted/questbench.tar.gz/questbench_data/GSM-Q/gsm_verbal_full.csv",
    "record": "6883",
    "kind": "source_file_record"
  },
  "source_revision": null,
  "input_hash": "4b2615c64f5cc77c9ae0c3d79209e01477468869866a7fc2bf11f99b1ee89c82"
}
```

</details>
