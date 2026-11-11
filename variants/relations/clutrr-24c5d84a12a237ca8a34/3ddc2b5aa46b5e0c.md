# Irrelevant details · Add a larger amount of irrelevant detail variant

[Original question](../../../questions/relations/clutrr-24c5d84a12a237ca8a34.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> \[Dwight\] was enjoying the delicious meal prepared by his mother \[Gabrielle\]. \[Dwight\] 'daughter \[Deborah\] was a beautiful women. \[Deborah\] also adored her father \[Dwight\]
> The dinner plates were white.
> The cups were blue.
> The table top was wooden.
> The tablecloth was patterned.
> The curtains were green.
> The serving tray was oval.

## Question

> What is Gabrielle’s relationship to Deborah?

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

**Reference answer:** `grandmother`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "[Dwight] was enjoying the delicious meal prepared by his mother [Gabrielle]. [Dwight] 'daughter [Deborah] was a beautiful women. [Deborah] also adored her father [Dwight]\nThe dinner plates were white.\nThe cups were blue.\nThe table top was wooden.\nThe tablecloth was patterned.\nThe curtains were green.\nThe serving tray was oval.",
  "question": "What is Gabrielle’s relationship to Deborah?",
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
| GLiDE v1.2 | `grandmother` — grandmother | `grandmother` — grandmother | Same answer |
| Decider v1.1 | `mother` — mother | `grandmother` — grandmother | Different answer |
| Jev | `grandmother` — grandmother | `grandmother` — grandmother | Same answer |
| Microsoft Decision-1 | `grandmother` — grandmother | `grandmother` — grandmother | Same answer |
| Clef | `mother` — mother | `mother` — mother | Same answer |
| Luna Decisions | `mother` — mother | `mother` — mother | Same answer |
| Clef Flash | `mother` — mother | `grandmother` — grandmother | Different answer |
| Strands Decider | `mother` — mother | `mother` — mother | Same answer |
| GLiNER2.5 Decide | `father` — father | `daughter` — daughter | Different answer |
| Laya | `daughter` — daughter | `mother` — mother | Different answer |
| CalDec v1 | `mother` — mother | `mother` — mother | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `clutrr/24c5d84a12a237ca8a34/irrelevant_details/high/clean-remaining_kinship_details_full_0021`

**Input fingerprint:** `28a8b825a0e68700f0168d15861731bb45892cb68a79b228ef5fe76401a6969c`

| Change | Recorded version |
| --- | --- |
| Irrelevant details | Add a larger amount of irrelevant detail |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/relations/clutrr-24c5d84a12a237ca8a34.md).
