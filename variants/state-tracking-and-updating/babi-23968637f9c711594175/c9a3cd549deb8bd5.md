# Similar distractors · Add more similar but irrelevant items variant

[Original question](../../../questions/state-tracking-and-updating/babi-23968637f9c711594175.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Sandra moved to the bedroom.
> John went to the hallway.
> Sandra travelled to the office.
> Sandra moved to the bathroom.
> Vesrin went to the office. Vesrin moved to the garden.
> Nerola travelled to the kitchen. Nerola went to the hallway.
> Kaseli journeyed to the bedroom. Kaseli moved to the bathroom.

## Question

> Where is Sandra? 

## Answer choices

- **A.** bathroom
- **B.** hallway
- **C.** kitchen
- **D.** bedroom
- **E.** garden
- **F.** office

**Reference answer:** `A`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Sandra moved to the bedroom.\nJohn went to the hallway.\nSandra travelled to the office.\nSandra moved to the bathroom.\nVesrin went to the office. Vesrin moved to the garden.\nNerola travelled to the kitchen. Nerola went to the hallway.\nKaseli journeyed to the bedroom. Kaseli moved to the bathroom.",
  "question": "Where is Sandra? ",
  "choices": {
    "A": "bathroom",
    "B": "hallway",
    "C": "kitchen",
    "D": "bedroom",
    "E": "garden",
    "F": "office"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `A` — bathroom | `A` — bathroom | Same answer |
| Decider v1.1 | `A` — bathroom | `A` — bathroom | Same answer |
| Jev | `A` — bathroom | `A` — bathroom | Same answer |
| Microsoft Decision-1 | `A` — bathroom | `A` — bathroom | Same answer |
| Clef | `A` — bathroom | `A` — bathroom | Same answer |
| Luna Decisions | `A` — bathroom | `A` — bathroom | Same answer |
| Clef Flash | `A` — bathroom | `A` — bathroom | Same answer |
| Strands Decider | `A` — bathroom | `A` — bathroom | Same answer |
| GLiNER2.5 Decide | `A` — bathroom | `A` — bathroom | Same answer |
| Laya | `A` — bathroom | `A` — bathroom | Same answer |
| CalDec v1 | `A` — bathroom | `A` — bathroom | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `babi/23968637f9c711594175/similar_distractors/high/clean-source_first_qa1_distractors_full_0146`

**Input fingerprint:** `6a7aedc792aa719d624e62a197d1929d3c7ec8d3409b5deadedbfd204016fc16`

| Change | Recorded version |
| --- | --- |
| Similar distractors | Add more similar but irrelevant items |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/state-tracking-and-updating/babi-23968637f9c711594175.md).
