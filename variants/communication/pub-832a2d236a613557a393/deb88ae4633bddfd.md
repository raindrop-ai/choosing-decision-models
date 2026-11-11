# Similar distractors · Add more similar but irrelevant items variant

[Original question](../../../questions/communication/pub-832a2d236a613557a393.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> «Context: Varelin and Nerava are choosing an outing.
> Varelin: Would you like to visit the gallery?
> Nerava: I would rather spend the afternoon outdoors.»
>
> «Context: Ovelin asks Zelmin about a meal.
> Ovelin: Would you like more soup?
> Zelmin: My bowl is still full.»
>
> «Context: Travon and Elvarin are discussing a concert.
> Travon: The rehearsal was as smooth as sandpaper.
> Elvarin: The musicians stumbled through every transition.»
>
> Context: "Could you please lend me a hand? "
> Question: What does "hand " refer to :?

## Question

> Choose the interpretation or answer requested by the text.

## Answer choices

- **A.** Hand of a person 
- **B.** Paper
- **C.** Help
- **D.** Leg

**Reference answer:** `C`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "«Context: Varelin and Nerava are choosing an outing.\nVarelin: Would you like to visit the gallery?\nNerava: I would rather spend the afternoon outdoors.»\n\n«Context: Ovelin asks Zelmin about a meal.\nOvelin: Would you like more soup?\nZelmin: My bowl is still full.»\n\n«Context: Travon and Elvarin are discussing a concert.\nTravon: The rehearsal was as smooth as sandpaper.\nElvarin: The musicians stumbled through every transition.»\n\nContext: \"Could you please lend me a hand? \"\nQuestion: What does \"hand \" refer to :?\n",
  "question": "Choose the interpretation or answer requested by the text.",
  "choices": {
    "A": "Hand of a person ",
    "B": "Paper",
    "C": "Help",
    "D": "Leg"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `C` — Help | `C` — Help | Same answer |
| Decider v1.1 | `C` — Help | `C` — Help | Same answer |
| Jev | `C` — Help | `C` — Help | Same answer |
| Microsoft Decision-1 | `C` — Help | `C` — Help | Same answer |
| Clef | `C` — Help | `C` — Help | Same answer |
| Luna Decisions | `C` — Help | `C` — Help | Same answer |
| Clef Flash | `C` — Help | `C` — Help | Same answer |
| Strands Decider | `C` — Help | `C` — Help | Same answer |
| GLiNER2.5 Decide | `A` — Hand of a person  | `A` — Hand of a person  | Same answer |
| Laya | `A` — Hand of a person  | `A` — Hand of a person  | Same answer |
| CalDec v1 | `A` — Hand of a person  | `A` — Hand of a person  | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `pub/832a2d236a613557a393/similar_distractors/high/clean-source_first_pub_near_records_full_0244`

**Input fingerprint:** `d535b70517bc62996d8ff5c7be218b9e6668a6a546cbb6555f9e704ad84e47c1`

| Change | Recorded version |
| --- | --- |
| Similar distractors | Add more similar but irrelevant items |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/communication/pub-832a2d236a613557a393.md).
