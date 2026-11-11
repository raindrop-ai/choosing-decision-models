# Relations · question 12

[Back to Relations](README.md) · [All capabilities](../README.md)

**Question ID:** `clutrr/a57c8a868bc882e02ddd`  
**Source:** [CLUTRR](https://github.com/kliang5/CLUTRR_huggingface_dataset)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/relations/clutrr-a57c8a868bc882e02ddd/README.md)

## Context

> \[Jonathan\] was so happy for his brother, \[Jason\], getting a promotion. \[Jonathan\] was trying to find his daughter, \[Diana\], but she was no where to be seen in the house. It turns out she was shopping with her sister, \[Traci\], at the time. \[Christian\] bought Christmas gifts for his brother \[Jason\] and his sister \[Rosa\].

## Question

> What is Rosa’s relationship to Traci?

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

**Reference answer:** aunt (`aunt`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "[Jonathan] was so happy for his brother, [Jason], getting a promotion. [Jonathan] was trying to find his daughter, [Diana], but she was no where to be seen in the house. It turns out she was shopping with her sister, [Traci], at the time. [Christian] bought Christmas gifts for his brother [Jason] and his sister [Rosa].",
  "question": "What is Rosa’s relationship to Traci?",
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
| Astra | aunt | Correct |
| Opus 5.5 | aunt | Correct |
| GLiDE v1.2 | aunt | Correct |
| Decider v1.1 | aunt | Correct |
| Jev | aunt | Correct |
| Microsoft Decision-1 | sister | Incorrect |
| Clef | niece | Incorrect |
| Luna Decisions | sister | Incorrect |
| Clef Flash | sister | Incorrect |
| Strands Decider | sister | Incorrect |
| GLiNER2.5 Decide | brother | Incorrect |
| Laya | sister | Incorrect |
| CalDec v1 | daughter | Incorrect |

## Source and sharing

Attribution: Koustuv Sinha, Shagun Sodhani, Jin Dong, Joelle Pineau, William L. Hamilton.  
Terms: **[CC-BY-NC-4.0](https://creativecommons.org/licenses/by-nc/4.0/)**. [Source sharing decision](../../docs/data-sharing.md).  
The capability assignment and choice-format normalization are part of this experiment. Source data retain their own terms.

<details>
<summary>Exact source locator and input fingerprint</summary>

```json
{
  "source_locator": {
    "path": "gen_train23_test2to10/test.csv",
    "record": "457",
    "kind": "source_file_record"
  },
  "source_revision": "e5b496941e91abb7c319d2618a3ce96752bc4ab7",
  "input_hash": "49b80ab4487013735b11468db886b8969d64168fc43eb54e5e047d042c70ad24"
}
```

</details>
