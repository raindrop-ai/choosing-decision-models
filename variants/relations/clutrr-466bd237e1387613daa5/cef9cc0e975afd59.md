# Irrelevant details · Add a larger amount of irrelevant detail variant

[Original question](../../../questions/relations/clutrr-466bd237e1387613daa5.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> \[Jeff\] and his sister, \[Stephanie\], went to a sneak preview of the Avengers movie and loved it. \[Ruth\] and her brother \[Christian\] walked to the park. \[Ruth\]'s son \[Jeremy\] joined them later on. \[Ruth\] likes taking her son \[Jeremy\] to baseball practice. She also likes taking her son \[Jeff\] to soccer practice.
> The park bench had wooden slats.
> The path was gravel.
> The fence was green.
> The sign panel was aluminum.
> The picnic table was rectangular.
> The lamp post was black.

## Question

> What is Stephanie’s relationship to Christian?

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
  "state": "[Jeff] and his sister, [Stephanie], went to a sneak preview of the Avengers movie and loved it. [Ruth] and her brother [Christian] walked to the park. [Ruth]'s son [Jeremy] joined them later on. [Ruth] likes taking her son [Jeremy] to baseball practice. She also likes taking her son [Jeff] to soccer practice.\nThe park bench had wooden slats.\nThe path was gravel.\nThe fence was green.\nThe sign panel was aluminum.\nThe picnic table was rectangular.\nThe lamp post was black.",
  "question": "What is Stephanie’s relationship to Christian?",
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
| Jev | `sister` — sister | `sister` — sister | Same answer |
| Microsoft Decision-1 | `aunt` — aunt | `aunt` — aunt | Same answer |
| Clef | `niece` — niece | `niece` — niece | Same answer |
| Luna Decisions | `sister` — sister | `sister` — sister | Same answer |
| Clef Flash | `aunt` — aunt | `aunt` — aunt | Same answer |
| Strands Decider | `sister` — sister | `sister` — sister | Same answer |
| GLiNER2.5 Decide | `brother` — brother | `brother` — brother | Same answer |
| Laya | `son` — son | `sister` — sister | Different answer |
| CalDec v1 | `son` — son | `son` — son | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `clutrr/466bd237e1387613daa5/irrelevant_details/high/clean-remaining_kinship_details_full_0021`

**Input fingerprint:** `15f4c0091e2f75e2f84b1084adb93c319ac9fc36f5562b1053135d9f81432159`

| Change | Recorded version |
| --- | --- |
| Irrelevant details | Add a larger amount of irrelevant detail |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/relations/clutrr-466bd237e1387613daa5.md).
