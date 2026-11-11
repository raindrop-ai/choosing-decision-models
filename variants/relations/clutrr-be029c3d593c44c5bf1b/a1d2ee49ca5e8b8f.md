# Extra events · Add 2 unrelated events variant

[Original question](../../../questions/relations/clutrr-be029c3d593c44c5bf1b.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Nolan is the editor of a poetry catalog. Its entries are Virel, Zorven, Kesil, Nereth, Pavrel, and Sovrin.
> Nolan classifies Virel as a dialogue. Nolan classifies Zorven as a monologue.
>
> \[William\] took his sister \[Sheila\] out to lunch after learning that she got accepted into her first choice for university. \[Seth\] and his daughter \[Ruth\] took a day off school to go to the zoo. \[Jonathan\] took his sister \[Ruth\] out to lunch after learning that she got accepted into her first choice for university. \[Jonathan\] is proud that his daughter is such a good student. Her name is \[Diana\]. \[Sheila\], who is the sister of \[Diana\], is a lovely girl.

## Question

> What is William’s relationship to Seth?

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
  "state": "Nolan is the editor of a poetry catalog. Its entries are Virel, Zorven, Kesil, Nereth, Pavrel, and Sovrin.\nNolan classifies Virel as a dialogue. Nolan classifies Zorven as a monologue.\n\n[William] took his sister [Sheila] out to lunch after learning that she got accepted into her first choice for university. [Seth] and his daughter [Ruth] took a day off school to go to the zoo. [Jonathan] took his sister [Ruth] out to lunch after learning that she got accepted into her first choice for university. [Jonathan] is proud that his daughter is such a good student. Her name is [Diana]. [Sheila], who is the sister of [Diana], is a lovely girl.",
  "question": "What is William’s relationship to Seth?",
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
| GLiDE v1.2 | `son-in-law` — son-in-law | `nephew` — nephew | Different answer |
| Decider v1.1 | `son-in-law` — son-in-law | `nephew` — nephew | Different answer |
| Jev | `brother` — brother | `brother` — brother | Same answer |
| Microsoft Decision-1 | `uncle` — uncle | `uncle` — uncle | Same answer |
| Clef | `uncle` — uncle | `uncle` — uncle | Same answer |
| Luna Decisions | `brother` — brother | `brother` — brother | Same answer |
| Clef Flash | `uncle` — uncle | `uncle` — uncle | Same answer |
| Strands Decider | `sister` — sister | `sister` — sister | Same answer |
| GLiNER2.5 Decide | `sister` — sister | `sister` — sister | Same answer |
| Laya | `sister` — sister | `father` — father | Different answer |
| CalDec v1 | `sister` — sister | `sister` — sister | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `clutrr/be029c3d593c44c5bf1b/event_count/2/clean-source_first_kinship_length_position_events_full_0103`

**Input fingerprint:** `46e1dfc8e0311b9f3e2039a809c02723f5add249644035c517f72ecc6063a651`

| Change | Recorded version |
| --- | --- |
| Extra events | Add 2 unrelated events |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/relations/clutrr-be029c3d593c44c5bf1b.md).
