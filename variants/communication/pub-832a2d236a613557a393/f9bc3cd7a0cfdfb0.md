# Misleading details · Add an unverified claim that conflicts with the evidence variant

[Original question](../../../questions/communication/pub-832a2d236a613557a393.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> A reader thinks: «Hand refers to the physical hand of a person as the intended meaning of this request.»
>
> Context: "Could you please lend me a hand? "
> Question: What does "hand " refer to :?

## Question

> Choose the interpretation or answer requested by the text.

## Answer choices

- **A.** Hand of a person 
- **B.** Paper
- **C.** Help
- **D.** Leg

**Reference answer:** `C`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "A reader thinks: «Hand refers to the physical hand of a person as the intended meaning of this request.»\n\nContext: \"Could you please lend me a hand? \"\nQuestion: What does \"hand \" refer to :?\n",
  "question": "Choose the interpretation or answer requested by the text.",
  "choices": {
    "A": "Hand of a person ",
    "B": "Paper",
    "C": "Help",
    "D": "Leg"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `C` — Help | `C` — Help | Same answer |
| Decider v1.1 | `C` — Help | `C` — Help | Same answer |
| Jev | `C` — Help | `C` — Help | Same answer |
| Microsoft Decision-1 | `C` — Help | `C` — Help | Same answer |
| Clef | `C` — Help | `C` — Help | Same answer |
| Luna Decisions | `C` — Help | `A` — Hand of a person  | Different answer |
| Clef Flash | `C` — Help | `A` — Hand of a person  | Different answer |
| Strands Decider | `C` — Help | `A` — Hand of a person  | Different answer |
| GLiNER2.5 Decide | `A` — Hand of a person  | `A` — Hand of a person  | Same answer |
| Laya | `A` — Hand of a person  | `A` — Hand of a person  | Same answer |
| CalDec v1 | `A` — Hand of a person  | `A` — Hand of a person  | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `pub/832a2d236a613557a393/misleading_summary/misleading/clean-source_first_pub_music_contexts_full_0166`

**Input fingerprint:** `05674a347b434cf12a8d0f7964bdf66c2066cae712566a85c9faae910d8b28cd`

| Change | Recorded version |
| --- | --- |
| Misleading details | Add an unverified claim that conflicts with the evidence |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/communication/pub-832a2d236a613557a393.md).
