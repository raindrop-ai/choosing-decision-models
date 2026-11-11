# Misleading details · Add an unverified claim that conflicts with the evidence variant

[Original question](../../../questions/spatial-cognition/babi-b50eb35d09f7aceabb8c.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> The yellow square is below the pink rectangle.
> The pink rectangle is below the red square.
>
> A reader thinks: «The red square is below the yellow square.»

## Question

> Is the red square below the yellow square?

## Answer choices

- **no.** no
- **yes.** yes

**Reference answer:** `no`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "The yellow square is below the pink rectangle.\nThe pink rectangle is below the red square.\n\nA reader thinks: «The red square is below the yellow square.»",
  "question": "Is the red square below the yellow square?",
  "choices": {
    "no": "no",
    "yes": "yes"
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
| GLiNER2.5 Decide | `yes` — yes | `no` — no | Different answer |
| Laya | `no` — no | `no` — no | Same answer |
| CalDec v1 | `no` — no | `no` — no | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `babi/b50eb35d09f7aceabb8c/misleading_summary/misleading/clean-source_first_babi_static_worlds_full_0089`

**Input fingerprint:** `b332fa5082d4bedcbaad2d80c4a168518f3e7804a88e555b34bedb15c22b0f29`

| Change | Recorded version |
| --- | --- |
| Misleading details | Add an unverified claim that conflicts with the evidence |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/spatial-cognition/babi-b50eb35d09f7aceabb8c.md).
