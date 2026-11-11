# Paraphrasing · Change the sentence structure variant

[Original question](../../../questions/spatial-cognition/babi-237546dc12bd8314dc61.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** question instructions.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> The triangle is above the yellow square.
> The triangle is below the red sphere.

## Question

> Is the red sphere above the yellow square?

## Answer choices

- **yes.** yes
- **no.** no

**Reference answer:** `yes`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "The triangle is above the yellow square.\nThe triangle is below the red sphere.",
  "question": "Is the red sphere above the yellow square?",
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
| Laya | `no` — no | `no` — no | Same answer |
| CalDec v1 | `yes` — yes | `no` — no | Different answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `babi/237546dc12bd8314dc61/paraphrasing/structural`

**Input fingerprint:** `672b8e56f9a911b7c38f8265c3a0e96719d4c8a4eba712f9e55532bce2be2387`

| Change | Recorded version |
| --- | --- |
| Paraphrasing | Change the sentence structure |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/spatial-cognition/babi-237546dc12bd8314dc61.md).
