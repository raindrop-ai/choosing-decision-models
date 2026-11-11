# Similar distractors · Add more similar but irrelevant items variant

[Original question](../../../questions/rule-application/cruxeval-51df29174c7033f287b1.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

```text
def neighbor_a(text):
    return text.lower()

def neighbor_b(text):
    return text[::-1]

def neighbor_c(text):
    return text.strip()

def f(a_str, prefix):
    if a_str.removeprefix(prefix):
        return a_str
    else:
        return prefix + a_str
```

## Question

> What does f('abc', 'abcd') return?

## Answer choices

- **A.** &#x27;aac&#x27;
- **B.** &#x27;abc&#x27;
- **C.** &#x27;bca&#x27;
- **D.** &#x27;ABC&#x27;

**Reference answer:** `B`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "def neighbor_a(text):\n    return text.lower()\n\ndef neighbor_b(text):\n    return text[::-1]\n\ndef neighbor_c(text):\n    return text.strip()\n\ndef f(a_str, prefix):\n    if a_str.removeprefix(prefix):\n        return a_str\n    else:\n        return prefix + a_str",
  "question": "What does f('abc', 'abcd') return?",
  "choices": {
    "A": "'aac'",
    "B": "'abc'",
    "C": "'bca'",
    "D": "'ABC'"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `B` — &#x27;abc&#x27; | `B` — &#x27;abc&#x27; | Same answer |
| Decider v1.1 | `B` — &#x27;abc&#x27; | `B` — &#x27;abc&#x27; | Same answer |
| Jev | `B` — &#x27;abc&#x27; | `B` — &#x27;abc&#x27; | Same answer |
| Microsoft Decision-1 | `B` — &#x27;abc&#x27; | `B` — &#x27;abc&#x27; | Same answer |
| Clef | `B` — &#x27;abc&#x27; | `B` — &#x27;abc&#x27; | Same answer |
| Luna Decisions | `A` — &#x27;aac&#x27; | `A` — &#x27;aac&#x27; | Same answer |
| Clef Flash | `A` — &#x27;aac&#x27; | `A` — &#x27;aac&#x27; | Same answer |
| Strands Decider | `B` — &#x27;abc&#x27; | `B` — &#x27;abc&#x27; | Same answer |
| GLiNER2.5 Decide | `D` — &#x27;ABC&#x27; | `D` — &#x27;ABC&#x27; | Same answer |
| Laya | `D` — &#x27;ABC&#x27; | `D` — &#x27;ABC&#x27; | Same answer |
| CalDec v1 | `B` — &#x27;abc&#x27; | `A` — &#x27;aac&#x27; | Different answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `cruxeval/51df29174c7033f287b1/similar_distractors/high/clean-source_first_crux_neighbor_definitions_full_0083`

**Input fingerprint:** `7e24e882df254e8e77f0a7043ddee7ee8146ba2b280786d21fc8fb2226e1dcd2`

| Change | Recorded version |
| --- | --- |
| Similar distractors | Add more similar but irrelevant items |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/rule-application/cruxeval-51df29174c7033f287b1.md).
