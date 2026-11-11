# Paraphrasing · Change individual words and phrases variant

[Original question](../../../questions/social-cognition/tombench-22239a3652a340bfad6e.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** question instructions.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Xiao Bei and Xiao Li are wandering in the parking lot, they see boxes and baskets, they find bananas in the box, Xiao Li leaves the parking lot, Xiao Bei moves the bananas to the basket.

## Question

> After Xiao Li returns to the parking lot, in which place does Xiao Bei think Xiao Li looks for the bananas?

## Answer choices

- **A.** Briefcase
- **B.** Box
- **C.** Basket
- **D.** Cabinet

**Reference answer:** `B`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Xiao Bei and Xiao Li are wandering in the parking lot, they see boxes and baskets, they find bananas in the box, Xiao Li leaves the parking lot, Xiao Bei moves the bananas to the basket.",
  "question": "After Xiao Li returns to the parking lot, in which place does Xiao Bei think Xiao Li looks for the bananas?",
  "choices": {
    "A": "Briefcase",
    "B": "Box",
    "C": "Basket",
    "D": "Cabinet"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `B` — Box | `B` — Box | Same answer |
| Decider v1.1 | `B` — Box | `B` — Box | Same answer |
| Jev | `B` — Box | `B` — Box | Same answer |
| Microsoft Decision-1 | `B` — Box | `B` — Box | Same answer |
| Clef | `B` — Box | `B` — Box | Same answer |
| Luna Decisions | `B` — Box | `B` — Box | Same answer |
| Clef Flash | `B` — Box | `B` — Box | Same answer |
| Strands Decider | `B` — Box | `C` — Basket | Different answer |
| GLiNER2.5 Decide | `C` — Basket | `C` — Basket | Same answer |
| Laya | `B` — Box | `B` — Box | Same answer |
| CalDec v1 | `B` — Box | `B` — Box | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `tombench/22239a3652a340bfad6e/paraphrasing/surface`

**Input fingerprint:** `2d150828aedb6fdca0fff393948c8aa00fa07e937afd39eeb1b93e5130daa3e6`

| Change | Recorded version |
| --- | --- |
| Paraphrasing | Change individual words and phrases |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/social-cognition/tombench-22239a3652a340bfad6e.md).
