# Irrelevant details · Add a small amount of irrelevant detail variant

[Original question](../../../questions/relations/clutrr-3c137fa09a5fd06f07e0.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> \[Alan\] made his son \[Emmanuel\] mow the lawn. \[Emmanuel\]'s sister \[Eunice\] tanned in the yard instead. \[Annie\]'s father \[Alan\] is taking her to a movie because she got good grades.
> The yard gate was wooden.

## Question

> What is Annie’s relationship to Eunice?

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
  "state": "[Alan] made his son [Emmanuel] mow the lawn. [Emmanuel]'s sister [Eunice] tanned in the yard instead. [Annie]'s father [Alan] is taking her to a movie because she got good grades.\nThe yard gate was wooden.",
  "question": "What is Annie’s relationship to Eunice?",
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
| Jev | `sister` — sister | `sister` — sister | Same answer |
| Microsoft Decision-1 | `niece` — niece | `niece` — niece | Same answer |
| Clef | `niece` — niece | `niece` — niece | Same answer |
| Luna Decisions | `sister` — sister | `sister` — sister | Same answer |
| Clef Flash | `niece` — niece | `niece` — niece | Same answer |
| Strands Decider | `niece` — niece | `sister` — sister | Different answer |
| GLiNER2.5 Decide | `father` — father | `father` — father | Same answer |
| Laya | `sister` — sister | `sister` — sister | Same answer |
| CalDec v1 | `sister` — sister | `sister` — sister | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `clutrr/3c137fa09a5fd06f07e0/irrelevant_details/low/clean-remaining_kinship_details_full_0021`

**Input fingerprint:** `78691b06ff5ea729acba78af3ffb412ad46e5b0fa4dfdf56b0c000a00a3817d1`

| Change | Recorded version |
| --- | --- |
| Irrelevant details | Add a small amount of irrelevant detail |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/relations/clutrr-3c137fa09a5fd06f07e0.md).
