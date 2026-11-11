# Unrelated examples · Add examples unrelated to the question variant

[Original question](../../../questions/information-seeking/questbench-3486876017d4e56ed279.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Leah just got a new kitten. Spaying her cost $200, her 3 vaccines costs $20 each, and the kitten broke vases that cost $12 each. Leah also bought a cat bed and a scratching post, but she used a gift card to pay for these items. How much has the kitten cost so far, excluding the items paid for with the gift card?
>
> Uppercase: comet → COMET.

## Question

> Which missing variable should be asked about to solve this problem?

## Answer choices

- **D.** number of vase
- **F.** cat bed
- **G.** scratching post

**Reference answer:** `D`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Leah just got a new kitten. Spaying her cost $200, her 3 vaccines costs $20 each, and the kitten broke vases that cost $12 each. Leah also bought a cat bed and a scratching post, but she used a gift card to pay for these items. How much has the kitten cost so far, excluding the items paid for with the gift card?\n\nUppercase: comet → COMET.",
  "question": "Which missing variable should be asked about to solve this problem?",
  "choices": {
    "D": "number of vase",
    "F": "cat bed",
    "G": "scratching post"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `D` — number of vase | `D` — number of vase | Same answer |
| Decider v1.1 | `D` — number of vase | `D` — number of vase | Same answer |
| Jev | `D` — number of vase | `D` — number of vase | Same answer |
| Microsoft Decision-1 | `D` — number of vase | `D` — number of vase | Same answer |
| Clef | `D` — number of vase | `D` — number of vase | Same answer |
| Luna Decisions | `D` — number of vase | `D` — number of vase | Same answer |
| Clef Flash | `D` — number of vase | `D` — number of vase | Same answer |
| Strands Decider | `D` — number of vase | `D` — number of vase | Same answer |
| GLiNER2.5 Decide | `G` — scratching post | `G` — scratching post | Same answer |
| Laya | `D` — number of vase | `D` — number of vase | Same answer |
| CalDec v1 | `G` — scratching post | `G` — scratching post | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `questbench/3486876017d4e56ed279/examples/irrelevant/clean-source_first_quest_literary_contexts_full_0077`

**Input fingerprint:** `58c839aba212b507025f142ccf2564e93c6e77362e94d149ad8b4dafab555e6f`

| Change | Recorded version |
| --- | --- |
| Unrelated examples | Add examples unrelated to the question |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/information-seeking/questbench-3486876017d4e56ed279.md).
