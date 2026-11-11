# Unrelated examples · Add examples unrelated to the question variant

[Original question](../../../questions/rule-application/cruxeval-0ac3f5256ca2c072c21c.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

```text
def f(numbers):
    floats = [n % 1 for n in numbers]
    return floats if 1 in floats else []
# Luma is an otter. Every otter is an animal. Is Luma an animal? Answer: yes.
```

## Question

> What does f(range(100, 120)) return?

## Answer choices

- **A.** []
- **B.** [2]
- **C.** [0]
- **D.** [1]

**Reference answer:** `A`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "def f(numbers):\n    floats = [n % 1 for n in numbers]\n    return floats if 1 in floats else []\n# Luma is an otter. Every otter is an animal. Is Luma an animal? Answer: yes.",
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
| GLiNER2.5 Decide | `A` — \[\] | `D` — \[1\] | Different answer |
| Laya | `A` — \[\] | `C` — \[0\] | Different answer |
| CalDec v1 | `A` — \[\] | `A` — \[\] | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `cruxeval/0ac3f5256ca2c072c21c/examples/irrelevant/clean-source_first_crux_comment_contexts_full_0080`

**Input fingerprint:** `014f2967a72918c19b4c067ef3791526306843d9aa3b10d0d95966e5159b1416`

| Change | Recorded version |
| --- | --- |
| Unrelated examples | Add examples unrelated to the question |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/rule-application/cruxeval-0ac3f5256ca2c072c21c.md).
