# Similar distractors · Add more similar but irrelevant items variant

[Original question](../../../questions/concepts-and-categorization/mmlu-c711ab08d0ab008e3ab1.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> «A separate invented poem reads: "The harbor closes its gates; the old ships sleep beneath a silver moon."»
>
> «Another independent invented poem reads: "We planted new gardens after the towers fell; the roots outlasted the stone."»
>
> «A third independent invented poem reads: "The city races toward tomorrow, leaving its quiet lanterns by the road."»

## Question

> This question refers to the following information.
> You are the United States,
> you are the future invader
> of the native America that has Indian blood,
> that still prays to Jesus Christ and still speaks Spanish.
> . . .
> you are Alexander-Nebuchadnezzar.
> You think that life is fire,
> that progress is eruption,
> that wherever you shoot
> you hit the future.
> No.
> . . .
> But our America, that has had poets
> since the ancient times of Netzahualcoyotl,
> . . .
> that consulted the stars, that knew Atlantis
> whose resounding name comes to us from Plato,
> that since the remote times of its life
> has lived on light, on fire, on perfume, on love,
> America of the great Montezuma, of the Inca,
> the fragrant America of Christopher Columbus,
> Catholic America, Spanish America,
> the America in which noble Cuauhtémoc said:
> "I'm not in a bed of roses", that America
> that trembles in hurricanes and lives on love,
> it lives, you men of Saxon eyes and barbarous soul.
> And it dreams. And it loves, and it vibrates, and it is the daughter of the sun.
> Be careful. Viva Spanish America!
> There are a thousand cubs loosed from the Spanish lion.
> Roosevelt, one would have to be, through God himself,
> the-fearful rifleman and strong hunter,
> to manage to grab us in your iron claws.
> And, although you count on everything, you lack one thing: God!
> —Adapted from "To Roosevelt" by Ruben Dario, 1904
> Which statement best reflects the theme of the poem?

## Answer choices

- **A.** Latin Americans are too na?ve and should fight back.
- **B.** Latin America has survived many invaders and will endure.
- **C.** The Spanish have already destroyed Latin American culture.
- **D.** Change is necessary for progress.

**Reference answer:** `B`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "«A separate invented poem reads: \"The harbor closes its gates; the old ships sleep beneath a silver moon.\"»\n\n«Another independent invented poem reads: \"We planted new gardens after the towers fell; the roots outlasted the stone.\"»\n\n«A third independent invented poem reads: \"The city races toward tomorrow, leaving its quiet lanterns by the road.\"»",
  "question": "This question refers to the following information.\nYou are the United States,\nyou are the future invader\nof the native America that has Indian blood,\nthat still prays to Jesus Christ and still speaks Spanish.\n. . .\nyou are Alexander-Nebuchadnezzar.\nYou think that life is fire,\nthat progress is eruption,\nthat wherever you shoot\nyou hit the future.\nNo.\n. . .\nBut our America, that has had poets\nsince the ancient times of Netzahualcoyotl,\n. . .\nthat consulted the stars, that knew Atlantis\nwhose resounding name comes to us from Plato,\nthat since the remote times of its life\nhas lived on light, on fire, on perfume, on love,\nAmerica of the great Montezuma, of the Inca,\nthe fragrant America of Christopher Columbus,\nCatholic America, Spanish America,\nthe America in which noble Cuauhtémoc said:\n\"I'm not in a bed of roses\", that America\nthat trembles in hurricanes and lives on love,\nit lives, you men of Saxon eyes and barbarous soul.\nAnd it dreams. And it loves, and it vibrates, and it is the daughter of the sun.\nBe careful. Viva Spanish America!\nThere are a thousand cubs loosed from the Spanish lion.\nRoosevelt, one would have to be, through God himself,\nthe-fearful rifleman and strong hunter,\nto manage to grab us in your iron claws.\nAnd, although you count on everything, you lack one thing: God!\n—Adapted from \"To Roosevelt\" by Ruben Dario, 1904\nWhich statement best reflects the theme of the poem?",
  "choices": {
    "A": "Latin Americans are too na?ve and should fight back.",
    "B": "Latin America has survived many invaders and will endure.",
    "C": "The Spanish have already destroyed Latin American culture.",
    "D": "Change is necessary for progress."
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `B` — Latin America has survived many invaders and will endure. | `B` — Latin America has survived many invaders and will endure. | Same answer |
| Decider v1.1 | `B` — Latin America has survived many invaders and will endure. | `B` — Latin America has survived many invaders and will endure. | Same answer |
| Jev | `B` — Latin America has survived many invaders and will endure. | `B` — Latin America has survived many invaders and will endure. | Same answer |
| Microsoft Decision-1 | `B` — Latin America has survived many invaders and will endure. | `B` — Latin America has survived many invaders and will endure. | Same answer |
| Clef | `B` — Latin America has survived many invaders and will endure. | `B` — Latin America has survived many invaders and will endure. | Same answer |
| Luna Decisions | `B` — Latin America has survived many invaders and will endure. | `B` — Latin America has survived many invaders and will endure. | Same answer |
| Clef Flash | `B` — Latin America has survived many invaders and will endure. | `B` — Latin America has survived many invaders and will endure. | Same answer |
| Strands Decider | `B` — Latin America has survived many invaders and will endure. | `B` — Latin America has survived many invaders and will endure. | Same answer |
| GLiNER2.5 Decide | `B` — Latin America has survived many invaders and will endure. | `B` — Latin America has survived many invaders and will endure. | Same answer |
| Laya | `B` — Latin America has survived many invaders and will endure. | `B` — Latin America has survived many invaders and will endure. | Same answer |
| CalDec v1 | `B` — Latin America has survived many invaders and will endure. | `B` — Latin America has survived many invaders and will endure. | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `mmlu/c711ab08d0ab008e3ab1/similar_distractors/high/clean-source_first_parallel_b_near_accounts_0301`

**Input fingerprint:** `e3b223307473a6879b8153e33bb1b5c0c559cca459121c98a273f7fa9b8b3402`

| Change | Recorded version |
| --- | --- |
| Similar distractors | Add more similar but irrelevant items |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/concepts-and-categorization/mmlu-c711ab08d0ab008e3ab1.md).
