# Extra events · Add 6 unrelated events variant

[Original question](../../../questions/state-tracking-and-updating/babi-2f265669fdfd296e8814.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

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
> Sandra travelled to the office.
> Sandra travelled to the bathroom.

## Question

> Where is Sandra? 

## Answer choices

- **A.** hallway
- **B.** office
- **C.** bedroom
- **D.** garden
- **E.** kitchen
- **F.** bathroom

**Reference answer:** `F`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Nora went to the garden.\nNora went to the office.\nNora went to the kitchen.\nNora went to the bathroom.\nNora went to the hallway.\nNora went to the bedroom.\nSandra travelled to the office.\nSandra travelled to the bathroom.",
  "question": "Where is Sandra? ",
  "choices": {
    "A": "hallway",
    "B": "office",
    "C": "bedroom",
    "D": "garden",
    "E": "kitchen",
    "F": "bathroom"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `F` — bathroom | `F` — bathroom | Same answer |
| Decider v1.1 | `F` — bathroom | `F` — bathroom | Same answer |
| Jev | `F` — bathroom | `F` — bathroom | Same answer |
| Microsoft Decision-1 | `F` — bathroom | `F` — bathroom | Same answer |
| Clef | `F` — bathroom | `F` — bathroom | Same answer |
| Luna Decisions | `F` — bathroom | `F` — bathroom | Same answer |
| Clef Flash | `F` — bathroom | `F` — bathroom | Same answer |
| Strands Decider | `F` — bathroom | `F` — bathroom | Same answer |
| GLiNER2.5 Decide | `F` — bathroom | `F` — bathroom | Same answer |
| Laya | `B` — office | `B` — office | Same answer |
| CalDec v1 | `F` — bathroom | `F` — bathroom | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `babi/2f265669fdfd296e8814/event_count/6/clean-movement_natural_contexts_0005`

**Input fingerprint:** `07a0c64105d5da8caebe25b38fe301aaf020f10fc5f6426ee64e830518dda913`

| Change | Recorded version |
| --- | --- |
| Extra events | Add 6 unrelated events |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/state-tracking-and-updating/babi-2f265669fdfd296e8814.md).
