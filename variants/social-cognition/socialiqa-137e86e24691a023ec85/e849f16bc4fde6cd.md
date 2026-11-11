# Misleading details · Add an unverified claim that conflicts with the evidence variant

[Original question](../../../questions/social-cognition/socialiqa-137e86e24691a023ec85.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Addison's fish died recently and Addison wanted to buy a replacement.
>
> A reader thinks: «Addison wants a replacement in order to get a frog.»

## Question

> Why did Addison do this?

## Answer choices

- **A.** fill her aquarium
- **B.** get a frog
- **C.** discover that their fish was dead

**Reference answer:** `A`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Addison's fish died recently and Addison wanted to buy a replacement.\n\nA reader thinks: «Addison wants a replacement in order to get a frog.»",
  "question": "Why did Addison do this?",
  "choices": {
    "A": "fill her aquarium",
    "B": "get a frog",
    "C": "discover that their fish was dead"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `A` — fill her aquarium | `A` — fill her aquarium | Same answer |
| Decider v1.1 | `A` — fill her aquarium | `A` — fill her aquarium | Same answer |
| Jev | `A` — fill her aquarium | `A` — fill her aquarium | Same answer |
| Microsoft Decision-1 | `C` — discover that their fish was dead | `A` — fill her aquarium | Different answer |
| Clef | `A` — fill her aquarium | `A` — fill her aquarium | Same answer |
| Luna Decisions | `A` — fill her aquarium | `A` — fill her aquarium | Same answer |
| Clef Flash | `A` — fill her aquarium | `A` — fill her aquarium | Same answer |
| Strands Decider | `C` — discover that their fish was dead | `C` — discover that their fish was dead | Same answer |
| GLiNER2.5 Decide | `C` — discover that their fish was dead | `B` — get a frog | Different answer |
| Laya | `A` — fill her aquarium | `B` — get a frog | Different answer |
| CalDec v1 | `C` — discover that their fish was dead | `B` — get a frog | Different answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `socialiqa/137e86e24691a023ec85/misleading_summary/misleading/clean-source_first_socialiqa_music_contexts_full_0158`

**Input fingerprint:** `62a41bab212905f1908a0359f3aec4c285a598c865b7d7d4419a3e00c06ab92e`

| Change | Recorded version |
| --- | --- |
| Misleading details | Add an unverified claim that conflicts with the evidence |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/social-cognition/socialiqa-137e86e24691a023ec85.md).
