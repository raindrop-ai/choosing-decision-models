# Paraphrasing · Change the sentence structure variant

[Original question](../../../questions/relations/clutrr-076959ca0290ffb07463.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** question instructions.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> \[Connie\] and her husband \[Arnold\] danced together at the party. \[Christine\] asked her brother \[Timothy\] if he could babysit. When he said no, she asked her sister \[Connie\] instead. \[Patricia\] gave birth to a son named \[Timothy\].

## Question

> Which family relationship does Patricia have to Arnold?

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

**Reference answer:** `mother-in-law`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "[Connie] and her husband [Arnold] danced together at the party. [Christine] asked her brother [Timothy] if he could babysit. When he said no, she asked her sister [Connie] instead. [Patricia] gave birth to a son named [Timothy].",
  "question": "Which family relationship does Patricia have to Arnold?",
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
| GLiDE v1.2 | `mother-in-law` — mother-in-law | `mother-in-law` — mother-in-law | Same answer |
| Decider v1.1 | `mother-in-law` — mother-in-law | `mother-in-law` — mother-in-law | Same answer |
| Jev | `mother-in-law` — mother-in-law | `mother-in-law` — mother-in-law | Same answer |
| Microsoft Decision-1 | `mother-in-law` — mother-in-law | `aunt` — aunt | Different answer |
| Clef | `sister` — sister | `sister` — sister | Same answer |
| Luna Decisions | Refused | Refused | — |
| Clef Flash | `sister` — sister | `sister` — sister | Same answer |
| Strands Decider | `sister` — sister | `sister` — sister | Same answer |
| GLiNER2.5 Decide | `son` — son | `son` — son | Same answer |
| Laya | `son` — son | `son` — son | Same answer |
| CalDec v1 | `son` — son | `son` — son | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `clutrr/076959ca0290ffb07463/paraphrasing/structural`

**Input fingerprint:** `9095a5c37840d88e1b9c8ab00051afaea11e3832a864e67dabecc99f495d34d2`

| Change | Recorded version |
| --- | --- |
| Paraphrasing | Change the sentence structure |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/relations/clutrr-076959ca0290ffb07463.md).
