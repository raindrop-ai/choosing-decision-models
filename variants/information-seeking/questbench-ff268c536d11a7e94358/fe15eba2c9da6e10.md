# Option order · Move the first answer choice to the end variant

[Original question](../../../questions/information-seeking/questbench-ff268c536d11a7e94358.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** answer choices or their order.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Jay is making snowballs to prepare for a snowball fight with his sister. It takes his sister a while to build a snowman. He can build some amount of snowballs in an hour, but 2 melt every 15 minutes. How long will it take before he has 60 snowballs?

## Question

> Which missing variable should be asked about to solve this problem?

## Answer choices

- **H.** Number of hours taken to build snowman
- **A.** Number of snowballs build in an hour

**Reference answer:** `A`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Jay is making snowballs to prepare for a snowball fight with his sister. It takes his sister a while to build a snowman. He can build some amount of snowballs in an hour, but 2 melt every 15 minutes. How long will it take before he has 60 snowballs?",
  "question": "Which missing variable should be asked about to solve this problem?",
  "choices": {
    "H": "Number of hours taken to build snowman",
    "A": "Number of snowballs build in an hour"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `A` — Number of snowballs build in an hour | `A` — Number of snowballs build in an hour | Same answer |
| Decider v1.1 | `A` — Number of snowballs build in an hour | `A` — Number of snowballs build in an hour | Same answer |
| Jev | `A` — Number of snowballs build in an hour | `A` — Number of snowballs build in an hour | Same answer |
| Microsoft Decision-1 | `A` — Number of snowballs build in an hour | `A` — Number of snowballs build in an hour | Same answer |
| Clef | `A` — Number of snowballs build in an hour | `A` — Number of snowballs build in an hour | Same answer |
| Luna Decisions | `A` — Number of snowballs build in an hour | `A` — Number of snowballs build in an hour | Same answer |
| Clef Flash | `A` — Number of snowballs build in an hour | `A` — Number of snowballs build in an hour | Same answer |
| Strands Decider | `A` — Number of snowballs build in an hour | `A` — Number of snowballs build in an hour | Same answer |
| GLiNER2.5 Decide | `A` — Number of snowballs build in an hour | `A` — Number of snowballs build in an hour | Same answer |
| Laya | `A` — Number of snowballs build in an hour | `A` — Number of snowballs build in an hour | Same answer |
| CalDec v1 | `A` — Number of snowballs build in an hour | `A` — Number of snowballs build in an hour | Same answer |

Clef and Clef Flash sort answer choices in their published input-processing code. Their choice-order results describe that preprocessing.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `questbench/ff268c536d11a7e94358/option_order/rotate_1`

**Input fingerprint:** `75d83ac8c78f0048fef914277f93d544b43ff8110e6ef8fc09abe9ece1023ed2`

| Change | Recorded version |
| --- | --- |
| Option order | Move the first answer choice to the end |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/information-seeking/questbench-ff268c536d11a7e94358.md).
