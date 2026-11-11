# Irrelevant details · Add a small amount of irrelevant detail variant

[Original question](../../../questions/state-tracking-and-updating/bbh-f94fb50f65001324ed12.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> The notebook has a linen cover.

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
  "state": "The notebook has a linen cover.",
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
| Strands Decider | `C` — Rodrigo | `C` — Rodrigo | Same answer |
| GLiNER2.5 Decide | `A` — Izzi | `A` — Izzi | Same answer |
| Laya | `A` — Izzi | `A` — Izzi | Same answer |
| CalDec v1 | `A` — Izzi | `A` — Izzi | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `bbh/f94fb50f65001324ed12/irrelevant_details/low/clean-source_first_tracking_short_contexts_full_0120`

**Input fingerprint:** `039defc9ee7c702aea89d878c81eae8ec311f27b647979b40b54cd0ce61c22cc`

| Change | Recorded version |
| --- | --- |
| Irrelevant details | Add a small amount of irrelevant detail |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/state-tracking-and-updating/bbh-f94fb50f65001324ed12.md).
