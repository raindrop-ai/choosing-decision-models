# Misleading details · Add an unverified claim that conflicts with the evidence variant

[Original question](../../../questions/concepts-and-categorization/socialiqa-2e44383838889746f4be.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Kai gave them a huge hug when they were feeling down.
>
> A reader thinks: «Kai ignored someone who was feeling down and offered no comfort.»

## Question

> How would you describe Kai?

## Answer choices

- **A.** uncaring
- **B.** affectionate
- **C.** rude

**Reference answer:** `B`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Kai gave them a huge hug when they were feeling down.\n\nA reader thinks: «Kai ignored someone who was feeling down and offered no comfort.»",
  "question": "How would you describe Kai?",
  "choices": {
    "A": "uncaring",
    "B": "affectionate",
    "C": "rude"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `B` — affectionate | `A` — uncaring | Different answer |
| Decider v1.1 | `B` — affectionate | `A` — uncaring | Different answer |
| Jev | `B` — affectionate | `B` — affectionate | Same answer |
| Microsoft Decision-1 | `B` — affectionate | `B` — affectionate | Same answer |
| Clef | `B` — affectionate | `B` — affectionate | Same answer |
| Luna Decisions | `B` — affectionate | `B` — affectionate | Same answer |
| Clef Flash | `B` — affectionate | `B` — affectionate | Same answer |
| Strands Decider | `B` — affectionate | `B` — affectionate | Same answer |
| GLiNER2.5 Decide | `B` — affectionate | `A` — uncaring | Different answer |
| Laya | `B` — affectionate | `A` — uncaring | Different answer |
| CalDec v1 | `B` — affectionate | `A` — uncaring | Different answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `socialiqa/2e44383838889746f4be/misleading_summary/misleading/clean-source_first_socialiqa_music_contexts_full_0158`

**Input fingerprint:** `ec14a2a4cbd870134a4e82ca362d837d678d67a1cab286cf447efbd521957b86`

| Change | Recorded version |
| --- | --- |
| Misleading details | Add an unverified claim that conflicts with the evidence |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/concepts-and-categorization/socialiqa-2e44383838889746f4be.md).
