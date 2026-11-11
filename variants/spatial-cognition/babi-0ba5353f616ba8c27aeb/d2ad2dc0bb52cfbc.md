# Unrelated examples · Add examples unrelated to the question variant

[Original question](../../../questions/spatial-cognition/babi-0ba5353f616ba8c27aeb.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> The yellow square is below the red square.
> The triangle is above the red square.
>
> Uppercase: comet → COMET.

## Question

> Is the yellow square below the triangle?

## Answer choices

- **no.** no
- **yes.** yes

**Reference answer:** `yes`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "The yellow square is below the red square.\nThe triangle is above the red square.\n\nUppercase: comet → COMET.",
  "question": "Is the yellow square below the triangle?",
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
| GLiDE v1.2 | `yes` — yes | `yes` — yes | Same answer |
| Decider v1.1 | `yes` — yes | `yes` — yes | Same answer |
| Jev | `yes` — yes | `yes` — yes | Same answer |
| Microsoft Decision-1 | `yes` — yes | `yes` — yes | Same answer |
| Clef | `yes` — yes | `yes` — yes | Same answer |
| Luna Decisions | `no` — no | `yes` — yes | Different answer |
| Clef Flash | `yes` — yes | `yes` — yes | Same answer |
| Strands Decider | `yes` — yes | `yes` — yes | Same answer |
| GLiNER2.5 Decide | `yes` — yes | `yes` — yes | Same answer |
| Laya | `yes` — yes | `no` — no | Different answer |
| CalDec v1 | `yes` — yes | `no` — no | Different answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `babi/0ba5353f616ba8c27aeb/examples/irrelevant/clean-source_first_babi_static_worlds_full_0089`

**Input fingerprint:** `6d3daeb9630fef9503ff38c847149ae4bf7e1e2918d74b8c5ad585ddf0171485`

| Change | Recorded version |
| --- | --- |
| Unrelated examples | Add examples unrelated to the question |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/spatial-cognition/babi-0ba5353f616ba8c27aeb.md).
