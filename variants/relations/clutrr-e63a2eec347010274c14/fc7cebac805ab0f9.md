# Evidence order · Reverse the order of sections variant

[Original question](../../../questions/relations/clutrr-e63a2eec347010274c14.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> \[Matthew\] 'uncle, \[Kent\], always took him fishing on summer weekends. \[Kent\] 'son, \[Davis\], aced his math class and made his father proud. \[Laura\] planned a trip to the zoo for her brother, \[Phillip\]. They had a great time. \[Phillip\] bought to dress for his father \[Thomas\] \[Lee\] asked her brother \[Matthew\] if he could babysit. When he said no, she asked her sister \[Laura\] instead.

## Question

> What is Davis’s relationship to Thomas?

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

**Reference answer:** `nephew`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "[Matthew] 'uncle, [Kent], always took him fishing on summer weekends. [Kent] 'son, [Davis], aced his math class and made his father proud. [Laura] planned a trip to the zoo for her brother, [Phillip]. They had a great time. [Phillip] bought to dress for his father [Thomas] [Lee] asked her brother [Matthew] if he could babysit. When he said no, she asked her sister [Laura] instead.",
  "question": "What is Davis’s relationship to Thomas?",
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
| GLiDE v1.2 | `grandson` — grandson | `grandson` — grandson | Same answer |
| Decider v1.1 | `grandson` — grandson | `nephew` — nephew | Different answer |
| Jev | `grandson` — grandson | `nephew` — nephew | Different answer |
| Microsoft Decision-1 | `nephew` — nephew | `nephew` — nephew | Same answer |
| Clef | `nephew` — nephew | `grandson` — grandson | Different answer |
| Luna Decisions | `son` — son | `son` — son | Same answer |
| Clef Flash | `nephew` — nephew | `son` — son | Different answer |
| Strands Decider | `son` — son | `son` — son | Same answer |
| GLiNER2.5 Decide | `father` — father | `father` — father | Same answer |
| Laya | `son` — son | `sister` — sister | Different answer |
| CalDec v1 | `sister` — sister | `sister` — sister | Same answer |

**Ordering comparison:** literal local or custom unit permutation. Only the exact matched comparison sets contribute to the reported ordering contrasts.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `clutrr/e63a2eec347010274c14/presentation_order/reverse_blocks/clean-source_first_clutrr_order_full_0218`

**Input fingerprint:** `acf0bbe7a338dad8583815a1d9ac1766c22506d2b6ac77ba68e92ce76fb8dc11`

| Change | Recorded version |
| --- | --- |
| Evidence order | Reverse the order of sections |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/relations/clutrr-e63a2eec347010274c14.md).
