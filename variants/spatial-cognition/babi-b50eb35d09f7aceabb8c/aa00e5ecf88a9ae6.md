# Evidence order · Present the evidence in reverse order variant

[Original question](../../../questions/spatial-cognition/babi-b50eb35d09f7aceabb8c.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> The pink rectangle is below the red square.
> The yellow square is below the pink rectangle.

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
  "state": "The pink rectangle is below the red square.\nThe yellow square is below the pink rectangle.",
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
| Luna Decisions | `no` — no | `yes` — yes | Different answer |
| Clef Flash | `no` — no | `no` — no | Same answer |
| Strands Decider | `no` — no | `no` — no | Same answer |
| GLiNER2.5 Decide | `yes` — yes | `yes` — yes | Same answer |
| Laya | `no` — no | `no` — no | Same answer |
| CalDec v1 | `no` — no | `no` — no | Same answer |

**Ordering comparison:** literal requested source unit permutation. Only the exact matched comparison sets contribute to the reported ordering contrasts.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `babi/b50eb35d09f7aceabb8c/presentation_order/reverse_presentation/clean-source_first_babi_static_worlds_full_0089`

**Input fingerprint:** `673b1ac429e0cd442eb043eb3d7a26ebae73a7a54a97ece7f7699fe1f7f97283`

| Change | Recorded version |
| --- | --- |
| Evidence order | Present the evidence in reverse order |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/spatial-cognition/babi-b50eb35d09f7aceabb8c.md).
