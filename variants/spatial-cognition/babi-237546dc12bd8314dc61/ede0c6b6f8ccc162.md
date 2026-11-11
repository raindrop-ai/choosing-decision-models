# Repetition · Present the same evidence three times variant

[Original question](../../../questions/spatial-cognition/babi-237546dc12bd8314dc61.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> The triangle is above the yellow square.
> The triangle is below the red sphere.
> The triangle is above the yellow square.
> The triangle is below the red sphere.
> The triangle is above the yellow square.
> The triangle is below the red sphere.

## Question

> Is the yellow square below the red sphere?

## Answer choices

- **yes.** yes
- **no.** no

**Reference answer:** `yes`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "The triangle is above the yellow square.\nThe triangle is below the red sphere.\nThe triangle is above the yellow square.\nThe triangle is below the red sphere.\nThe triangle is above the yellow square.\nThe triangle is below the red sphere.",
  "question": "Is the yellow square below the red sphere?",
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
| CalDec v1 | `yes` — yes | `yes` — yes | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `babi/237546dc12bd8314dc61/evidence_repetition/3/clean-source_first_babi_static_worlds_full_0089`

**Input fingerprint:** `a334f57d149dde6e68c4851f2ce569fd6ef103ed8e2f4e70e2b85e9b80aa11e7`

| Change | Recorded version |
| --- | --- |
| Repetition | Present the same evidence three times |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/spatial-cognition/babi-237546dc12bd8314dc61.md).
