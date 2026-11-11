# Misleading details · Add an unverified claim that conflicts with the evidence variant

[Original question](../../../questions/relations/clutrr-689c776d03722217056d.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> \[Molly\] just celebrated her first wedding anniversary with her husband \[Stanley\]. \[Teresa\] is a woman with a sister named \[Enedina\]. \[Stanley\] loves buying her granddaughter, \[Enedina\], new clothes.
>
> A reader thinks: «Teresa is Molly's daughter.»

## Question

> What is Teresa’s relationship to Molly?

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

**Reference answer:** `granddaughter`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "[Molly] just celebrated her first wedding anniversary with her husband [Stanley]. [Teresa] is a woman with a sister named [Enedina]. [Stanley] loves buying her granddaughter, [Enedina], new clothes.\n\nA reader thinks: «Teresa is Molly's daughter.»",
  "question": "What is Teresa’s relationship to Molly?",
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
| GLiDE v1.2 | `aunt` — aunt | `daughter` — daughter | Different answer |
| Decider v1.1 | `daughter-in-law` — daughter-in-law | `daughter` — daughter | Different answer |
| Jev | `grandmother` — grandmother | `mother` — mother | Different answer |
| Microsoft Decision-1 | `niece` — niece | `niece` — niece | Same answer |
| Clef | `aunt` — aunt | `daughter` — daughter | Different answer |
| Luna Decisions | `sister` — sister | `daughter` — daughter | Different answer |
| Clef Flash | `mother-in-law` — mother-in-law | `daughter-in-law` — daughter-in-law | Different answer |
| Strands Decider | `sister` — sister | `sister` — sister | Same answer |
| GLiNER2.5 Decide | `granddaughter` — granddaughter | `granddaughter` — granddaughter | Same answer |
| Laya | `sister` — sister | `daughter` — daughter | Different answer |
| CalDec v1 | `sister` — sister | `sister` — sister | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `clutrr/689c776d03722217056d/misleading_summary/misleading/clean-source_first_kinship_reader_opinions_full_0104`

**Input fingerprint:** `9b3d8470730dc199574c73286e19b528f9be097cca705ad6c11512844d409978`

| Change | Recorded version |
| --- | --- |
| Misleading details | Add an unverified claim that conflicts with the evidence |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/relations/clutrr-689c776d03722217056d.md).
