# Unrelated examples · Add examples unrelated to the question variant

[Original question](../../../questions/information-seeking/questbench-7ee42f4b2058b3907c2f.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Alisa biked 12 miles per hour while carrying a backpack. Stanley biked at 10 miles per hour for 2.5 hours. How many miles did Alisa and Stanley bike in total, regardless of the weight of Alisa's backpack or the temperature during Stanley's ride?
>
> Uppercase: comet → COMET.

## Question

> Which missing variable should be asked about to solve this problem?

## Answer choices

- **A2.** Alisa&#x27;s time (hours)
- **X1.** Alisa&#x27;s backpack weight (pounds)
- **X2.** Temperature during Stanley&#x27;s ride (degrees)

**Reference answer:** `A2`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Alisa biked 12 miles per hour while carrying a backpack. Stanley biked at 10 miles per hour for 2.5 hours. How many miles did Alisa and Stanley bike in total, regardless of the weight of Alisa's backpack or the temperature during Stanley's ride?\n\nUppercase: comet → COMET.",
  "question": "Which missing variable should be asked about to solve this problem?",
  "choices": {
    "A2": "Alisa's time (hours)",
    "X1": "Alisa's backpack weight (pounds)",
    "X2": "Temperature during Stanley's ride (degrees)"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `A2` — Alisa&#x27;s time (hours) | `A2` — Alisa&#x27;s time (hours) | Same answer |
| Decider v1.1 | `A2` — Alisa&#x27;s time (hours) | `A2` — Alisa&#x27;s time (hours) | Same answer |
| Jev | `A2` — Alisa&#x27;s time (hours) | `A2` — Alisa&#x27;s time (hours) | Same answer |
| Microsoft Decision-1 | `A2` — Alisa&#x27;s time (hours) | `A2` — Alisa&#x27;s time (hours) | Same answer |
| Clef | `A2` — Alisa&#x27;s time (hours) | `A2` — Alisa&#x27;s time (hours) | Same answer |
| Luna Decisions | `A2` — Alisa&#x27;s time (hours) | `A2` — Alisa&#x27;s time (hours) | Same answer |
| Clef Flash | `A2` — Alisa&#x27;s time (hours) | `A2` — Alisa&#x27;s time (hours) | Same answer |
| Strands Decider | `A2` — Alisa&#x27;s time (hours) | `A2` — Alisa&#x27;s time (hours) | Same answer |
| GLiNER2.5 Decide | `X2` — Temperature during Stanley&#x27;s ride (degrees) | `X2` — Temperature during Stanley&#x27;s ride (degrees) | Same answer |
| Laya | `A2` — Alisa&#x27;s time (hours) | `A2` — Alisa&#x27;s time (hours) | Same answer |
| CalDec v1 | `A2` — Alisa&#x27;s time (hours) | `A2` — Alisa&#x27;s time (hours) | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `questbench/7ee42f4b2058b3907c2f/examples/irrelevant/clean-source_first_quest_literary_contexts_full_0079`

**Input fingerprint:** `2b6f8d844f61deba050a4dd0134ae3c4c63d22f794d7994f89767434ba5fa978`

| Change | Recorded version |
| --- | --- |
| Unrelated examples | Add examples unrelated to the question |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/information-seeking/questbench-7ee42f4b2058b3907c2f.md).
