# Option order · Move the first answer choice to the end variant

[Original question](../../../questions/relations/clutrr-522aec94c070e77f1132.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** answer choices or their order.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> \[Patricia\] took her son \[Timothy\] to school because he missed the bus. \[Patricia\] dropped her son, \[Timothy\], off for soccer practice. Afterwards she went home to make a cake for her daughter, \[Christina\]. \[Christina\] took her sister, \[Connie\], out to dinner for her birthday.

## Question

> What is Patricia’s relationship to Connie?

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

**Reference answer:** `mother`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "[Patricia] took her son [Timothy] to school because he missed the bus. [Patricia] dropped her son, [Timothy], off for soccer practice. Afterwards she went home to make a cake for her daughter, [Christina]. [Christina] took her sister, [Connie], out to dinner for her birthday.",
  "question": "What is Patricia’s relationship to Connie?",
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
| GLiDE v1.2 | `mother` — mother | `mother` — mother | Same answer |
| Decider v1.1 | `mother` — mother | `mother` — mother | Same answer |
| Jev | `mother` — mother | `mother` — mother | Same answer |
| Microsoft Decision-1 | `aunt` — aunt | `aunt` — aunt | Same answer |
| Clef | `aunt` — aunt | `aunt` — aunt | Same answer |
| Luna Decisions | `mother` — mother | `mother` — mother | Same answer |
| Clef Flash | `aunt` — aunt | `aunt` — aunt | Same answer |
| Strands Decider | `mother` — mother | `mother` — mother | Same answer |
| GLiNER2.5 Decide | `sister` — sister | `sister` — sister | Same answer |
| Laya | `sister` — sister | `sister` — sister | Same answer |
| CalDec v1 | `sister` — sister | `sister` — sister | Same answer |

Clef and Clef Flash sort answer choices in their published input-processing code. Their choice-order results describe that preprocessing.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `clutrr/522aec94c070e77f1132/option_order/rotate_1`

**Input fingerprint:** `7ecb008ca4dcf8cae1f78ce56189b71543da6f088d05c8de7aa0aa373fde3473`

| Change | Recorded version |
| --- | --- |
| Option order | Move the first answer choice to the end |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/relations/clutrr-522aec94c070e77f1132.md).
