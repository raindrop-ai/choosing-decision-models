# Extra events · Add 12 unrelated events variant

[Original question](../../../questions/state-tracking-and-updating/babi-e52715c73f1a2fd2bbc8.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Nora went to the garden.
> Nora went to the office.
> Nora went to the kitchen.
> Nora went to the bathroom.
> Nora went to the hallway.
> Nora went to the bedroom.
> Nora went to the bathroom.
> Nora went to the kitchen.
> Nora went to the garden.
> Nora went to the hallway.
> Nora went to the office.
> Nora went to the bedroom.
> John travelled to the garden.
> Mary journeyed to the office.
> Sandra went to the garden.
> John went back to the office.
> John moved to the bedroom.
> John moved to the garden.

## Question

> Where is John? 

## Answer choices

- **A.** bedroom
- **B.** hallway
- **C.** bathroom
- **D.** office
- **E.** garden
- **F.** kitchen

**Reference answer:** `E`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Nora went to the garden.\nNora went to the office.\nNora went to the kitchen.\nNora went to the bathroom.\nNora went to the hallway.\nNora went to the bedroom.\nNora went to the bathroom.\nNora went to the kitchen.\nNora went to the garden.\nNora went to the hallway.\nNora went to the office.\nNora went to the bedroom.\nJohn travelled to the garden.\nMary journeyed to the office.\nSandra went to the garden.\nJohn went back to the office.\nJohn moved to the bedroom.\nJohn moved to the garden.",
  "question": "Where is John? ",
  "choices": {
    "A": "bedroom",
    "B": "hallway",
    "C": "bathroom",
    "D": "office",
    "E": "garden",
    "F": "kitchen"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `E` — garden | `E` — garden | Same answer |
| Decider v1.1 | `E` — garden | `E` — garden | Same answer |
| Jev | `E` — garden | `E` — garden | Same answer |
| Microsoft Decision-1 | `E` — garden | `E` — garden | Same answer |
| Clef | `E` — garden | `E` — garden | Same answer |
| Luna Decisions | `E` — garden | `E` — garden | Same answer |
| Clef Flash | `E` — garden | `E` — garden | Same answer |
| Strands Decider | `E` — garden | `E` — garden | Same answer |
| GLiNER2.5 Decide | `E` — garden | `E` — garden | Same answer |
| Laya | `A` — bedroom | `A` — bedroom | Same answer |
| CalDec v1 | `E` — garden | `A` — bedroom | Different answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `babi/e52715c73f1a2fd2bbc8/event_count/12/clean-movement_natural_contexts_0005`

**Input fingerprint:** `c78106587e2b04679ba1e4baf470653a5618a75c1c82ff507edd7df22ac34494`

| Change | Recorded version |
| --- | --- |
| Extra events | Add 12 unrelated events |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/state-tracking-and-updating/babi-e52715c73f1a2fd2bbc8.md).
