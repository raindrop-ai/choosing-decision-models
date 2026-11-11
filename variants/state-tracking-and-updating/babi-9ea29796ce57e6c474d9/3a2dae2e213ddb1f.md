# Evidence order · Present the evidence in reverse order variant

[Original question](../../../questions/state-tracking-and-updating/babi-9ea29796ce57e6c474d9.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Mary moved to the kitchen.
> Mary journeyed to the bedroom.
> Daniel went back to the bedroom.
> Daniel went to the garden.
> Daniel went back to the kitchen.
> Sandra went to the kitchen.
> John went back to the hallway.
> John journeyed to the bedroom.
> John went back to the garden.
> John went to the bathroom.

## Question

> Where is Mary? 

## Answer choices

- **A.** bathroom
- **B.** hallway
- **C.** bedroom
- **D.** kitchen
- **E.** office
- **F.** garden

**Reference answer:** `C`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Mary moved to the kitchen.\nMary journeyed to the bedroom.\nDaniel went back to the bedroom.\nDaniel went to the garden.\nDaniel went back to the kitchen.\nSandra went to the kitchen.\nJohn went back to the hallway.\nJohn journeyed to the bedroom.\nJohn went back to the garden.\nJohn went to the bathroom.",
  "question": "Where is Mary? ",
  "choices": {
    "A": "bathroom",
    "B": "hallway",
    "C": "bedroom",
    "D": "kitchen",
    "E": "office",
    "F": "garden"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `C` — bedroom | `C` — bedroom | Same answer |
| Decider v1.1 | `C` — bedroom | `C` — bedroom | Same answer |
| Jev | `C` — bedroom | `C` — bedroom | Same answer |
| Microsoft Decision-1 | `C` — bedroom | `C` — bedroom | Same answer |
| Clef | `C` — bedroom | `C` — bedroom | Same answer |
| Luna Decisions | `C` — bedroom | `C` — bedroom | Same answer |
| Clef Flash | `C` — bedroom | `D` — kitchen | Different answer |
| Strands Decider | `C` — bedroom | `D` — kitchen | Different answer |
| GLiNER2.5 Decide | `C` — bedroom | `A` — bathroom | Different answer |
| Laya | `A` — bathroom | `C` — bedroom | Different answer |
| CalDec v1 | `A` — bathroom | `A` — bathroom | Same answer |

**Ordering comparison:** literal local or custom unit permutation. Only the exact matched comparison sets contribute to the reported ordering contrasts.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `babi/9ea29796ce57e6c474d9/presentation_order/reverse_presentation/clean-source_first_babi_qa1_full_0084`

**Input fingerprint:** `0f98e069d200981d3923db8976e029c0a67ad5f452b9b643a67da401a7f2b334`

| Change | Recorded version |
| --- | --- |
| Evidence order | Present the evidence in reverse order |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/state-tracking-and-updating/babi-9ea29796ce57e6c474d9.md).
