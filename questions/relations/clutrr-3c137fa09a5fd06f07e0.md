# Relations · question 2

[Back to Relations](README.md) · [All capabilities](../README.md)

**Question ID:** `clutrr/3c137fa09a5fd06f07e0`  
**Source:** [CLUTRR](https://github.com/kliang5/CLUTRR_huggingface_dataset)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/relations/clutrr-3c137fa09a5fd06f07e0/README.md)

## Context

> \[Alan\] made his son \[Emmanuel\] mow the lawn. \[Emmanuel\]'s sister \[Eunice\] tanned in the yard instead. \[Annie\]'s father \[Alan\] is taking her to a movie because she got good grades.

## Question

> What is Annie’s relationship to Eunice?

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

**Reference answer:** sister (`sister`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "[Alan] made his son [Emmanuel] mow the lawn. [Emmanuel]'s sister [Eunice] tanned in the yard instead. [Annie]'s father [Alan] is taking her to a movie because she got good grades.",
  "question": "What is Annie’s relationship to Eunice?",
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
| Astra | sister | Correct |
| Opus 5.5 | sister | Correct |
| GLiDE v1.2 | sister | Correct |
| Decider v1.1 | sister | Correct |
| Jev | sister | Correct |
| Microsoft Decision-1 | niece | Incorrect |
| Clef | niece | Incorrect |
| Luna Decisions | sister | Correct |
| Clef Flash | niece | Incorrect |
| Strands Decider | niece | Incorrect |
| GLiNER2.5 Decide | father | Incorrect |
| Laya | sister | Correct |
| CalDec v1 | sister | Correct |

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
    "record": "4125",
    "kind": "source_file_record"
  },
  "source_revision": "e5b496941e91abb7c319d2618a3ce96752bc4ab7",
  "input_hash": "1fdc2f11e5a1725c01eca8337dde5ded8563bf2fea7028494b1e02feb492d0e8"
}
```

</details>
