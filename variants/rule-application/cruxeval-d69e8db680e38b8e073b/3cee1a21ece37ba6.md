# Option order · Reverse the answer choices variant

[Original question](../../../questions/rule-application/cruxeval-d69e8db680e38b8e073b.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** answer choices or their order.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

```text
def f(text):
    return len(text.splitlines())
```

## Question

> What does f('ncdsdfdaaa0a1cdscsk\*XFd') return?

## Answer choices

- **D.** 3
- **C.** 2
- **B.** 1
- **A.** 0

**Reference answer:** `B`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "def f(text):\n    return len(text.splitlines())",
  "question": "What does f('ncdsdfdaaa0a1cdscsk*XFd') return?",
  "choices": {
    "D": "3",
    "C": "2",
    "B": "1",
    "A": "0"
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
| Laya | `A` — 0 | `D` — 3 | Different answer |
| CalDec v1 | `B` — 1 | `B` — 1 | Same answer |

Clef and Clef Flash sort answer choices in their published input-processing code. Their choice-order results describe that preprocessing.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `cruxeval/d69e8db680e38b8e073b/option_order/reverse`

**Input fingerprint:** `2cd4f7593ce3a725a515a4528be462224e3d256d4c69a3a8c0b21ea0cdb2fe90`

| Change | Recorded version |
| --- | --- |
| Option order | Reverse the answer choices |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/rule-application/cruxeval-d69e8db680e38b8e073b.md).
