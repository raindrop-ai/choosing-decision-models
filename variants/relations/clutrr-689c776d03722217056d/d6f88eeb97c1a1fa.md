# Extra events · Add 6 unrelated events variant

[Original question](../../../questions/relations/clutrr-689c776d03722217056d.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Nolan is the editor of a poetry catalog. Its entries are Virel, Zorven, Kesil, Nereth, Pavrel, and Sovrin.
> Nolan classifies Virel as a dialogue. Nolan classifies Zorven as a monologue. Nolan classifies Kesil as an elegy. Nolan classifies Nereth as a satire. Nolan classifies Pavrel as a fable. Nolan classifies Sovrin as a ballad.
>
> \[Molly\] just celebrated her first wedding anniversary with her husband \[Stanley\]. \[Teresa\] is a woman with a sister named \[Enedina\]. \[Stanley\] loves buying her granddaughter, \[Enedina\], new clothes.

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
  "state": "Nolan is the editor of a poetry catalog. Its entries are Virel, Zorven, Kesil, Nereth, Pavrel, and Sovrin.\nNolan classifies Virel as a dialogue. Nolan classifies Zorven as a monologue. Nolan classifies Kesil as an elegy. Nolan classifies Nereth as a satire. Nolan classifies Pavrel as a fable. Nolan classifies Sovrin as a ballad.\n\n[Molly] just celebrated her first wedding anniversary with her husband [Stanley]. [Teresa] is a woman with a sister named [Enedina]. [Stanley] loves buying her granddaughter, [Enedina], new clothes.",
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
| GLiDE v1.2 | `aunt` — aunt | `sister` — sister | Different answer |
| Decider v1.1 | `daughter-in-law` — daughter-in-law | `niece` — niece | Different answer |
| Jev | `grandmother` — grandmother | `mother-in-law` — mother-in-law | Different answer |
| Microsoft Decision-1 | `niece` — niece | `aunt` — aunt | Different answer |
| Clef | `aunt` — aunt | `grandmother` — grandmother | Different answer |
| Luna Decisions | `sister` — sister | `sister` — sister | Same answer |
| Clef Flash | `mother-in-law` — mother-in-law | `daughter-in-law` — daughter-in-law | Different answer |
| Strands Decider | `sister` — sister | `sister` — sister | Same answer |
| GLiNER2.5 Decide | `granddaughter` — granddaughter | `sister` — sister | Different answer |
| Laya | `sister` — sister | `granddaughter` — granddaughter | Different answer |
| CalDec v1 | `sister` — sister | `granddaughter` — granddaughter | Different answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `clutrr/689c776d03722217056d/event_count/6/clean-source_first_kinship_length_position_events_full_0103`

**Input fingerprint:** `d331416c162baec5e7e7bffd1ae79800d79d30eda6f3fe70e5cc975188e0a714`

| Change | Recorded version |
| --- | --- |
| Extra events | Add 6 unrelated events |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/relations/clutrr-689c776d03722217056d.md).
