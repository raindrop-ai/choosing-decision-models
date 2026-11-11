# Option order · Reverse the answer choices variant

[Original question](../../../questions/communication/pub-3d63e1258d2078a92871.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** answer choices or their order.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Context: X wants to know about Y's food preferences.
> X: Are you okay with spice?
> Y: I like most spices, except curry.

## Question

> Choose the interpretation or answer requested by the text.

## Answer choices

- **E.** Other
- **D.** In the middle, neither yes nor no
- **C.** Yes, subject to some conditions
- **B.** No
- **A.** Yes

**Reference answer:** `C`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Context: X wants to know about Y's food preferences.\nX: Are you okay with spice?\nY: I like most spices, except curry.\n",
  "question": "Choose the interpretation or answer requested by the text.",
  "choices": {
    "E": "Other",
    "D": "In the middle, neither yes nor no",
    "C": "Yes, subject to some conditions",
    "B": "No",
    "A": "Yes"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `C` — Yes, subject to some conditions | `C` — Yes, subject to some conditions | Same answer |
| Decider v1.1 | `C` — Yes, subject to some conditions | `C` — Yes, subject to some conditions | Same answer |
| Jev | `C` — Yes, subject to some conditions | `C` — Yes, subject to some conditions | Same answer |
| Microsoft Decision-1 | `C` — Yes, subject to some conditions | `C` — Yes, subject to some conditions | Same answer |
| Clef | `C` — Yes, subject to some conditions | `C` — Yes, subject to some conditions | Same answer |
| Luna Decisions | `C` — Yes, subject to some conditions | `C` — Yes, subject to some conditions | Same answer |
| Clef Flash | `C` — Yes, subject to some conditions | `C` — Yes, subject to some conditions | Same answer |
| Strands Decider | `B` — No | `C` — Yes, subject to some conditions | Different answer |
| GLiNER2.5 Decide | `E` — Other | `E` — Other | Same answer |
| Laya | `A` — Yes | `A` — Yes | Same answer |
| CalDec v1 | `A` — Yes | `A` — Yes | Same answer |

Clef and Clef Flash sort answer choices in their published input-processing code. Their choice-order results describe that preprocessing.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `pub/3d63e1258d2078a92871/option_order/reverse`

**Input fingerprint:** `b0bba88df206ce7a97d3fd40e4691e2e131526d611b8d6c6274e46cd043befb7`

| Change | Recorded version |
| --- | --- |
| Option order | Reverse the answer choices |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/communication/pub-3d63e1258d2078a92871.md).
