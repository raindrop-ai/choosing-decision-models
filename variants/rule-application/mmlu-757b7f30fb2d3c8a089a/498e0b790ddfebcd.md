# Evidence order · Present the evidence in reverse order variant

[Original question](../../../questions/rule-application/mmlu-757b7f30fb2d3c8a089a.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** question instructions.

[How the edits were constructed](../../../docs/variant-methods.md)

## Question

> Use indirect truth tables to determine whether the following argument is valid. If the argument is invalid, choose an option which presents a counterexample. (There may be other counterexamples as well.)
> G ⊃ ~F
> E ⊃ F / ~G ∨ ~E

## Answer choices

- **A.** Valid
- **B.** Invalid. Counterexample when E, F, and G are true
- **C.** Invalid. Counterexample when E and G are true and F is false
- **D.** Invalid. Counterexample when F and G are true and E is false

**Reference answer:** `A`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "",
  "question": "Use indirect truth tables to determine whether the following argument is valid. If the argument is invalid, choose an option which presents a counterexample. (There may be other counterexamples as well.)\nG ⊃ ~F\nE ⊃ F / ~G ∨ ~E",
  "choices": {
    "A": "Valid",
    "B": "Invalid. Counterexample when E, F, and G are true",
    "C": "Invalid. Counterexample when E and G are true and F is false",
    "D": "Invalid. Counterexample when F and G are true and E is false"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `A` — Valid | `A` — Valid | Same answer |
| Decider v1.1 | `A` — Valid | `A` — Valid | Same answer |
| Jev | `A` — Valid | `A` — Valid | Same answer |
| Microsoft Decision-1 | `A` — Valid | `A` — Valid | Same answer |
| Clef | `A` — Valid | `A` — Valid | Same answer |
| Luna Decisions | `A` — Valid | `A` — Valid | Same answer |
| Clef Flash | `A` — Valid | `A` — Valid | Same answer |
| Strands Decider | `B` — Invalid. Counterexample when E, F, and G are true | `C` — Invalid. Counterexample when E and G are true and F is false | Different answer |
| GLiNER2.5 Decide | `A` — Valid | `A` — Valid | Same answer |
| Laya | `A` — Valid | `A` — Valid | Same answer |
| CalDec v1 | `A` — Valid | `A` — Valid | Same answer |

**Ordering comparison:** literal requested source unit permutation. Only the exact matched comparison sets contribute to the reported ordering contrasts.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `mmlu/757b7f30fb2d3c8a089a/presentation_order/reverse_presentation/clean-source_first_parallel_b_operations_0302`

**Input fingerprint:** `49745b4026d67303afe4568abaa830ac3d875be52c57e61d87666a767599718c`

| Change | Recorded version |
| --- | --- |
| Evidence order | Present the evidence in reverse order |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/rule-application/mmlu-757b7f30fb2d3c8a089a.md).
