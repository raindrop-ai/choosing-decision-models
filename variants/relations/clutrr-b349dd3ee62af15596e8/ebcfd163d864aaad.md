# Irrelevant details · Add a larger amount of irrelevant detail variant

[Original question](../../../questions/relations/clutrr-b349dd3ee62af15596e8.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> \[Richard\] took his sister \[April\] too the zoo but his sister \[Patricia\] could n't come because she had to work. \[Frank\] helped his daughter \[Beverly\] into her booster seat and sat behind the wheel of the car. His sister \[Patricia\] rode in passenger seat beside him.
> The car dashboard was black.
> The steering wheel had a textured rim.
> The door handle was metal.
> The floor mat was rubber.
> The window glass was clear.
> The seat covers were fabric.

## Question

> What is Beverly’s relationship to April?

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

**Reference answer:** `niece`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "[Richard] took his sister [April] too the zoo but his sister [Patricia] could n't come because she had to work. [Frank] helped his daughter [Beverly] into her booster seat and sat behind the wheel of the car. His sister [Patricia] rode in passenger seat beside him.\nThe car dashboard was black.\nThe steering wheel had a textured rim.\nThe door handle was metal.\nThe floor mat was rubber.\nThe window glass was clear.\nThe seat covers were fabric.",
  "question": "What is Beverly’s relationship to April?",
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
| GLiDE v1.2 | `niece` — niece | `niece` — niece | Same answer |
| Decider v1.1 | `niece` — niece | `niece` — niece | Same answer |
| Jev | `niece` — niece | `niece` — niece | Same answer |
| Microsoft Decision-1 | `niece` — niece | `niece` — niece | Same answer |
| Clef | `niece` — niece | `niece` — niece | Same answer |
| Luna Decisions | Refused | Refused | — |
| Clef Flash | `niece` — niece | `niece` — niece | Same answer |
| Strands Decider | `daughter` — daughter | `daughter` — daughter | Same answer |
| GLiNER2.5 Decide | `daughter` — daughter | `sister` — sister | Different answer |
| Laya | `sister` — sister | `daughter` — daughter | Different answer |
| CalDec v1 | `sister` — sister | `daughter` — daughter | Different answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `clutrr/b349dd3ee62af15596e8/irrelevant_details/high/clean-remaining_kinship_details_full_0021`

**Input fingerprint:** `2b3cbdb3c162f8dc66b9cd76bdf05d38cb518b93094ad5ea2e996838dff4d749`

| Change | Recorded version |
| --- | --- |
| Irrelevant details | Add a larger amount of irrelevant detail |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/relations/clutrr-b349dd3ee62af15596e8.md).
