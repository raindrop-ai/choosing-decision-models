# Unrelated examples · No worked example (absence-control recipe) variant

[Original question](../../../questions/relations/clutrr-24c5d84a12a237ca8a34.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> \[Dwight\] was enjoying the delicious meal prepared by his mother \[Gabrielle\]. \[Dwight\] 'daughter \[Deborah\] was a beautiful women. \[Deborah\] also adored her father \[Dwight\]
> The notebook has a blue cloth cover and a stitched binding.

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
  "state": "[Dwight] was enjoying the delicious meal prepared by his mother [Gabrielle]. [Dwight] 'daughter [Deborah] was a beautiful women. [Deborah] also adored her father [Dwight]\nThe notebook has a blue cloth cover and a stitched binding.",
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
| Laya | `daughter` — daughter | `daughter` — daughter | Same answer |
| CalDec v1 | `mother` — mother | `mother` — mother | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `clutrr/24c5d84a12a237ca8a34/examples/absent/clean-source_first_kinship_example_controls_full_0105`

**Input fingerprint:** `4e8dad576093534fa0734e3c4a9a49ca0d80879d8b9356c123534c93c8a73064`

| Change | Recorded version |
| --- | --- |
| Unrelated examples | No worked example (absence-control recipe) |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/relations/clutrr-24c5d84a12a237ca8a34.md).
