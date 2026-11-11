# Evidence order · Present the evidence in a shuffled order variant

[Original question](../../../questions/state-tracking-and-updating/tombench-f081edc079ce9161fefc.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> After Xiao Ming and Zhang Wei find the sponge, Zhang Wei leaves the hall
> Xiao Ming moves the sponge to the box.
> Before that, Xiao Ming and Zhang Wei are wandering in the hall
> they see a handbag and a box
> they find a sponge in the handbag

## Question

> Where is the sponge now?

## Answer choices

- **A.** Box
- **B.** Handbag
- **C.** Storage locker
- **D.** Briefcase

**Reference answer:** `A`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "After Xiao Ming and Zhang Wei find the sponge, Zhang Wei leaves the hall\nXiao Ming moves the sponge to the box.\nBefore that, Xiao Ming and Zhang Wei are wandering in the hall\nthey see a handbag and a box\nthey find a sponge in the handbag",
  "question": "Where is the sponge now?",
  "choices": {
    "A": "Box",
    "B": "Handbag",
    "C": "Storage locker",
    "D": "Briefcase"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `A` — Box | `A` — Box | Same answer |
| Decider v1.1 | `A` — Box | `A` — Box | Same answer |
| Jev | `A` — Box | `A` — Box | Same answer |
| Microsoft Decision-1 | `A` — Box | `A` — Box | Same answer |
| Clef | `A` — Box | `A` — Box | Same answer |
| Luna Decisions | `A` — Box | `A` — Box | Same answer |
| Clef Flash | `A` — Box | `A` — Box | Same answer |
| Strands Decider | `A` — Box | `A` — Box | Same answer |
| GLiNER2.5 Decide | `A` — Box | `B` — Handbag | Different answer |
| Laya | `A` — Box | `A` — Box | Same answer |
| CalDec v1 | `A` — Box | `A` — Box | Same answer |

**Ordering comparison:** coupled wording reference chronology or representation. Only the exact matched comparison sets contribute to the reported ordering contrasts.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `tombench/f081edc079ce9161fefc/presentation_order/shuffled_presentation/clean-source_first_parallel_b_retrospective_batch_0397`

**Input fingerprint:** `609fbe700c3672fa01584d13e4f444ff5b283eb6ba82b0edec23c99ee1a0f107`

| Change | Recorded version |
| --- | --- |
| Evidence order | Present the evidence in a shuffled order |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/state-tracking-and-updating/tombench-f081edc079ce9161fefc.md).
