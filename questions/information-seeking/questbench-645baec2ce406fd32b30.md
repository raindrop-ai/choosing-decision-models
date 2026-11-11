# Information seeking · question 45

[Back to Information seeking](README.md) · [All capabilities](../README.md)

**Question ID:** `questbench/645baec2ce406fd32b30`  
**Source:** [QuestBench (Google DeepMind)](https://storage.googleapis.com/questbench/questbench_data.tar.gz)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/information-seeking/questbench-645baec2ce406fd32b30/README.md)

## Context

> Joelle has a beautiful balcony garden. She has 5 orchids. If each orchid has 5 petals and each African daisy has 10 petals, how many more petals do the African daisies have compared to the orchids?

## Question

> Which missing variable should be asked about to solve this problem?

## Answer choices

- **D1:** Number of African daisies
- **X1:** Number of roses
- **X2:** Number of petals per rose

**Reference answer:** Number of African daisies (`D1`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Joelle has a beautiful balcony garden. She has 5 orchids. If each orchid has 5 petals and each African daisy has 10 petals, how many more petals do the African daisies have compared to the orchids?",
  "question": "Which missing variable should be asked about to solve this problem?",
  "choices": {
    "D1": "Number of African daisies",
    "X1": "Number of roses",
    "X2": "Number of petals per rose"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | Number of African daisies | Correct |
| Opus 5.5 | Number of African daisies | Correct |
| GLiDE v1.2 | Number of African daisies | Correct |
| Decider v1.1 | Number of African daisies | Correct |
| Jev | Number of African daisies | Correct |
| Microsoft Decision-1 | Number of African daisies | Correct |
| Clef | Number of African daisies | Correct |
| Luna Decisions | Number of African daisies | Correct |
| Clef Flash | Number of African daisies | Correct |
| Strands Decider | Number of African daisies | Correct |
| GLiNER2.5 Decide | Number of African daisies | Correct |
| Laya | Number of African daisies | Correct |
| CalDec v1 | Number of African daisies | Correct |

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
    "record": "14246",
    "kind": "source_file_record"
  },
  "source_revision": null,
  "input_hash": "43a570e1b076a3a72eed76ec035521fb916a866240f95f3c889cbd38a29dfcc7"
}
```

</details>
