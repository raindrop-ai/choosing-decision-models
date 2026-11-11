# Concepts and categorization · question 48

[Back to Concepts and categorization](README.md) · [All capabilities](../README.md)

**Question ID:** `mnli/e3ace8a0142dc5ef923e`  
**Source:** [MNLI](https://huggingface.co/datasets/nyu-mll/multi_nli)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/concepts-and-categorization/mnli-e3ace8a0142dc5ef923e/README.md)

## Context

> 11 These departures permit them take advantage of the lower cost of living as well as to be reunited with their spouses and children.

## Question

> Does the premise entail, contradict, or leave undetermined this statement? The departures help them take advantage of the high cost of living in other areas.

## Answer choices

- **0:** Entailment
- **1:** Neither entailed nor contradicted
- **2:** Contradiction

**Reference answer:** Contradiction (`2`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "11 These departures permit them take advantage of the lower cost of living as well as to be reunited with their spouses and children.",
  "question": "Does the premise entail, contradict, or leave undetermined this statement? The departures help them take advantage of the high cost of living in other areas.",
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
| Astra | Contradiction | Correct |
| Opus 5.5 | Contradiction | Correct |
| GLiDE v1.2 | Contradiction | Correct |
| Decider v1.1 | Contradiction | Correct |
| Jev | Contradiction | Correct |
| Microsoft Decision-1 | Contradiction | Correct |
| Clef | Contradiction | Correct |
| Luna Decisions | Contradiction | Correct |
| Clef Flash | Contradiction | Correct |
| Strands Decider | Contradiction | Correct |
| GLiNER2.5 Decide | Entailment | Incorrect |
| Laya | Contradiction | Correct |
| CalDec v1 | Contradiction | Correct |

## Source and sharing

Original MultiNLI pair: `132309c`; OANC genre: **government**. Transparent modification: selected excerpts and format normalization by Raindrop, 2026-11-09. Premise wording is unchanged. The original unmodified sentence pair is identified by pairID in the MultiNLI 1.0 release, available from the source URL. No source endorsement is implied.

Attribution: Adina Williams, Nikita Nangia, Samuel R. Bowman (MultiNLI); OANC government texts; American National Corpus Consortium.  
Terms: **[OANC (selected non-fiction genres)](https://anc.org/OANC/license.txt)**. [Source sharing decision](../../docs/data-sharing.md).  
The capability assignment and choice-format normalization are part of this experiment. Source data retain their own terms.

<details>
<summary>Exact source locator and input fingerprint</summary>

```json
{
  "source_locator": {
    "path": "data/validation_matched-00000-of-00001.parquet",
    "record": "1587",
    "kind": "source_file_record"
  },
  "source_revision": "da70db2af9d09693783c3320c4249840212ee221",
  "input_hash": "4b3c6ea1f7c0e02f74ee22b9dd131ae3ddcf33d4622a8d4296ed71e1f6c36c93"
}
```

</details>
