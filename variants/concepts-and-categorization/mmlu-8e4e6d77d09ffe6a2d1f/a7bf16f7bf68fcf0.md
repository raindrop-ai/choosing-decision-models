# Misleading details · Add an unverified claim that conflicts with the evidence variant

[Original question](../../../questions/concepts-and-categorization/mmlu-8e4e6d77d09ffe6a2d1f.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> A reader thinks, "Budding is the listed exception to the asexual reproduction modes."

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
  "state": "A reader thinks, \"Budding is the listed exception to the asexual reproduction modes.\"",
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
| Strands Decider | `D` — meiosis | `C` — budding | Different answer |
| GLiNER2.5 Decide | `A` — sporulation | `C` — budding | Different answer |
| Laya | `B` — fission | `C` — budding | Different answer |
| CalDec v1 | `D` — meiosis | `C` — budding | Different answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `mmlu/8e4e6d77d09ffe6a2d1f/misleading_summary/misleading/clean-source_first_mmlu_reader_claims_full_0197`

**Input fingerprint:** `5dd608d8c1f1a352b275231133200b58ce9ea4f048e6046d90c9eed9e03d9fbd`

| Change | Recorded version |
| --- | --- |
| Misleading details | Add an unverified claim that conflicts with the evidence |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/concepts-and-categorization/mmlu-8e4e6d77d09ffe6a2d1f.md).
