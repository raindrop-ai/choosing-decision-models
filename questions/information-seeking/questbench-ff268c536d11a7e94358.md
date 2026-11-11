# Information seeking · question 61

[Back to Information seeking](README.md) · [All capabilities](../README.md)

**Question ID:** `questbench/ff268c536d11a7e94358`  
**Source:** [QuestBench (Google DeepMind)](https://storage.googleapis.com/questbench/questbench_data.tar.gz)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/information-seeking/questbench-ff268c536d11a7e94358/README.md)

## Context

> Jay is making snowballs to prepare for a snowball fight with his sister. It takes his sister a while to build a snowman. He can build some amount of snowballs in an hour, but 2 melt every 15 minutes. How long will it take before he has 60 snowballs?

## Question

> Which missing variable should be asked about to solve this problem?

## Answer choices

- **A:** Number of snowballs build in an hour
- **H:** Number of hours taken to build snowman

**Reference answer:** Number of snowballs build in an hour (`A`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Jay is making snowballs to prepare for a snowball fight with his sister. It takes his sister a while to build a snowman. He can build some amount of snowballs in an hour, but 2 melt every 15 minutes. How long will it take before he has 60 snowballs?",
  "question": "Which missing variable should be asked about to solve this problem?",
  "choices": {
    "A": "Number of snowballs build in an hour",
    "H": "Number of hours taken to build snowman"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | Number of snowballs build in an hour | Correct |
| Opus 5.5 | Number of snowballs build in an hour | Correct |
| GLiDE v1.2 | Number of snowballs build in an hour | Correct |
| Decider v1.1 | Number of snowballs build in an hour | Correct |
| Jev | Number of snowballs build in an hour | Correct |
| Microsoft Decision-1 | Number of snowballs build in an hour | Correct |
| Clef | Number of snowballs build in an hour | Correct |
| Luna Decisions | Number of snowballs build in an hour | Correct |
| Clef Flash | Number of snowballs build in an hour | Correct |
| Strands Decider | Number of snowballs build in an hour | Correct |
| GLiNER2.5 Decide | Number of snowballs build in an hour | Correct |
| Laya | Number of snowballs build in an hour | Correct |
| CalDec v1 | Number of snowballs build in an hour | Correct |

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
    "record": "16170",
    "kind": "source_file_record"
  },
  "source_revision": null,
  "input_hash": "1dea62df411487cc64853a9b25dd3d94c8b5781d699cb521c3d743655fe53b93"
}
```

</details>
