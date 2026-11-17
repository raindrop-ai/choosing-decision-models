# Unrelated examples · Add examples unrelated to the question variant

[Original question](../../../questions/learning-and-induction/list_functions-3e2239ccffbdb2c9f6ba.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> \[{"input": "\[3, 5, 4\]", "output": "\[5, 7, 6\]"}, {"input": "\[7, 5, 3, 6, 1, 4, 0\]", "output": "\[9, 7, 5, 8, 3, 6, 2\]"}, {"input": "\[1, 5, 4, 7, 0\]", "output": "\[3, 7, 6, 9, 2\]"}, {"input": "\[5, 3, 0, 1\]", "output": "\[7, 5, 2, 3\]"}, {"input": "\[6, 5, 7\]", "output": "\[8, 7, 9\]"}, {"input": "\[7, 6, 0, 3\]", "output": "\[9, 8, 2, 5\]"}, {"input": "\[1, 0, 6, 3, 2, 5\]", "output": "\[3, 2, 8, 5, 4, 7\]"}, {"input": "\[3, 7, 6, 1\]", "output": "\[5, 9, 8, 3\]"}\]
> Uppercase: meadow → MEADOW

## Question

> Apply the same inferred rule to this new input: \[2\]

## Answer choices

- **A.** \[4\]
- **B.** \[1\]
- **C.** \[3\]
- **D.** \[2\]

**Reference answer:** `A`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "[{\"input\": \"[3, 5, 4]\", \"output\": \"[5, 7, 6]\"}, {\"input\": \"[7, 5, 3, 6, 1, 4, 0]\", \"output\": \"[9, 7, 5, 8, 3, 6, 2]\"}, {\"input\": \"[1, 5, 4, 7, 0]\", \"output\": \"[3, 7, 6, 9, 2]\"}, {\"input\": \"[5, 3, 0, 1]\", \"output\": \"[7, 5, 2, 3]\"}, {\"input\": \"[6, 5, 7]\", \"output\": \"[8, 7, 9]\"}, {\"input\": \"[7, 6, 0, 3]\", \"output\": \"[9, 8, 2, 5]\"}, {\"input\": \"[1, 0, 6, 3, 2, 5]\", \"output\": \"[3, 2, 8, 5, 4, 7]\"}, {\"input\": \"[3, 7, 6, 1]\", \"output\": \"[5, 9, 8, 3]\"}]\nUppercase: meadow → MEADOW",
  "question": "Apply the same inferred rule to this new input: [2]",
  "choices": {
    "A": "[4]",
    "B": "[1]",
    "C": "[3]",
    "D": "[2]"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `A` — \[4\] | `A` — \[4\] | Same answer |
| Decider v1.1 | `A` — \[4\] | `A` — \[4\] | Same answer |
| Jev | `A` — \[4\] | `A` — \[4\] | Same answer |
| Microsoft Decision-1 | `A` — \[4\] | `A` — \[4\] | Same answer |
| Clef | `A` — \[4\] | `A` — \[4\] | Same answer |
| Luna Decisions | `A` — \[4\] | `A` — \[4\] | Same answer |
| Clef Flash | `A` — \[4\] | `A` — \[4\] | Same answer |
| Strands Decider | `C` — \[3\] | `C` — \[3\] | Same answer |
| GLiNER2.5 Decide | `D` — \[2\] | `D` — \[2\] | Same answer |
| Laya | `C` — \[3\] | `C` — \[3\] | Same answer |
| CalDec v1 | `B` — \[1\] | `B` — \[1\] | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `list_functions/3e2239ccffbdb2c9f6ba/examples/irrelevant/clean-bare_induction_irrelevant_examples_full_0042`

**Input fingerprint:** `76d27c322e1586783c97f20f969e1b4ae0307769bb72991994fc3580786bd92f`

| Change | Recorded version |
| --- | --- |
| Unrelated examples | Add examples unrelated to the question |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/learning-and-induction/list_functions-3e2239ccffbdb2c9f6ba.md).
