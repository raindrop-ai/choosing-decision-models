# Text length · bAbI: longer added prose variant

[Original question](../../../questions/retrieval/babi-156151f03e8572ae7d0c.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> The office had a broad oak desk beside a window. A brass lamp stood on the desk,and two empty chairs faced it. A framed map hung above a low shelf of books. The hallway outside had a tiled floor,pale walls and a narrow bench.
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
  "state": "The office had a broad oak desk beside a window. A brass lamp stood on the desk,and two empty chairs faced it. A framed map hung above a low shelf of books. The hallway outside had a tiled floor,pale walls and a narrow bench.\nSandra went to the kitchen.\nMary moved to the kitchen.",
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
| Laya | `E` — kitchen | `D` — office | Different answer |
| CalDec v1 | `E` — kitchen | `E` — kitchen | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `babi/156151f03e8572ae7d0c/text_length/longer_natural/clean-movement_natural_contexts_0005`

**Input fingerprint:** `0fbb105650eb0fbbbaaea8148c0009d124ce4618127e40275c05d6700b4e0bdb`

| Change | Recorded version |
| --- | --- |
| Text length | bAbI: longer added prose |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/retrieval/babi-156151f03e8572ae7d0c.md).
