# Option order · Reverse the answer choices variant

[Original question](../../../questions/rule-application/cruxeval-0ac3f5256ca2c072c21c.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** answer choices or their order.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

```text
def f(numbers):
    floats = [n % 1 for n in numbers]
    return floats if 1 in floats else []
```

## Question

> What does f(range(100, 120)) return?

## Answer choices

- **D.** [1]
- **C.** [0]
- **B.** [2]
- **A.** []

**Reference answer:** `A`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "def f(numbers):\n    floats = [n % 1 for n in numbers]\n    return floats if 1 in floats else []",
  "question": "What does f(range(100, 120)) return?",
  "choices": {
    "D": "[1]",
    "C": "[0]",
    "B": "[2]",
    "A": "[]"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `A` — \[\] | `A` — \[\] | Same answer |
| Decider v1.1 | `A` — \[\] | `A` — \[\] | Same answer |
| Jev | `A` — \[\] | `A` — \[\] | Same answer |
| Microsoft Decision-1 | `A` — \[\] | `A` — \[\] | Same answer |
| Clef | `A` — \[\] | `A` — \[\] | Same answer |
| Luna Decisions | `C` — \[0\] | `A` — \[\] | Different answer |
| Clef Flash | `A` — \[\] | `A` — \[\] | Same answer |
| Strands Decider | `D` — \[1\] | `A` — \[\] | Different answer |
| GLiNER2.5 Decide | `A` — \[\] | `D` — \[1\] | Different answer |
| Laya | `A` — \[\] | `A` — \[\] | Same answer |
| CalDec v1 | `A` — \[\] | `A` — \[\] | Same answer |

Clef and Clef Flash sort answer choices in their published input-processing code. Their choice-order results describe that preprocessing.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `cruxeval/0ac3f5256ca2c072c21c/option_order/reverse`

**Input fingerprint:** `975ff3aaf2c7a29acdd866461874e1c3b87aff5e9b9fca0c0fb0fef0189fa933`

| Change | Recorded version |
| --- | --- |
| Option order | Reverse the answer choices |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/rule-application/cruxeval-0ac3f5256ca2c072c21c.md).
