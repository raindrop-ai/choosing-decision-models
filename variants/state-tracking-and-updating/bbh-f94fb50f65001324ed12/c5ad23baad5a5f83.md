# Misleading details · Add an unverified claim that conflicts with the evidence variant

[Original question](../../../questions/state-tracking-and-updating/bbh-f94fb50f65001324ed12.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> A reader thinks: «At the end of the dance, Alice is dancing with Jamie.»

## Question

> Alice, Bob, and Claire are dancers at a square dance. At the start of a song, they each have a partner: Alice is dancing with Izzi, Bob is dancing with Jamie, and Claire is dancing with Rodrigo.
> Throughout the song, the dancers often trade partners. First, Bob and Alice switch partners. Then, Alice and Claire switch partners. Finally, Claire and Bob switch partners. At the end of the dance, Alice is dancing with

## Answer choices

- **A.** Izzi
- **B.** Jamie
- **C.** Rodrigo

**Reference answer:** `C`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "A reader thinks: «At the end of the dance, Alice is dancing with Jamie.»",
  "question": "Alice, Bob, and Claire are dancers at a square dance. At the start of a song, they each have a partner: Alice is dancing with Izzi, Bob is dancing with Jamie, and Claire is dancing with Rodrigo.\nThroughout the song, the dancers often trade partners. First, Bob and Alice switch partners. Then, Alice and Claire switch partners. Finally, Claire and Bob switch partners. At the end of the dance, Alice is dancing with",
  "choices": {
    "A": "Izzi",
    "B": "Jamie",
    "C": "Rodrigo"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `C` — Rodrigo | `C` — Rodrigo | Same answer |
| Decider v1.1 | `C` — Rodrigo | `C` — Rodrigo | Same answer |
| Jev | `C` — Rodrigo | `C` — Rodrigo | Same answer |
| Microsoft Decision-1 | `A` — Izzi | `A` — Izzi | Same answer |
| Clef | `C` — Rodrigo | `C` — Rodrigo | Same answer |
| Luna Decisions | `B` — Jamie | `B` — Jamie | Same answer |
| Clef Flash | `C` — Rodrigo | `C` — Rodrigo | Same answer |
| Strands Decider | `C` — Rodrigo | `B` — Jamie | Different answer |
| GLiNER2.5 Decide | `A` — Izzi | `B` — Jamie | Different answer |
| Laya | `A` — Izzi | `B` — Jamie | Different answer |
| CalDec v1 | `A` — Izzi | `B` — Jamie | Different answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `bbh/f94fb50f65001324ed12/misleading_summary/misleading/clean-source_first_tracking_reader_predictions_full_0122`

**Input fingerprint:** `1e135d12273c3ad3f99dc81f6ef97383111a35ed8246741e618a73f67842acc6`

| Change | Recorded version |
| --- | --- |
| Misleading details | Add an unverified claim that conflicts with the evidence |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/state-tracking-and-updating/bbh-f94fb50f65001324ed12.md).
