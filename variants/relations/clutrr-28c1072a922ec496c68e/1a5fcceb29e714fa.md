# Evidence order · Reverse the order of sections variant

[Original question](../../../questions/relations/clutrr-28c1072a922ec496c68e.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> \[Gloria\] and \[Jeff\] are siblings who are enjoying lunch together. \[Gloria\] went to her brother \[Jeff\]'s birthday party \[Jeremy\] and his sister, \[Gloria\] love it when their grandmother visits because she spoils them. She is coming this week to watch them while their parents are out of town. \[Gloria\] went to the store with her sister \[Stephanie\] \[Jason\] took his daughter \[Stephanie\] to the park that afternoon to play.

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
  "state": "[Gloria] and [Jeff] are siblings who are enjoying lunch together. [Gloria] went to her brother [Jeff]'s birthday party [Jeremy] and his sister, [Gloria] love it when their grandmother visits because she spoils them. She is coming this week to watch them while their parents are out of town. [Gloria] went to the store with her sister [Stephanie] [Jason] took his daughter [Stephanie] to the park that afternoon to play.",
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
| Jev | `son` — son | `son` — son | Same answer |
| Microsoft Decision-1 | `nephew` — nephew | `nephew` — nephew | Same answer |
| Clef | `uncle` — uncle | `uncle` — uncle | Same answer |
| Luna Decisions | `brother` — brother | `son` — son | Different answer |
| Clef Flash | `uncle` — uncle | `uncle` — uncle | Same answer |
| Strands Decider | `sister` — sister | `grandmother` — grandmother | Different answer |
| GLiNER2.5 Decide | `grandmother` — grandmother | `grandmother` — grandmother | Same answer |
| Laya | `grandmother` — grandmother | `grandmother` — grandmother | Same answer |
| CalDec v1 | `grandmother` — grandmother | `grandmother` — grandmother | Same answer |

**Ordering comparison:** literal local or custom unit permutation. Only the exact matched comparison sets contribute to the reported ordering contrasts.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `clutrr/28c1072a922ec496c68e/presentation_order/reverse_blocks/clean-source_first_clutrr_order_full_0218`

**Input fingerprint:** `c0deb0630eaf367309f0cbe39064014f88c754578cf38bde597f17026aa2017e`

| Change | Recorded version |
| --- | --- |
| Evidence order | Reverse the order of sections |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/relations/clutrr-28c1072a922ec496c68e.md).
