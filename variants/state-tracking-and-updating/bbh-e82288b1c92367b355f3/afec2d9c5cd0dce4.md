# Unrelated examples · Add examples unrelated to the question variant

[Original question](../../../questions/state-tracking-and-updating/bbh-e82288b1c92367b355f3.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Capitalization: harbor → Harbor

## Question

> Alice, Bob, and Claire are on the same team in a soccer match. At the start of the match, they are each assigned to a position: Alice is playing cheerleader, Bob is playing benchwarmer, and Claire is playing left winger.
> As the game progresses, pairs of players occasionally swap positions. First, Claire and Bob trade positions. Then, Claire and Alice trade positions. Finally, Claire and Bob trade positions. At the end of the match, Claire is playing

## Answer choices

- **A.** cheerleader
- **B.** benchwarmer
- **C.** left winger

**Reference answer:** `C`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Capitalization: harbor → Harbor",
  "question": "Alice, Bob, and Claire are on the same team in a soccer match. At the start of the match, they are each assigned to a position: Alice is playing cheerleader, Bob is playing benchwarmer, and Claire is playing left winger.\nAs the game progresses, pairs of players occasionally swap positions. First, Claire and Bob trade positions. Then, Claire and Alice trade positions. Finally, Claire and Bob trade positions. At the end of the match, Claire is playing",
  "choices": {
    "A": "cheerleader",
    "B": "benchwarmer",
    "C": "left winger"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `C` — left winger | `C` — left winger | Same answer |
| Decider v1.1 | `B` — benchwarmer | `A` — cheerleader | Different answer |
| Jev | `C` — left winger | `C` — left winger | Same answer |
| Microsoft Decision-1 | `C` — left winger | `C` — left winger | Same answer |
| Clef | `B` — benchwarmer | `B` — benchwarmer | Same answer |
| Luna Decisions | `A` — cheerleader | `A` — cheerleader | Same answer |
| Clef Flash | `B` — benchwarmer | `B` — benchwarmer | Same answer |
| Strands Decider | `B` — benchwarmer | `A` — cheerleader | Different answer |
| GLiNER2.5 Decide | `A` — cheerleader | `A` — cheerleader | Same answer |
| Laya | `C` — left winger | `C` — left winger | Same answer |
| CalDec v1 | `C` — left winger | `C` — left winger | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `bbh/e82288b1c92367b355f3/examples/irrelevant/clean-source_first_tracking_short_contexts_full_0120`

**Input fingerprint:** `b4f13fecfb24df96d52cc6946eee0eea25674f5835c98557726a2610e54ab787`

| Change | Recorded version |
| --- | --- |
| Unrelated examples | Add examples unrelated to the question |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/state-tracking-and-updating/bbh-e82288b1c92367b355f3.md).
