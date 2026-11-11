# Evidence order · Present the evidence in reverse order variant

[Original question](../../../questions/retrieval/babi-cc3432e648d116c87be2.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> John went to the office.
> Mary moved to the bedroom.
> Daniel journeyed to the garden.
> Sandra moved to the bedroom.
> Sandra went back to the hallway.
> Sandra went back to the bathroom.

## Question

> Where is Daniel? 

## Answer choices

- **A.** bathroom
- **B.** garden
- **C.** kitchen
- **D.** office
- **E.** bedroom
- **F.** hallway

**Reference answer:** `B`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "John went to the office.\nMary moved to the bedroom.\nDaniel journeyed to the garden.\nSandra moved to the bedroom.\nSandra went back to the hallway.\nSandra went back to the bathroom.",
  "question": "Where is Daniel? ",
  "choices": {
    "A": "bathroom",
    "B": "garden",
    "C": "kitchen",
    "D": "office",
    "E": "bedroom",
    "F": "hallway"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `B` — garden | `B` — garden | Same answer |
| Decider v1.1 | `B` — garden | `B` — garden | Same answer |
| Jev | `B` — garden | `B` — garden | Same answer |
| Microsoft Decision-1 | `B` — garden | `B` — garden | Same answer |
| Clef | `B` — garden | `B` — garden | Same answer |
| Luna Decisions | `B` — garden | `B` — garden | Same answer |
| Clef Flash | `B` — garden | `B` — garden | Same answer |
| Strands Decider | `B` — garden | `B` — garden | Same answer |
| GLiNER2.5 Decide | `A` — bathroom | `A` — bathroom | Same answer |
| Laya | `A` — bathroom | `B` — garden | Different answer |
| CalDec v1 | `A` — bathroom | `A` — bathroom | Same answer |

**Ordering comparison:** literal local or custom unit permutation. Only the exact matched comparison sets contribute to the reported ordering contrasts.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `babi/cc3432e648d116c87be2/presentation_order/reverse_presentation/clean-source_first_babi_qa1_full_0084`

**Input fingerprint:** `2d60186902cfa4378f72b01f7a8d7aca1527ac4eb327d5001f129e60b40733e7`

| Change | Recorded version |
| --- | --- |
| Evidence order | Present the evidence in reverse order |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/retrieval/babi-cc3432e648d116c87be2.md).
