# Similar distractors · Add fewer similar but irrelevant items variant

[Original question](../../../questions/relations/clutrr-28c1072a922ec496c68e.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> \[Gloria\] went to the store with her sister \[Stephanie\] \[Jason\] took his daughter \[Stephanie\] to the park that afternoon to play. \[Gloria\] went to her brother \[Jeff\]'s birthday party \[Jeremy\] and his sister, \[Gloria\] love it when their grandmother visits because she spoils them. She is coming this week to watch them while their parents are out of town. \[Gloria\] and \[Jeff\] are siblings who are enjoying lunch together.
>
> Velora is the mother of Tisven. Tisven is the brother of Merali.

## Question

> What is Jeremy’s relationship to Jason?

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

**Reference answer:** `son`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "[Gloria] went to the store with her sister [Stephanie] [Jason] took his daughter [Stephanie] to the park that afternoon to play. [Gloria] went to her brother [Jeff]'s birthday party [Jeremy] and his sister, [Gloria] love it when their grandmother visits because she spoils them. She is coming this week to watch them while their parents are out of town. [Gloria] and [Jeff] are siblings who are enjoying lunch together.\n\nVelora is the mother of Tisven. Tisven is the brother of Merali.",
  "question": "What is Jeremy’s relationship to Jason?",
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
| GLiDE v1.2 | `son` — son | `son` — son | Same answer |
| Decider v1.1 | `son` — son | `son` — son | Same answer |
| Jev | `son` — son | `brother` — brother | Different answer |
| Microsoft Decision-1 | `nephew` — nephew | `nephew` — nephew | Same answer |
| Clef | `uncle` — uncle | `uncle` — uncle | Same answer |
| Luna Decisions | `brother` — brother | Refused | — |
| Clef Flash | `uncle` — uncle | `uncle` — uncle | Same answer |
| Strands Decider | `sister` — sister | `sister` — sister | Same answer |
| GLiNER2.5 Decide | `grandmother` — grandmother | `grandmother` — grandmother | Same answer |
| Laya | `grandmother` — grandmother | `grandmother` — grandmother | Same answer |
| CalDec v1 | `grandmother` — grandmother | `grandmother` — grandmother | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `clutrr/28c1072a922ec496c68e/similar_distractors/low/clean-source_first_kinship_distractors_full_0142`

**Input fingerprint:** `096777eb27bca7f063ef40029a4600984ffea46ab8b71230d4b43292c84ee7a7`

| Change | Recorded version |
| --- | --- |
| Similar distractors | Add fewer similar but irrelevant items |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/relations/clutrr-28c1072a922ec496c68e.md).
