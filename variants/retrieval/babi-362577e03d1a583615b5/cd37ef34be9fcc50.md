# Similar distractors · Add fewer similar but irrelevant items variant

[Original question](../../../questions/retrieval/babi-362577e03d1a583615b5.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Mary journeyed to the kitchen.
> Sandra went back to the garden.
> Vesrin went to the office. Vesrin moved to the garden.

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
  "state": "Mary journeyed to the kitchen.\nSandra went back to the garden.\nVesrin went to the office. Vesrin moved to the garden.",
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
| Laya | `F` — garden | `F` — garden | Same answer |
| CalDec v1 | `F` — garden | `F` — garden | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `babi/362577e03d1a583615b5/similar_distractors/low/clean-source_first_qa1_distractors_full_0146`

**Input fingerprint:** `9d05d66b795b0d77a034fabc412b07a60f222b752c8d183c3537247d12c8f60b`

| Change | Recorded version |
| --- | --- |
| Similar distractors | Add fewer similar but irrelevant items |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/retrieval/babi-362577e03d1a583615b5.md).
