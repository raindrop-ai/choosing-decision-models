# Similar distractors · Add more similar but irrelevant items variant

[Original question](../../../questions/state-tracking-and-updating/tombench-f081edc079ce9161fefc.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> «In a different workshop, Rina moves a sponge from a handbag into a storage locker.»
>
> «At another hall, Daro puts a sponge in a briefcase before leaving.»
>
> «In a separate room, Mira leaves a box containing a folded cloth beside an empty handbag.»
>
> Xiao Ming and Zhang Wei are wandering in the hall, they see a handbag and a box, they find a sponge in the handbag, Zhang Wei leaves the hall, Xiao Ming moves the sponge to the box.

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
  "state": "«In a different workshop, Rina moves a sponge from a handbag into a storage locker.»\n\n«At another hall, Daro puts a sponge in a briefcase before leaving.»\n\n«In a separate room, Mira leaves a box containing a folded cloth beside an empty handbag.»\n\nXiao Ming and Zhang Wei are wandering in the hall, they see a handbag and a box, they find a sponge in the handbag, Zhang Wei leaves the hall, Xiao Ming moves the sponge to the box.",
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
| GLiNER2.5 Decide | `A` — Box | `A` — Box | Same answer |
| Laya | `A` — Box | `A` — Box | Same answer |
| CalDec v1 | `A` — Box | `A` — Box | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `tombench/f081edc079ce9161fefc/similar_distractors/high/clean-source_first_tombench_near_scenes_full_0215`

**Input fingerprint:** `5f6f7e6de8904e1c3e2c4b752b61f7103e1ac8a692bfa3ec32f28707133bec4e`

| Change | Recorded version |
| --- | --- |
| Similar distractors | Add more similar but irrelevant items |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/state-tracking-and-updating/tombench-f081edc079ce9161fefc.md).
