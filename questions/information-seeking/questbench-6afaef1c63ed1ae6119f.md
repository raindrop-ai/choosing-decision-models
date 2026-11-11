# Information seeking · question 27

[Back to Information seeking](README.md) · [All capabilities](../README.md)

**Question ID:** `questbench/6afaef1c63ed1ae6119f`  
**Source:** [QuestBench (Google DeepMind)](https://storage.googleapis.com/questbench/questbench_data.tar.gz)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/information-seeking/questbench-6afaef1c63ed1ae6119f/README.md)

## Context

> Millie decides to open a lemonade stand. She spends $18 to buy enough supplies to make 3 pitchers of lemonade. Each pitcher holds 12 cups of lemonade. She sells each cup of lemonade for $1. If Millie sells all of the lemonade, how much profit will she make per hour that she spends running the lemonade stand?

## Question

> Which missing variable should be asked about to solve this problem?

## Answer choices

- **A:** Number of cups Millie sells per hour
- **X1:** Amount of a glass of lemonade in ml

**Reference answer:** Number of cups Millie sells per hour (`A`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Millie decides to open a lemonade stand. She spends $18 to buy enough supplies to make 3 pitchers of lemonade. Each pitcher holds 12 cups of lemonade. She sells each cup of lemonade for $1. If Millie sells all of the lemonade, how much profit will she make per hour that she spends running the lemonade stand?",
  "question": "Which missing variable should be asked about to solve this problem?",
  "choices": {
    "A": "Number of cups Millie sells per hour",
    "X1": "Amount of a glass of lemonade in ml"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | Number of cups Millie sells per hour | Correct |
| Opus 5.5 | Number of cups Millie sells per hour | Correct |
| GLiDE v1.2 | Number of cups Millie sells per hour | Correct |
| Decider v1.1 | Number of cups Millie sells per hour | Correct |
| Jev | Number of cups Millie sells per hour | Correct |
| Microsoft Decision-1 | Number of cups Millie sells per hour | Correct |
| Clef | Number of cups Millie sells per hour | Correct |
| Luna Decisions | Number of cups Millie sells per hour | Correct |
| Clef Flash | Number of cups Millie sells per hour | Correct |
| Strands Decider | Number of cups Millie sells per hour | Correct |
| GLiNER2.5 Decide | Number of cups Millie sells per hour | Correct |
| Laya | Number of cups Millie sells per hour | Correct |
| CalDec v1 | Number of cups Millie sells per hour | Correct |

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
    "record": "15109",
    "kind": "source_file_record"
  },
  "source_revision": null,
  "input_hash": "4c7797b55a6889cb6736c477a2dabda958c7a0ffb90277f254dc11137078f443"
}
```

</details>
