# Relations · question 26

[Back to Relations](README.md) · [All capabilities](../README.md)

**Question ID:** `clutrr/ab17eae6f36050b8783e`  
**Source:** [CLUTRR](https://github.com/kliang5/CLUTRR_huggingface_dataset)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/relations/clutrr-ab17eae6f36050b8783e/README.md)

## Context

> \[Annie\] and her sisters \[Lisa\] went to the spa. \[Margaret\], another sister of \[Annie\], had to babysit and could n't join them. \[Jason\] likes to visit his sister. Her name is \[Rosa\]. \[Melissa\] and her sister \[Lisa\] went to the mall. While at the mall \[Melissa\] found the perfect Mother's Day gift for her mother \[Rosa\].

## Question

> What is Jason’s relationship to Margaret?

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
  "state": "[Annie] and her sisters [Lisa] went to the spa. [Margaret], another sister of [Annie], had to babysit and could n't join them. [Jason] likes to visit his sister. Her name is [Rosa]. [Melissa] and her sister [Lisa] went to the mall. While at the mall [Melissa] found the perfect Mother's Day gift for her mother [Rosa].",
  "question": "What is Jason’s relationship to Margaret?",
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
| Decider v1.1 | nephew | Incorrect |
| Jev | brother | Incorrect |
| Microsoft Decision-1 | nephew | Incorrect |
| Clef | nephew | Incorrect |
| Luna Decisions | brother | Incorrect |
| Clef Flash | nephew | Incorrect |
| Strands Decider | sister | Incorrect |
| GLiNER2.5 Decide | sister | Incorrect |
| Laya | mother | Incorrect |
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
    "record": "351",
    "kind": "source_file_record"
  },
  "source_revision": "e5b496941e91abb7c319d2618a3ce96752bc4ab7",
  "input_hash": "402b8056de7a6810e3e726770c9ee65dcf852f576d82d66af51b5cadca69454f"
}
```

</details>
