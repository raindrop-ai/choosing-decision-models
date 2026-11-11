# Evidence order · Present the evidence in reverse order variant

[Original question](../../../questions/relations/bbh-8315801669ef12c9085e.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** question instructions.

[How the edits were constructed](../../../docs/variant-methods.md)

## Question

> The following paragraphs each describe a set of five objects arranged in a fixed order. The statements are logically consistent within each paragraph. In an antique car show, there are five vehicles: a minivan, a hatchback, a bus, a convertible, and a motorcyle. The minivan is the newest. The bus is older than the motorcyle. The bus is newer than the hatchback. The hatchback is newer than the convertible.

## Answer choices

- **A.** The minivan is the third-newest
- **B.** The hatchback is the third-newest
- **C.** The bus is the third-newest
- **D.** The convertible is the third-newest
- **E.** The motorcyle is the third-newest

**Reference answer:** `C`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "",
  "question": "The following paragraphs each describe a set of five objects arranged in a fixed order. The statements are logically consistent within each paragraph. In an antique car show, there are five vehicles: a minivan, a hatchback, a bus, a convertible, and a motorcyle. The minivan is the newest. The bus is older than the motorcyle. The bus is newer than the hatchback. The hatchback is newer than the convertible.",
  "choices": {
    "A": "The minivan is the third-newest",
    "B": "The hatchback is the third-newest",
    "C": "The bus is the third-newest",
    "D": "The convertible is the third-newest",
    "E": "The motorcyle is the third-newest"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `C` — The bus is the third-newest | `C` — The bus is the third-newest | Same answer |
| Decider v1.1 | `C` — The bus is the third-newest | `C` — The bus is the third-newest | Same answer |
| Jev | `C` — The bus is the third-newest | `C` — The bus is the third-newest | Same answer |
| Microsoft Decision-1 | `B` — The hatchback is the third-newest | `C` — The bus is the third-newest | Different answer |
| Clef | `C` — The bus is the third-newest | `C` — The bus is the third-newest | Same answer |
| Luna Decisions | `C` — The bus is the third-newest | `C` — The bus is the third-newest | Same answer |
| Clef Flash | `E` — The motorcyle is the third-newest | `B` — The hatchback is the third-newest | Different answer |
| Strands Decider | `C` — The bus is the third-newest | `C` — The bus is the third-newest | Same answer |
| GLiNER2.5 Decide | `A` — The minivan is the third-newest | `A` — The minivan is the third-newest | Same answer |
| Laya | `B` — The hatchback is the third-newest | `C` — The bus is the third-newest | Different answer |
| CalDec v1 | `A` — The minivan is the third-newest | `A` — The minivan is the third-newest | Same answer |

**Ordering comparison:** literal requested source unit permutation. Only the exact matched comparison sets contribute to the reported ordering contrasts.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `bbh/8315801669ef12c9085e/presentation_order/reverse_presentation/clean-bare_ordinal_fact_order_full_0050`

**Input fingerprint:** `d87c963198414279bc1df84082aef9a7d786e8f338e21248c27ac95425f90213`

| Change | Recorded version |
| --- | --- |
| Evidence order | Present the evidence in reverse order |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/relations/bbh-8315801669ef12c9085e.md).
