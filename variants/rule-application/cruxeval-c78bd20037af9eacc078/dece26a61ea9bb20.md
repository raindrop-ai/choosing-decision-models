# Invented names · Use familiar names variant

[Original question](../../../questions/rule-application/cruxeval-c78bd20037af9eacc078.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context, question instructions.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

```text
def transform (text ,mode ):
    length =len (text )
    return text [length *(mode %4 ):length ]
```

## Question

> What does transform('abc', 1) return?

## Answer choices

- **A.** &#x27;b&#x27;
- **B.** &#x27;a&#x27;
- **C.** &#x27;0&#x27;
- **D.** &#x27;&#x27;

**Reference answer:** `D`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "def transform (text ,mode ):\n    length =len (text )\n    return text [length *(mode %4 ):length ]",
  "question": "What does transform('abc', 1) return?",
  "choices": {
    "A": "'b'",
    "B": "'a'",
    "C": "'0'",
    "D": "''"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `D` — &#x27;&#x27; | `D` — &#x27;&#x27; | Same answer |
| Decider v1.1 | `D` — &#x27;&#x27; | `D` — &#x27;&#x27; | Same answer |
| Jev | `D` — &#x27;&#x27; | `A` — &#x27;b&#x27; | Different answer |
| Microsoft Decision-1 | `B` — &#x27;a&#x27; | `D` — &#x27;&#x27; | Different answer |
| Clef | `D` — &#x27;&#x27; | `D` — &#x27;&#x27; | Same answer |
| Luna Decisions | `D` — &#x27;&#x27; | `D` — &#x27;&#x27; | Same answer |
| Clef Flash | `D` — &#x27;&#x27; | `D` — &#x27;&#x27; | Same answer |
| Strands Decider | `D` — &#x27;&#x27; | `D` — &#x27;&#x27; | Same answer |
| GLiNER2.5 Decide | `A` — &#x27;b&#x27; | `A` — &#x27;b&#x27; | Same answer |
| Laya | `A` — &#x27;b&#x27; | `A` — &#x27;b&#x27; | Same answer |
| CalDec v1 | `A` — &#x27;b&#x27; | `A` — &#x27;b&#x27; | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `cruxeval/c78bd20037af9eacc078/unfamiliar_names/familiar`

**Input fingerprint:** `300bb9317d98851a3b3605ce40a9dab1e6addc45f63305527d409873e4787b3c`

| Change | Recorded version |
| --- | --- |
| Invented names | Use familiar names |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/rule-application/cruxeval-c78bd20037af9eacc078.md).
