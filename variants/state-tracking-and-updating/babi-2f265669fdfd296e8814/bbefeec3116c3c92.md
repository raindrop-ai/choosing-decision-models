# Text length · bAbI: extended added prose variant

[Original question](../../../questions/state-tracking-and-updating/babi-2f265669fdfd296e8814.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> The office had a broad oak desk beside a window. A brass lamp stood on the desk,and two empty chairs faced it. A framed map hung above a low shelf of books. The hallway outside had a tiled floor,pale walls and a narrow bench. The kitchen had cream-colored cupboards with round ceramic knobs. A row of blue cups stood on the upper shelf, and a green mixing bowl rested beside them. The worktop was made of pale stone with dark flecks. A folded cotton cloth lay beside an empty wooden tray. In the bedroom, a striped rug covered part of the floor. The bed had a dark wooden headboard and a quilt with a pattern of small white leaves. A round mirror hung above a narrow chest of drawers. The bathroom had square gray tiles and a white basin with separate brass taps. A small frosted window was set high in the wall. In the garden, the flower beds had low stone borders. The path was covered with fine gravel, and a wooden fence marked the far edge. The gate had a curved metal handle and a faded coat of green paint.
> Sandra travelled to the office.
> Sandra travelled to the bathroom.

## Question

> Where is Sandra? 

## Answer choices

- **A.** hallway
- **B.** office
- **C.** bedroom
- **D.** garden
- **E.** kitchen
- **F.** bathroom

**Reference answer:** `F`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "The office had a broad oak desk beside a window. A brass lamp stood on the desk,and two empty chairs faced it. A framed map hung above a low shelf of books. The hallway outside had a tiled floor,pale walls and a narrow bench. The kitchen had cream-colored cupboards with round ceramic knobs. A row of blue cups stood on the upper shelf, and a green mixing bowl rested beside them. The worktop was made of pale stone with dark flecks. A folded cotton cloth lay beside an empty wooden tray. In the bedroom, a striped rug covered part of the floor. The bed had a dark wooden headboard and a quilt with a pattern of small white leaves. A round mirror hung above a narrow chest of drawers. The bathroom had square gray tiles and a white basin with separate brass taps. A small frosted window was set high in the wall. In the garden, the flower beds had low stone borders. The path was covered with fine gravel, and a wooden fence marked the far edge. The gate had a curved metal handle and a faded coat of green paint.\nSandra travelled to the office.\nSandra travelled to the bathroom.",
  "question": "Where is Sandra? ",
  "choices": {
    "A": "hallway",
    "B": "office",
    "C": "bedroom",
    "D": "garden",
    "E": "kitchen",
    "F": "bathroom"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `F` — bathroom | `F` — bathroom | Same answer |
| Decider v1.1 | `F` — bathroom | `F` — bathroom | Same answer |
| Jev | `F` — bathroom | `F` — bathroom | Same answer |
| Microsoft Decision-1 | `F` — bathroom | `F` — bathroom | Same answer |
| Clef | `F` — bathroom | `F` — bathroom | Same answer |
| Luna Decisions | `F` — bathroom | `F` — bathroom | Same answer |
| Clef Flash | `F` — bathroom | `F` — bathroom | Same answer |
| Strands Decider | `F` — bathroom | `F` — bathroom | Same answer |
| GLiNER2.5 Decide | `F` — bathroom | `B` — office | Different answer |
| Laya | `B` — office | `B` — office | Same answer |
| CalDec v1 | `F` — bathroom | `F` — bathroom | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `babi/2f265669fdfd296e8814/text_length/longest_natural/clean-movement_natural_contexts_0005`

**Input fingerprint:** `f468692afe103c232d13d8828daf214f623fbb59e45707f2a41ac9737c0f4a1a`

| Change | Recorded version |
| --- | --- |
| Text length | bAbI: extended added prose |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/state-tracking-and-updating/babi-2f265669fdfd296e8814.md).
