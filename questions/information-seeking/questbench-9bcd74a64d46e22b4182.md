# Information seeking · question 35

[Back to Information seeking](README.md) · [All capabilities](../README.md)

**Question ID:** `questbench/9bcd74a64d46e22b4182`  
**Source:** [QuestBench (Google DeepMind)](https://storage.googleapis.com/questbench/questbench_data.tar.gz)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/information-seeking/questbench-9bcd74a64d46e22b4182/README.md)

## Context

> Aiden and 12 of his friends are going to see a film at the cinema, and meet up with 7 more friends there. They each save a seat and then buy enough drinks and snacks to fill the seats. Each seat has enough room to hold one person, two drinks, and three snacks. Additionally, each person decides to buy a souvenir keychain, but they later realize that the keychains are free today, so they don't have to spend any extra money on them. If drinks cost $2 each, how much money, in dollars, has the group spent overall on snacks and drinks?

## Question

> Which missing variable should be asked about to solve this problem?

## Answer choices

- **F:** Cost of one snack
- **L:** Cost of each keychain

**Reference answer:** Cost of one snack (`F`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Aiden and 12 of his friends are going to see a film at the cinema, and meet up with 7 more friends there. They each save a seat and then buy enough drinks and snacks to fill the seats. Each seat has enough room to hold one person, two drinks, and three snacks. Additionally, each person decides to buy a souvenir keychain, but they later realize that the keychains are free today, so they don't have to spend any extra money on them. If drinks cost $2 each, how much money, in dollars, has the group spent overall on snacks and drinks?",
  "question": "Which missing variable should be asked about to solve this problem?",
  "choices": {
    "F": "Cost of one snack",
    "L": "Cost of each keychain"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | Cost of one snack | Correct |
| Opus 5.5 | Cost of one snack | Correct |
| GLiDE v1.2 | Cost of one snack | Correct |
| Decider v1.1 | Cost of one snack | Correct |
| Jev | Cost of one snack | Correct |
| Microsoft Decision-1 | Cost of one snack | Correct |
| Clef | Cost of one snack | Correct |
| Luna Decisions | Cost of one snack | Correct |
| Clef Flash | Cost of one snack | Correct |
| Strands Decider | Cost of one snack | Correct |
| GLiNER2.5 Decide | Cost of each keychain | Incorrect |
| Laya | Cost of one snack | Correct |
| CalDec v1 | Cost of one snack | Correct |

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
    "record": "9565",
    "kind": "source_file_record"
  },
  "source_revision": null,
  "input_hash": "52609fe30cd2ab8089a198bf0c6e9596141b5b03f17814ee6733a288c46e85a3"
}
```

</details>
