# Similar distractors · Add fewer similar but irrelevant items variant

[Original question](../../../questions/relations/bbh-427bb77735cc3cf1ca0d.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> In the Estel Maritime Museum registry, a tugboat is newer than a sailboat. A ferry is older than the sailboat.

## Question

> The following paragraphs each describe a set of five objects arranged in a fixed order. The statements are logically consistent within each paragraph. In an antique car show, there are five vehicles: a truck, a station wagon, a motorcyle, a limousine, and a hatchback. The motorcyle is the second-newest. The truck is newer than the limousine. The motorcyle is older than the station wagon. The limousine is newer than the hatchback.

## Answer choices

- **A.** The truck is the oldest
- **B.** The station wagon is the oldest
- **C.** The motorcyle is the oldest
- **D.** The limousine is the oldest
- **E.** The hatchback is the oldest

**Reference answer:** `E`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "In the Estel Maritime Museum registry, a tugboat is newer than a sailboat. A ferry is older than the sailboat.",
  "question": "The following paragraphs each describe a set of five objects arranged in a fixed order. The statements are logically consistent within each paragraph. In an antique car show, there are five vehicles: a truck, a station wagon, a motorcyle, a limousine, and a hatchback. The motorcyle is the second-newest. The truck is newer than the limousine. The motorcyle is older than the station wagon. The limousine is newer than the hatchback.",
  "choices": {
    "A": "The truck is the oldest",
    "B": "The station wagon is the oldest",
    "C": "The motorcyle is the oldest",
    "D": "The limousine is the oldest",
    "E": "The hatchback is the oldest"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `E` — The hatchback is the oldest | `E` — The hatchback is the oldest | Same answer |
| Decider v1.1 | `E` — The hatchback is the oldest | `E` — The hatchback is the oldest | Same answer |
| Jev | `E` — The hatchback is the oldest | `E` — The hatchback is the oldest | Same answer |
| Microsoft Decision-1 | `E` — The hatchback is the oldest | `E` — The hatchback is the oldest | Same answer |
| Clef | `E` — The hatchback is the oldest | `E` — The hatchback is the oldest | Same answer |
| Luna Decisions | `B` — The station wagon is the oldest | `E` — The hatchback is the oldest | Different answer |
| Clef Flash | `E` — The hatchback is the oldest | `E` — The hatchback is the oldest | Same answer |
| Strands Decider | `A` — The truck is the oldest | `D` — The limousine is the oldest | Different answer |
| GLiNER2.5 Decide | `D` — The limousine is the oldest | `C` — The motorcyle is the oldest | Different answer |
| Laya | `A` — The truck is the oldest | `A` — The truck is the oldest | Same answer |
| CalDec v1 | `A` — The truck is the oldest | `C` — The motorcyle is the oldest | Different answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `bbh/427bb77735cc3cf1ca0d/similar_distractors/low/clean-source_first_ordinal_distractors_full_0140`

**Input fingerprint:** `9e9a738afd5466987b663276b1ab3a68bc5f659ecc0f2d2e03cb30821436c97c`

| Change | Recorded version |
| --- | --- |
| Similar distractors | Add fewer similar but irrelevant items |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/relations/bbh-427bb77735cc3cf1ca0d.md).
