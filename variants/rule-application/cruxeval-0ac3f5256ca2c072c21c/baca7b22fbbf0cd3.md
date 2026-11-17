# Similar distractors · Add more similar but irrelevant items variant

[Original question](../../../questions/rule-application/cruxeval-0ac3f5256ca2c072c21c.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

```text
def neighbor_a(numbers):
    return [n % 2 for n in numbers]

def neighbor_b(numbers):
    return [n // 2 for n in numbers]

def neighbor_c(numbers):
    return list(numbers)

def f(numbers):
    floats = [n % 1 for n in numbers]
    return floats if 1 in floats else []
```

## Question

> What does f(range(100, 120)) return?

## Answer choices

- **A.** \[\]
- **B.** \[2\]
- **C.** \[0\]
- **D.** \[1\]

**Reference answer:** `A`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "def neighbor_a(numbers):\n    return [n % 2 for n in numbers]\n\ndef neighbor_b(numbers):\n    return [n // 2 for n in numbers]\n\ndef neighbor_c(numbers):\n    return list(numbers)\n\ndef f(numbers):\n    floats = [n % 1 for n in numbers]\n    return floats if 1 in floats else []",
  "question": "What does f(range(100, 120)) return?",
  "choices": {
    "A": "[]",
    "B": "[2]",
    "C": "[0]",
    "D": "[1]"
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
| Luna Decisions | `C` — \[0\] | `C` — \[0\] | Same answer |
| Clef Flash | `A` — \[\] | `A` — \[\] | Same answer |
| Strands Decider | `D` — \[1\] | `D` — \[1\] | Same answer |
| GLiNER2.5 Decide | `A` — \[\] | `A` — \[\] | Same answer |
| Laya | `A` — \[\] | `B` — \[2\] | Different answer |
| CalDec v1 | `A` — \[\] | `A` — \[\] | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `cruxeval/0ac3f5256ca2c072c21c/similar_distractors/high/clean-source_first_crux_neighbor_definitions_full_0083`

**Input fingerprint:** `309fa48f21a5f8c083f10580da309e35df1d49613ba713ef478563dc3b8dcddb`

| Change | Recorded version |
| --- | --- |
| Similar distractors | Add more similar but irrelevant items |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/rule-application/cruxeval-0ac3f5256ca2c072c21c.md).
