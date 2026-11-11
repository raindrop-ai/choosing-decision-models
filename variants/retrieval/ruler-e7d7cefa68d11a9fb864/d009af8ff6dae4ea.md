# Misleading details · Add an unverified claim that conflicts with the evidence variant

[Original question](../../../questions/retrieval/ruler-e7d7cefa68d11a9fb864.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Use the authoritative record. Summaries are unverified claims about that record. Separate records are independent.
> The code assigned to record-10115 is 7312345.
> A reader thinks: «The code assigned to record-10115 is 7312011.»

## Question

> Which code is assigned to record-10115?

## Answer choices

- **A.** 7312011
- **B.** 7312183
- **C.** 7312244
- **D.** 7312345
- **unknown.** Insufficient information

**Reference answer:** `D`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Use the authoritative record. Summaries are unverified claims about that record. Separate records are independent.\nThe code assigned to record-10115 is 7312345.\nA reader thinks: «The code assigned to record-10115 is 7312011.»",
  "question": "Which code is assigned to record-10115?",
  "choices": {
    "A": "7312011",
    "B": "7312183",
    "C": "7312244",
    "D": "7312345",
    "unknown": "Insufficient information"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `D` — 7312345 | `D` — 7312345 | Same answer |
| Decider v1.1 | `D` — 7312345 | `D` — 7312345 | Same answer |
| Jev | `D` — 7312345 | `D` — 7312345 | Same answer |
| Microsoft Decision-1 | `D` — 7312345 | `D` — 7312345 | Same answer |
| Clef | `D` — 7312345 | `D` — 7312345 | Same answer |
| Luna Decisions | `D` — 7312345 | `D` — 7312345 | Same answer |
| Clef Flash | `D` — 7312345 | `D` — 7312345 | Same answer |
| Strands Decider | `D` — 7312345 | `D` — 7312345 | Same answer |
| GLiNER2.5 Decide | `D` — 7312345 | `D` — 7312345 | Same answer |
| Laya | `D` — 7312345 | `D` — 7312345 | Same answer |
| CalDec v1 | `D` — 7312345 | `D` — 7312345 | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `ruler/e7d7cefa68d11a9fb864/misleading_summary/misleading/clean-source_first_ruler_reader_repairs_full_0141`

**Input fingerprint:** `a16d296fadf5752ee9ecc5da819d1435cd59b370bfc614688e67bdefd23c335d`

| Change | Recorded version |
| --- | --- |
| Misleading details | Add an unverified claim that conflicts with the evidence |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/retrieval/ruler-e7d7cefa68d11a9fb864.md).
