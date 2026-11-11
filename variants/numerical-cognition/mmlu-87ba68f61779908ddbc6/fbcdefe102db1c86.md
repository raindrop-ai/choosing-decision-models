# Evidence order · Present the evidence in reverse order variant

[Original question](../../../questions/numerical-cognition/mmlu-87ba68f61779908ddbc6.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** question instructions.

[How the edits were constructed](../../../docs/variant-methods.md)

## Question

> The theater sold 500 tickets to the movie. The theater collected $6 for each ticket sold to a movie. The expression below can be used to find how much money the theater collected for the tickets. 6 × 500 Which expression can also be used to find how much money the theater collected for the tickets?

## Answer choices

- **A.** 30 × 10^1
- **B.** 30 × 10^3
- **C.** (6 × 5) × 10^2
- **D.** (6 × 5) × 10^3

**Reference answer:** `C`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "",
  "question": "The theater sold 500 tickets to the movie. The theater collected $6 for each ticket sold to a movie. The expression below can be used to find how much money the theater collected for the tickets. 6 × 500 Which expression can also be used to find how much money the theater collected for the tickets?",
  "choices": {
    "A": "30 × 10^1",
    "B": "30 × 10^3",
    "C": "(6 × 5) × 10^2",
    "D": "(6 × 5) × 10^3"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `C` — (6 × 5) × 10^2 | `C` — (6 × 5) × 10^2 | Same answer |
| Decider v1.1 | `C` — (6 × 5) × 10^2 | `C` — (6 × 5) × 10^2 | Same answer |
| Jev | `C` — (6 × 5) × 10^2 | `C` — (6 × 5) × 10^2 | Same answer |
| Microsoft Decision-1 | `C` — (6 × 5) × 10^2 | `C` — (6 × 5) × 10^2 | Same answer |
| Clef | `C` — (6 × 5) × 10^2 | `C` — (6 × 5) × 10^2 | Same answer |
| Luna Decisions | `C` — (6 × 5) × 10^2 | `C` — (6 × 5) × 10^2 | Same answer |
| Clef Flash | `C` — (6 × 5) × 10^2 | `C` — (6 × 5) × 10^2 | Same answer |
| Strands Decider | `C` — (6 × 5) × 10^2 | `C` — (6 × 5) × 10^2 | Same answer |
| GLiNER2.5 Decide | `D` — (6 × 5) × 10^3 | `D` — (6 × 5) × 10^3 | Same answer |
| Laya | `C` — (6 × 5) × 10^2 | `C` — (6 × 5) × 10^2 | Same answer |
| CalDec v1 | `C` — (6 × 5) × 10^2 | `C` — (6 × 5) × 10^2 | Same answer |

**Ordering comparison:** coupled wording reference chronology or representation. Only the exact matched comparison sets contribute to the reported ordering contrasts.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `mmlu/87ba68f61779908ddbc6/presentation_order/reverse_presentation/clean-source_first_parallel_b_reference_constrained_orders_0360`

**Input fingerprint:** `cea0f43aac8b3eb34e8d4cd4b49b17d92e78bf8cdbb2dece4ebbd12858730460`

| Change | Recorded version |
| --- | --- |
| Evidence order | Present the evidence in reverse order |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/numerical-cognition/mmlu-87ba68f61779908ddbc6.md).
