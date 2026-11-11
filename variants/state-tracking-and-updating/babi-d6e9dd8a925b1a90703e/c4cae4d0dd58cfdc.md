# Invented names · Use invented names variant

[Original question](../../../questions/state-tracking-and-updating/babi-d6e9dd8a925b1a90703e.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context, question instructions.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Nelora went back to the kitchen.
> Vaelis travelled to the kitchen.
> Zorvik moved to the bathroom.
> Vaelis travelled to the bedroom.
> Zorvik went to the hallway.
> Tavren went to the hallway.
> Zorvik went to the kitchen.
> Vaelis moved to the kitchen.

## Question

> Where is Zorvik? 

## Answer choices

- **A.** hallway
- **B.** kitchen
- **C.** garden
- **D.** bedroom
- **E.** bathroom
- **F.** office

**Reference answer:** `B`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Nelora went back to the kitchen.\nVaelis travelled to the kitchen.\nZorvik moved to the bathroom.\nVaelis travelled to the bedroom.\nZorvik went to the hallway.\nTavren went to the hallway.\nZorvik went to the kitchen.\nVaelis moved to the kitchen.",
  "question": "Where is Zorvik? ",
  "choices": {
    "A": "hallway",
    "B": "kitchen",
    "C": "garden",
    "D": "bedroom",
    "E": "bathroom",
    "F": "office"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `B` — kitchen | `B` — kitchen | Same answer |
| Decider v1.1 | `B` — kitchen | `B` — kitchen | Same answer |
| Jev | `B` — kitchen | `B` — kitchen | Same answer |
| Microsoft Decision-1 | `B` — kitchen | `B` — kitchen | Same answer |
| Clef | `B` — kitchen | `B` — kitchen | Same answer |
| Luna Decisions | `B` — kitchen | `B` — kitchen | Same answer |
| Clef Flash | `B` — kitchen | `B` — kitchen | Same answer |
| Strands Decider | `B` — kitchen | `B` — kitchen | Same answer |
| GLiNER2.5 Decide | `B` — kitchen | `B` — kitchen | Same answer |
| Laya | `B` — kitchen | `B` — kitchen | Same answer |
| CalDec v1 | `B` — kitchen | `B` — kitchen | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `babi/d6e9dd8a925b1a90703e/unfamiliar_names/invented`

**Input fingerprint:** `90884de4e429ed8dc4e0813710ace65c2b3a4ea74c0897dd96a332af307fae76`

| Change | Recorded version |
| --- | --- |
| Invented names | Use invented names |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/state-tracking-and-updating/babi-d6e9dd8a925b1a90703e.md).
