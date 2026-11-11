# Text length · bAbI: extended added prose variant

[Original question](../../../questions/retrieval/babi-40d6874c302e41b99cdb.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> The office had a broad oak desk beside a window. A brass lamp stood on the desk,and two empty chairs faced it. A framed map hung above a low shelf of books. The hallway outside had a tiled floor,pale walls and a narrow bench. The kitchen had cream-colored cupboards with round ceramic knobs. A row of blue cups stood on the upper shelf, and a green mixing bowl rested beside them. The worktop was made of pale stone with dark flecks. A folded cotton cloth lay beside an empty wooden tray. In the bedroom, a striped rug covered part of the floor. The bed had a dark wooden headboard and a quilt with a pattern of small white leaves. A round mirror hung above a narrow chest of drawers. The bathroom had square gray tiles and a white basin with separate brass taps. A small frosted window was set high in the wall. In the garden, the flower beds had low stone borders. The path was covered with fine gravel, and a wooden fence marked the far edge. The gate had a curved metal handle and a faded coat of green paint.
> Mary journeyed to the hallway.
> John went back to the bathroom.

## Question

> Where is Mary? 

## Answer choices

- **A.** garden
- **B.** kitchen
- **C.** bathroom
- **D.** hallway
- **E.** office
- **F.** bedroom

**Reference answer:** `D`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "The office had a broad oak desk beside a window. A brass lamp stood on the desk,and two empty chairs faced it. A framed map hung above a low shelf of books. The hallway outside had a tiled floor,pale walls and a narrow bench. The kitchen had cream-colored cupboards with round ceramic knobs. A row of blue cups stood on the upper shelf, and a green mixing bowl rested beside them. The worktop was made of pale stone with dark flecks. A folded cotton cloth lay beside an empty wooden tray. In the bedroom, a striped rug covered part of the floor. The bed had a dark wooden headboard and a quilt with a pattern of small white leaves. A round mirror hung above a narrow chest of drawers. The bathroom had square gray tiles and a white basin with separate brass taps. A small frosted window was set high in the wall. In the garden, the flower beds had low stone borders. The path was covered with fine gravel, and a wooden fence marked the far edge. The gate had a curved metal handle and a faded coat of green paint.\nMary journeyed to the hallway.\nJohn went back to the bathroom.",
  "question": "Where is Mary? ",
  "choices": {
    "A": "garden",
    "B": "kitchen",
    "C": "bathroom",
    "D": "hallway",
    "E": "office",
    "F": "bedroom"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `D` — hallway | `D` — hallway | Same answer |
| Decider v1.1 | `D` — hallway | `D` — hallway | Same answer |
| Jev | `D` — hallway | `D` — hallway | Same answer |
| Microsoft Decision-1 | `D` — hallway | `D` — hallway | Same answer |
| Clef | `D` — hallway | `D` — hallway | Same answer |
| Luna Decisions | `D` — hallway | `D` — hallway | Same answer |
| Clef Flash | `D` — hallway | `D` — hallway | Same answer |
| Strands Decider | `D` — hallway | `D` — hallway | Same answer |
| GLiNER2.5 Decide | `D` — hallway | `D` — hallway | Same answer |
| Laya | `D` — hallway | `D` — hallway | Same answer |
| CalDec v1 | `D` — hallway | `D` — hallway | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `babi/40d6874c302e41b99cdb/text_length/longest_natural/clean-movement_natural_contexts_0005`

**Input fingerprint:** `04750fdaa5ce6941c71db101df97c756bf30dc652740b6bc53d551bfca1df854`

| Change | Recorded version |
| --- | --- |
| Text length | bAbI: extended added prose |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/retrieval/babi-40d6874c302e41b99cdb.md).
