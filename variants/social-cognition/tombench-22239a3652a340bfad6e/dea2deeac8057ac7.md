# Irrelevant details · Add a larger amount of irrelevant detail variant

[Original question](../../../questions/social-cognition/tombench-22239a3652a340bfad6e.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Xiao Bei and Xiao Li are wandering in the parking lot, they see boxes and baskets, they find bananas in the box, Xiao Li leaves the parking lot, Xiao Bei moves the bananas to the basket.
>
> The musical suite Merovan includes a refrain. Merovan uses a tonic cadence. Merovan includes rests. Merovan has sustained harmonies. Merovan has detached melodic notes. Merovan varies its accompaniment.

## Question

> After Xiao Li returns to the parking lot, where does Xiao Bei think Xiao Li looks for the bananas?

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
  "state": "Xiao Bei and Xiao Li are wandering in the parking lot, they see boxes and baskets, they find bananas in the box, Xiao Li leaves the parking lot, Xiao Bei moves the bananas to the basket.\n\nThe musical suite Merovan includes a refrain. Merovan uses a tonic cadence. Merovan includes rests. Merovan has sustained harmonies. Merovan has detached melodic notes. Merovan varies its accompaniment.",
  "question": "After Xiao Li returns to the parking lot, where does Xiao Bei think Xiao Li looks for the bananas?",
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

**Variant ID:** `tombench/22239a3652a340bfad6e/irrelevant_details/high/clean-source_first_tombench_music_contexts_full_0155`

**Input fingerprint:** `eb5e8d023ac94e5d784162b212d7fbe4c90a8a94ef48946086461b4900e962a8`

| Change | Recorded version |
| --- | --- |
| Irrelevant details | Add a larger amount of irrelevant detail |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/social-cognition/tombench-22239a3652a340bfad6e.md).
