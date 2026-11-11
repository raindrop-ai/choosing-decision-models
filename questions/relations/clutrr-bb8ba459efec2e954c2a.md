# Relations · question 34

[Back to Relations](README.md) · [All capabilities](../README.md)

**Question ID:** `clutrr/bb8ba459efec2e954c2a`  
**Source:** [CLUTRR](https://github.com/kliang5/CLUTRR_huggingface_dataset)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/relations/clutrr-bb8ba459efec2e954c2a/README.md)

## Context

> \[Alma\] took her son \[Robert\] to the park yesterday. \[Robert\]'s sister \[Vanessa\] was playing at a friends house and did n't get to go.

## Question

> What is Alma’s relationship to Vanessa?

## Answer choices

- **aunt:** aunt
- **brother:** brother
- **daughter:** daughter
- **daughter-in-law:** daughter-in-law
- **father:** father
- **father-in-law:** father-in-law
- **granddaughter:** granddaughter
- **grandfather:** grandfather
- **grandmother:** grandmother
- **grandson:** grandson
- **mother:** mother
- **mother-in-law:** mother-in-law
- **nephew:** nephew
- **niece:** niece
- **sister:** sister
- **son:** son
- **son-in-law:** son-in-law
- **uncle:** uncle

**Reference answer:** mother (`mother`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "[Alma] took her son [Robert] to the park yesterday. [Robert]'s sister [Vanessa] was playing at a friends house and did n't get to go.",
  "question": "What is Alma’s relationship to Vanessa?",
  "choices": {
    "aunt": "aunt",
    "brother": "brother",
    "daughter": "daughter",
    "daughter-in-law": "daughter-in-law",
    "father": "father",
    "father-in-law": "father-in-law",
    "granddaughter": "granddaughter",
    "grandfather": "grandfather",
    "grandmother": "grandmother",
    "grandson": "grandson",
    "mother": "mother",
    "mother-in-law": "mother-in-law",
    "nephew": "nephew",
    "niece": "niece",
    "sister": "sister",
    "son": "son",
    "son-in-law": "son-in-law",
    "uncle": "uncle"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | mother | Correct |
| Opus 5.5 | mother | Correct |
| GLiDE v1.2 | mother | Correct |
| Decider v1.1 | mother | Correct |
| Jev | mother | Correct |
| Microsoft Decision-1 | mother | Correct |
| Clef | mother | Correct |
| Luna Decisions | mother | Correct |
| Clef Flash | aunt | Incorrect |
| Strands Decider | nephew | Incorrect |
| GLiNER2.5 Decide | sister | Incorrect |
| Laya | mother | Correct |
| CalDec v1 | sister | Incorrect |

## Source and sharing

Attribution: Koustuv Sinha, Shagun Sodhani, Jin Dong, Joelle Pineau, William L. Hamilton.  
Terms: **[CC-BY-NC-4.0](https://creativecommons.org/licenses/by-nc/4.0/)**. [Source sharing decision](../../docs/data-sharing.md).  
The capability assignment and choice-format normalization are part of this experiment. Source data retain their own terms.

<details>
<summary>Exact source locator and input fingerprint</summary>

```json
{
  "source_locator": {
    "path": "gen_train23_test2to10/train.csv",
    "record": "1160",
    "kind": "source_file_record"
  },
  "source_revision": "e5b496941e91abb7c319d2618a3ce96752bc4ab7",
  "input_hash": "3dcc5c7941249e48cc97a0e43e5709ab75542b49a36018ae59bf7facd8e73092"
}
```

</details>
