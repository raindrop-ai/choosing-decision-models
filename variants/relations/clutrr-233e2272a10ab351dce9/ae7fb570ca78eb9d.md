# Misleading details · Add an unverified claim that conflicts with the evidence variant

[Original question](../../../questions/relations/clutrr-233e2272a10ab351dce9.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> \[Christopher\] asked his father \[Jason\] if he could have a video game and he said okay. \[Christopher\] did n't get along very well with his sister \[Dorothy\] for some reason.
>
> A reader thinks: «Dorothy is Jason's granddaughter.»

## Question

> What is Dorothy’s relationship to Jason?

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

**Reference answer:** `daughter`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "[Christopher] asked his father [Jason] if he could have a video game and he said okay. [Christopher] did n't get along very well with his sister [Dorothy] for some reason.\n\nA reader thinks: «Dorothy is Jason's granddaughter.»",
  "question": "What is Dorothy’s relationship to Jason?",
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
| GLiDE v1.2 | `daughter` — daughter | `daughter` — daughter | Same answer |
| Decider v1.1 | `daughter` — daughter | `daughter` — daughter | Same answer |
| Jev | `daughter` — daughter | `daughter` — daughter | Same answer |
| Microsoft Decision-1 | `daughter` — daughter | `daughter` — daughter | Same answer |
| Clef | `daughter` — daughter | `daughter` — daughter | Same answer |
| Luna Decisions | `daughter` — daughter | `granddaughter` — granddaughter | Different answer |
| Clef Flash | `daughter` — daughter | `daughter` — daughter | Same answer |
| Strands Decider | `sister` — sister | `sister` — sister | Same answer |
| GLiNER2.5 Decide | `father` — father | `granddaughter` — granddaughter | Different answer |
| Laya | `sister` — sister | `sister` — sister | Same answer |
| CalDec v1 | `sister` — sister | `sister` — sister | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `clutrr/233e2272a10ab351dce9/misleading_summary/misleading/clean-source_first_kinship_reader_opinions_full_0104`

**Input fingerprint:** `d04659435c25e64b30444018c6e854a964c93c189c2859bd023d2b357abe40c0`

| Change | Recorded version |
| --- | --- |
| Misleading details | Add an unverified claim that conflicts with the evidence |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/relations/clutrr-233e2272a10ab351dce9.md).
