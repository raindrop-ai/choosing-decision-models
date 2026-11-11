# Unrelated examples · No worked example (absence-control recipe) variant

[Original question](../../../questions/relations/clutrr-ab17eae6f36050b8783e.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> \[Annie\] and her sisters \[Lisa\] went to the spa. \[Margaret\], another sister of \[Annie\], had to babysit and could n't join them. \[Jason\] likes to visit his sister. Her name is \[Rosa\]. \[Melissa\] and her sister \[Lisa\] went to the mall. While at the mall \[Melissa\] found the perfect Mother's Day gift for her mother \[Rosa\].
> The notebook has a blue cloth cover and a stitched binding.

## Question

> What is Jason’s relationship to Margaret?

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

**Reference answer:** `uncle`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "[Annie] and her sisters [Lisa] went to the spa. [Margaret], another sister of [Annie], had to babysit and could n't join them. [Jason] likes to visit his sister. Her name is [Rosa]. [Melissa] and her sister [Lisa] went to the mall. While at the mall [Melissa] found the perfect Mother's Day gift for her mother [Rosa].\nThe notebook has a blue cloth cover and a stitched binding.",
  "question": "What is Jason’s relationship to Margaret?",
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
| GLiDE v1.2 | `uncle` — uncle | `uncle` — uncle | Same answer |
| Decider v1.1 | `nephew` — nephew | `nephew` — nephew | Same answer |
| Jev | `brother` — brother | `brother` — brother | Same answer |
| Microsoft Decision-1 | `nephew` — nephew | `nephew` — nephew | Same answer |
| Clef | `nephew` — nephew | `nephew` — nephew | Same answer |
| Luna Decisions | `brother` — brother | `brother` — brother | Same answer |
| Clef Flash | `nephew` — nephew | `nephew` — nephew | Same answer |
| Strands Decider | `sister` — sister | `sister` — sister | Same answer |
| GLiNER2.5 Decide | `sister` — sister | `sister` — sister | Same answer |
| Laya | `mother` — mother | `sister` — sister | Different answer |
| CalDec v1 | `mother` — mother | `mother` — mother | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `clutrr/ab17eae6f36050b8783e/examples/absent/clean-source_first_kinship_example_controls_full_0105`

**Input fingerprint:** `e4e58c64a14bc07bc6790e8867772e27cf0d0b860e2a5b1febe8cd3df522ba7b`

| Change | Recorded version |
| --- | --- |
| Unrelated examples | No worked example (absence-control recipe) |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/relations/clutrr-ab17eae6f36050b8783e.md).
