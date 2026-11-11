# Evidence order · Present the evidence in reverse order variant

[Original question](../../../questions/concepts-and-categorization/mmlu-5562d36bb02e0bb2040a.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** question instructions.

[How the edits were constructed](../../../docs/variant-methods.md)

## Question

> For which of these two scenarios does the main character (who uses I/me/my) do something clearly morally wrong, according to ordinary moral standards in the US as of 2020? Scenario 2 | I was due to start work soon, so I went there. Scenario 1 | I watched the nurse grab a box of crackers and put them in her purse at work.

## Answer choices

- **A.** Wrong, Wrong
- **B.** Wrong, Not wrong
- **C.** Not wrong, Wrong
- **D.** Not wrong, Not wrong

**Reference answer:** `D`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "",
  "question": "For which of these two scenarios does the main character (who uses I/me/my) do something clearly morally wrong, according to ordinary moral standards in the US as of 2020? Scenario 2 | I was due to start work soon, so I went there. Scenario 1 | I watched the nurse grab a box of crackers and put them in her purse at work.",
  "choices": {
    "A": "Wrong, Wrong",
    "B": "Wrong, Not wrong",
    "C": "Not wrong, Wrong",
    "D": "Not wrong, Not wrong"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `D` — Not wrong, Not wrong | `D` — Not wrong, Not wrong | Same answer |
| Decider v1.1 | `D` — Not wrong, Not wrong | `D` — Not wrong, Not wrong | Same answer |
| Jev | `D` — Not wrong, Not wrong | `D` — Not wrong, Not wrong | Same answer |
| Microsoft Decision-1 | `D` — Not wrong, Not wrong | `D` — Not wrong, Not wrong | Same answer |
| Clef | `D` — Not wrong, Not wrong | `D` — Not wrong, Not wrong | Same answer |
| Luna Decisions | `D` — Not wrong, Not wrong | `D` — Not wrong, Not wrong | Same answer |
| Clef Flash | `D` — Not wrong, Not wrong | `D` — Not wrong, Not wrong | Same answer |
| Strands Decider | `B` — Wrong, Not wrong | `A` — Wrong, Wrong | Different answer |
| GLiNER2.5 Decide | `A` — Wrong, Wrong | `A` — Wrong, Wrong | Same answer |
| Laya | `A` — Wrong, Wrong | `A` — Wrong, Wrong | Same answer |
| CalDec v1 | `A` — Wrong, Wrong | `A` — Wrong, Wrong | Same answer |

**Ordering comparison:** literal requested source unit permutation. Only the exact matched comparison sets contribute to the reported ordering contrasts.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `mmlu/5562d36bb02e0bb2040a/presentation_order/reverse_presentation/clean-source_first_parallel_b_scenario_ID_alias_revision_0441`

**Input fingerprint:** `b9351090e9cb564124877019b02ea51301021faecd2a06510f6e0922f23e2817`

| Change | Recorded version |
| --- | --- |
| Evidence order | Present the evidence in reverse order |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/concepts-and-categorization/mmlu-5562d36bb02e0bb2040a.md).
