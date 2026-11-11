# Similar distractors · Add fewer similar but irrelevant items variant

[Original question](../../../questions/rule-application/cruxeval-d69e8db680e38b8e073b.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

```text
def neighbor_a(text):
    return text.lower()

def f(text):
    return len(text.splitlines())
```

## Question

> What does f('ncdsdfdaaa0a1cdscsk\*XFd') return?

## Answer choices

- **A.** 0
- **B.** 1
- **C.** 2
- **D.** 3

**Reference answer:** `B`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "def neighbor_a(text):\n    return text.lower()\n\ndef f(text):\n    return len(text.splitlines())",
  "question": "What does f('ncdsdfdaaa0a1cdscsk*XFd') return?",
  "choices": {
    "A": "0",
    "B": "1",
    "C": "2",
    "D": "3"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `B` — 1 | `B` — 1 | Same answer |
| Decider v1.1 | `B` — 1 | `B` — 1 | Same answer |
| Jev | `B` — 1 | `B` — 1 | Same answer |
| Microsoft Decision-1 | `B` — 1 | `B` — 1 | Same answer |
| Clef | `B` — 1 | `B` — 1 | Same answer |
| Luna Decisions | `B` — 1 | `B` — 1 | Same answer |
| Clef Flash | `B` — 1 | `B` — 1 | Same answer |
| Strands Decider | `B` — 1 | `B` — 1 | Same answer |
| GLiNER2.5 Decide | `B` — 1 | `B` — 1 | Same answer |
| Laya | `A` — 0 | `A` — 0 | Same answer |
| CalDec v1 | `B` — 1 | `A` — 0 | Different answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `cruxeval/d69e8db680e38b8e073b/similar_distractors/low/clean-source_first_crux_neighbor_definitions_full_0083`

**Input fingerprint:** `4f851fd0695ef7fe405d664a2e42e8176d4333ede15bbec398afc0a2c7520a64`

| Change | Recorded version |
| --- | --- |
| Similar distractors | Add fewer similar but irrelevant items |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/rule-application/cruxeval-d69e8db680e38b8e073b.md).
