# Extra events · Add 6 unrelated events variant

[Original question](../../../questions/retrieval/spartqa-b862b916bd8e951302e0.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Nolan is the editor of a poetry catalog. Its entries are Virel, Zorven, Kesil, Nereth, Pavrel, and Sovrin.
> Nolan classifies Virel as a dialogue. Nolan classifies Zorven as a monologue. Nolan classifies Kesil as an elegy. Nolan classifies Nereth as a satire. Nolan classifies Pavrel as a fable. Nolan classifies Sovrin as a ballad.
>
> There are three blocks. We call them A, B and C. Block C is to the right of A. Block A is above B. Block A has one small yellow triangle and one medium yellow triangle. The small yellow triangle is touching the right edge of this block. This block also has a medium black triangle. Below the medium yellow triangle and the medium black triangle there is the small yellow triangle. Block B contains one small yellow triangle. And block C has one small blue triangle and a big yellow square. The small blue triangle is to the left of, near to and above the big yellow square.

## Question

> Is the blue triangle , above the big yellow square?

## Answer choices

- **Yes.** Yes
- **No.** No
- **DK.** DK

**Reference answer:** `Yes`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Nolan is the editor of a poetry catalog. Its entries are Virel, Zorven, Kesil, Nereth, Pavrel, and Sovrin.\nNolan classifies Virel as a dialogue. Nolan classifies Zorven as a monologue. Nolan classifies Kesil as an elegy. Nolan classifies Nereth as a satire. Nolan classifies Pavrel as a fable. Nolan classifies Sovrin as a ballad.\n\nThere are three blocks. We call them A, B and C. Block C is to the right of A. Block A is above B. Block A has one small yellow triangle and one medium yellow triangle. The small yellow triangle is touching the right edge of this block. This block also has a medium black triangle. Below the medium yellow triangle and the medium black triangle there is the small yellow triangle. Block B contains one small yellow triangle. And block C has one small blue triangle and a big yellow square. The small blue triangle is to the left of, near to and above the big yellow square.",
  "question": "Is the blue triangle , above the big yellow square?",
  "choices": {
    "Yes": "Yes",
    "No": "No",
    "DK": "DK"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `Yes` — Yes | `Yes` — Yes | Same answer |
| Decider v1.1 | `Yes` — Yes | `Yes` — Yes | Same answer |
| Jev | `Yes` — Yes | `Yes` — Yes | Same answer |
| Microsoft Decision-1 | `Yes` — Yes | `Yes` — Yes | Same answer |
| Clef | `Yes` — Yes | `Yes` — Yes | Same answer |
| Luna Decisions | `Yes` — Yes | `Yes` — Yes | Same answer |
| Clef Flash | `Yes` — Yes | `Yes` — Yes | Same answer |
| Strands Decider | `Yes` — Yes | `Yes` — Yes | Same answer |
| GLiNER2.5 Decide | `No` — No | `Yes` — Yes | Different answer |
| Laya | `Yes` — Yes | `Yes` — Yes | Same answer |
| CalDec v1 | `Yes` — Yes | `Yes` — Yes | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `spartqa/b862b916bd8e951302e0/event_count/6/clean-source_first_spartqa_short_contexts_full_0136`

**Input fingerprint:** `0e9358f8ff63a19ff8d315a635a96fa66f043b58f4a793a4c27f18f044f80382`

| Change | Recorded version |
| --- | --- |
| Extra events | Add 6 unrelated events |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/retrieval/spartqa-b862b916bd8e951302e0.md).
