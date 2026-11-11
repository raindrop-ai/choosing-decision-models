# Unrelated examples · No worked example (absence-control recipe) variant

[Original question](../../../questions/relations/clutrr-865f24d475598cdce57e.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> \[Matthew\] likes to watch baseball with his brother. His name is \[Anthony\]. \[Stanley\] had a conversation with his grandson, \[Matthew\]. \[Stanley\] asked his wife \[Molly\] to keep her distance.
> The notebook has a blue cloth cover and a stitched binding.

## Question

> What is Anthony’s relationship to Molly?

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

**Reference answer:** `grandson`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "[Matthew] likes to watch baseball with his brother. His name is [Anthony]. [Stanley] had a conversation with his grandson, [Matthew]. [Stanley] asked his wife [Molly] to keep her distance.\nThe notebook has a blue cloth cover and a stitched binding.",
  "question": "What is Anthony’s relationship to Molly?",
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
| Decider v1.1 | `grandson` — grandson | `grandson` — grandson | Same answer |
| Jev | `grandson` — grandson | `grandson` — grandson | Same answer |
| Microsoft Decision-1 | `nephew` — nephew | `nephew` — nephew | Same answer |
| Clef | `grandson` — grandson | `grandson` — grandson | Same answer |
| Luna Decisions | `son` — son | `son` — son | Same answer |
| Clef Flash | `nephew` — nephew | `nephew` — nephew | Same answer |
| Strands Decider | `nephew` — nephew | `nephew` — nephew | Same answer |
| GLiNER2.5 Decide | `grandson` — grandson | `grandson` — grandson | Same answer |
| Laya | `grandson` — grandson | `grandson` — grandson | Same answer |
| CalDec v1 | `grandson` — grandson | `grandson` — grandson | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `clutrr/865f24d475598cdce57e/examples/absent/clean-source_first_kinship_example_controls_full_0105`

**Input fingerprint:** `1baf00561929c9b87cf3239afd33243cd567e2296f5f80511ba5895272d271f6`

| Change | Recorded version |
| --- | --- |
| Unrelated examples | No worked example (absence-control recipe) |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/relations/clutrr-865f24d475598cdce57e.md).
