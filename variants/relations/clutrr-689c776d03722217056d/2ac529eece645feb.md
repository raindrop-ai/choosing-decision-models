# Paraphrasing · Change the sentence structure variant

[Original question](../../../questions/relations/clutrr-689c776d03722217056d.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** question instructions.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> \[Molly\] just celebrated her first wedding anniversary with her husband \[Stanley\]. \[Teresa\] is a woman with a sister named \[Enedina\]. \[Stanley\] loves buying her granddaughter, \[Enedina\], new clothes.

## Question

> Which family relationship does Teresa have to Molly?

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
  "state": "[Molly] just celebrated her first wedding anniversary with her husband [Stanley]. [Teresa] is a woman with a sister named [Enedina]. [Stanley] loves buying her granddaughter, [Enedina], new clothes.",
  "question": "Which family relationship does Teresa have to Molly?",
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
| GLiDE v1.2 | `aunt` — aunt | `aunt` — aunt | Same answer |
| Decider v1.1 | `daughter-in-law` — daughter-in-law | `niece` — niece | Different answer |
| Jev | `grandmother` — grandmother | `grandmother` — grandmother | Same answer |
| Microsoft Decision-1 | `niece` — niece | `niece` — niece | Same answer |
| Clef | `aunt` — aunt | `mother-in-law` — mother-in-law | Different answer |
| Luna Decisions | `sister` — sister | `sister` — sister | Same answer |
| Clef Flash | `mother-in-law` — mother-in-law | `mother-in-law` — mother-in-law | Same answer |
| Strands Decider | `sister` — sister | `sister` — sister | Same answer |
| GLiNER2.5 Decide | `granddaughter` — granddaughter | `granddaughter` — granddaughter | Same answer |
| Laya | `sister` — sister | `sister` — sister | Same answer |
| CalDec v1 | `sister` — sister | `sister` — sister | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `clutrr/689c776d03722217056d/paraphrasing/structural`

**Input fingerprint:** `7cbabfb5c01685d28e4f4620da8e9d8a5e8f29564b33790c99ea828cdaf97ec8`

| Change | Recorded version |
| --- | --- |
| Paraphrasing | Change the sentence structure |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/relations/clutrr-689c776d03722217056d.md).
