# Extra events · Add 12 unrelated events variant

[Original question](../../../questions/spatial-cognition/spartqa-e957e04abe5a035ea3a3.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Nolan is the editor of a poetry catalog. Its entries are Virel, Zorven, Kesil, Nereth, Pavrel, and Sovrin.
> Nolan classifies Virel as a dialogue. Nolan classifies Zorven as a monologue. Nolan classifies Kesil as an elegy. Nolan classifies Nereth as a satire. Nolan classifies Pavrel as a fable. Nolan classifies Sovrin as a ballad. Nolan reclassifies Virel as a monologue. Nolan reclassifies Zorven as a dialogue. Nolan reclassifies Kesil as a ballad. Nolan reclassifies Nereth as a fable. Nolan reclassifies Pavrel as a satire. Nolan reclassifies Sovrin as an elegy.
>
> There are three blocks. We call them A, B and C. Block A is above B. Block B is to the right of C. Block A contains one medium yellow square. Block B contains a medium black square. A medium blue square is below the medium black square. Block C contains two medium yellow squares. Medium yellow square number one is below medium yellow square number two.. A medium blue square is below medium yellow square number one and medium yellow square number two.

## Question

> Which object is to the left of a medium blue square? the medium yellow square that is in block A or medium yellow square number one?

## Answer choices

- **0.** the medium yellow square  that is in block A
- **1.** medium yellow square  number one
- **2.** both of them
- **3.** none of them

**Reference answer:** `1`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Nolan is the editor of a poetry catalog. Its entries are Virel, Zorven, Kesil, Nereth, Pavrel, and Sovrin.\nNolan classifies Virel as a dialogue. Nolan classifies Zorven as a monologue. Nolan classifies Kesil as an elegy. Nolan classifies Nereth as a satire. Nolan classifies Pavrel as a fable. Nolan classifies Sovrin as a ballad. Nolan reclassifies Virel as a monologue. Nolan reclassifies Zorven as a dialogue. Nolan reclassifies Kesil as a ballad. Nolan reclassifies Nereth as a fable. Nolan reclassifies Pavrel as a satire. Nolan reclassifies Sovrin as an elegy.\n\nThere are three blocks. We call them A, B and C. Block A is above B. Block B is to the right of C. Block A contains one medium yellow square. Block B contains a medium black square. A medium blue square is below the medium black square. Block C contains two medium yellow squares. Medium yellow square number one is below medium yellow square number two.. A medium blue square is below medium yellow square number one and medium yellow square number two.",
  "question": "Which object is to the left of a medium blue square? the medium yellow square that is in block A or medium yellow square number one?",
  "choices": {
    "0": "the medium yellow square  that is in block A",
    "1": "medium yellow square  number one",
    "2": "both of them",
    "3": "none of them"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `1` — medium yellow square  number one | `1` — medium yellow square  number one | Same answer |
| Decider v1.1 | `1` — medium yellow square  number one | `1` — medium yellow square  number one | Same answer |
| Jev | `1` — medium yellow square  number one | `1` — medium yellow square  number one | Same answer |
| Microsoft Decision-1 | `1` — medium yellow square  number one | `1` — medium yellow square  number one | Same answer |
| Clef | `2` — both of them | `1` — medium yellow square  number one | Different answer |
| Luna Decisions | `3` — none of them | `2` — both of them | Different answer |
| Clef Flash | `1` — medium yellow square  number one | `0` — the medium yellow square  that is in block A | Different answer |
| Strands Decider | `1` — medium yellow square  number one | `1` — medium yellow square  number one | Same answer |
| GLiNER2.5 Decide | `1` — medium yellow square  number one | `1` — medium yellow square  number one | Same answer |
| Laya | `2` — both of them | `2` — both of them | Same answer |
| CalDec v1 | `2` — both of them | `2` — both of them | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `spartqa/e957e04abe5a035ea3a3/event_count/12/clean-source_first_spartqa_short_contexts_full_0136`

**Input fingerprint:** `3c7864ec1a6b0ee7e4180f5677ea96d6793a44019869578cbcd05f63d6fd45aa`

| Change | Recorded version |
| --- | --- |
| Extra events | Add 12 unrelated events |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/spatial-cognition/spartqa-e957e04abe5a035ea3a3.md).
