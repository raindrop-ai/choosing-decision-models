# Invented names · Use invented names variant

[Original question](../../../questions/retrieval/babi-362577e03d1a583615b5.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context, question instructions.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Nelora journeyed to the kitchen.
> Vaelis went back to the garden.

## Question

> Where is Vaelis? 

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
  "state": "Nelora journeyed to the kitchen.\nVaelis went back to the garden.",
  "question": "Where is Vaelis? ",
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

**Variant ID:** `babi/362577e03d1a583615b5/unfamiliar_names/invented`

**Input fingerprint:** `4d551213e2e4fe78c70e6525ba6d51ad6a554801a04b9d4406e7ac89e9529d61`

| Change | Recorded version |
| --- | --- |
| Invented names | Use invented names |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/retrieval/babi-362577e03d1a583615b5.md).
