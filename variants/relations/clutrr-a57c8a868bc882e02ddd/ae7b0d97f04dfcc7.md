# Misleading details · Add an unverified claim that conflicts with the evidence variant

[Original question](../../../questions/relations/clutrr-a57c8a868bc882e02ddd.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> \[Jonathan\] was so happy for his brother, \[Jason\], getting a promotion. \[Jonathan\] was trying to find his daughter, \[Diana\], but she was no where to be seen in the house. It turns out she was shopping with her sister, \[Traci\], at the time. \[Christian\] bought Christmas gifts for his brother \[Jason\] and his sister \[Rosa\].
>
> A reader thinks: «Rosa is Traci's niece.»

## Question

> What is Rosa’s relationship to Traci?

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

**Reference answer:** `aunt`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "[Jonathan] was so happy for his brother, [Jason], getting a promotion. [Jonathan] was trying to find his daughter, [Diana], but she was no where to be seen in the house. It turns out she was shopping with her sister, [Traci], at the time. [Christian] bought Christmas gifts for his brother [Jason] and his sister [Rosa].\n\nA reader thinks: «Rosa is Traci's niece.»",
  "question": "What is Rosa’s relationship to Traci?",
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
| GLiDE v1.2 | `aunt` — aunt | `niece` — niece | Different answer |
| Decider v1.1 | `aunt` — aunt | `aunt` — aunt | Same answer |
| Jev | `aunt` — aunt | `niece` — niece | Different answer |
| Microsoft Decision-1 | `sister` — sister | `sister` — sister | Same answer |
| Clef | `niece` — niece | `sister` — sister | Different answer |
| Luna Decisions | `sister` — sister | `niece` — niece | Different answer |
| Clef Flash | `sister` — sister | `niece` — niece | Different answer |
| Strands Decider | `sister` — sister | `sister` — sister | Same answer |
| GLiNER2.5 Decide | `brother` — brother | `niece` — niece | Different answer |
| Laya | `sister` — sister | `sister` — sister | Same answer |
| CalDec v1 | `sister` — sister | `sister` — sister | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `clutrr/a57c8a868bc882e02ddd/misleading_summary/misleading/clean-source_first_kinship_reader_opinions_full_0104`

**Input fingerprint:** `3ce891320938df5498e1f3dc218a3fe9d2170897a31b9bc4763027f98d056740`

| Change | Recorded version |
| --- | --- |
| Misleading details | Add an unverified claim that conflicts with the evidence |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/relations/clutrr-a57c8a868bc882e02ddd.md).
