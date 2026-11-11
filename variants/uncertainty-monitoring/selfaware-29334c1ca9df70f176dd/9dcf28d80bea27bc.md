# Irrelevant details · Add a larger amount of irrelevant detail variant

[Original question](../../../questions/uncertainty-monitoring/selfaware-29334c1ca9df70f176dd.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> The notebook has a linen cover. The cover has an embossed title. The page edges are uneven. The binding is stitched. A ribbon marks a page. The back cover has a pocket.
>
> "Billy Blaze, an 8-year-old genius who constructed a spaceship in his backyard from old soup cans and other household objects called ""The Bean-with-Bacon Megarocket"" puts on his brother's football helmet and becomes what character in a video game series?"

## Question

> Does this question have a determinate answer?

## Answer choices

- **yes.** Answerable
- **no.** Unanswerable

**Reference answer:** `yes`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "The notebook has a linen cover. The cover has an embossed title. The page edges are uneven. The binding is stitched. A ribbon marks a page. The back cover has a pocket.\n\n\"Billy Blaze, an 8-year-old genius who constructed a spaceship in his backyard from old soup cans and other household objects called \"\"The Bean-with-Bacon Megarocket\"\" puts on his brother's football helmet and becomes what character in a video game series?\"",
  "question": "Does this question have a determinate answer?",
  "choices": {
    "yes": "Answerable",
    "no": "Unanswerable"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `no` — Unanswerable | `yes` — Answerable | Different answer |
| Decider v1.1 | `no` — Unanswerable | `no` — Unanswerable | Same answer |
| Jev | `yes` — Answerable | `yes` — Answerable | Same answer |
| Microsoft Decision-1 | `yes` — Answerable | `yes` — Answerable | Same answer |
| Clef | `yes` — Answerable | `yes` — Answerable | Same answer |
| Luna Decisions | `yes` — Answerable | `no` — Unanswerable | Different answer |
| Clef Flash | `yes` — Answerable | `yes` — Answerable | Same answer |
| Strands Decider | `no` — Unanswerable | `no` — Unanswerable | Same answer |
| GLiNER2.5 Decide | `yes` — Answerable | `yes` — Answerable | Same answer |
| Laya | `yes` — Answerable | `no` — Unanswerable | Different answer |
| CalDec v1 | `no` — Unanswerable | `no` — Unanswerable | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `selfaware/29334c1ca9df70f176dd/irrelevant_details/high/clean-source_first_selfaware_short_contexts_full_0125`

**Input fingerprint:** `f366ba56b836e5f23ffcbbf2c7f0f9db8b78f5d2eda20f26a6bcca2a37494a44`

| Change | Recorded version |
| --- | --- |
| Irrelevant details | Add a larger amount of irrelevant detail |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/uncertainty-monitoring/selfaware-29334c1ca9df70f176dd.md).
