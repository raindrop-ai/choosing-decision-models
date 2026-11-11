# Concepts and categorization · question 2

[Back to Concepts and categorization](README.md) · [All capabilities](../README.md)

**Question ID:** `mnli/ba47e276b2b7b8b7fd71`  
**Source:** [MNLI](https://huggingface.co/datasets/nyu-mll/multi_nli)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/concepts-and-categorization/mnli-ba47e276b2b7b8b7fd71/README.md)

## Context

> That would be a tenfold increase in the Internet's share.

## Question

> Does the premise entail, contradict, or leave undetermined this statement? That would cause the Internet's share to rise by a factor of ten.

## Answer choices

- **0:** Entailment
- **1:** Neither entailed nor contradicted
- **2:** Contradiction

**Reference answer:** Entailment (`0`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "That would be a tenfold increase in the Internet's share.",
  "question": "Does the premise entail, contradict, or leave undetermined this statement? That would cause the Internet's share to rise by a factor of ten.",
  "choices": {
    "0": "Entailment",
    "1": "Neither entailed nor contradicted",
    "2": "Contradiction"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | Entailment | Correct |
| Opus 5.5 | Entailment | Correct |
| GLiDE v1.2 | Entailment | Correct |
| Decider v1.1 | Entailment | Correct |
| Jev | Entailment | Correct |
| Microsoft Decision-1 | Entailment | Correct |
| Clef | Entailment | Correct |
| Luna Decisions | Neither entailed nor contradicted | Incorrect |
| Clef Flash | Entailment | Correct |
| Strands Decider | Entailment | Correct |
| GLiNER2.5 Decide | Neither entailed nor contradicted | Incorrect |
| Laya | Entailment | Correct |
| CalDec v1 | Entailment | Correct |

## Source and sharing

Original MultiNLI pair: `25200e`; OANC genre: **slate**. Transparent modification: selected excerpts and format normalization by Raindrop, 2026-11-09. Premise wording is unchanged. The original unmodified sentence pair is identified by pairID in the MultiNLI 1.0 release, available from the source URL. No source endorsement is implied.

Attribution: Adina Williams, Nikita Nangia, Samuel R. Bowman (MultiNLI); Slate Magazine; Copyright (c) 1996-2000 Microsoft Corporation.  
Terms: **[OANC (selected non-fiction genres)](https://anc.org/OANC/license.txt)**. [Source sharing decision](../../docs/data-sharing.md).  
The capability assignment and choice-format normalization are part of this experiment. Source data retain their own terms.

<details>
<summary>Exact source locator and input fingerprint</summary>

```json
{
  "source_locator": {
    "path": "data/validation_matched-00000-of-00001.parquet",
    "record": "7840",
    "kind": "source_file_record"
  },
  "source_revision": "da70db2af9d09693783c3320c4249840212ee221",
  "input_hash": "7053f0151e93d87fcebc62b07201f049debd0c01b1cf8a6b3a49a14db8cd4ecb"
}
```

</details>
