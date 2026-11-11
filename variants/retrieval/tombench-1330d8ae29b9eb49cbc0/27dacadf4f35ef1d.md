# Evidence order · Present the evidence in a shuffled order variant

[Original question](../../../questions/retrieval/tombench-1330d8ae29b9eb49cbc0.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> After Xiao Bei opens the suitcase, there is no corn inside the suitcase
> Xiao Bei closes the suitcase and puts it back in its place
> Xiao Ming enters the parking lot and sees the suitcase.
> Before that, Xiao Bei finds a suitcase in the parking lot
> the label on the suitcase is corn
> Xiao Bei cannot see what is inside the suitcase
> Xiao Bei opens the suitcase and finds a pencil

## Question

> What is inside the suitcase?

## Answer choices

- **A.** Pencil
- **B.** Compass
- **C.** Corn
- **D.** Watch

**Reference answer:** `A`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "After Xiao Bei opens the suitcase, there is no corn inside the suitcase\nXiao Bei closes the suitcase and puts it back in its place\nXiao Ming enters the parking lot and sees the suitcase.\nBefore that, Xiao Bei finds a suitcase in the parking lot\nthe label on the suitcase is corn\nXiao Bei cannot see what is inside the suitcase\nXiao Bei opens the suitcase and finds a pencil",
  "question": "What is inside the suitcase?",
  "choices": {
    "A": "Pencil",
    "B": "Compass",
    "C": "Corn",
    "D": "Watch"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `A` — Pencil | `A` — Pencil | Same answer |
| Decider v1.1 | `A` — Pencil | `A` — Pencil | Same answer |
| Jev | `A` — Pencil | `A` — Pencil | Same answer |
| Microsoft Decision-1 | `A` — Pencil | `A` — Pencil | Same answer |
| Clef | `A` — Pencil | `A` — Pencil | Same answer |
| Luna Decisions | `A` — Pencil | `A` — Pencil | Same answer |
| Clef Flash | `A` — Pencil | `A` — Pencil | Same answer |
| Strands Decider | `A` — Pencil | `A` — Pencil | Same answer |
| GLiNER2.5 Decide | `C` — Corn | `C` — Corn | Same answer |
| Laya | `A` — Pencil | `A` — Pencil | Same answer |
| CalDec v1 | `A` — Pencil | `A` — Pencil | Same answer |

**Ordering comparison:** coupled wording reference chronology or representation. Only the exact matched comparison sets contribute to the reported ordering contrasts.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `tombench/1330d8ae29b9eb49cbc0/presentation_order/shuffled_presentation/clean-source_first_parallel_b_retrospective_batch_0397`

**Input fingerprint:** `740f5fc2d351aff6e8db505c3b1f672d21ed9404fe8fa3936d684df85cfde0d7`

| Change | Recorded version |
| --- | --- |
| Evidence order | Present the evidence in a shuffled order |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/retrieval/tombench-1330d8ae29b9eb49cbc0.md).
