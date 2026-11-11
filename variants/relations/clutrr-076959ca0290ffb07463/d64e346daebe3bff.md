# Evidence order · Reverse the order of sections variant

[Original question](../../../questions/relations/clutrr-076959ca0290ffb07463.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> \[Patricia\] gave birth to a son named \[Timothy\]. \[Christine\] asked her brother \[Timothy\] if he could babysit. When he said no, she asked her sister \[Connie\] instead. \[Connie\] and her husband \[Arnold\] danced together at the party.

## Question

> What is Patricia’s relationship to Arnold?

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

**Reference answer:** `mother-in-law`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "[Patricia] gave birth to a son named [Timothy]. [Christine] asked her brother [Timothy] if he could babysit. When he said no, she asked her sister [Connie] instead. [Connie] and her husband [Arnold] danced together at the party.",
  "question": "What is Patricia’s relationship to Arnold?",
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
| GLiDE v1.2 | `mother-in-law` — mother-in-law | `mother-in-law` — mother-in-law | Same answer |
| Decider v1.1 | `mother-in-law` — mother-in-law | `mother-in-law` — mother-in-law | Same answer |
| Jev | `mother-in-law` — mother-in-law | `mother-in-law` — mother-in-law | Same answer |
| Microsoft Decision-1 | `mother-in-law` — mother-in-law | `aunt` — aunt | Different answer |
| Clef | `sister` — sister | `aunt` — aunt | Different answer |
| Luna Decisions | Refused | `mother-in-law` — mother-in-law | — |
| Clef Flash | `sister` — sister | `aunt` — aunt | Different answer |
| Strands Decider | `sister` — sister | `sister` — sister | Same answer |
| GLiNER2.5 Decide | `son` — son | `sister` — sister | Different answer |
| Laya | `son` — son | `son` — son | Same answer |
| CalDec v1 | `son` — son | `son` — son | Same answer |

**Ordering comparison:** literal local or custom unit permutation. Only the exact matched comparison sets contribute to the reported ordering contrasts.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `clutrr/076959ca0290ffb07463/presentation_order/reverse_blocks/clean-source_first_clutrr_order_full_0218`

**Input fingerprint:** `fbf3d7bf3499b38b2fd8dd4ccb55aaf3ac677434abccb84201004cac7af1fed2`

| Change | Recorded version |
| --- | --- |
| Evidence order | Reverse the order of sections |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/relations/clutrr-076959ca0290ffb07463.md).
