# Relations · question 18

[Back to Relations](README.md) · [All capabilities](../README.md)

**Question ID:** `clutrr/b9d7e4ecfba4a2dd0903`  
**Source:** [CLUTRR](https://github.com/kliang5/CLUTRR_huggingface_dataset)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/relations/clutrr-b9d7e4ecfba4a2dd0903/README.md)

## Context

> \[Molly\] sat anxiously in the airport terminal, waiting to see her son \[Michael\] walk through the gate. \[Molly\] is weary of her son \[Alan\]'s behaviour. He is often in trouble at school. \[Elizabeth\] went out for pizza with her father \[Alan\].

## Question

> What is Michael’s relationship to Elizabeth?

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

**Reference answer:** uncle (`uncle`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "[Molly] sat anxiously in the airport terminal, waiting to see her son [Michael] walk through the gate. [Molly] is weary of her son [Alan]'s behaviour. He is often in trouble at school. [Elizabeth] went out for pizza with her father [Alan].",
  "question": "What is Michael’s relationship to Elizabeth?",
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
| Astra | uncle | Correct |
| Opus 5.5 | uncle | Correct |
| GLiDE v1.2 | uncle | Correct |
| Decider v1.1 | brother | Incorrect |
| Jev | brother | Incorrect |
| Microsoft Decision-1 | uncle | Correct |
| Clef | nephew | Incorrect |
| Luna Decisions | son | Incorrect |
| Clef Flash | nephew | Incorrect |
| Strands Decider | son | Incorrect |
| GLiNER2.5 Decide | father | Incorrect |
| Laya | son | Incorrect |
| CalDec v1 | son | Incorrect |

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
    "record": "7187",
    "kind": "source_file_record"
  },
  "source_revision": "e5b496941e91abb7c319d2618a3ce96752bc4ab7",
  "input_hash": "d3c309255ebce269ceb2d2b6ab38158b64a89f3f43388992d6278efc41585f22"
}
```

</details>
