# Similar distractors · Add fewer similar but irrelevant items variant

[Original question](../../../questions/spatial-cognition/babi-f23876e41cd917cc4bba.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> The red sphere is below the triangle.
> The blue square is below the red sphere.
> The orange hexagon is below the violet star.

## Question

> Is the triangle above the blue square?

## Answer choices

- **yes.** yes
- **no.** no

**Reference answer:** `yes`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "The red sphere is below the triangle.\nThe blue square is below the red sphere.\nThe orange hexagon is below the violet star.",
  "question": "Is the triangle above the blue square?",
  "choices": {
    "yes": "yes",
    "no": "no"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `yes` — yes | `yes` — yes | Same answer |
| Decider v1.1 | `yes` — yes | `yes` — yes | Same answer |
| Jev | `yes` — yes | `yes` — yes | Same answer |
| Microsoft Decision-1 | `yes` — yes | `yes` — yes | Same answer |
| Clef | `yes` — yes | `yes` — yes | Same answer |
| Luna Decisions | `yes` — yes | `yes` — yes | Same answer |
| Clef Flash | `yes` — yes | `yes` — yes | Same answer |
| Strands Decider | `yes` — yes | `yes` — yes | Same answer |
| GLiNER2.5 Decide | `yes` — yes | `yes` — yes | Same answer |
| Laya | `no` — no | `yes` — yes | Different answer |
| CalDec v1 | `no` — no | `no` — no | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `babi/f23876e41cd917cc4bba/similar_distractors/low/clean-similar_predicates_0006`

**Input fingerprint:** `3767c52bb99618dab4336be6c00b26fd2093a1bfaec60bfeead0c22f8d254f3f`

| Change | Recorded version |
| --- | --- |
| Similar distractors | Add fewer similar but irrelevant items |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/spatial-cognition/babi-f23876e41cd917cc4bba.md).
