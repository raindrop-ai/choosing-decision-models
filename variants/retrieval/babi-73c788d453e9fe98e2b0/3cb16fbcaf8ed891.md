# Irrelevant details · Add a larger amount of irrelevant detail variant

[Original question](../../../questions/retrieval/babi-73c788d453e9fe98e2b0.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> The office desk has brass handles.
> The kitchen cupboards are cream-colored.
> The bedroom rug is striped.
> The bathroom tiles are gray.
> The garden fence is wooden.
> The hallway bench has a woven seat.
> Mary journeyed to the garden.
> Sandra went back to the office.

## Question

> Where is Sandra? 

## Answer choices

- **A.** kitchen
- **B.** office
- **C.** bathroom
- **D.** hallway
- **E.** garden
- **F.** bedroom

**Reference answer:** `B`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "The office desk has brass handles.\nThe kitchen cupboards are cream-colored.\nThe bedroom rug is striped.\nThe bathroom tiles are gray.\nThe garden fence is wooden.\nThe hallway bench has a woven seat.\nMary journeyed to the garden.\nSandra went back to the office.",
  "question": "Where is Sandra? ",
  "choices": {
    "A": "kitchen",
    "B": "office",
    "C": "bathroom",
    "D": "hallway",
    "E": "garden",
    "F": "bedroom"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `B` — office | `B` — office | Same answer |
| Decider v1.1 | `B` — office | `B` — office | Same answer |
| Jev | `B` — office | `B` — office | Same answer |
| Microsoft Decision-1 | `B` — office | `B` — office | Same answer |
| Clef | `B` — office | `B` — office | Same answer |
| Luna Decisions | `B` — office | `B` — office | Same answer |
| Clef Flash | `B` — office | `B` — office | Same answer |
| Strands Decider | `B` — office | `B` — office | Same answer |
| GLiNER2.5 Decide | `B` — office | `B` — office | Same answer |
| Laya | `B` — office | `B` — office | Same answer |
| CalDec v1 | `B` — office | `B` — office | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `babi/73c788d453e9fe98e2b0/irrelevant_details/high/clean-movement_natural_contexts_0005`

**Input fingerprint:** `772228cab7d95053657a1dcd2ccc1466c22638a449e877b2626d25f8772b99b6`

| Change | Recorded version |
| --- | --- |
| Irrelevant details | Add a larger amount of irrelevant detail |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/retrieval/babi-73c788d453e9fe98e2b0.md).
