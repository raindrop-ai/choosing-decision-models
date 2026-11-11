# Retrieval · question 33

[Back to Retrieval](README.md) · [All capabilities](../README.md)

**Question ID:** `boolq/ec63ada344a152ccf20a`  
**Source:** [BoolQ](https://huggingface.co/datasets/google/boolq)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/retrieval/boolq-ec63ada344a152ccf20a/README.md)

## Context

> As part of Marvel's Marvel NOW! initiative a new Deadpool ongoing series was launched, written by Brian Posehn and Gerry Duggan and illustrated by Tony Moore. He is also a member of the Thunderbolts. In the 27th issue of his new series, as part of \`\`All-New Marvel NOW!'', Deadpool was married for the third time. Initially a secret, his bride was revealed in the webcomic Deadpool: The Gauntlet to be Shiklah, Queen of the Undead. Deadpool also discovers that he has a daughter by the name of Eleanor from a former flame of Deadpool named Carmelita.

## Question

> does deadpool have a kid in the comics

## Answer choices

- **yes:** Yes
- **no:** No

**Reference answer:** Yes (`yes`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "As part of Marvel's Marvel NOW! initiative a new Deadpool ongoing series was launched, written by Brian Posehn and Gerry Duggan and illustrated by Tony Moore. He is also a member of the Thunderbolts. In the 27th issue of his new series, as part of ``All-New Marvel NOW!'', Deadpool was married for the third time. Initially a secret, his bride was revealed in the webcomic Deadpool: The Gauntlet to be Shiklah, Queen of the Undead. Deadpool also discovers that he has a daughter by the name of Eleanor from a former flame of Deadpool named Carmelita.",
  "question": "does deadpool have a kid in the comics",
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
| Jev | Yes | Correct |
| Microsoft Decision-1 | Yes | Correct |
| Clef | Yes | Correct |
| Luna Decisions | Yes | Correct |
| Clef Flash | Yes | Correct |
| Strands Decider | Yes | Correct |
| GLiNER2.5 Decide | Yes | Correct |
| Laya | Yes | Correct |
| CalDec v1 | Yes | Correct |

## Source and sharing

Original Wikipedia passage: [Deadpool](https://en.wikipedia.org/wiki/Deadpool); [contributor history](https://en.wikipedia.org/w/index.php?title=Deadpool&action=history). The BoolQ excerpt is unchanged. This question material retains CC BY-SA 3.0.

Attribution: Wikipedia contributors; Christopher Clark, Kenton Lee, Ming-Wei Chang, Tom Kwiatkowski, Michael Collins, Kristina Toutanova (BoolQ).  
Terms: **[CC-BY-SA-3.0](https://creativecommons.org/licenses/by-sa/3.0/)**. [Source sharing decision](../../docs/data-sharing.md).  
The capability assignment and choice-format normalization are part of this experiment. Source data retain their own terms.

<details>
<summary>Exact source locator and input fingerprint</summary>

```json
{
  "source_locator": {
    "path": "data/validation-00000-of-00001.parquet",
    "record": "30",
    "kind": "source_file_record"
  },
  "source_revision": "35b264d03638db9f4ce671b711558bf7ff0f80d5",
  "input_hash": "ba22fd3a883e3d9f556104d5aaf8d3b65b961e02ceb9dc7a1ad1201197f1a2f9"
}
```

</details>
