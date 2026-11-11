# Option order · Move the first answer choice to the end variant

[Original question](../../../questions/relations/clutrr-076959ca0290ffb07463.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** answer choices or their order.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> \[Connie\] and her husband \[Arnold\] danced together at the party. \[Christine\] asked her brother \[Timothy\] if he could babysit. When he said no, she asked her sister \[Connie\] instead. \[Patricia\] gave birth to a son named \[Timothy\].

## Question

> What is Patricia’s relationship to Arnold?

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

**Reference answer:** `mother-in-law`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "[Connie] and her husband [Arnold] danced together at the party. [Christine] asked her brother [Timothy] if he could babysit. When he said no, she asked her sister [Connie] instead. [Patricia] gave birth to a son named [Timothy].",
  "question": "What is Patricia’s relationship to Arnold?",
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
| GLiDE v1.2 | `mother-in-law` — mother-in-law | `mother-in-law` — mother-in-law | Same answer |
| Decider v1.1 | `mother-in-law` — mother-in-law | `mother-in-law` — mother-in-law | Same answer |
| Jev | `mother-in-law` — mother-in-law | `mother-in-law` — mother-in-law | Same answer |
| Microsoft Decision-1 | `mother-in-law` — mother-in-law | `mother-in-law` — mother-in-law | Same answer |
| Clef | `sister` — sister | `sister` — sister | Same answer |
| Luna Decisions | Refused | Refused | — |
| Clef Flash | `sister` — sister | `sister` — sister | Same answer |
| Strands Decider | `sister` — sister | `sister` — sister | Same answer |
| GLiNER2.5 Decide | `son` — son | `son` — son | Same answer |
| Laya | `son` — son | `son` — son | Same answer |
| CalDec v1 | `son` — son | `son` — son | Same answer |

Clef and Clef Flash sort answer choices in their published input-processing code. Their choice-order results describe that preprocessing.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `clutrr/076959ca0290ffb07463/option_order/rotate_1`

**Input fingerprint:** `0d524678c021f19a8655bd3faf4ec8b9c9001882b6d72d19e5314edbbcab7e10`

| Change | Recorded version |
| --- | --- |
| Option order | Move the first answer choice to the end |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/relations/clutrr-076959ca0290ffb07463.md).
