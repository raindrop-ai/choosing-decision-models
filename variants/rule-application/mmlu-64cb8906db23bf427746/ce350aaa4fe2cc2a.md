# Unrelated examples · Add examples unrelated to the question variant

[Original question](../../../questions/rule-application/mmlu-64cb8906db23bf427746.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Capitalize the first letter: harbor → Harbor.

## Question

>  Construct a complete truth table for the following argument. Then, using the truth table, determine whether the argument is valid or invalid. If the argument is invalid, choose an option which presents a counterexample. (There may be other counterexamples as well.)
> T ∨ U
> W · T / U

## Answer choices

- **A.** Valid
- **B.** Invalid. Counterexample when T and W are true and U is false
- **C.** Invalid. Counterexample when T is true and W and U are false
- **D.** Invalid. Counterexample when W is true and T and U are false

**Reference answer:** `B`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Capitalize the first letter: harbor → Harbor.",
  "question": " Construct a complete truth table for the following argument. Then, using the truth table, determine whether the argument is valid or invalid. If the argument is invalid, choose an option which presents a counterexample. (There may be other counterexamples as well.)\nT ∨ U\nW · T / U",
  "choices": {
    "A": "Valid",
    "B": "Invalid. Counterexample when T and W are true and U is false",
    "C": "Invalid. Counterexample when T is true and W and U are false",
    "D": "Invalid. Counterexample when W is true and T and U are false"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `B` — Invalid. Counterexample when T and W are true and U is false | `B` — Invalid. Counterexample when T and W are true and U is false | Same answer |
| Decider v1.1 | `B` — Invalid. Counterexample when T and W are true and U is false | `B` — Invalid. Counterexample when T and W are true and U is false | Same answer |
| Jev | `B` — Invalid. Counterexample when T and W are true and U is false | `B` — Invalid. Counterexample when T and W are true and U is false | Same answer |
| Microsoft Decision-1 | `B` — Invalid. Counterexample when T and W are true and U is false | `B` — Invalid. Counterexample when T and W are true and U is false | Same answer |
| Clef | `D` — Invalid. Counterexample when W is true and T and U are false | `B` — Invalid. Counterexample when T and W are true and U is false | Different answer |
| Luna Decisions | `A` — Valid | `A` — Valid | Same answer |
| Clef Flash | `A` — Valid | `A` — Valid | Same answer |
| Strands Decider | `B` — Invalid. Counterexample when T and W are true and U is false | `B` — Invalid. Counterexample when T and W are true and U is false | Same answer |
| GLiNER2.5 Decide | `A` — Valid | `A` — Valid | Same answer |
| Laya | `A` — Valid | `A` — Valid | Same answer |
| CalDec v1 | `A` — Valid | `A` — Valid | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `mmlu/64cb8906db23bf427746/examples/irrelevant/clean-source_first_mmlu_other_short_contexts_full_0100`

**Input fingerprint:** `f5b282a93abf0bc9cc7c7684774c038caef750535e16eac5603b492c5f641f24`

| Change | Recorded version |
| --- | --- |
| Unrelated examples | Add examples unrelated to the question |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/rule-application/mmlu-64cb8906db23bf427746.md).
