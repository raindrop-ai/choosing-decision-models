# Unrelated examples · No worked example (absence-control recipe) variant

[Original question](../../../questions/spatial-cognition/babi-b44ce789d424787dbc9a.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> The red square is below the yellow square.
> The pink rectangle is above the yellow square.
>
> The poem has a refrain and an anonymous narrator.

## Question

> Is the pink rectangle below the red square?

## Answer choices

- **yes.** yes
- **no.** no

**Reference answer:** `no`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "The red square is below the yellow square.\nThe pink rectangle is above the yellow square.\n\nThe poem has a refrain and an anonymous narrator.",
  "question": "Is the pink rectangle below the red square?",
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
| GLiDE v1.2 | `no` — no | `no` — no | Same answer |
| Decider v1.1 | `no` — no | `no` — no | Same answer |
| Jev | `no` — no | `no` — no | Same answer |
| Microsoft Decision-1 | `no` — no | `no` — no | Same answer |
| Clef | `no` — no | `no` — no | Same answer |
| Luna Decisions | `no` — no | `no` — no | Same answer |
| Clef Flash | `no` — no | `no` — no | Same answer |
| Strands Decider | `no` — no | `no` — no | Same answer |
| GLiNER2.5 Decide | `yes` — yes | `yes` — yes | Same answer |
| Laya | `no` — no | `no` — no | Same answer |
| CalDec v1 | `no` — no | `yes` — yes | Different answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `babi/b44ce789d424787dbc9a/examples/absent/clean-source_first_babi_static_worlds_full_0089`

**Input fingerprint:** `2e63a2ce65bd24a1da9b91c84ba40872e2a7b0cfcd7d4865f29655c5887aa007`

| Change | Recorded version |
| --- | --- |
| Unrelated examples | No worked example (absence-control recipe) |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/spatial-cognition/babi-b44ce789d424787dbc9a.md).
