# Paraphrasing · Change individual words and phrases variant

[Original question](../../../questions/relations/clutrr-282edc4d20a524990d65.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** question instructions.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> \[Richard\] was thrilled his brother, \[Oscar\], was able to make it to the party. \[Joel\] invited his father \[Daniel\] and his brother \[Oscar\] to go on a weekend fishing trip. \[Roger\] was so pleased to spend time with his nephew, \[Richard\]. \[Julie\] and her brother \[Daniel\] went to see a movie. \[Jamie\] has not seen her brother, \[Roger\] in over a year. She wants to take her son, \[Joel\] to meet him. \[Julie\] and her sister, \[Faye\], frequently bicker. However, they always make up quickly.

## Question

> How is Joel related to Faye?

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

**Reference answer:** `nephew`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "[Richard] was thrilled his brother, [Oscar], was able to make it to the party. [Joel] invited his father [Daniel] and his brother [Oscar] to go on a weekend fishing trip. [Roger] was so pleased to spend time with his nephew, [Richard]. [Julie] and her brother [Daniel] went to see a movie. [Jamie] has not seen her brother, [Roger] in over a year. She wants to take her son, [Joel] to meet him. [Julie] and her sister, [Faye], frequently bicker. However, they always make up quickly.",
  "question": "How is Joel related to Faye?",
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
| GLiDE v1.2 | `nephew` — nephew | `nephew` — nephew | Same answer |
| Decider v1.1 | `grandson` — grandson | `nephew` — nephew | Different answer |
| Jev | `nephew` — nephew | `nephew` — nephew | Same answer |
| Microsoft Decision-1 | `nephew` — nephew | `nephew` — nephew | Same answer |
| Clef | `nephew` — nephew | `nephew` — nephew | Same answer |
| Luna Decisions | `nephew` — nephew | `nephew` — nephew | Same answer |
| Clef Flash | `uncle` — uncle | `nephew` — nephew | Different answer |
| Strands Decider | `son` — son | `son` — son | Same answer |
| GLiNER2.5 Decide | `brother` — brother | `brother` — brother | Same answer |
| Laya | `sister` — sister | `sister` — sister | Same answer |
| CalDec v1 | `sister` — sister | `sister` — sister | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `clutrr/282edc4d20a524990d65/paraphrasing/surface`

**Input fingerprint:** `857c04073aca138fc3e77eb149ff18a68f4d025ba703401ad5e1bb7a1b052ba7`

| Change | Recorded version |
| --- | --- |
| Paraphrasing | Change individual words and phrases |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/relations/clutrr-282edc4d20a524990d65.md).
