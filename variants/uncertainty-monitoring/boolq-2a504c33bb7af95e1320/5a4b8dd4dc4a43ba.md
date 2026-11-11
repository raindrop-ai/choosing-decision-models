# Evidence order · Present the evidence in reverse order variant

[Original question](../../../questions/uncertainty-monitoring/boolq-2a504c33bb7af95e1320.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> A replacement throne based on the original Peacock Throne was commissioned afterwards and existed until the Indian Rebellion of 1857.
> The original Peacock Throne was subsequently captured and taken as a war trophy in 1739 by the Persian emperor Nadir Shah, and has been lost since.
> The Peacock Throne was a famous jeweled throne that was the seat of the Mughal emperors of India. It was commissioned in the early 17th century by emperor Shah Jahan and was located in the Diwan-i-Khas (Hall of Private Audiences) in the Red Fort of Delhi.

## Question

> do you know the place where the peacock throne is now

## Answer choices

- **yes.** Yes
- **no.** No

**Reference answer:** `no`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "A replacement throne based on the original Peacock Throne was commissioned afterwards and existed until the Indian Rebellion of 1857.\nThe original Peacock Throne was subsequently captured and taken as a war trophy in 1739 by the Persian emperor Nadir Shah, and has been lost since.\nThe Peacock Throne was a famous jeweled throne that was the seat of the Mughal emperors of India. It was commissioned in the early 17th century by emperor Shah Jahan and was located in the Diwan-i-Khas (Hall of Private Audiences) in the Red Fort of Delhi.",
  "question": "do you know the place where the peacock throne is now",
  "choices": {
    "yes": "Yes",
    "no": "No"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `no` — No | `no` — No | Same answer |
| Decider v1.1 | `no` — No | `no` — No | Same answer |
| Jev | `no` — No | `no` — No | Same answer |
| Microsoft Decision-1 | `no` — No | `no` — No | Same answer |
| Clef | `no` — No | `no` — No | Same answer |
| Luna Decisions | `yes` — Yes | `yes` — Yes | Same answer |
| Clef Flash | `no` — No | `no` — No | Same answer |
| Strands Decider | `no` — No | `no` — No | Same answer |
| GLiNER2.5 Decide | `yes` — Yes | `yes` — Yes | Same answer |
| Laya | `no` — No | `no` — No | Same answer |
| CalDec v1 | `no` — No | `no` — No | Same answer |

**Ordering comparison:** coupled wording reference chronology or representation. Only the exact matched comparison sets contribute to the reported ordering contrasts.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `boolq/2a504c33bb7af95e1320/presentation_order/reverse_presentation/clean-source_first_parallel_b_residual_reference_questions_0398`

**Input fingerprint:** `dc49a9178284b242103e2885b9353b578f0529b62d5f998ef741f423d78ff0fe`

| Change | Recorded version |
| --- | --- |
| Evidence order | Present the evidence in reverse order |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/uncertainty-monitoring/boolq-2a504c33bb7af95e1320.md).
