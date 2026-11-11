# Unrelated examples · Add examples unrelated to the question variant

[Original question](../../../questions/state-tracking-and-updating/bbh-11517ef69a2d8f856467.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Capitalization: harbor → Harbor

## Question

> Alice, Bob, Claire, Dave, and Eve are holding a white elephant gift exchange. At the start of the event, they are each holding a present of a different color: Alice has a purple present, Bob has a blue present, Claire has a brown present, Dave has a yellow present, and Eve has a black ball.
> As the event progresses, pairs of people swap gifts. First, Alice and Bob swap their gifts. Then, Bob and Dave swap their gifts. Then, Claire and Bob swap their gifts. Then, Dave and Alice swap their gifts. Finally, Dave and Eve swap their gifts. At the end of the event, Dave has the

## Answer choices

- **A.** purple present
- **B.** blue present
- **C.** brown present
- **D.** yellow present
- **E.** black ball

**Reference answer:** `E`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Capitalization: harbor → Harbor",
  "question": "Alice, Bob, Claire, Dave, and Eve are holding a white elephant gift exchange. At the start of the event, they are each holding a present of a different color: Alice has a purple present, Bob has a blue present, Claire has a brown present, Dave has a yellow present, and Eve has a black ball.\nAs the event progresses, pairs of people swap gifts. First, Alice and Bob swap their gifts. Then, Bob and Dave swap their gifts. Then, Claire and Bob swap their gifts. Then, Dave and Alice swap their gifts. Finally, Dave and Eve swap their gifts. At the end of the event, Dave has the",
  "choices": {
    "A": "purple present",
    "B": "blue present",
    "C": "brown present",
    "D": "yellow present",
    "E": "black ball"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `E` — black ball | `E` — black ball | Same answer |
| Decider v1.1 | `E` — black ball | `E` — black ball | Same answer |
| Jev | `E` — black ball | `E` — black ball | Same answer |
| Microsoft Decision-1 | `E` — black ball | `E` — black ball | Same answer |
| Clef | `E` — black ball | `E` — black ball | Same answer |
| Luna Decisions | `A` — purple present | `A` — purple present | Same answer |
| Clef Flash | `E` — black ball | `E` — black ball | Same answer |
| Strands Decider | `A` — purple present | `A` — purple present | Same answer |
| GLiNER2.5 Decide | `A` — purple present | `A` — purple present | Same answer |
| Laya | `D` — yellow present | `D` — yellow present | Same answer |
| CalDec v1 | `D` — yellow present | `D` — yellow present | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `bbh/11517ef69a2d8f856467/examples/irrelevant/clean-source_first_tracking_short_contexts_full_0120`

**Input fingerprint:** `0c14e5250d5d96d81ea65de5d127d6956f5f056d1ef1ff49f602fc114c043b6b`

| Change | Recorded version |
| --- | --- |
| Unrelated examples | Add examples unrelated to the question |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/state-tracking-and-updating/bbh-11517ef69a2d8f856467.md).
