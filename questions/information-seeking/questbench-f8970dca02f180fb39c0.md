# Information seeking · question 51

[Back to Information seeking](README.md) · [All capabilities](../README.md)

**Question ID:** `questbench/f8970dca02f180fb39c0`  
**Source:** [QuestBench (Google DeepMind)](https://storage.googleapis.com/questbench/questbench_data.tar.gz)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/information-seeking/questbench-f8970dca02f180fb39c0/README.md)

## Context

> Eve had pieces of pomelos and strawberries. After giving her friend some pomelos, Eve is left with 1/4 of the pomelos she originally had. How many pomelos did Eve give away?

## Question

> Which missing variable should be asked about to solve this problem?

## Answer choices

- **P:** Number of pomelos Eve originally had
- **S:** Number of strawberries Eve had

**Reference answer:** Number of pomelos Eve originally had (`P`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Eve had pieces of pomelos and strawberries. After giving her friend some pomelos, Eve is left with 1/4 of the pomelos she originally had. How many pomelos did Eve give away?",
  "question": "Which missing variable should be asked about to solve this problem?",
  "choices": {
    "P": "Number of pomelos Eve originally had",
    "S": "Number of strawberries Eve had"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | Number of pomelos Eve originally had | Correct |
| Opus 5.5 | Number of pomelos Eve originally had | Correct |
| GLiDE v1.2 | Number of pomelos Eve originally had | Correct |
| Decider v1.1 | Number of pomelos Eve originally had | Correct |
| Jev | Number of pomelos Eve originally had | Correct |
| Microsoft Decision-1 | Number of pomelos Eve originally had | Correct |
| Clef | Number of pomelos Eve originally had | Correct |
| Luna Decisions | Number of pomelos Eve originally had | Correct |
| Clef Flash | Number of pomelos Eve originally had | Correct |
| Strands Decider | Number of pomelos Eve originally had | Correct |
| GLiNER2.5 Decide | Number of pomelos Eve originally had | Correct |
| Laya | Number of pomelos Eve originally had | Correct |
| CalDec v1 | Number of pomelos Eve originally had | Correct |

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
    "record": "12956",
    "kind": "source_file_record"
  },
  "source_revision": null,
  "input_hash": "0d489f4df9b08260e07c2e826a3bf94b8c2423ab234854ada35ec75eeac7a21f"
}
```

</details>
