# Similar distractors · Add fewer similar but irrelevant items variant

[Original question](../../../questions/retrieval/babi-156151f03e8572ae7d0c.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Sandra went to the kitchen.
> Mary moved to the kitchen.
> Vesrin went to the office. Vesrin moved to the garden.

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
  "state": "Sandra went to the kitchen.\nMary moved to the kitchen.\nVesrin went to the office. Vesrin moved to the garden.",
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

**Variant ID:** `babi/156151f03e8572ae7d0c/similar_distractors/low/clean-source_first_qa1_distractors_full_0146`

**Input fingerprint:** `d8dca22c802ab7b00119b1c16344e8d426d43608ad2ca315357d4aad146b4ab9`

| Change | Recorded version |
| --- | --- |
| Similar distractors | Add fewer similar but irrelevant items |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/retrieval/babi-156151f03e8572ae7d0c.md).
