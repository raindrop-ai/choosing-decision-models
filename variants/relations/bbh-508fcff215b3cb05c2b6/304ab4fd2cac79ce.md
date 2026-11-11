# Evidence order · Present the evidence in a shuffled order variant

[Original question](../../../questions/relations/bbh-508fcff215b3cb05c2b6.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** question instructions.

[How the edits were constructed](../../../docs/variant-methods.md)

## Question

> The following paragraphs each describe a set of seven objects arranged in a fixed order. The statements are logically consistent within each paragraph. In an antique car show, there are seven vehicles: a sedan, a minivan, a motorcyle, a limousine, a hatchback, a truck, and a tractor. The hatchback is older than the limousine. The truck is newer than the tractor. The sedan is the third-newest. The motorcyle is older than the tractor. The hatchback is newer than the truck. The minivan is the second-newest.

## Answer choices

- **A.** The sedan is the oldest
- **B.** The minivan is the oldest
- **C.** The motorcyle is the oldest
- **D.** The limousine is the oldest
- **E.** The hatchback is the oldest
- **F.** The truck is the oldest
- **G.** The tractor is the oldest

**Reference answer:** `C`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "",
  "question": "The following paragraphs each describe a set of seven objects arranged in a fixed order. The statements are logically consistent within each paragraph. In an antique car show, there are seven vehicles: a sedan, a minivan, a motorcyle, a limousine, a hatchback, a truck, and a tractor. The hatchback is older than the limousine. The truck is newer than the tractor. The sedan is the third-newest. The motorcyle is older than the tractor. The hatchback is newer than the truck. The minivan is the second-newest.",
  "choices": {
    "A": "The sedan is the oldest",
    "B": "The minivan is the oldest",
    "C": "The motorcyle is the oldest",
    "D": "The limousine is the oldest",
    "E": "The hatchback is the oldest",
    "F": "The truck is the oldest",
    "G": "The tractor is the oldest"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `C` — The motorcyle is the oldest | `C` — The motorcyle is the oldest | Same answer |
| Decider v1.1 | `C` — The motorcyle is the oldest | `C` — The motorcyle is the oldest | Same answer |
| Jev | `C` — The motorcyle is the oldest | `C` — The motorcyle is the oldest | Same answer |
| Microsoft Decision-1 | `C` — The motorcyle is the oldest | `G` — The tractor is the oldest | Different answer |
| Clef | `D` — The limousine is the oldest | `D` — The limousine is the oldest | Same answer |
| Luna Decisions | `C` — The motorcyle is the oldest | `C` — The motorcyle is the oldest | Same answer |
| Clef Flash | `C` — The motorcyle is the oldest | `C` — The motorcyle is the oldest | Same answer |
| Strands Decider | `C` — The motorcyle is the oldest | `E` — The hatchback is the oldest | Different answer |
| GLiNER2.5 Decide | `G` — The tractor is the oldest | `G` — The tractor is the oldest | Same answer |
| Laya | `C` — The motorcyle is the oldest | `A` — The sedan is the oldest | Different answer |
| CalDec v1 | `B` — The minivan is the oldest | `A` — The sedan is the oldest | Different answer |

**Ordering comparison:** literal requested source unit permutation. Only the exact matched comparison sets contribute to the reported ordering contrasts.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `bbh/508fcff215b3cb05c2b6/presentation_order/shuffled_presentation/clean-bare_ordinal_fact_order_full_0050`

**Input fingerprint:** `43cca42e132546fc27b5e6939f018a61263766ecab39ea32db358b3f8a043a4c`

| Change | Recorded version |
| --- | --- |
| Evidence order | Present the evidence in a shuffled order |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/relations/bbh-508fcff215b3cb05c2b6.md).
