# Unrelated examples · Add examples unrelated to the question variant

[Original question](../../../questions/relations/bbh-a3c4787ea5640260cdd0.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Uppercase: meadow → MEADOW

## Question

> The following paragraphs each describe a set of seven objects arranged in a fixed order. The statements are logically consistent within each paragraph. In an antique car show, there are seven vehicles: a limousine, a sedan, a tractor, a motorcyle, a minivan, a hatchback, and a truck. The minivan is newer than the limousine. The tractor is the second-newest. The truck is older than the sedan. The minivan is older than the truck. The hatchback is newer than the tractor. The motorcyle is the fourth-newest.

## Answer choices

- **A.** The limousine is the oldest
- **B.** The sedan is the oldest
- **C.** The tractor is the oldest
- **D.** The motorcyle is the oldest
- **E.** The minivan is the oldest
- **F.** The hatchback is the oldest
- **G.** The truck is the oldest

**Reference answer:** `A`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Uppercase: meadow → MEADOW",
  "question": "The following paragraphs each describe a set of seven objects arranged in a fixed order. The statements are logically consistent within each paragraph. In an antique car show, there are seven vehicles: a limousine, a sedan, a tractor, a motorcyle, a minivan, a hatchback, and a truck. The minivan is newer than the limousine. The tractor is the second-newest. The truck is older than the sedan. The minivan is older than the truck. The hatchback is newer than the tractor. The motorcyle is the fourth-newest.",
  "choices": {
    "A": "The limousine is the oldest",
    "B": "The sedan is the oldest",
    "C": "The tractor is the oldest",
    "D": "The motorcyle is the oldest",
    "E": "The minivan is the oldest",
    "F": "The hatchback is the oldest",
    "G": "The truck is the oldest"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `A` — The limousine is the oldest | `A` — The limousine is the oldest | Same answer |
| Decider v1.1 | `A` — The limousine is the oldest | `A` — The limousine is the oldest | Same answer |
| Jev | `A` — The limousine is the oldest | `A` — The limousine is the oldest | Same answer |
| Microsoft Decision-1 | `A` — The limousine is the oldest | `A` — The limousine is the oldest | Same answer |
| Clef | `A` — The limousine is the oldest | `A` — The limousine is the oldest | Same answer |
| Luna Decisions | `B` — The sedan is the oldest | `A` — The limousine is the oldest | Different answer |
| Clef Flash | `A` — The limousine is the oldest | `A` — The limousine is the oldest | Same answer |
| Strands Decider | `A` — The limousine is the oldest | `A` — The limousine is the oldest | Same answer |
| GLiNER2.5 Decide | `E` — The minivan is the oldest | `E` — The minivan is the oldest | Same answer |
| Laya | `E` — The minivan is the oldest | `E` — The minivan is the oldest | Same answer |
| CalDec v1 | `E` — The minivan is the oldest | `E` — The minivan is the oldest | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `bbh/a3c4787ea5640260cdd0/examples/irrelevant/clean-ordinal_irrelevant_examples_full_0029`

**Input fingerprint:** `f40d3ae8d2bb2f8918001e960896bf76597e0e5b8f03e1da99d0cc13c32ee620`

| Change | Recorded version |
| --- | --- |
| Unrelated examples | Add examples unrelated to the question |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/relations/bbh-a3c4787ea5640260cdd0.md).
