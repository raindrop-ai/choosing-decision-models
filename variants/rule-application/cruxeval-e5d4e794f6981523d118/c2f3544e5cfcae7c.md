# Similar distractors · Add fewer similar but irrelevant items variant

[Original question](../../../questions/rule-application/cruxeval-e5d4e794f6981523d118.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

```text
def neighbor_a(text):
    return text.lower()

def f(strs):
    strs = strs.split()
    for i in range(1, len(strs), 2):
        strs[i] = ''.join(reversed(strs[i]))
    return ' '.join(strs)
```

## Question

> What does f('K zBK') return?

## Answer choices

- **A.** &#x27;K KKz&#x27;
- **B.** &#x27;K  Bz&#x27;
- **C.** &#x27;K KBz&#x27;
- **D.** &#x27;zK KB&#x27;

**Reference answer:** `C`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "def neighbor_a(text):\n    return text.lower()\n\ndef f(strs):\n    strs = strs.split()\n    for i in range(1, len(strs), 2):\n        strs[i] = ''.join(reversed(strs[i]))\n    return ' '.join(strs)",
  "question": "What does f('K zBK') return?",
  "choices": {
    "A": "'K KKz'",
    "B": "'K  Bz'",
    "C": "'K KBz'",
    "D": "'zK KB'"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `C` — &#x27;K KBz&#x27; | `C` — &#x27;K KBz&#x27; | Same answer |
| Decider v1.1 | `C` — &#x27;K KBz&#x27; | `C` — &#x27;K KBz&#x27; | Same answer |
| Jev | `C` — &#x27;K KBz&#x27; | `C` — &#x27;K KBz&#x27; | Same answer |
| Microsoft Decision-1 | `C` — &#x27;K KBz&#x27; | `C` — &#x27;K KBz&#x27; | Same answer |
| Clef | `C` — &#x27;K KBz&#x27; | `C` — &#x27;K KBz&#x27; | Same answer |
| Luna Decisions | `C` — &#x27;K KBz&#x27; | `C` — &#x27;K KBz&#x27; | Same answer |
| Clef Flash | `B` — &#x27;K  Bz&#x27; | `B` — &#x27;K  Bz&#x27; | Same answer |
| Strands Decider | `C` — &#x27;K KBz&#x27; | `C` — &#x27;K KBz&#x27; | Same answer |
| GLiNER2.5 Decide | `A` — &#x27;K KKz&#x27; | `B` — &#x27;K  Bz&#x27; | Different answer |
| Laya | `D` — &#x27;zK KB&#x27; | `D` — &#x27;zK KB&#x27; | Same answer |
| CalDec v1 | `C` — &#x27;K KBz&#x27; | `A` — &#x27;K KKz&#x27; | Different answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `cruxeval/e5d4e794f6981523d118/similar_distractors/low/clean-source_first_crux_neighbor_definitions_full_0083`

**Input fingerprint:** `844fc4307e4d4b9dced41cebfa97203cda28a1c888829726e09fa772db4db297`

| Change | Recorded version |
| --- | --- |
| Similar distractors | Add fewer similar but irrelevant items |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/rule-application/cruxeval-e5d4e794f6981523d118.md).
