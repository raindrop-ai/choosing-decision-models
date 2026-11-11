# Irrelevant details · Add a larger amount of irrelevant detail variant

[Original question](../../../questions/relations/bbh-508fcff215b3cb05c2b6.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> The exhibition hall has a stone floor.
> The ceiling is vaulted.
> The window frames are metal.
> The entrance mat is rubber.
> The wall panels are wood.
> The noticeboard has an aluminum frame.

## Question

> The following paragraphs each describe a set of seven objects arranged in a fixed order. The statements are logically consistent within each paragraph. In an antique car show, there are seven vehicles: a sedan, a minivan, a motorcyle, a limousine, a hatchback, a truck, and a tractor. The motorcyle is older than the tractor. The hatchback is older than the limousine. The hatchback is newer than the truck. The truck is newer than the tractor. The minivan is the second-newest. The sedan is the third-newest.

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
  "state": "The exhibition hall has a stone floor.\nThe ceiling is vaulted.\nThe window frames are metal.\nThe entrance mat is rubber.\nThe wall panels are wood.\nThe noticeboard has an aluminum frame.",
  "question": "The following paragraphs each describe a set of seven objects arranged in a fixed order. The statements are logically consistent within each paragraph. In an antique car show, there are seven vehicles: a sedan, a minivan, a motorcyle, a limousine, a hatchback, a truck, and a tractor. The motorcyle is older than the tractor. The hatchback is older than the limousine. The hatchback is newer than the truck. The truck is newer than the tractor. The minivan is the second-newest. The sedan is the third-newest.",
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
| Microsoft Decision-1 | `C` — The motorcyle is the oldest | `C` — The motorcyle is the oldest | Same answer |
| Clef | `D` — The limousine is the oldest | `G` — The tractor is the oldest | Different answer |
| Luna Decisions | `C` — The motorcyle is the oldest | `G` — The tractor is the oldest | Different answer |
| Clef Flash | `C` — The motorcyle is the oldest | `G` — The tractor is the oldest | Different answer |
| Strands Decider | `C` — The motorcyle is the oldest | `C` — The motorcyle is the oldest | Same answer |
| GLiNER2.5 Decide | `G` — The tractor is the oldest | `G` — The tractor is the oldest | Same answer |
| Laya | `C` — The motorcyle is the oldest | `C` — The motorcyle is the oldest | Same answer |
| CalDec v1 | `B` — The minivan is the oldest | `B` — The minivan is the oldest | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `bbh/508fcff215b3cb05c2b6/irrelevant_details/high/clean-ordinal_scene_details_full_0028`

**Input fingerprint:** `74e4dc174571c9ca4a2a065bece5d28b72e475d0c2e2318debc490e987f71d72`

| Change | Recorded version |
| --- | --- |
| Irrelevant details | Add a larger amount of irrelevant detail |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/relations/bbh-508fcff215b3cb05c2b6.md).
