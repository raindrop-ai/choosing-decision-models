# Option order · Move the first answer choice to the end variant

[Original question](../../../questions/relations/clutrr-b349dd3ee62af15596e8.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** answer choices or their order.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> \[Richard\] took his sister \[April\] too the zoo but his sister \[Patricia\] could n't come because she had to work. \[Frank\] helped his daughter \[Beverly\] into her booster seat and sat behind the wheel of the car. His sister \[Patricia\] rode in passenger seat beside him.

## Question

> What is Beverly’s relationship to April?

## Answer choices

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
- **aunt.** aunt

**Reference answer:** `niece`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "[Richard] took his sister [April] too the zoo but his sister [Patricia] could n't come because she had to work. [Frank] helped his daughter [Beverly] into her booster seat and sat behind the wheel of the car. His sister [Patricia] rode in passenger seat beside him.",
  "question": "What is Beverly’s relationship to April?",
  "choices": {
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
    "uncle": "uncle",
    "aunt": "aunt"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `niece` — niece | `niece` — niece | Same answer |
| Decider v1.1 | `niece` — niece | `niece` — niece | Same answer |
| Jev | `niece` — niece | `niece` — niece | Same answer |
| Microsoft Decision-1 | `niece` — niece | `niece` — niece | Same answer |
| Clef | `niece` — niece | `niece` — niece | Same answer |
| Luna Decisions | Refused | Refused | — |
| Clef Flash | `niece` — niece | `niece` — niece | Same answer |
| Strands Decider | `daughter` — daughter | `daughter` — daughter | Same answer |
| GLiNER2.5 Decide | `daughter` — daughter | `daughter` — daughter | Same answer |
| Laya | `sister` — sister | `sister` — sister | Same answer |
| CalDec v1 | `sister` — sister | `sister` — sister | Same answer |

Clef and Clef Flash sort answer choices in their published input-processing code. Their choice-order results describe that preprocessing.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `clutrr/b349dd3ee62af15596e8/option_order/rotate_1`

**Input fingerprint:** `15f1207cb4603acbb95fa5e591bbfd416519eb2bb6d47e1221ee973056485f9d`

| Change | Recorded version |
| --- | --- |
| Option order | Move the first answer choice to the end |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/relations/clutrr-b349dd3ee62af15596e8.md).
