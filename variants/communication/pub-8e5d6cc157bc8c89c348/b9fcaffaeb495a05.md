# Irrelevant details · Add a small amount of irrelevant detail variant

[Original question](../../../questions/communication/pub-8e5d6cc157bc8c89c348.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> The musical suite Merovan includes a refrain.
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
  "state": "The musical suite Merovan includes a refrain.\n\nContext: X and Y are childhood neighbours who unexpectedly run into each other at a cafe.\nX: Are you working nearby?\nY: I work in this building.\n",
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
| GLiDE v1.2 | `A` — Yes | `A` — Yes | Same answer |
| Decider v1.1 | `A` — Yes | `A` — Yes | Same answer |
| Jev | `A` — Yes | `E` — Other | Different answer |
| Microsoft Decision-1 | `A` — Yes | `A` — Yes | Same answer |
| Clef | `A` — Yes | `A` — Yes | Same answer |
| Luna Decisions | `E` — Other | `E` — Other | Same answer |
| Clef Flash | `A` — Yes | `B` — No | Different answer |
| Strands Decider | `A` — Yes | `B` — No | Different answer |
| GLiNER2.5 Decide | `E` — Other | `E` — Other | Same answer |
| Laya | `C` — Yes, subject to some conditions | `C` — Yes, subject to some conditions | Same answer |
| CalDec v1 | `A` — Yes | `A` — Yes | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `pub/8e5d6cc157bc8c89c348/irrelevant_details/low/clean-source_first_pub_music_contexts_full_0166`

**Input fingerprint:** `0042304768b372d1f647e73e43e4b461c04670c4635a901f22c89bda11d67eb4`

| Change | Recorded version |
| --- | --- |
| Irrelevant details | Add a small amount of irrelevant detail |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/communication/pub-8e5d6cc157bc8c89c348.md).
