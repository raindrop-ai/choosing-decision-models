# Unrelated examples · Add examples unrelated to the question variant

[Original question](../../../questions/social-cognition/tombench-af01864109c5ac190db3.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Xiao Li and Li Lei are strolling in the hallway. They see cabinets and boxes, and inside the cabinet, they find a vest. Li Lei leaves the hallway, and Xiao Li moves the vest to the box.
>
> 2 + 3 = 5.

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
  "state": "Xiao Li and Li Lei are strolling in the hallway. They see cabinets and boxes, and inside the cabinet, they find a vest. Li Lei leaves the hallway, and Xiao Li moves the vest to the box.\n\n2 + 3 = 5.",
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

**Variant ID:** `tombench/af01864109c5ac190db3/examples/irrelevant/clean-source_first_tombench_music_contexts_full_0155`

**Input fingerprint:** `5aa337b68bfe60d5623c053d14f0a95ad71e29a792237eb89af5659fd978c6a0`

| Change | Recorded version |
| --- | --- |
| Unrelated examples | Add examples unrelated to the question |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/social-cognition/tombench-af01864109c5ac190db3.md).
