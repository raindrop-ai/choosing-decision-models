# Unrelated examples · Add examples unrelated to the question variant

[Original question](../../../questions/information-seeking/questbench-70f3e0ce25a345f3b019.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> In a family, there are 2 brothers and 3 sisters. All sisters are the same age. One of the brothers is 12 years old, which is half the age of the older brother. The family also has a pet dog that is years old and a pet parrot that is years old. What is the total age of all these siblings, not including the ages of the pets?
>
> Uppercase: comet → COMET.

## Question

> Which missing variable should be asked about to solve this problem?

## Answer choices

- **B.** SECOND SISTER&#x27;S AGE
- **F.** PET DOG&#x27;S AGE
- **G.** PET PARROT&#x27;S AGE

**Reference answer:** `B`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "In a family, there are 2 brothers and 3 sisters. All sisters are the same age. One of the brothers is 12 years old, which is half the age of the older brother. The family also has a pet dog that is years old and a pet parrot that is years old. What is the total age of all these siblings, not including the ages of the pets?\n\nUppercase: comet → COMET.",
  "question": "Which missing variable should be asked about to solve this problem?",
  "choices": {
    "B": "SECOND SISTER'S AGE",
    "F": "PET DOG'S AGE",
    "G": "PET PARROT'S AGE"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `B` — SECOND SISTER&#x27;S AGE | `B` — SECOND SISTER&#x27;S AGE | Same answer |
| Decider v1.1 | `B` — SECOND SISTER&#x27;S AGE | `B` — SECOND SISTER&#x27;S AGE | Same answer |
| Jev | `B` — SECOND SISTER&#x27;S AGE | `B` — SECOND SISTER&#x27;S AGE | Same answer |
| Microsoft Decision-1 | `B` — SECOND SISTER&#x27;S AGE | `B` — SECOND SISTER&#x27;S AGE | Same answer |
| Clef | `B` — SECOND SISTER&#x27;S AGE | `B` — SECOND SISTER&#x27;S AGE | Same answer |
| Luna Decisions | `B` — SECOND SISTER&#x27;S AGE | `B` — SECOND SISTER&#x27;S AGE | Same answer |
| Clef Flash | `B` — SECOND SISTER&#x27;S AGE | `B` — SECOND SISTER&#x27;S AGE | Same answer |
| Strands Decider | `B` — SECOND SISTER&#x27;S AGE | `B` — SECOND SISTER&#x27;S AGE | Same answer |
| GLiNER2.5 Decide | `F` — PET DOG&#x27;S AGE | `G` — PET PARROT&#x27;S AGE | Different answer |
| Laya | `F` — PET DOG&#x27;S AGE | `B` — SECOND SISTER&#x27;S AGE | Different answer |
| CalDec v1 | `B` — SECOND SISTER&#x27;S AGE | `B` — SECOND SISTER&#x27;S AGE | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `questbench/70f3e0ce25a345f3b019/examples/irrelevant/clean-source_first_quest_literary_contexts_full_0079`

**Input fingerprint:** `f645cd7ea23b59b477380d21774548998e9b3759335255c63abe112aaf2d8d78`

| Change | Recorded version |
| --- | --- |
| Unrelated examples | Add examples unrelated to the question |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/information-seeking/questbench-70f3e0ce25a345f3b019.md).
