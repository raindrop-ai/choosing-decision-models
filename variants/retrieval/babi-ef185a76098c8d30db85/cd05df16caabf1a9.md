# Evidence order · Present the evidence in a shuffled order variant

[Original question](../../../questions/retrieval/babi-ef185a76098c8d30db85.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Daniel went to the hallway.
> Daniel moved to the bedroom.
> Daniel went to the bathroom.
> John travelled to the bathroom.

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
  "state": "Daniel went to the hallway.\nDaniel moved to the bedroom.\nDaniel went to the bathroom.\nJohn travelled to the bathroom.",
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
| GLiNER2.5 Decide | `B` — hallway | `A` — bathroom | Different answer |
| Laya | `A` — bathroom | `A` — bathroom | Same answer |
| CalDec v1 | `A` — bathroom | `A` — bathroom | Same answer |

**Ordering comparison:** literal requested source unit permutation. Only the exact matched comparison sets contribute to the reported ordering contrasts.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `babi/ef185a76098c8d30db85/presentation_order/shuffled_presentation/clean-bare_babi_natural_order_check_full_0074`

**Input fingerprint:** `71f19b1d697fb99db008179e5bebb750ad5ad240ac62c74ca03190c314cc3866`

| Change | Recorded version |
| --- | --- |
| Evidence order | Present the evidence in a shuffled order |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/retrieval/babi-ef185a76098c8d30db85.md).
