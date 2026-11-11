# Option order · Move the first answer choice to the end variant

[Original question](../../../questions/communication/pub-3ba7063951dab02a3bdd.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** answer choices or their order.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Context: X wants to know what sorts of books Y likes to read.
> X: Do you read newspapers?
> Y: I prefer novels.

## Question

> Choose the interpretation or answer requested by the text.

## Answer choices

- **B.** No
- **C.** Yes, subject to some conditions
- **D.** In the middle, neither yes nor no
- **E.** Other
- **A.** Yes

**Reference answer:** `B`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Context: X wants to know what sorts of books Y likes to read.\nX: Do you read newspapers?\nY: I prefer novels.\n",
  "question": "Choose the interpretation or answer requested by the text.",
  "choices": {
    "B": "No",
    "C": "Yes, subject to some conditions",
    "D": "In the middle, neither yes nor no",
    "E": "Other",
    "A": "Yes"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `B` — No | `B` — No | Same answer |
| Decider v1.1 | `B` — No | `B` — No | Same answer |
| Jev | `B` — No | `B` — No | Same answer |
| Microsoft Decision-1 | `B` — No | `B` — No | Same answer |
| Clef | `B` — No | `B` — No | Same answer |
| Luna Decisions | `E` — Other | `E` — Other | Same answer |
| Clef Flash | `B` — No | `B` — No | Same answer |
| Strands Decider | `B` — No | `B` — No | Same answer |
| GLiNER2.5 Decide | `E` — Other | `E` — Other | Same answer |
| Laya | `C` — Yes, subject to some conditions | `C` — Yes, subject to some conditions | Same answer |
| CalDec v1 | `A` — Yes | `A` — Yes | Same answer |

Clef and Clef Flash sort answer choices in their published input-processing code. Their choice-order results describe that preprocessing.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `pub/3ba7063951dab02a3bdd/option_order/rotate_1`

**Input fingerprint:** `dab5297832a093f30851c26376460034d89447b03f46d16895e24307c70dfe22`

| Change | Recorded version |
| --- | --- |
| Option order | Move the first answer choice to the end |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/communication/pub-3ba7063951dab02a3bdd.md).
