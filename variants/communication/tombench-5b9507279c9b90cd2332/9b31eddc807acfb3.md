# Similar distractors · Add fewer similar but irrelevant items variant

[Original question](../../../questions/communication/tombench-5b9507279c9b90cd2332.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> «Alina and Bruno examine a wooden model while Celine watches. Celine leaves for a phone call; the other two open a box of clay shapes before she returns to the table.»
>
> On a sunny weekend afternoon, Li Juan, Wang Qiang, and Xiao Fang play toys together at home. They first play with the first novel toy - a maze 3D puzzle, then they play with the second novel toy - an electric flyer. At this time, Li Juan says, "I have something to do and need to leave the room", and she leaves after closing the door. Wang Qiang says, "Oh, she leaves, it's okay, we play together." Wang Qiang and Xiao Fang play with the third novel toy - a smart rotating color light. After playing, they put all three toys in a plate on the table. At this time, Li Juan comes back, looks at the three toys in the tray, and excitedly says, "Oh, look! Look at that toy!", "Xiao Fang, can you pass it to me?"

## Question

> What does Xiao Fang most likely do?

## Answer choices

- **A.** Xiao Fang picks out the electric flyer and gives it to Li Juan
- **B.** Xiao Fang picks out the smart rotating color light and gives it to Li Juan
- **C.** Xiao Fang randomly picks one of the three toys and gives it to Li Juan
- **D.** Xiao Fang picks out the maze 3D puzzle and gives it to Li Juan

**Reference answer:** `B`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "«Alina and Bruno examine a wooden model while Celine watches. Celine leaves for a phone call; the other two open a box of clay shapes before she returns to the table.»\n\nOn a sunny weekend afternoon, Li Juan, Wang Qiang, and Xiao Fang play toys together at home. They first play with the first novel toy - a maze 3D puzzle, then they play with the second novel toy - an electric flyer. At this time, Li Juan says, \"I have something to do and need to leave the room\", and she leaves after closing the door. Wang Qiang says, \"Oh, she leaves, it's okay, we play together.\" Wang Qiang and Xiao Fang play with the third novel toy - a smart rotating color light. After playing, they put all three toys in a plate on the table. At this time, Li Juan comes back, looks at the three toys in the tray, and excitedly says, \"Oh, look! Look at that toy!\", \"Xiao Fang, can you pass it to me?\"",
  "question": "What does Xiao Fang most likely do?",
  "choices": {
    "A": "Xiao Fang picks out the electric flyer and gives it to Li Juan",
    "B": "Xiao Fang picks out the smart rotating color light and gives it to Li Juan",
    "C": "Xiao Fang randomly picks one of the three toys and gives it to Li Juan",
    "D": "Xiao Fang picks out the maze 3D puzzle and gives it to Li Juan"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `B` — Xiao Fang picks out the smart rotating color light and gives it to Li Juan | `B` — Xiao Fang picks out the smart rotating color light and gives it to Li Juan | Same answer |
| Decider v1.1 | `B` — Xiao Fang picks out the smart rotating color light and gives it to Li Juan | `B` — Xiao Fang picks out the smart rotating color light and gives it to Li Juan | Same answer |
| Jev | `C` — Xiao Fang randomly picks one of the three toys and gives it to Li Juan | `B` — Xiao Fang picks out the smart rotating color light and gives it to Li Juan | Different answer |
| Microsoft Decision-1 | `D` — Xiao Fang picks out the maze 3D puzzle and gives it to Li Juan | `B` — Xiao Fang picks out the smart rotating color light and gives it to Li Juan | Different answer |
| Clef | `B` — Xiao Fang picks out the smart rotating color light and gives it to Li Juan | `B` — Xiao Fang picks out the smart rotating color light and gives it to Li Juan | Same answer |
| Luna Decisions | `B` — Xiao Fang picks out the smart rotating color light and gives it to Li Juan | `B` — Xiao Fang picks out the smart rotating color light and gives it to Li Juan | Same answer |
| Clef Flash | `D` — Xiao Fang picks out the maze 3D puzzle and gives it to Li Juan | `A` — Xiao Fang picks out the electric flyer and gives it to Li Juan | Different answer |
| Strands Decider | `B` — Xiao Fang picks out the smart rotating color light and gives it to Li Juan | `B` — Xiao Fang picks out the smart rotating color light and gives it to Li Juan | Same answer |
| GLiNER2.5 Decide | `B` — Xiao Fang picks out the smart rotating color light and gives it to Li Juan | `B` — Xiao Fang picks out the smart rotating color light and gives it to Li Juan | Same answer |
| Laya | `A` — Xiao Fang picks out the electric flyer and gives it to Li Juan | `A` — Xiao Fang picks out the electric flyer and gives it to Li Juan | Same answer |
| CalDec v1 | `C` — Xiao Fang randomly picks one of the three toys and gives it to Li Juan | `A` — Xiao Fang picks out the electric flyer and gives it to Li Juan | Different answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `tombench/5b9507279c9b90cd2332/similar_distractors/low/clean-source_first_tombench_near_scenes_full_0215`

**Input fingerprint:** `83aadfdfc9cec7ae40fa32a887aeeda5cd93a53926fa627df892b1fae35c1ac9`

| Change | Recorded version |
| --- | --- |
| Similar distractors | Add fewer similar but irrelevant items |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/communication/tombench-5b9507279c9b90cd2332.md).
