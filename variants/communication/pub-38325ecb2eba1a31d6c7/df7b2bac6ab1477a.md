# Misleading details · Add an unverified claim that conflicts with the evidence variant

[Original question](../../../questions/communication/pub-38325ecb2eba1a31d6c7.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> A reader thinks: «Y gives an affirmative response to the invitation to see a movie tonight.»
>
> Context: X and Y are colleagues who are leaving work on a Friday at the same time.
> X: Do you want to go see a movie tonight?
> Y: I'd rather do something physical.

## Question

> Choose the interpretation or answer requested by the text.

## Answer choices

- **A.** Yes
- **B.** No
- **C.** Yes, subject to some conditions
- **D.** In the middle, neither yes nor no
- **E.** Other

**Reference answer:** `B`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "A reader thinks: «Y gives an affirmative response to the invitation to see a movie tonight.»\n\nContext: X and Y are colleagues who are leaving work on a Friday at the same time.\nX: Do you want to go see a movie tonight?\nY: I'd rather do something physical.\n",
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
| GLiDE v1.2 | `B` — No | `B` — No | Same answer |
| Decider v1.1 | `B` — No | `B` — No | Same answer |
| Jev | `B` — No | `B` — No | Same answer |
| Microsoft Decision-1 | `B` — No | `B` — No | Same answer |
| Clef | `B` — No | `B` — No | Same answer |
| Luna Decisions | `E` — Other | `B` — No | Different answer |
| Clef Flash | `B` — No | `B` — No | Same answer |
| Strands Decider | `B` — No | `B` — No | Same answer |
| GLiNER2.5 Decide | `E` — Other | `E` — Other | Same answer |
| Laya | `B` — No | `B` — No | Same answer |
| CalDec v1 | `B` — No | `B` — No | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `pub/38325ecb2eba1a31d6c7/misleading_summary/misleading/clean-source_first_pub_music_contexts_full_0166`

**Input fingerprint:** `90a7b7596a7c7a4b981e1139e44aabb4c9d2c02b4b5b19a421a3f230a57e66da`

| Change | Recorded version |
| --- | --- |
| Misleading details | Add an unverified claim that conflicts with the evidence |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/communication/pub-38325ecb2eba1a31d6c7.md).
