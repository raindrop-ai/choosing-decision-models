# Option order · Reverse the answer choices variant

[Original question](../../../questions/relations/clutrr-be029c3d593c44c5bf1b.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** answer choices or their order.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> \[William\] took his sister \[Sheila\] out to lunch after learning that she got accepted into her first choice for university. \[Seth\] and his daughter \[Ruth\] took a day off school to go to the zoo. \[Jonathan\] took his sister \[Ruth\] out to lunch after learning that she got accepted into her first choice for university. \[Jonathan\] is proud that his daughter is such a good student. Her name is \[Diana\]. \[Sheila\], who is the sister of \[Diana\], is a lovely girl.

## Question

> What is William’s relationship to Seth?

## Answer choices

- **uncle.** uncle
- **son-in-law.** son-in-law
- **son.** son
- **sister.** sister
- **niece.** niece
- **nephew.** nephew
- **mother-in-law.** mother-in-law
- **mother.** mother
- **grandson.** grandson
- **grandmother.** grandmother
- **grandfather.** grandfather
- **granddaughter.** granddaughter
- **father-in-law.** father-in-law
- **father.** father
- **daughter-in-law.** daughter-in-law
- **daughter.** daughter
- **brother.** brother
- **aunt.** aunt

**Reference answer:** `grandson`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "[William] took his sister [Sheila] out to lunch after learning that she got accepted into her first choice for university. [Seth] and his daughter [Ruth] took a day off school to go to the zoo. [Jonathan] took his sister [Ruth] out to lunch after learning that she got accepted into her first choice for university. [Jonathan] is proud that his daughter is such a good student. Her name is [Diana]. [Sheila], who is the sister of [Diana], is a lovely girl.",
  "question": "What is William’s relationship to Seth?",
  "choices": {
    "uncle": "uncle",
    "son-in-law": "son-in-law",
    "son": "son",
    "sister": "sister",
    "niece": "niece",
    "nephew": "nephew",
    "mother-in-law": "mother-in-law",
    "mother": "mother",
    "grandson": "grandson",
    "grandmother": "grandmother",
    "grandfather": "grandfather",
    "granddaughter": "granddaughter",
    "father-in-law": "father-in-law",
    "father": "father",
    "daughter-in-law": "daughter-in-law",
    "daughter": "daughter",
    "brother": "brother",
    "aunt": "aunt"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `son-in-law` — son-in-law | `son-in-law` — son-in-law | Same answer |
| Decider v1.1 | `son-in-law` — son-in-law | `son-in-law` — son-in-law | Same answer |
| Jev | `brother` — brother | `brother` — brother | Same answer |
| Microsoft Decision-1 | `uncle` — uncle | `uncle` — uncle | Same answer |
| Clef | `uncle` — uncle | `uncle` — uncle | Same answer |
| Luna Decisions | `brother` — brother | `nephew` — nephew | Different answer |
| Clef Flash | `uncle` — uncle | `uncle` — uncle | Same answer |
| Strands Decider | `sister` — sister | `aunt` — aunt | Different answer |
| GLiNER2.5 Decide | `sister` — sister | `sister` — sister | Same answer |
| Laya | `sister` — sister | `sister` — sister | Same answer |
| CalDec v1 | `sister` — sister | `sister` — sister | Same answer |

Clef and Clef Flash sort answer choices in their published input-processing code. Their choice-order results describe that preprocessing.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `clutrr/be029c3d593c44c5bf1b/option_order/reverse`

**Input fingerprint:** `2947742ec5f95222bd29d24956f11860a3f25594e0bcd4b743fc679b3e777bd4`

| Change | Recorded version |
| --- | --- |
| Option order | Reverse the answer choices |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/relations/clutrr-be029c3d593c44c5bf1b.md).
