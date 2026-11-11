# Similar distractors · Add fewer similar but irrelevant items variant

[Original question](../../../questions/relations/clutrr-bb8ba459efec2e954c2a.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> \[Alma\] took her son \[Robert\] to the park yesterday. \[Robert\]'s sister \[Vanessa\] was playing at a friends house and did n't get to go.
>
> Velora is the mother of Tisven. Tisven is the brother of Merali.

## Question

> What is Alma’s relationship to Vanessa?

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

**Reference answer:** `mother`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "[Alma] took her son [Robert] to the park yesterday. [Robert]'s sister [Vanessa] was playing at a friends house and did n't get to go.\n\nVelora is the mother of Tisven. Tisven is the brother of Merali.",
  "question": "What is Alma’s relationship to Vanessa?",
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
| GLiDE v1.2 | `mother` — mother | `mother` — mother | Same answer |
| Decider v1.1 | `mother` — mother | `mother` — mother | Same answer |
| Jev | `mother` — mother | `mother` — mother | Same answer |
| Microsoft Decision-1 | `mother` — mother | `mother` — mother | Same answer |
| Clef | `mother` — mother | `mother` — mother | Same answer |
| Luna Decisions | `mother` — mother | `mother` — mother | Same answer |
| Clef Flash | `aunt` — aunt | `aunt` — aunt | Same answer |
| Strands Decider | `nephew` — nephew | `aunt` — aunt | Different answer |
| GLiNER2.5 Decide | `sister` — sister | `sister` — sister | Same answer |
| Laya | `mother` — mother | `mother` — mother | Same answer |
| CalDec v1 | `sister` — sister | `sister` — sister | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `clutrr/bb8ba459efec2e954c2a/similar_distractors/low/clean-source_first_kinship_distractors_full_0142`

**Input fingerprint:** `7a509eb09198d45cc311281dda6e4d7bd9716c82f021b08b9fe3923a39cc43b4`

| Change | Recorded version |
| --- | --- |
| Similar distractors | Add fewer similar but irrelevant items |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/relations/clutrr-bb8ba459efec2e954c2a.md).
