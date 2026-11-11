# Similar distractors · Add fewer similar but irrelevant items variant

[Original question](../../../questions/rule-application/cruxeval-363fc9a9b97936a06028.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

```text
def neighbor_a(text):
    return text.lower()

def f(text):
    return not text.isdecimal()
```

## Question

> What does f('the speed is -36 miles per hour') return?

## Answer choices

- **A.** True
- **B.** False

**Reference answer:** `A`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "def neighbor_a(text):\n    return text.lower()\n\ndef f(text):\n    return not text.isdecimal()",
  "question": "What does f('the speed is -36 miles per hour') return?",
  "choices": {
    "A": "True",
    "B": "False"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `A` — True | `A` — True | Same answer |
| Decider v1.1 | `A` — True | `A` — True | Same answer |
| Jev | `A` — True | `A` — True | Same answer |
| Microsoft Decision-1 | `A` — True | `A` — True | Same answer |
| Clef | `A` — True | `A` — True | Same answer |
| Luna Decisions | `A` — True | `A` — True | Same answer |
| Clef Flash | `A` — True | `A` — True | Same answer |
| Strands Decider | `A` — True | `A` — True | Same answer |
| GLiNER2.5 Decide | `B` — False | `B` — False | Same answer |
| Laya | `A` — True | `A` — True | Same answer |
| CalDec v1 | `A` — True | `A` — True | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `cruxeval/363fc9a9b97936a06028/similar_distractors/low/clean-source_first_crux_neighbor_definitions_full_0083`

**Input fingerprint:** `5ce582fc3a4b8220a9a452a3d503edcf3cd301a11841f889f5a9874703b5b0d1`

| Change | Recorded version |
| --- | --- |
| Similar distractors | Add fewer similar but irrelevant items |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/rule-application/cruxeval-363fc9a9b97936a06028.md).
