# Similar distractors · Add fewer similar but irrelevant items variant

[Original question](../../../questions/state-tracking-and-updating/bbh-e9d5fa0fe20ed7cd4ead.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Varelin holds a flute. Zorven holds a maraca. Nereth holds an oboe. Varelin and Zorven exchange their instruments.

## Question

> Alice, Bob, and Claire are holding a white elephant gift exchange. At the start of the event, they are each holding a present of a different color: Alice has a orange ball, Bob has a green present, and Claire has a red present.
> As the event progresses, pairs of people swap gifts. First, Bob and Alice swap their gifts. Then, Bob and Claire swap their gifts. Finally, Alice and Claire swap their gifts. At the end of the event, Alice has the

## Answer choices

- **A.** orange ball
- **B.** green present
- **C.** red present

**Reference answer:** `A`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Varelin holds a flute. Zorven holds a maraca. Nereth holds an oboe. Varelin and Zorven exchange their instruments.",
  "question": "Alice, Bob, and Claire are holding a white elephant gift exchange. At the start of the event, they are each holding a present of a different color: Alice has a orange ball, Bob has a green present, and Claire has a red present.\nAs the event progresses, pairs of people swap gifts. First, Bob and Alice swap their gifts. Then, Bob and Claire swap their gifts. Finally, Alice and Claire swap their gifts. At the end of the event, Alice has the",
  "choices": {
    "A": "orange ball",
    "B": "green present",
    "C": "red present"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `A` — orange ball | `A` — orange ball | Same answer |
| Decider v1.1 | `C` — red present | `C` — red present | Same answer |
| Jev | `A` — orange ball | `B` — green present | Different answer |
| Microsoft Decision-1 | `A` — orange ball | `A` — orange ball | Same answer |
| Clef | `C` — red present | `C` — red present | Same answer |
| Luna Decisions | `B` — green present | `A` — orange ball | Different answer |
| Clef Flash | `C` — red present | `C` — red present | Same answer |
| Strands Decider | `C` — red present | `C` — red present | Same answer |
| GLiNER2.5 Decide | `A` — orange ball | `A` — orange ball | Same answer |
| Laya | `A` — orange ball | `A` — orange ball | Same answer |
| CalDec v1 | `A` — orange ball | `A` — orange ball | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `bbh/e9d5fa0fe20ed7cd4ead/similar_distractors/low/clean-source_first_tracking_new_distractors_full_0165`

**Input fingerprint:** `6f8bf4dc816c500b102b15d86d17b90767765034e95dbd9578c3e28117fb72bc`

| Change | Recorded version |
| --- | --- |
| Similar distractors | Add fewer similar but irrelevant items |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/state-tracking-and-updating/bbh-e9d5fa0fe20ed7cd4ead.md).
