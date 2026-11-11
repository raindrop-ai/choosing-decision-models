# Similar distractors · Add fewer similar but irrelevant items variant

[Original question](../../../questions/relations/clutrr-11d1d65191878ec246b5.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> \[Joy\] and her son \[Victor\] traveled around the world \[Kevin\] bought a new dress for his daughter \[Valerie\]. \[Debra\] gave birth to a son named \[Kenneth\]. \[Kerrie\] went to her brother \[Victor\]'s birthday party \[Valerie\] went to her brother \[Brian\]'s birthday party \[Joy\] spent a great day shopping with her daughter, \[Kerrie\]. \[Kerrie\] and her siblings \[Machelle\] and \[Cyrus\] went on a business trip to Asia \[Kenneth\] enjoys going fishing with his brother. His name is \[Brian\]. \[Kevin\] knitted a new sweater for his granddaughter \[Kerrie\].
>
> Velora is the mother of Tisven. Tisven is the brother of Merali.

## Question

> What is Debra’s relationship to Machelle?

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

**Reference answer:** `grandmother`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "[Joy] and her son [Victor] traveled around the world [Kevin] bought a new dress for his daughter [Valerie]. [Debra] gave birth to a son named [Kenneth]. [Kerrie] went to her brother [Victor]'s birthday party [Valerie] went to her brother [Brian]'s birthday party [Joy] spent a great day shopping with her daughter, [Kerrie]. [Kerrie] and her siblings [Machelle] and [Cyrus] went on a business trip to Asia [Kenneth] enjoys going fishing with his brother. His name is [Brian]. [Kevin] knitted a new sweater for his granddaughter [Kerrie].\n\nVelora is the mother of Tisven. Tisven is the brother of Merali.",
  "question": "What is Debra’s relationship to Machelle?",
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
| GLiDE v1.2 | `grandmother` — grandmother | `sister` — sister | Different answer |
| Decider v1.1 | `mother-in-law` — mother-in-law | `aunt` — aunt | Different answer |
| Jev | `mother` — mother | `mother` — mother | Same answer |
| Microsoft Decision-1 | `aunt` — aunt | `aunt` — aunt | Same answer |
| Clef | `aunt` — aunt | `aunt` — aunt | Same answer |
| Luna Decisions | `mother` — mother | `mother` — mother | Same answer |
| Clef Flash | `aunt` — aunt | `aunt` — aunt | Same answer |
| Strands Decider | `sister` — sister | `sister` — sister | Same answer |
| GLiNER2.5 Decide | `granddaughter` — granddaughter | `mother` — mother | Different answer |
| Laya | `son` — son | `mother-in-law` — mother-in-law | Different answer |
| CalDec v1 | `niece` — niece | `daughter` — daughter | Different answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `clutrr/11d1d65191878ec246b5/similar_distractors/low/clean-source_first_kinship_distractors_full_0142`

**Input fingerprint:** `ce05f22438dafd243c1c118dc313b67d5481d517e5f019a96c978774db30462b`

| Change | Recorded version |
| --- | --- |
| Similar distractors | Add fewer similar but irrelevant items |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/relations/clutrr-11d1d65191878ec246b5.md).
