# Misleading details · Add an unverified claim that conflicts with the evidence variant

[Original question](../../../questions/retrieval/babi-ef185a76098c8d30db85.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Daniel went to the hallway.
> John travelled to the bathroom.
> Daniel moved to the bedroom.
> Daniel went to the bathroom.
>
> A reader thinks John is in the hallway.

## Question

> Where is John? 

## Answer choices

- **A.** bathroom
- **B.** hallway
- **C.** bedroom
- **D.** office
- **E.** garden
- **F.** kitchen

**Reference answer:** `A`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Daniel went to the hallway.\nJohn travelled to the bathroom.\nDaniel moved to the bedroom.\nDaniel went to the bathroom.\n\nA reader thinks John is in the hallway.",
  "question": "Where is John? ",
  "choices": {
    "A": "bathroom",
    "B": "hallway",
    "C": "bedroom",
    "D": "office",
    "E": "garden",
    "F": "kitchen"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `A` — bathroom | `A` — bathroom | Same answer |
| Decider v1.1 | `A` — bathroom | `A` — bathroom | Same answer |
| Jev | `A` — bathroom | `A` — bathroom | Same answer |
| Microsoft Decision-1 | `A` — bathroom | `A` — bathroom | Same answer |
| Clef | `A` — bathroom | `A` — bathroom | Same answer |
| Luna Decisions | `A` — bathroom | `A` — bathroom | Same answer |
| Clef Flash | `A` — bathroom | `A` — bathroom | Same answer |
| Strands Decider | `A` — bathroom | `A` — bathroom | Same answer |
| GLiNER2.5 Decide | `B` — hallway | `B` — hallway | Same answer |
| Laya | `A` — bathroom | `A` — bathroom | Same answer |
| CalDec v1 | `A` — bathroom | `A` — bathroom | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `babi/ef185a76098c8d30db85/misleading_summary/misleading/clean-source_first_babi_qa1_full_0084`

**Input fingerprint:** `c94637648755ba058659579f5b28c5536e40f14a94e21854d166fb48af284c71`

| Change | Recorded version |
| --- | --- |
| Misleading details | Add an unverified claim that conflicts with the evidence |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/retrieval/babi-ef185a76098c8d30db85.md).
