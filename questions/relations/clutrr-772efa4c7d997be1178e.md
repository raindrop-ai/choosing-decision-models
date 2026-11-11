# Relations · question 4

[Back to Relations](README.md) · [All capabilities](../README.md)

**Question ID:** `clutrr/772efa4c7d997be1178e`  
**Source:** [CLUTRR](https://github.com/kliang5/CLUTRR_huggingface_dataset)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/relations/clutrr-772efa4c7d997be1178e/README.md)

## Context

> \[David\] asked his sister \[Michele\] for some money. He was going to use the money to buy his grandfather, \[Jason\], a present.

## Question

> What is Michele’s relationship to Jason?

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

**Reference answer:** granddaughter (`granddaughter`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "[David] asked his sister [Michele] for some money. He was going to use the money to buy his grandfather, [Jason], a present.",
  "question": "What is Michele’s relationship to Jason?",
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
| Astra | granddaughter | Correct |
| Opus 5.5 | granddaughter | Correct |
| GLiDE v1.2 | granddaughter | Correct |
| Decider v1.1 | granddaughter | Correct |
| Jev | granddaughter | Correct |
| Microsoft Decision-1 | aunt | Incorrect |
| Clef | granddaughter | Correct |
| Luna Decisions | granddaughter | Correct |
| Clef Flash | aunt | Incorrect |
| Strands Decider | sister | Incorrect |
| GLiNER2.5 Decide | sister | Incorrect |
| Laya | grandfather | Incorrect |
| CalDec v1 | grandfather | Incorrect |

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
    "record": "2651",
    "kind": "source_file_record"
  },
  "source_revision": "e5b496941e91abb7c319d2618a3ce96752bc4ab7",
  "input_hash": "e0b6f13079846e97395918d80928859bcc952b9fa21e962f6fab6532d6cedebf"
}
```

</details>
