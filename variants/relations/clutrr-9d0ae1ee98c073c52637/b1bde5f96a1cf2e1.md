# Similar distractors · Add fewer similar but irrelevant items variant

[Original question](../../../questions/relations/clutrr-9d0ae1ee98c073c52637.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> \[Brad\] and his brother \[Floyd\] went to the park to play basketball. \[Roger\] bought Christmas gifts for his brother \[Gregory\] and his sister \[Faye\]. \[Ashley\] asked her mother, \[Mary\], what they were going to have for lunch. \[Charles\] needed to go pick his son \[Anthony\] up a Christmas present. So he asked his daughter \[Ashley\] to help pick something out for \[Anthony\]. \[Floyd\] and his brother, \[Anthony\] run a turtle farm. \[Mary\] went to her brother \[Gregory\]'s birthday party
>
> Velora is the mother of Tisven. Tisven is the brother of Merali.

## Question

> What is Faye’s relationship to Brad?

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
  "state": "[Brad] and his brother [Floyd] went to the park to play basketball. [Roger] bought Christmas gifts for his brother [Gregory] and his sister [Faye]. [Ashley] asked her mother, [Mary], what they were going to have for lunch. [Charles] needed to go pick his son [Anthony] up a Christmas present. So he asked his daughter [Ashley] to help pick something out for [Anthony]. [Floyd] and his brother, [Anthony] run a turtle farm. [Mary] went to her brother [Gregory]'s birthday party\n\nVelora is the mother of Tisven. Tisven is the brother of Merali.",
  "question": "What is Faye’s relationship to Brad?",
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
| Decider v1.1 | `aunt` — aunt | `aunt` — aunt | Same answer |
| Jev | `aunt` — aunt | `sister` — sister | Different answer |
| Microsoft Decision-1 | `aunt` — aunt | `uncle` — uncle | Different answer |
| Clef | `niece` — niece | `niece` — niece | Same answer |
| Luna Decisions | `sister` — sister | `sister` — sister | Same answer |
| Clef Flash | `niece` — niece | `niece` — niece | Same answer |
| Strands Decider | `sister` — sister | `sister` — sister | Same answer |
| GLiNER2.5 Decide | `brother` — brother | `brother` — brother | Same answer |
| Laya | `brother` — brother | `daughter` — daughter | Different answer |
| CalDec v1 | `daughter` — daughter | `daughter` — daughter | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `clutrr/9d0ae1ee98c073c52637/similar_distractors/low/clean-source_first_kinship_distractors_full_0142`

**Input fingerprint:** `26f6d6e3b841f3d4540345f3b286df807c539510f029ad33517f90ba82d3a955`

| Change | Recorded version |
| --- | --- |
| Similar distractors | Add fewer similar but irrelevant items |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/relations/clutrr-9d0ae1ee98c073c52637.md).
