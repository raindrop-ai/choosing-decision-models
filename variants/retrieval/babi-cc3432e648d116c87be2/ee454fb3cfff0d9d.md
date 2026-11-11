# Paraphrasing · Change individual words and phrases variant

[Original question](../../../questions/retrieval/babi-cc3432e648d116c87be2.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Sandra went to the bedroom.
> Daniel travelled to the garden.
> Mary went to the bedroom.
> Sandra returned to the hallway.
> John went to the office.
> Sandra returned to the bathroom.

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
  "state": "Sandra went to the bedroom.\nDaniel travelled to the garden.\nMary went to the bedroom.\nSandra returned to the hallway.\nJohn went to the office.\nSandra returned to the bathroom.",
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
| Laya | `A` — bathroom | `A` — bathroom | Same answer |
| CalDec v1 | `A` — bathroom | `A` — bathroom | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `babi/cc3432e648d116c87be2/paraphrasing/surface`

**Input fingerprint:** `2c27467033a24376a72ef8d93a92d5dd1f87b10ce05da474cc55edaa5f1f296b`

| Change | Recorded version |
| --- | --- |
| Paraphrasing | Change individual words and phrases |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/retrieval/babi-cc3432e648d116c87be2.md).
