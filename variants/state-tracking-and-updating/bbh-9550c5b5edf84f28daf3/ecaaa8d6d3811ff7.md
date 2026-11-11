# Invented names · Use invented names variant

[Original question](../../../questions/state-tracking-and-updating/bbh-9550c5b5edf84f28daf3.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** question instructions.

[How the edits were constructed](../../../docs/variant-methods.md)

## Question

> Varelin, Zorven, Nelarik, Tovrin, Kasel, Mireth, and Dazorin are friends and avid readers who occasionally trade books. At the start of the semester, they each buy one new book: Varelin gets The Great Gatsby, Zorven gets The Fellowship of the Ring, Nelarik gets Ulysses, Tovrin gets The Odyssey, Kasel gets Frankenstein, Mireth gets Hound of the Baskervilles, and Dazorin gets Moby Dick.
> As the semester proceeds, they start trading around the new books. First, Nelarik and Kasel swap books. Then, Tovrin and Mireth swap books. Then, Varelin and Kasel swap books. Then, Nelarik and Tovrin swap books. Then, Mireth and Nelarik swap books. Then, Nelarik and Dazorin swap books. Finally, Mireth and Zorven swap books. At the end of the semester, Mireth has

## Answer choices

- **A.** The Great Gatsby
- **B.** The Fellowship of the Ring
- **C.** Ulysses
- **D.** The Odyssey
- **E.** Frankenstein
- **F.** Hound of the Baskervilles
- **G.** Moby Dick

**Reference answer:** `B`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "",
  "question": "Varelin, Zorven, Nelarik, Tovrin, Kasel, Mireth, and Dazorin are friends and avid readers who occasionally trade books. At the start of the semester, they each buy one new book: Varelin gets The Great Gatsby, Zorven gets The Fellowship of the Ring, Nelarik gets Ulysses, Tovrin gets The Odyssey, Kasel gets Frankenstein, Mireth gets Hound of the Baskervilles, and Dazorin gets Moby Dick.\nAs the semester proceeds, they start trading around the new books. First, Nelarik and Kasel swap books. Then, Tovrin and Mireth swap books. Then, Varelin and Kasel swap books. Then, Nelarik and Tovrin swap books. Then, Mireth and Nelarik swap books. Then, Nelarik and Dazorin swap books. Finally, Mireth and Zorven swap books. At the end of the semester, Mireth has",
  "choices": {
    "A": "The Great Gatsby",
    "B": "The Fellowship of the Ring",
    "C": "Ulysses",
    "D": "The Odyssey",
    "E": "Frankenstein",
    "F": "Hound of the Baskervilles",
    "G": "Moby Dick"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `B` — The Fellowship of the Ring | `B` — The Fellowship of the Ring | Same answer |
| Decider v1.1 | `B` — The Fellowship of the Ring | `B` — The Fellowship of the Ring | Same answer |
| Jev | `B` — The Fellowship of the Ring | `B` — The Fellowship of the Ring | Same answer |
| Microsoft Decision-1 | `B` — The Fellowship of the Ring | `B` — The Fellowship of the Ring | Same answer |
| Clef | `B` — The Fellowship of the Ring | `B` — The Fellowship of the Ring | Same answer |
| Luna Decisions | `B` — The Fellowship of the Ring | `C` — Ulysses | Different answer |
| Clef Flash | `B` — The Fellowship of the Ring | `B` — The Fellowship of the Ring | Same answer |
| Strands Decider | `G` — Moby Dick | `E` — Frankenstein | Different answer |
| GLiNER2.5 Decide | `A` — The Great Gatsby | `A` — The Great Gatsby | Same answer |
| Laya | `A` — The Great Gatsby | `A` — The Great Gatsby | Same answer |
| CalDec v1 | `F` — Hound of the Baskervilles | `A` — The Great Gatsby | Different answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `bbh/9550c5b5edf84f28daf3/unfamiliar_names/invented`

**Input fingerprint:** `00000b9f421bb58370cf4066e3c2ea6b04c2ae8f597f7d8659d0b021ace4ca29`

| Change | Recorded version |
| --- | --- |
| Invented names | Use invented names |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/state-tracking-and-updating/bbh-9550c5b5edf84f28daf3.md).
