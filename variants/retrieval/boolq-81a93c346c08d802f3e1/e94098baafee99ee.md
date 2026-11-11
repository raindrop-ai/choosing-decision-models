# Option order · Move the first answer choice to the end variant

[Original question](../../../questions/retrieval/boolq-81a93c346c08d802f3e1.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** answer choices or their order.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> The Mercedes-Benz Stadium is a multi-purpose retractable roof stadium located in Atlanta, Georgia. The home of the Atlanta Falcons of the National Football League (NFL) and Atlanta United FC of Major League Soccer (MLS), it replaced the adjacent Georgia Dome, the Falcons' home stadium for a quarter century, from 1992 through 2016. This stadium holds the record of the world's largest halo board and is one of few stadiums with retractable roofs.

## Question

> did the atlanta falcons get a new stadium

## Answer choices

- **no.** No
- **yes.** Yes

**Reference answer:** `yes`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "The Mercedes-Benz Stadium is a multi-purpose retractable roof stadium located in Atlanta, Georgia. The home of the Atlanta Falcons of the National Football League (NFL) and Atlanta United FC of Major League Soccer (MLS), it replaced the adjacent Georgia Dome, the Falcons' home stadium for a quarter century, from 1992 through 2016. This stadium holds the record of the world's largest halo board and is one of few stadiums with retractable roofs.",
  "question": "did the atlanta falcons get a new stadium",
  "choices": {
    "no": "No",
    "yes": "Yes"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `yes` — Yes | `yes` — Yes | Same answer |
| Decider v1.1 | `yes` — Yes | `yes` — Yes | Same answer |
| Jev | `yes` — Yes | `yes` — Yes | Same answer |
| Microsoft Decision-1 | `yes` — Yes | `yes` — Yes | Same answer |
| Clef | `yes` — Yes | `yes` — Yes | Same answer |
| Luna Decisions | `yes` — Yes | `yes` — Yes | Same answer |
| Clef Flash | `yes` — Yes | `yes` — Yes | Same answer |
| Strands Decider | `yes` — Yes | `yes` — Yes | Same answer |
| GLiNER2.5 Decide | `yes` — Yes | `yes` — Yes | Same answer |
| Laya | `yes` — Yes | `yes` — Yes | Same answer |
| CalDec v1 | `yes` — Yes | `yes` — Yes | Same answer |

Clef and Clef Flash sort answer choices in their published input-processing code. Their choice-order results describe that preprocessing.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `boolq/81a93c346c08d802f3e1/option_order/rotate_1`

**Input fingerprint:** `7c163db39416b6993a1ca458ee742bf47c8a80f4212445c203cd4c22606ac774`

| Change | Recorded version |
| --- | --- |
| Option order | Move the first answer choice to the end |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/retrieval/boolq-81a93c346c08d802f3e1.md).
