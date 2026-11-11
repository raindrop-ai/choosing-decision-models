# Evidence order · Swap the records assigning values to function parameters variant

[Original question](../../../questions/rule-application/cruxeval-a6e2537971b4a62dfde7.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context, question instructions.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

```text
def f(char, text):
    if not text.endswith(char):
        return f(char, char + text)
    return text
```

## Question

> What does f('k', 'staovk') return?

## Answer choices

- **A.** &#x27;staovv&#x27;
- **B.** &#x27;staoak&#x27;
- **C.** &#x27;staovk&#x27;
- **D.** &#x27;taovks&#x27;

**Reference answer:** `C`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "def f(char, text):\n    if not text.endswith(char):\n        return f(char, char + text)\n    return text",
  "question": "What does f('k', 'staovk') return?",
  "choices": {
    "A": "'staovv'",
    "B": "'staoak'",
    "C": "'staovk'",
    "D": "'taovks'"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `C` — &#x27;staovk&#x27; | `C` — &#x27;staovk&#x27; | Same answer |
| Decider v1.1 | `C` — &#x27;staovk&#x27; | `C` — &#x27;staovk&#x27; | Same answer |
| Jev | `C` — &#x27;staovk&#x27; | `C` — &#x27;staovk&#x27; | Same answer |
| Microsoft Decision-1 | `C` — &#x27;staovk&#x27; | `C` — &#x27;staovk&#x27; | Same answer |
| Clef | `C` — &#x27;staovk&#x27; | `C` — &#x27;staovk&#x27; | Same answer |
| Luna Decisions | `C` — &#x27;staovk&#x27; | `C` — &#x27;staovk&#x27; | Same answer |
| Clef Flash | `C` — &#x27;staovk&#x27; | `C` — &#x27;staovk&#x27; | Same answer |
| Strands Decider | `C` — &#x27;staovk&#x27; | `C` — &#x27;staovk&#x27; | Same answer |
| GLiNER2.5 Decide | `A` — &#x27;staovv&#x27; | `A` — &#x27;staovv&#x27; | Same answer |
| Laya | `D` — &#x27;taovks&#x27; | `C` — &#x27;staovk&#x27; | Different answer |
| CalDec v1 | `B` — &#x27;staoak&#x27; | `A` — &#x27;staovv&#x27; | Different answer |

**Ordering comparison:** coupled wording reference chronology or representation. Only the exact matched comparison sets contribute to the reported ordering contrasts.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `cruxeval/a6e2537971b4a62dfde7/presentation_order/swap_all_native_parameter_argument_binding_records/clean-source_first_grouped_scoped_binding_orders_full_0321`

**Input fingerprint:** `15124208b1f2cbaf9f8d0c29dbea095cfbe65e765b6875a775bac9d220146187`

| Change | Recorded version |
| --- | --- |
| Evidence order | Swap the records assigning values to function parameters |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/rule-application/cruxeval-a6e2537971b4a62dfde7.md).
