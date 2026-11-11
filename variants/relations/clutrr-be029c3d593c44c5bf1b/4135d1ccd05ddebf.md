# Irrelevant details · Add a small amount of irrelevant detail variant

[Original question](../../../questions/relations/clutrr-be029c3d593c44c5bf1b.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> \[William\] took his sister \[Sheila\] out to lunch after learning that she got accepted into her first choice for university. \[Seth\] and his daughter \[Ruth\] took a day off school to go to the zoo. \[Jonathan\] took his sister \[Ruth\] out to lunch after learning that she got accepted into her first choice for university. \[Jonathan\] is proud that his daughter is such a good student. Her name is \[Diana\]. \[Sheila\], who is the sister of \[Diana\], is a lovely girl.
> The lunch table had a wooden top.

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
  "state": "[William] took his sister [Sheila] out to lunch after learning that she got accepted into her first choice for university. [Seth] and his daughter [Ruth] took a day off school to go to the zoo. [Jonathan] took his sister [Ruth] out to lunch after learning that she got accepted into her first choice for university. [Jonathan] is proud that his daughter is such a good student. Her name is [Diana]. [Sheila], who is the sister of [Diana], is a lovely girl.\nThe lunch table had a wooden top.",
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
| GLiDE v1.2 | `son-in-law` — son-in-law | `son-in-law` — son-in-law | Same answer |
| Decider v1.1 | `son-in-law` — son-in-law | `son-in-law` — son-in-law | Same answer |
| Jev | `brother` — brother | `brother` — brother | Same answer |
| Microsoft Decision-1 | `uncle` — uncle | `uncle` — uncle | Same answer |
| Clef | `uncle` — uncle | `uncle` — uncle | Same answer |
| Luna Decisions | `brother` — brother | `brother` — brother | Same answer |
| Clef Flash | `uncle` — uncle | `uncle` — uncle | Same answer |
| Strands Decider | `sister` — sister | `sister` — sister | Same answer |
| GLiNER2.5 Decide | `sister` — sister | `sister` — sister | Same answer |
| Laya | `sister` — sister | `sister` — sister | Same answer |
| CalDec v1 | `sister` — sister | `sister` — sister | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `clutrr/be029c3d593c44c5bf1b/irrelevant_details/low/clean-kinship_examples_details_full_0020`

**Input fingerprint:** `42057ace3b6754dc28d30b4bfca98532bcaa5355bfa8588a2269137b51822ff0`

| Change | Recorded version |
| --- | --- |
| Irrelevant details | Add a small amount of irrelevant detail |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/relations/clutrr-be029c3d593c44c5bf1b.md).
