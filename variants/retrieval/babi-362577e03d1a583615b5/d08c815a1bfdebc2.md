# Irrelevant details · Add a larger amount of irrelevant detail variant

[Original question](../../../questions/retrieval/babi-362577e03d1a583615b5.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

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
> Mary journeyed to the kitchen.
> Sandra went back to the garden.

## Question

> Where is Sandra? 

## Answer choices

- **A.** bedroom
- **B.** kitchen
- **C.** hallway
- **D.** office
- **E.** bathroom
- **F.** garden

**Reference answer:** `F`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "The office desk has brass handles.\nThe kitchen cupboards are cream-colored.\nThe bedroom rug is striped.\nThe bathroom tiles are gray.\nThe garden fence is wooden.\nThe hallway bench has a woven seat.\nMary journeyed to the kitchen.\nSandra went back to the garden.",
  "question": "Where is Sandra? ",
  "choices": {
    "A": "bedroom",
    "B": "kitchen",
    "C": "hallway",
    "D": "office",
    "E": "bathroom",
    "F": "garden"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `F` — garden | `F` — garden | Same answer |
| Decider v1.1 | `F` — garden | `F` — garden | Same answer |
| Jev | `F` — garden | `F` — garden | Same answer |
| Microsoft Decision-1 | `F` — garden | `F` — garden | Same answer |
| Clef | `F` — garden | `F` — garden | Same answer |
| Luna Decisions | `F` — garden | `F` — garden | Same answer |
| Clef Flash | `F` — garden | `F` — garden | Same answer |
| Strands Decider | `F` — garden | `F` — garden | Same answer |
| GLiNER2.5 Decide | `F` — garden | `F` — garden | Same answer |
| Laya | `F` — garden | `A` — bedroom | Different answer |
| CalDec v1 | `F` — garden | `F` — garden | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `babi/362577e03d1a583615b5/irrelevant_details/high/clean-movement_natural_contexts_0005`

**Input fingerprint:** `9e22464b93d483dcd89fe1576b7787771c5d69d1416f10141b02a2f7c80de0b1`

| Change | Recorded version |
| --- | --- |
| Irrelevant details | Add a larger amount of irrelevant detail |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/retrieval/babi-362577e03d1a583615b5.md).
