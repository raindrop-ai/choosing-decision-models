# Irrelevant details · Add a larger amount of irrelevant detail variant

[Original question](../../../questions/social-cognition/socialiqa-c3e978f0dc5e7c441e01.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Sydney found Jesse a way to the store after they had gotten lost.
>
> The musical suite Merovan includes a refrain. Merovan uses a tonic cadence. Merovan includes rests. Merovan has sustained harmonies. Merovan has detached melodic notes. Merovan varies its accompaniment.

## Question

> What will Jesse want to do next?

## Answer choices

- **A.** get lost again
- **B.** buy a coffee at the store
- **C.** go to the store

**Reference answer:** `C`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Sydney found Jesse a way to the store after they had gotten lost.\n\nThe musical suite Merovan includes a refrain. Merovan uses a tonic cadence. Merovan includes rests. Merovan has sustained harmonies. Merovan has detached melodic notes. Merovan varies its accompaniment.",
  "question": "What will Jesse want to do next?",
  "choices": {
    "A": "get lost again",
    "B": "buy a coffee at the store",
    "C": "go to the store"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `C` — go to the store | `C` — go to the store | Same answer |
| Decider v1.1 | `C` — go to the store | `C` — go to the store | Same answer |
| Jev | `C` — go to the store | `C` — go to the store | Same answer |
| Microsoft Decision-1 | `C` — go to the store | `C` — go to the store | Same answer |
| Clef | `C` — go to the store | `C` — go to the store | Same answer |
| Luna Decisions | `C` — go to the store | `C` — go to the store | Same answer |
| Clef Flash | `C` — go to the store | `B` — buy a coffee at the store | Different answer |
| Strands Decider | `C` — go to the store | `C` — go to the store | Same answer |
| GLiNER2.5 Decide | `C` — go to the store | `C` — go to the store | Same answer |
| Laya | `A` — get lost again | `A` — get lost again | Same answer |
| CalDec v1 | `A` — get lost again | `A` — get lost again | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `socialiqa/c3e978f0dc5e7c441e01/irrelevant_details/high/clean-source_first_socialiqa_music_contexts_full_0158`

**Input fingerprint:** `368dcce94d6e1c5296a28dd1cbb606bd95cdd05db17d643f7837666a90b8cfd3`

| Change | Recorded version |
| --- | --- |
| Irrelevant details | Add a larger amount of irrelevant detail |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/social-cognition/socialiqa-c3e978f0dc5e7c441e01.md).
