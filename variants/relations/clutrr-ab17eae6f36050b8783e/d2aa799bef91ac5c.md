# Invented names · Use invented names variant

[Original question](../../../questions/relations/clutrr-ab17eae6f36050b8783e.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context, question instructions.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> \[Varelin\] and her sisters \[Zorven\] went to the spa. \[Nelarik\], another sister of \[Varelin\], had to babysit and could n't join them. \[Tovrin\] likes to visit his sister. Her name is \[Kasel\]. \[Mireth\] and her sister \[Zorven\] went to the mall. While at the mall \[Mireth\] found the perfect Mother's Day gift for her mother \[Kasel\].

## Question

> What is Tovrin’s relationship to Nelarik?

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
  "state": "[Varelin] and her sisters [Zorven] went to the spa. [Nelarik], another sister of [Varelin], had to babysit and could n't join them. [Tovrin] likes to visit his sister. Her name is [Kasel]. [Mireth] and her sister [Zorven] went to the mall. While at the mall [Mireth] found the perfect Mother's Day gift for her mother [Kasel].",
  "question": "What is Tovrin’s relationship to Nelarik?",
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
| Decider v1.1 | `nephew` — nephew | `uncle` — uncle | Different answer |
| Jev | `brother` — brother | `sister` — sister | Different answer |
| Microsoft Decision-1 | `nephew` — nephew | `nephew` — nephew | Same answer |
| Clef | `nephew` — nephew | `nephew` — nephew | Same answer |
| Luna Decisions | `brother` — brother | `brother` — brother | Same answer |
| Clef Flash | `nephew` — nephew | `uncle` — uncle | Different answer |
| Strands Decider | `sister` — sister | `sister` — sister | Same answer |
| GLiNER2.5 Decide | `sister` — sister | `sister` — sister | Same answer |
| Laya | `mother` — mother | `mother` — mother | Same answer |
| CalDec v1 | `mother` — mother | `mother` — mother | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `clutrr/ab17eae6f36050b8783e/unfamiliar_names/invented`

**Input fingerprint:** `8c2a21c2d3a9efa01ecbf05607895cdc1f98f2385c446dd54c9fa34b56c667b8`

| Change | Recorded version |
| --- | --- |
| Invented names | Use invented names |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/relations/clutrr-ab17eae6f36050b8783e.md).
