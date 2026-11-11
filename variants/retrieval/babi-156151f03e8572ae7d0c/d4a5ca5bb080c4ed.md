# Extra events · Add 6 unrelated events variant

[Original question](../../../questions/retrieval/babi-156151f03e8572ae7d0c.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

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
> Sandra went to the kitchen.
> Mary moved to the kitchen.

## Question

> Where is Sandra? 

## Answer choices

- **A.** bathroom
- **B.** hallway
- **C.** garden
- **D.** office
- **E.** kitchen
- **F.** bedroom

**Reference answer:** `E`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Nora went to the garden.\nNora went to the office.\nNora went to the kitchen.\nNora went to the bathroom.\nNora went to the hallway.\nNora went to the bedroom.\nSandra went to the kitchen.\nMary moved to the kitchen.",
  "question": "Where is Sandra? ",
  "choices": {
    "A": "bathroom",
    "B": "hallway",
    "C": "garden",
    "D": "office",
    "E": "kitchen",
    "F": "bedroom"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `E` — kitchen | `E` — kitchen | Same answer |
| Decider v1.1 | `E` — kitchen | `E` — kitchen | Same answer |
| Jev | `E` — kitchen | `E` — kitchen | Same answer |
| Microsoft Decision-1 | `E` — kitchen | `E` — kitchen | Same answer |
| Clef | `E` — kitchen | `E` — kitchen | Same answer |
| Luna Decisions | `E` — kitchen | `E` — kitchen | Same answer |
| Clef Flash | `E` — kitchen | `E` — kitchen | Same answer |
| Strands Decider | `E` — kitchen | `E` — kitchen | Same answer |
| GLiNER2.5 Decide | `E` — kitchen | `E` — kitchen | Same answer |
| Laya | `E` — kitchen | `E` — kitchen | Same answer |
| CalDec v1 | `E` — kitchen | `E` — kitchen | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `babi/156151f03e8572ae7d0c/event_count/6/clean-movement_natural_contexts_0005`

**Input fingerprint:** `d7d4f06ab29b17e38193d8cfb803a440f0b2d1371af9f9092e6b902ca1e110e5`

| Change | Recorded version |
| --- | --- |
| Extra events | Add 6 unrelated events |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/retrieval/babi-156151f03e8572ae7d0c.md).
