# Similar distractors · Add fewer similar but irrelevant items variant

[Original question](../../../questions/concepts-and-categorization/mmlu-8e4e6d77d09ffe6a2d1f.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> «In a separate fictional teaching display, one tray contains drawings of a cell dividing into two sections.»

## Question

> All of the following are modes of asexual reproduction EXCEPT

## Answer choices

- **A.** sporulation
- **B.** fission
- **C.** budding
- **D.** meiosis

**Reference answer:** `D`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "«In a separate fictional teaching display, one tray contains drawings of a cell dividing into two sections.»",
  "question": "All of the following are modes of asexual reproduction EXCEPT",
  "choices": {
    "A": "sporulation",
    "B": "fission",
    "C": "budding",
    "D": "meiosis"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `D` — meiosis | `D` — meiosis | Same answer |
| Decider v1.1 | `D` — meiosis | `D` — meiosis | Same answer |
| Jev | `D` — meiosis | `D` — meiosis | Same answer |
| Microsoft Decision-1 | `D` — meiosis | `D` — meiosis | Same answer |
| Clef | `D` — meiosis | `D` — meiosis | Same answer |
| Luna Decisions | `D` — meiosis | `D` — meiosis | Same answer |
| Clef Flash | `D` — meiosis | `D` — meiosis | Same answer |
| Strands Decider | `D` — meiosis | `D` — meiosis | Same answer |
| GLiNER2.5 Decide | `A` — sporulation | `D` — meiosis | Different answer |
| Laya | `B` — fission | `D` — meiosis | Different answer |
| CalDec v1 | `D` — meiosis | `C` — budding | Different answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `mmlu/8e4e6d77d09ffe6a2d1f/similar_distractors/low/clean-source_first_parallel_b_near_accounts_0301`

**Input fingerprint:** `80ddab8e027d26f444e030ccb9d9180b9a04cd84a21412ef875924389b72c9fc`

| Change | Recorded version |
| --- | --- |
| Similar distractors | Add fewer similar but irrelevant items |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/concepts-and-categorization/mmlu-8e4e6d77d09ffe6a2d1f.md).
