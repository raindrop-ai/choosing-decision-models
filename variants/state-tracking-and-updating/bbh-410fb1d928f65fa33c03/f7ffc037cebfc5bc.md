# Paraphrasing · Change individual words and phrases variant

[Original question](../../../questions/state-tracking-and-updating/bbh-410fb1d928f65fa33c03.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** question instructions.

[How the edits were constructed](../../../docs/variant-methods.md)

## Question

> Alice, Bob, and Claire are friends and avid readers who occasionally trade books. At the start of the semester, they each buy one new book: Alice gets Catch-22, Bob gets Moby Dick, and Claire gets The Fellowship of the Ring.
> As the semester proceeds, they start trading around the new books. First, Claire and Alice swap books. Then, Bob and Alice swap books. Finally, Claire and Bob swap books. At the end of the semester, which book does Alice have?

## Answer choices

- **A.** Catch-22
- **B.** Moby Dick
- **C.** The Fellowship of the Ring

**Reference answer:** `B`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "",
  "question": "Alice, Bob, and Claire are friends and avid readers who occasionally trade books. At the start of the semester, they each buy one new book: Alice gets Catch-22, Bob gets Moby Dick, and Claire gets The Fellowship of the Ring.\nAs the semester proceeds, they start trading around the new books. First, Claire and Alice swap books. Then, Bob and Alice swap books. Finally, Claire and Bob swap books. At the end of the semester, which book does Alice have?",
  "choices": {
    "A": "Catch-22",
    "B": "Moby Dick",
    "C": "The Fellowship of the Ring"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `B` — Moby Dick | `B` — Moby Dick | Same answer |
| Decider v1.1 | `B` — Moby Dick | `B` — Moby Dick | Same answer |
| Jev | `B` — Moby Dick | `B` — Moby Dick | Same answer |
| Microsoft Decision-1 | `C` — The Fellowship of the Ring | `C` — The Fellowship of the Ring | Same answer |
| Clef | `B` — Moby Dick | `B` — Moby Dick | Same answer |
| Luna Decisions | `C` — The Fellowship of the Ring | `C` — The Fellowship of the Ring | Same answer |
| Clef Flash | `B` — Moby Dick | `C` — The Fellowship of the Ring | Different answer |
| Strands Decider | `C` — The Fellowship of the Ring | `C` — The Fellowship of the Ring | Same answer |
| GLiNER2.5 Decide | `A` — Catch-22 | `A` — Catch-22 | Same answer |
| Laya | `A` — Catch-22 | `A` — Catch-22 | Same answer |
| CalDec v1 | `A` — Catch-22 | `A` — Catch-22 | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `bbh/410fb1d928f65fa33c03/paraphrasing/surface`

**Input fingerprint:** `d3cbebecdda31654e2eb7d20be8432562a277460893ff9503f874e8e91017801`

| Change | Recorded version |
| --- | --- |
| Paraphrasing | Change individual words and phrases |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/state-tracking-and-updating/bbh-410fb1d928f65fa33c03.md).
