# Evidence order · Reverse the order of sections variant

[Original question](../../../questions/relations/clutrr-8e6c57910631826de276.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> \[Sharon\] and her sister, \[Toni\], frequently bicker. However, they always make up quickly. \[Melba\] went to the store with her sister \[Sharon\] \[Melba\] asked her mother, \[April\], what they were going to have for lunch. \[April\] went to the mall, because she wanted to look for a present for her daughter, \[Melba\].

## Question

> What is Melba’s relationship to Toni?

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

**Reference answer:** `sister`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "[Sharon] and her sister, [Toni], frequently bicker. However, they always make up quickly. [Melba] went to the store with her sister [Sharon] [Melba] asked her mother, [April], what they were going to have for lunch. [April] went to the mall, because she wanted to look for a present for her daughter, [Melba].",
  "question": "What is Melba’s relationship to Toni?",
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
| GLiDE v1.2 | `sister` — sister | `sister` — sister | Same answer |
| Decider v1.1 | `sister` — sister | `sister` — sister | Same answer |
| Jev | `sister` — sister | `niece` — niece | Different answer |
| Microsoft Decision-1 | `sister` — sister | `sister` — sister | Same answer |
| Clef | `niece` — niece | `niece` — niece | Same answer |
| Luna Decisions | `sister` — sister | `sister` — sister | Same answer |
| Clef Flash | `niece` — niece | `niece` — niece | Same answer |
| Strands Decider | `sister` — sister | `daughter` — daughter | Different answer |
| GLiNER2.5 Decide | `sister` — sister | `sister` — sister | Same answer |
| Laya | `sister` — sister | `sister` — sister | Same answer |
| CalDec v1 | `sister` — sister | `sister` — sister | Same answer |

**Ordering comparison:** literal local or custom unit permutation. Only the exact matched comparison sets contribute to the reported ordering contrasts.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `clutrr/8e6c57910631826de276/presentation_order/reverse_blocks/clean-source_first_clutrr_order_full_0218`

**Input fingerprint:** `e840c5320b2101f17a5397624bf4a1d0e49ea532dbde1d6c9c435186c17bbe63`

| Change | Recorded version |
| --- | --- |
| Evidence order | Reverse the order of sections |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/relations/clutrr-8e6c57910631826de276.md).
