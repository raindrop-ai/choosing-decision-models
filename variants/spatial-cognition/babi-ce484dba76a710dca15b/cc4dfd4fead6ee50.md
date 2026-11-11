# Similar distractors · Add fewer similar but irrelevant items variant

[Original question](../../../questions/spatial-cognition/babi-ce484dba76a710dca15b.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> The garden is south of the kitchen.
> The bathroom is west of the office.
> The bathroom is east of the bedroom.
> The hallway is south of the bathroom.
> The garden is north of the office.
> The atrium is north of the ballroom. The ballroom is west of the observatory.

## Question

> How do you go from the bathroom to the garden?

## Answer choices

- **A.** e,n
- **B.** s,s
- **C.** e,e
- **D.** w,s

**Reference answer:** `A`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "The garden is south of the kitchen.\nThe bathroom is west of the office.\nThe bathroom is east of the bedroom.\nThe hallway is south of the bathroom.\nThe garden is north of the office.\nThe atrium is north of the ballroom. The ballroom is west of the observatory.",
  "question": "How do you go from the bathroom to the garden?",
  "choices": {
    "A": "e,n",
    "B": "s,s",
    "C": "e,e",
    "D": "w,s"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `A` — e,n | `A` — e,n | Same answer |
| Decider v1.1 | `A` — e,n | `A` — e,n | Same answer |
| Jev | `C` — e,e | `A` — e,n | Different answer |
| Microsoft Decision-1 | `A` — e,n | `A` — e,n | Same answer |
| Clef | `B` — s,s | `B` — s,s | Same answer |
| Luna Decisions | `A` — e,n | `A` — e,n | Same answer |
| Clef Flash | `B` — s,s | `B` — s,s | Same answer |
| Strands Decider | `A` — e,n | `A` — e,n | Same answer |
| GLiNER2.5 Decide | `A` — e,n | `A` — e,n | Same answer |
| Laya | `C` — e,e | `C` — e,e | Same answer |
| CalDec v1 | `A` — e,n | `A` — e,n | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `babi/ce484dba76a710dca15b/similar_distractors/low/clean-source_first_route_distractors_full_0143`

**Input fingerprint:** `2be97a27d5285d39aee6ee579a442b2f32cde477876751247c9a10dd0b0b6a04`

| Change | Recorded version |
| --- | --- |
| Similar distractors | Add fewer similar but irrelevant items |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/spatial-cognition/babi-ce484dba76a710dca15b.md).
