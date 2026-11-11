# Extra events · Add 2 unrelated events variant

[Original question](../../../questions/relations/clutrr-865f24d475598cdce57e.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Nolan is the editor of a poetry catalog. Its entries are Virel, Zorven, Kesil, Nereth, Pavrel, and Sovrin.
> Nolan classifies Virel as a dialogue. Nolan classifies Zorven as a monologue.
>
> \[Matthew\] likes to watch baseball with his brother. His name is \[Anthony\]. \[Stanley\] had a conversation with his grandson, \[Matthew\]. \[Stanley\] asked his wife \[Molly\] to keep her distance.

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
  "state": "Nolan is the editor of a poetry catalog. Its entries are Virel, Zorven, Kesil, Nereth, Pavrel, and Sovrin.\nNolan classifies Virel as a dialogue. Nolan classifies Zorven as a monologue.\n\n[Matthew] likes to watch baseball with his brother. His name is [Anthony]. [Stanley] had a conversation with his grandson, [Matthew]. [Stanley] asked his wife [Molly] to keep her distance.",
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
| Strands Decider | `nephew` — nephew | `brother` — brother | Different answer |
| GLiNER2.5 Decide | `grandson` — grandson | `grandson` — grandson | Same answer |
| Laya | `grandson` — grandson | `grandson` — grandson | Same answer |
| CalDec v1 | `grandson` — grandson | `grandson` — grandson | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `clutrr/865f24d475598cdce57e/event_count/2/clean-source_first_kinship_length_position_events_full_0102`

**Input fingerprint:** `ed679dfb838a68a52fc128f3d738c6cdbfc9bb4814a28dabc1c543fdf1ecfb6a`

| Change | Recorded version |
| --- | --- |
| Extra events | Add 2 unrelated events |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/relations/clutrr-865f24d475598cdce57e.md).
