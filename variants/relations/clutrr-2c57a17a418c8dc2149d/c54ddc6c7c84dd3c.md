# Similar distractors · Add more similar but irrelevant items variant

[Original question](../../../questions/relations/clutrr-2c57a17a418c8dc2149d.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> \[Nicole\] loves cooking for her son. His name is \[Frank\] \[Frank\] went to the game with his sister \[Patricia\]. \[Nicole\] and her daughter \[April\] went to see a movie yesterday and then got ice cream afterwards. \[Richard\] took his sister, \[April\], to a baseball game.
>
> Velora is the mother of Tisven. Tisven is the brother of Merali.
>
> Dovren is the father of Kelira. Kelira is the sister of Zunel.
>
> Fenali is the daughter of Porven. Porven is the brother of Nerisa.

## Question

> What is Patricia’s relationship to Richard?

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
  "state": "[Nicole] loves cooking for her son. His name is [Frank] [Frank] went to the game with his sister [Patricia]. [Nicole] and her daughter [April] went to see a movie yesterday and then got ice cream afterwards. [Richard] took his sister, [April], to a baseball game.\n\nVelora is the mother of Tisven. Tisven is the brother of Merali.\n\nDovren is the father of Kelira. Kelira is the sister of Zunel.\n\nFenali is the daughter of Porven. Porven is the brother of Nerisa.",
  "question": "What is Patricia’s relationship to Richard?",
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
| GLiDE v1.2 | `niece` — niece | `sister` — sister | Different answer |
| Decider v1.1 | `niece` — niece | `niece` — niece | Same answer |
| Jev | `sister` — sister | `sister` — sister | Same answer |
| Microsoft Decision-1 | `niece` — niece | `niece` — niece | Same answer |
| Clef | `niece` — niece | `sister` — sister | Different answer |
| Luna Decisions | Refused | Refused | — |
| Clef Flash | `niece` — niece | `niece` — niece | Same answer |
| Strands Decider | `sister` — sister | `sister` — sister | Same answer |
| GLiNER2.5 Decide | `sister` — sister | `sister` — sister | Same answer |
| Laya | `sister` — sister | `sister` — sister | Same answer |
| CalDec v1 | `sister` — sister | `sister` — sister | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `clutrr/2c57a17a418c8dc2149d/similar_distractors/high/clean-source_first_kinship_distractors_full_0142`

**Input fingerprint:** `ba4cd4595b7e0f7ed94660dda8210890204ec24d5aacdfb021e2a5f4044e843e`

| Change | Recorded version |
| --- | --- |
| Similar distractors | Add more similar but irrelevant items |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/relations/clutrr-2c57a17a418c8dc2149d.md).
