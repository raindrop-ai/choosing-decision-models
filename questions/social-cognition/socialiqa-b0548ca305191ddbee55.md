# Social cognition · question 1

[Back to Social cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `socialiqa/b0548ca305191ddbee55`  
**Source:** [Social IQa](https://storage.googleapis.com/ai2-mosaic/public/socialiqa/socialiqa-train-dev.zip)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/social-cognition/socialiqa-b0548ca305191ddbee55/README.md)

## Context

> Quinn learned to play drums in his spare time between volunteering for the homeless and studying for school.

## Question

> What kind of person is Quinn?

## Answer choices

- **A:** lazy and selfish
- **B:** cares about the world
- **C:** hates other people

**Reference answer:** cares about the world (`B`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Quinn learned to play drums in his spare time between volunteering for the homeless and studying for school.",
  "question": "What kind of person is Quinn?",
  "choices": {
    "A": "lazy and selfish",
    "B": "cares about the world",
    "C": "hates other people"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | cares about the world | Correct |
| Opus 5.5 | cares about the world | Correct |
| GLiDE v1.2 | cares about the world | Correct |
| Decider v1.1 | cares about the world | Correct |
| Jev | cares about the world | Correct |
| Microsoft Decision-1 | cares about the world | Correct |
| Clef | cares about the world | Correct |
| Luna Decisions | cares about the world | Correct |
| Clef Flash | cares about the world | Correct |
| Strands Decider | cares about the world | Correct |
| GLiNER2.5 Decide | cares about the world | Correct |
| Laya | cares about the world | Correct |
| CalDec v1 | cares about the world | Correct |

## Source and sharing

Attribution: Maarten Sap, Hannah Rashkin, Derek Chen, Ronan LeBras, Yejin Choi.  
Terms: **[CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)**. [Source sharing decision](../../docs/data-sharing.md).  
The capability assignment and choice-format normalization are part of this experiment. Source data retain their own terms.

<details>
<summary>Exact source locator and input fingerprint</summary>

```json
{
  "source_locator": {
    "path": "extracted/socialiqa.zip/socialiqa-train-dev/train.jsonl",
    "record": "26974",
    "kind": "source_file_record"
  },
  "source_revision": null,
  "input_hash": "d4da44feb1cad40442cef86bd6c22f73ee457365f9ac0493803bbdadcf3ad69e"
}
```

</details>
