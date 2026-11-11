# Unrelated examples · No worked example (prose-control recipe) variant

[Original question](../../../questions/retrieval/tombench-2cdd646690b4d21c29b8.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Xiao Li finds a storage cabinet in the study, the label on the storage cabinet is carrot, Xiao Li cannot see what is inside the storage cabinet, Xiao Li opens the storage cabinet and finds a coat, there are no carrots in the storage cabinet, Xiao Li closes the storage cabinet and puts it back in its place, Xiao Zhang enters the study and sees the storage cabinet.
>
> Merovan has a melodic refrain.

## Question

> What is in the storage cabinet?

## Answer choices

- **A.** Coat
- **B.** Pencil
- **C.** Carrot
- **D.** Tape

**Reference answer:** `A`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Xiao Li finds a storage cabinet in the study, the label on the storage cabinet is carrot, Xiao Li cannot see what is inside the storage cabinet, Xiao Li opens the storage cabinet and finds a coat, there are no carrots in the storage cabinet, Xiao Li closes the storage cabinet and puts it back in its place, Xiao Zhang enters the study and sees the storage cabinet.\n\nMerovan has a melodic refrain.",
  "question": "What is in the storage cabinet?",
  "choices": {
    "A": "Coat",
    "B": "Pencil",
    "C": "Carrot",
    "D": "Tape"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `A` — Coat | `A` — Coat | Same answer |
| Decider v1.1 | `A` — Coat | `A` — Coat | Same answer |
| Jev | `A` — Coat | `A` — Coat | Same answer |
| Microsoft Decision-1 | `A` — Coat | `A` — Coat | Same answer |
| Clef | `A` — Coat | `A` — Coat | Same answer |
| Luna Decisions | `A` — Coat | `A` — Coat | Same answer |
| Clef Flash | `A` — Coat | `A` — Coat | Same answer |
| Strands Decider | `A` — Coat | `A` — Coat | Same answer |
| GLiNER2.5 Decide | `A` — Coat | `A` — Coat | Same answer |
| Laya | `A` — Coat | `A` — Coat | Same answer |
| CalDec v1 | `A` — Coat | `A` — Coat | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `tombench/2cdd646690b4d21c29b8/examples/prose_control/clean-source_first_tombench_music_contexts_full_0155`

**Input fingerprint:** `24b2dec38399a71352da817716716cda007452db5a21fd46820e527d71a2bdb7`

| Change | Recorded version |
| --- | --- |
| Unrelated examples | No worked example (prose-control recipe) |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/retrieval/tombench-2cdd646690b4d21c29b8.md).
