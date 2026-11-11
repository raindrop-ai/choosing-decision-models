# Relations · question 54

[Back to Relations](README.md) · [All capabilities](../README.md)

**Question ID:** `clutrr/b349dd3ee62af15596e8`  
**Source:** [CLUTRR](https://github.com/kliang5/CLUTRR_huggingface_dataset)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/relations/clutrr-b349dd3ee62af15596e8/README.md)

## Context

> \[Richard\] took his sister \[April\] too the zoo but his sister \[Patricia\] could n't come because she had to work. \[Frank\] helped his daughter \[Beverly\] into her booster seat and sat behind the wheel of the car. His sister \[Patricia\] rode in passenger seat beside him.

## Question

> What is Beverly’s relationship to April?

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

**Reference answer:** niece (`niece`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "[Richard] took his sister [April] too the zoo but his sister [Patricia] could n't come because she had to work. [Frank] helped his daughter [Beverly] into her booster seat and sat behind the wheel of the car. His sister [Patricia] rode in passenger seat beside him.",
  "question": "What is Beverly’s relationship to April?",
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
| Astra | niece | Correct |
| Opus 5.5 | niece | Correct |
| GLiDE v1.2 | niece | Correct |
| Decider v1.1 | niece | Correct |
| Jev | niece | Correct |
| Microsoft Decision-1 | niece | Correct |
| Clef | niece | Correct |
| Luna Decisions | — | Refusal |
| Clef Flash | niece | Correct |
| Strands Decider | daughter | Incorrect |
| GLiNER2.5 Decide | daughter | Incorrect |
| Laya | sister | Incorrect |
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
    "path": "gen_train23_test2to10/test.csv",
    "record": "288",
    "kind": "source_file_record"
  },
  "source_revision": "e5b496941e91abb7c319d2618a3ce96752bc4ab7",
  "input_hash": "26c8c3119ba883587988e27b2d795f9f7a9452d62cedd1594b14625dc59ee2f6"
}
```

</details>
