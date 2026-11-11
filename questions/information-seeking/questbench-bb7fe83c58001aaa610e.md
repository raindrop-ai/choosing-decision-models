# Information seeking · question 19

[Back to Information seeking](README.md) · [All capabilities](../README.md)

**Question ID:** `questbench/bb7fe83c58001aaa610e`  
**Source:** [QuestBench (Google DeepMind)](https://storage.googleapis.com/questbench/questbench_data.tar.gz)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/information-seeking/questbench-bb7fe83c58001aaa610e/README.md)

## Context

> A simple folding newspaper or tabloid can be made by folding a piece of paper vertically and unfolding it. Then, say, page 1 is printed on the left back, page 2 is printed on the left front, and then, perhaps page 32 is printed on the right back, and page 31 is printed on the right front. How many pieces of paper would be used in a -page tabloid 2 inches long by 3 inches wide?

## Question

> Which missing variable should be asked about to solve this problem?

## Answer choices

- **P:** Total number of pages in the tabloid
- **L:** Length of each piece (in inches)
- **W:** Width of each piece (in inches)

**Reference answer:** Total number of pages in the tabloid (`P`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "A simple folding newspaper or tabloid can be made by folding a piece of paper vertically and unfolding it. Then, say, page 1 is printed on the left back, page 2 is printed on the left front, and then, perhaps page 32 is printed on the right back, and page 31 is printed on the right front. How many pieces of paper would be used in a -page tabloid 2 inches long by 3 inches wide?",
  "question": "Which missing variable should be asked about to solve this problem?",
  "choices": {
    "P": "Total number of pages in the tabloid",
    "L": "Length of each piece (in inches)",
    "W": "Width of each piece (in inches)"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | Total number of pages in the tabloid | Correct |
| Opus 5.5 | Total number of pages in the tabloid | Correct |
| GLiDE v1.2 | Total number of pages in the tabloid | Correct |
| Decider v1.1 | Total number of pages in the tabloid | Correct |
| Jev | Total number of pages in the tabloid | Correct |
| Microsoft Decision-1 | Total number of pages in the tabloid | Correct |
| Clef | Total number of pages in the tabloid | Correct |
| Luna Decisions | Total number of pages in the tabloid | Correct |
| Clef Flash | Total number of pages in the tabloid | Correct |
| Strands Decider | Total number of pages in the tabloid | Correct |
| GLiNER2.5 Decide | Length of each piece (in inches) | Incorrect |
| Laya | Length of each piece (in inches) | Incorrect |
| CalDec v1 | Length of each piece (in inches) | Incorrect |

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
    "record": "17792",
    "kind": "source_file_record"
  },
  "source_revision": null,
  "input_hash": "e0bd6335dd5acecbf60fdc65b9626ef3856f2a84ce0e9d268b4cf758a99ca43a"
}
```

</details>
