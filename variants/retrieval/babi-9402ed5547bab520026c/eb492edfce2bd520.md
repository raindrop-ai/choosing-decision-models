# Paraphrasing · Change the sentence structure variant

[Original question](../../../questions/retrieval/babi-9402ed5547bab520026c.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** question instructions.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> John travelled to the bathroom.
> Daniel went to the hallway.
> John moved to the kitchen.
> Mary journeyed to the kitchen.
> Daniel travelled to the bathroom.
> John travelled to the bathroom.
> Daniel went to the garden.
> Sandra travelled to the hallway.

## Question

> Sandra is currently in which location?

## Answer choices

- **A.** office
- **B.** garden
- **C.** hallway
- **D.** bathroom
- **E.** kitchen
- **F.** bedroom

**Reference answer:** `C`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "John travelled to the bathroom.\nDaniel went to the hallway.\nJohn moved to the kitchen.\nMary journeyed to the kitchen.\nDaniel travelled to the bathroom.\nJohn travelled to the bathroom.\nDaniel went to the garden.\nSandra travelled to the hallway.",
  "question": "Sandra is currently in which location?",
  "choices": {
    "A": "office",
    "B": "garden",
    "C": "hallway",
    "D": "bathroom",
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
| GLiDE v1.2 | `C` — hallway | `C` — hallway | Same answer |
| Decider v1.1 | `C` — hallway | `C` — hallway | Same answer |
| Jev | `C` — hallway | `C` — hallway | Same answer |
| Microsoft Decision-1 | `C` — hallway | `C` — hallway | Same answer |
| Clef | `C` — hallway | `C` — hallway | Same answer |
| Luna Decisions | `C` — hallway | `C` — hallway | Same answer |
| Clef Flash | `C` — hallway | `C` — hallway | Same answer |
| Strands Decider | `C` — hallway | `C` — hallway | Same answer |
| GLiNER2.5 Decide | `C` — hallway | `C` — hallway | Same answer |
| Laya | `C` — hallway | `C` — hallway | Same answer |
| CalDec v1 | `C` — hallway | `C` — hallway | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `babi/9402ed5547bab520026c/paraphrasing/structural`

**Input fingerprint:** `c79d7c3eabc8f7147647cd7b6ae0a3c6f8370aeb91130ce7dd2c25926f2072bc`

| Change | Recorded version |
| --- | --- |
| Paraphrasing | Change the sentence structure |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/retrieval/babi-9402ed5547bab520026c.md).
