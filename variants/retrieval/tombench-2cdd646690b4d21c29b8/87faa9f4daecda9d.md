# Irrelevant details · Add a small amount of irrelevant detail variant

[Original question](../../../questions/retrieval/tombench-2cdd646690b4d21c29b8.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Xiao Li finds a storage cabinet in the study, the label on the storage cabinet is carrot, Xiao Li cannot see what is inside the storage cabinet, Xiao Li opens the storage cabinet and finds a coat, there are no carrots in the storage cabinet, Xiao Li closes the storage cabinet and puts it back in its place, Xiao Zhang enters the study and sees the storage cabinet.
>
> The musical suite Merovan includes a refrain.

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
  "state": "Xiao Li finds a storage cabinet in the study, the label on the storage cabinet is carrot, Xiao Li cannot see what is inside the storage cabinet, Xiao Li opens the storage cabinet and finds a coat, there are no carrots in the storage cabinet, Xiao Li closes the storage cabinet and puts it back in its place, Xiao Zhang enters the study and sees the storage cabinet.\n\nThe musical suite Merovan includes a refrain.",
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
| Laya | `A` — Coat | `C` — Carrot | Different answer |
| CalDec v1 | `A` — Coat | `A` — Coat | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `tombench/2cdd646690b4d21c29b8/irrelevant_details/low/clean-source_first_tombench_music_contexts_full_0155`

**Input fingerprint:** `356fb351936eea83509c8475dfa06060138ff40ee97ae0bf43b36af1bfaf8593`

| Change | Recorded version |
| --- | --- |
| Irrelevant details | Add a small amount of irrelevant detail |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/retrieval/tombench-2cdd646690b4d21c29b8.md).
