# Unrelated examples · No worked example (absence-control recipe) variant

[Original question](../../../questions/relations/clutrr-689c776d03722217056d.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> \[Molly\] just celebrated her first wedding anniversary with her husband \[Stanley\]. \[Teresa\] is a woman with a sister named \[Enedina\]. \[Stanley\] loves buying her granddaughter, \[Enedina\], new clothes.
> The notebook has a blue cloth cover and a stitched binding.

## Question

> What is Teresa’s relationship to Molly?

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

**Reference answer:** `granddaughter`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "[Molly] just celebrated her first wedding anniversary with her husband [Stanley]. [Teresa] is a woman with a sister named [Enedina]. [Stanley] loves buying her granddaughter, [Enedina], new clothes.\nThe notebook has a blue cloth cover and a stitched binding.",
  "question": "What is Teresa’s relationship to Molly?",
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
| GLiDE v1.2 | `aunt` — aunt | `aunt` — aunt | Same answer |
| Decider v1.1 | `daughter-in-law` — daughter-in-law | `daughter-in-law` — daughter-in-law | Same answer |
| Jev | `grandmother` — grandmother | `mother-in-law` — mother-in-law | Different answer |
| Microsoft Decision-1 | `niece` — niece | `niece` — niece | Same answer |
| Clef | `aunt` — aunt | `grandmother` — grandmother | Different answer |
| Luna Decisions | `sister` — sister | `sister` — sister | Same answer |
| Clef Flash | `mother-in-law` — mother-in-law | `grandmother` — grandmother | Different answer |
| Strands Decider | `sister` — sister | `sister` — sister | Same answer |
| GLiNER2.5 Decide | `granddaughter` — granddaughter | `granddaughter` — granddaughter | Same answer |
| Laya | `sister` — sister | `sister` — sister | Same answer |
| CalDec v1 | `sister` — sister | `sister` — sister | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `clutrr/689c776d03722217056d/examples/absent/clean-source_first_kinship_example_controls_full_0105`

**Input fingerprint:** `43356c041fb255cbba2a4ed1193221b1ed76f4dbe9eada2ea5b5bb95a60d2cba`

| Change | Recorded version |
| --- | --- |
| Unrelated examples | No worked example (absence-control recipe) |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/relations/clutrr-689c776d03722217056d.md).
