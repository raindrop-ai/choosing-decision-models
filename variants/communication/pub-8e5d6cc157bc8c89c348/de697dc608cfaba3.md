# Misleading details · Add an unverified claim that conflicts with the evidence variant

[Original question](../../../questions/communication/pub-8e5d6cc157bc8c89c348.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> A reader thinks: «Y gives a negative response about working nearby.»
>
> Context: X and Y are childhood neighbours who unexpectedly run into each other at a cafe.
> X: Are you working nearby?
> Y: I work in this building.

## Question

> Choose the interpretation or answer requested by the text.

## Answer choices

- **A.** Yes
- **B.** No
- **C.** Yes, subject to some conditions
- **D.** In the middle, neither yes nor no
- **E.** Other

**Reference answer:** `A`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "A reader thinks: «Y gives a negative response about working nearby.»\n\nContext: X and Y are childhood neighbours who unexpectedly run into each other at a cafe.\nX: Are you working nearby?\nY: I work in this building.\n",
  "question": "Choose the interpretation or answer requested by the text.",
  "choices": {
    "A": "Yes",
    "B": "No",
    "C": "Yes, subject to some conditions",
    "D": "In the middle, neither yes nor no",
    "E": "Other"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `A` — Yes | `B` — No | Different answer |
| Decider v1.1 | `A` — Yes | `B` — No | Different answer |
| Jev | `A` — Yes | `A` — Yes | Same answer |
| Microsoft Decision-1 | `A` — Yes | `A` — Yes | Same answer |
| Clef | `A` — Yes | `B` — No | Different answer |
| Luna Decisions | `E` — Other | `E` — Other | Same answer |
| Clef Flash | `A` — Yes | `A` — Yes | Same answer |
| Strands Decider | `A` — Yes | `A` — Yes | Same answer |
| GLiNER2.5 Decide | `E` — Other | `E` — Other | Same answer |
| Laya | `C` — Yes, subject to some conditions | `C` — Yes, subject to some conditions | Same answer |
| CalDec v1 | `A` — Yes | `A` — Yes | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `pub/8e5d6cc157bc8c89c348/misleading_summary/misleading/clean-source_first_pub_music_contexts_full_0166`

**Input fingerprint:** `9b9c11b3a83bd9c41e38addc3b4aa8072af3d1b3454d6c66dd40b5121389770d`

| Change | Recorded version |
| --- | --- |
| Misleading details | Add an unverified claim that conflicts with the evidence |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/communication/pub-8e5d6cc157bc8c89c348.md).
