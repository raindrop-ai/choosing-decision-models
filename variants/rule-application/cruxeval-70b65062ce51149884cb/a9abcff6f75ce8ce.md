# Paraphrasing · Change individual words and phrases variant

[Original question](../../../questions/rule-application/cruxeval-70b65062ce51149884cb.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** question instructions.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

```text
def f(text):
    ans = ''
    while text != '':
        x, sep, text = text.partition('(')
        ans = x + sep.replace('(', '|') + ans
        ans = ans + text[0] + ans
        text = text[1:]
    return ans
```

## Question

> What value is returned by f("")?

## Answer choices

- **A.** &#x27;&#x27;
- **B.** &#x27;a&#x27;
- **C.** &#x27;b&#x27;
- **D.** &#x27;0&#x27;

**Reference answer:** `A`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "def f(text):\n    ans = ''\n    while text != '':\n        x, sep, text = text.partition('(')\n        ans = x + sep.replace('(', '|') + ans\n        ans = ans + text[0] + ans\n        text = text[1:]\n    return ans",
  "question": "What value is returned by f(\"\")?",
  "choices": {
    "A": "''",
    "B": "'a'",
    "C": "'b'",
    "D": "'0'"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `A` — &#x27;&#x27; | `A` — &#x27;&#x27; | Same answer |
| Decider v1.1 | `A` — &#x27;&#x27; | `A` — &#x27;&#x27; | Same answer |
| Jev | `A` — &#x27;&#x27; | `A` — &#x27;&#x27; | Same answer |
| Microsoft Decision-1 | `A` — &#x27;&#x27; | `A` — &#x27;&#x27; | Same answer |
| Clef | `A` — &#x27;&#x27; | `A` — &#x27;&#x27; | Same answer |
| Luna Decisions | `A` — &#x27;&#x27; | `A` — &#x27;&#x27; | Same answer |
| Clef Flash | `A` — &#x27;&#x27; | `A` — &#x27;&#x27; | Same answer |
| Strands Decider | `A` — &#x27;&#x27; | `A` — &#x27;&#x27; | Same answer |
| GLiNER2.5 Decide | `A` — &#x27;&#x27; | `A` — &#x27;&#x27; | Same answer |
| Laya | `A` — &#x27;&#x27; | `A` — &#x27;&#x27; | Same answer |
| CalDec v1 | `A` — &#x27;&#x27; | `A` — &#x27;&#x27; | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `cruxeval/70b65062ce51149884cb/paraphrasing/surface`

**Input fingerprint:** `2db7dbc3ec3beb6e3e1da1cd73fb86e876ac3cf85da5f6ed0179974613bbdb66`

| Change | Recorded version |
| --- | --- |
| Paraphrasing | Change individual words and phrases |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/rule-application/cruxeval-70b65062ce51149884cb.md).
