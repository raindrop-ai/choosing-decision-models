# Misleading details · Add an unverified claim that conflicts with the evidence variant

[Original question](../../../questions/relations/clutrr-8e6c57910631826de276.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> \[April\] went to the mall, because she wanted to look for a present for her daughter, \[Melba\]. \[Melba\] went to the store with her sister \[Sharon\] \[Melba\] asked her mother, \[April\], what they were going to have for lunch. \[Sharon\] and her sister, \[Toni\], frequently bicker. However, they always make up quickly.
>
> A reader thinks: «Melba is Toni's aunt.»

## Question

> What is Melba’s relationship to Toni?

## Answer choices

- **aunt.** aunt
- **brother.** brother
- **daughter.** daughter
- **daughter-in-law.** daughter-in-law
- **father.** father
- **father-in-law.** father-in-law
- **granddaughter.** granddaughter
- **grandfather.** grandfather
- **grandmother.** grandmother
- **grandson.** grandson
- **mother.** mother
- **mother-in-law.** mother-in-law
- **nephew.** nephew
- **niece.** niece
- **sister.** sister
- **son.** son
- **son-in-law.** son-in-law
- **uncle.** uncle

**Reference answer:** `sister`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "[April] went to the mall, because she wanted to look for a present for her daughter, [Melba]. [Melba] went to the store with her sister [Sharon] [Melba] asked her mother, [April], what they were going to have for lunch. [Sharon] and her sister, [Toni], frequently bicker. However, they always make up quickly.\n\nA reader thinks: «Melba is Toni's aunt.»",
  "question": "What is Melba’s relationship to Toni?",
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

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `sister` — sister | `sister` — sister | Same answer |
| Decider v1.1 | `sister` — sister | `sister` — sister | Same answer |
| Jev | `sister` — sister | `niece` — niece | Different answer |
| Microsoft Decision-1 | `sister` — sister | `sister` — sister | Same answer |
| Clef | `niece` — niece | `aunt` — aunt | Different answer |
| Luna Decisions | `sister` — sister | `sister` — sister | Same answer |
| Clef Flash | `niece` — niece | `sister` — sister | Different answer |
| Strands Decider | `sister` — sister | `niece` — niece | Different answer |
| GLiNER2.5 Decide | `sister` — sister | `aunt` — aunt | Different answer |
| Laya | `sister` — sister | `aunt` — aunt | Different answer |
| CalDec v1 | `sister` — sister | `aunt` — aunt | Different answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `clutrr/8e6c57910631826de276/misleading_summary/misleading/clean-source_first_kinship_reader_opinions_full_0104`

**Input fingerprint:** `9af2a24562700dcb240a329e7d79f2651e0046f9edb66ecf65467100a830058b`

| Change | Recorded version |
| --- | --- |
| Misleading details | Add an unverified claim that conflicts with the evidence |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/relations/clutrr-8e6c57910631826de276.md).
