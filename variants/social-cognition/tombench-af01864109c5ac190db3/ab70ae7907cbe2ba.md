# Irrelevant details · Add a larger amount of irrelevant detail variant

[Original question](../../../questions/social-cognition/tombench-af01864109c5ac190db3.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Xiao Li and Li Lei are strolling in the hallway. They see cabinets and boxes, and inside the cabinet, they find a vest. Li Lei leaves the hallway, and Xiao Li moves the vest to the box.
>
> The musical suite Merovan includes a refrain. Merovan uses a tonic cadence. Merovan includes rests. Merovan has sustained harmonies. Merovan has detached melodic notes. Merovan varies its accompaniment.

## Question

> Does Li Lei see anything in the box?

## Answer choices

- **A.** A vest
- **B.** Does not see
- **C.** Lockers
- **D.** Boxes

**Reference answer:** `B`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Xiao Li and Li Lei are strolling in the hallway. They see cabinets and boxes, and inside the cabinet, they find a vest. Li Lei leaves the hallway, and Xiao Li moves the vest to the box.\n\nThe musical suite Merovan includes a refrain. Merovan uses a tonic cadence. Merovan includes rests. Merovan has sustained harmonies. Merovan has detached melodic notes. Merovan varies its accompaniment.",
  "question": "Does Li Lei see anything in the box?",
  "choices": {
    "A": "A vest",
    "B": "Does not see",
    "C": "Lockers",
    "D": "Boxes"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `B` — Does not see | `B` — Does not see | Same answer |
| Decider v1.1 | `B` — Does not see | `B` — Does not see | Same answer |
| Jev | `B` — Does not see | `B` — Does not see | Same answer |
| Microsoft Decision-1 | `B` — Does not see | `B` — Does not see | Same answer |
| Clef | `B` — Does not see | `B` — Does not see | Same answer |
| Luna Decisions | `B` — Does not see | `B` — Does not see | Same answer |
| Clef Flash | `B` — Does not see | `B` — Does not see | Same answer |
| Strands Decider | `A` — A vest | `A` — A vest | Same answer |
| GLiNER2.5 Decide | `A` — A vest | `A` — A vest | Same answer |
| Laya | `A` — A vest | `A` — A vest | Same answer |
| CalDec v1 | `A` — A vest | `A` — A vest | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `tombench/af01864109c5ac190db3/irrelevant_details/high/clean-source_first_tombench_music_contexts_full_0155`

**Input fingerprint:** `d925d2798bb256a4ec922ee13476e81eee1f60f6dc4df9e217e0ef22f3cdb889`

| Change | Recorded version |
| --- | --- |
| Irrelevant details | Add a larger amount of irrelevant detail |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/social-cognition/tombench-af01864109c5ac190db3.md).
