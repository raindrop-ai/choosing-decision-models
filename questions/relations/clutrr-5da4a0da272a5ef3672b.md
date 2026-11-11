# Relations · question 30

[Back to Relations](README.md) · [All capabilities](../README.md)

**Question ID:** `clutrr/5da4a0da272a5ef3672b`  
**Source:** [CLUTRR](https://github.com/kliang5/CLUTRR_huggingface_dataset)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/relations/clutrr-5da4a0da272a5ef3672b/README.md)

## Context

> \[Johnny\] was so excited to surprise his son, \[Leo\], with the tickets to the playoffs. \[Gene\]'s mother \[Helen\] had to help him with his homework because he was having a test soon. \[Kecia\] and her sister, \[Helen\], frequently bicker. However, they always make up quickly. \[Gene\] asked his brother \[Clyde\] if he would come help him fix his car next weekend. \[Joanne\] took her father \[Johnny\] to his doctor's appointment and afterward her brother \[Clyde\] came over and visited for awhile.

## Question

> What is Kecia’s relationship to Leo?

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
  "state": "[Johnny] was so excited to surprise his son, [Leo], with the tickets to the playoffs. [Gene]'s mother [Helen] had to help him with his homework because he was having a test soon. [Kecia] and her sister, [Helen], frequently bicker. However, they always make up quickly. [Gene] asked his brother [Clyde] if he would come help him fix his car next weekend. [Joanne] took her father [Johnny] to his doctor's appointment and afterward her brother [Clyde] came over and visited for awhile.",
  "question": "What is Kecia’s relationship to Leo?",
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
| Microsoft Decision-1 | aunt | Correct |
| Clef | aunt | Correct |
| Luna Decisions | — | Refusal |
| Clef Flash | aunt | Correct |
| Strands Decider | sister | Incorrect |
| GLiNER2.5 Decide | brother | Incorrect |
| Laya | sister | Incorrect |
| CalDec v1 | mother | Incorrect |

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
    "record": "553",
    "kind": "source_file_record"
  },
  "source_revision": "e5b496941e91abb7c319d2618a3ce96752bc4ab7",
  "input_hash": "4dc580afe080368574ee823037a54a32091a71970a9d5201247fa89683ce6c36"
}
```

</details>
