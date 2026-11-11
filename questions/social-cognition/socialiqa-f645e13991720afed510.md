# Social cognition · question 36

[Back to Social cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `socialiqa/f645e13991720afed510`  
**Source:** [Social IQa](https://storage.googleapis.com/ai2-mosaic/public/socialiqa/socialiqa-train-dev.zip)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/social-cognition/socialiqa-f645e13991720afed510/README.md)

## Context

> Austin spent all afternoon working on homework to free up time at night.

## Question

> Why did Austin do this?

## Answer choices

- **A:** have fun later
- **B:** play games now
- **C:** play some games

**Reference answer:** have fun later (`A`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Austin spent all afternoon working on homework to free up time at night.",
  "question": "Why did Austin do this?",
  "choices": {
    "A": "have fun later",
    "B": "play games now",
    "C": "play some games"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | have fun later | Correct |
| Opus 5.5 | have fun later | Correct |
| GLiDE v1.2 | have fun later | Correct |
| Decider v1.1 | have fun later | Correct |
| Jev | have fun later | Correct |
| Microsoft Decision-1 | have fun later | Correct |
| Clef | have fun later | Correct |
| Luna Decisions | have fun later | Correct |
| Clef Flash | have fun later | Correct |
| Strands Decider | have fun later | Correct |
| GLiNER2.5 Decide | have fun later | Correct |
| Laya | play some games | Incorrect |
| CalDec v1 | have fun later | Correct |

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
    "record": "18630",
    "kind": "source_file_record"
  },
  "source_revision": null,
  "input_hash": "e1f02c1f04446f3558d6775cb0103705e083cd0ae6ba7dd197116a51c8e885f3"
}
```

</details>
