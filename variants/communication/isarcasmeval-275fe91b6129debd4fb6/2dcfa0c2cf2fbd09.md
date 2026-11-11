# Repetition · Present the same evidence twice variant

[Original question](../../../questions/communication/isarcasmeval-275fe91b6129debd4fb6.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** question instructions.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> James Harden is allowed to travel every time he drives apparently

## Question

> Is this message intended to be sarcastic?
>
> «James Harden is allowed to travel every time he drives apparently»

## Answer choices

- **no.** Not sarcastic
- **yes.** Sarcastic

**Reference answer:** `yes`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "James Harden is allowed to travel every time he drives apparently",
  "question": "Is this message intended to be sarcastic?\n\n«James Harden is allowed to travel every time he drives apparently»",
  "choices": {
    "no": "Not sarcastic",
    "yes": "Sarcastic"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `yes` — Sarcastic | `yes` — Sarcastic | Same answer |
| Decider v1.1 | `yes` — Sarcastic | `yes` — Sarcastic | Same answer |
| Jev | `yes` — Sarcastic | `yes` — Sarcastic | Same answer |
| Microsoft Decision-1 | `yes` — Sarcastic | `yes` — Sarcastic | Same answer |
| Clef | `no` — Not sarcastic | `no` — Not sarcastic | Same answer |
| Luna Decisions | `yes` — Sarcastic | `yes` — Sarcastic | Same answer |
| Clef Flash | `no` — Not sarcastic | `no` — Not sarcastic | Same answer |
| Strands Decider | `no` — Not sarcastic | `no` — Not sarcastic | Same answer |
| GLiNER2.5 Decide | `yes` — Sarcastic | `no` — Not sarcastic | Different answer |
| Laya | `no` — Not sarcastic | `no` — Not sarcastic | Same answer |
| CalDec v1 | `no` — Not sarcastic | `no` — Not sarcastic | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `isarcasmeval/275fe91b6129debd4fb6/evidence_repetition/2/clean-source_first_owned_completion_contexts_full_0233`

**Input fingerprint:** `00d6822e1d7871c9c6641ab5a4c725a3c1958316d2e999114f53cfd1d8041c58`

| Change | Recorded version |
| --- | --- |
| Repetition | Present the same evidence twice |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/communication/isarcasmeval-275fe91b6129debd4fb6.md).
