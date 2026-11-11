# Invented names · Use invented names variant

[Original question](../../../questions/state-tracking-and-updating/babi-25a8cecfd568bcdf37f2.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context, question instructions.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Tavren went to the hallway.
> Tavren went to the bedroom.
> Zorvik journeyed to the office.
> Nelora went back to the bedroom.
> Nelora travelled to the office.
> Zorvik travelled to the bedroom.
> Nelora went to the hallway.
> Nelora went back to the kitchen.
> Tavren moved to the hallway.
> Nelora moved to the office.

## Question

> Where is Nelora? 

## Answer choices

- **A.** office
- **B.** bathroom
- **C.** garden
- **D.** kitchen
- **E.** bedroom
- **F.** hallway

**Reference answer:** `A`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Tavren went to the hallway.\nTavren went to the bedroom.\nZorvik journeyed to the office.\nNelora went back to the bedroom.\nNelora travelled to the office.\nZorvik travelled to the bedroom.\nNelora went to the hallway.\nNelora went back to the kitchen.\nTavren moved to the hallway.\nNelora moved to the office.",
  "question": "Where is Nelora? ",
  "choices": {
    "A": "office",
    "B": "bathroom",
    "C": "garden",
    "D": "kitchen",
    "E": "bedroom",
    "F": "hallway"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `A` — office | `A` — office | Same answer |
| Decider v1.1 | `A` — office | `A` — office | Same answer |
| Jev | `A` — office | `A` — office | Same answer |
| Microsoft Decision-1 | `A` — office | `A` — office | Same answer |
| Clef | `A` — office | `A` — office | Same answer |
| Luna Decisions | `A` — office | `A` — office | Same answer |
| Clef Flash | `A` — office | `A` — office | Same answer |
| Strands Decider | `A` — office | `A` — office | Same answer |
| GLiNER2.5 Decide | `A` — office | `A` — office | Same answer |
| Laya | `A` — office | `A` — office | Same answer |
| CalDec v1 | `A` — office | `D` — kitchen | Different answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `babi/25a8cecfd568bcdf37f2/unfamiliar_names/invented`

**Input fingerprint:** `8fb4093199170c5e9696b6371e6bb93bb60e47770e927972e28d9880d1482635`

| Change | Recorded version |
| --- | --- |
| Invented names | Use invented names |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/state-tracking-and-updating/babi-25a8cecfd568bcdf37f2.md).
