# Unrelated examples · No worked example (prose-control recipe) variant

[Original question](../../../questions/social-cognition/bigtom-cb702e30e9a16eeca9a9.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Amara, a skilled Nigerian weaver, is preparing to create a traditional textile for an upcoming cultural exhibition. Amara wants to use a unique combination of colorful threads that represents her heritage. Amara carefully chooses a set of vibrant, high-quality threads for her project. She believes the threads she has chosen are strong and perfect for her textile. A curious toddler in her home finds the threads and tangles them, making them difficult to use in the weaving process. Amara notices the tangled threads.
>
> Merovan has a melodic refrain.

## Question

> Does Amara believe the threads are strong and perfect for her textile or tangled and difficult to use?

## Answer choices

- **A.** Amara believes the threads are tangled and difficult to use.
- **B.** Amara believes the threads are strong and perfect for her textile.

**Reference answer:** `A`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Amara, a skilled Nigerian weaver, is preparing to create a traditional textile for an upcoming cultural exhibition. Amara wants to use a unique combination of colorful threads that represents her heritage. Amara carefully chooses a set of vibrant, high-quality threads for her project. She believes the threads she has chosen are strong and perfect for her textile. A curious toddler in her home finds the threads and tangles them, making them difficult to use in the weaving process. Amara notices the tangled threads.\n\nMerovan has a melodic refrain.",
  "question": "Does Amara believe the threads are strong and perfect for her textile or tangled and difficult to use?",
  "choices": {
    "A": "Amara believes the threads are tangled and difficult to use.",
    "B": "Amara believes the threads are strong and perfect for her textile."
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `A` — Amara believes the threads are tangled and difficult to use. | `B` — Amara believes the threads are strong and perfect for her textile. | Different answer |
| Decider v1.1 | `A` — Amara believes the threads are tangled and difficult to use. | `B` — Amara believes the threads are strong and perfect for her textile. | Different answer |
| Jev | `B` — Amara believes the threads are strong and perfect for her textile. | `B` — Amara believes the threads are strong and perfect for her textile. | Same answer |
| Microsoft Decision-1 | `B` — Amara believes the threads are strong and perfect for her textile. | `B` — Amara believes the threads are strong and perfect for her textile. | Same answer |
| Clef | `B` — Amara believes the threads are strong and perfect for her textile. | `B` — Amara believes the threads are strong and perfect for her textile. | Same answer |
| Luna Decisions | `B` — Amara believes the threads are strong and perfect for her textile. | `B` — Amara believes the threads are strong and perfect for her textile. | Same answer |
| Clef Flash | `B` — Amara believes the threads are strong and perfect for her textile. | `B` — Amara believes the threads are strong and perfect for her textile. | Same answer |
| Strands Decider | `B` — Amara believes the threads are strong and perfect for her textile. | `B` — Amara believes the threads are strong and perfect for her textile. | Same answer |
| GLiNER2.5 Decide | `B` — Amara believes the threads are strong and perfect for her textile. | `B` — Amara believes the threads are strong and perfect for her textile. | Same answer |
| Laya | `A` — Amara believes the threads are tangled and difficult to use. | `A` — Amara believes the threads are tangled and difficult to use. | Same answer |
| CalDec v1 | `A` — Amara believes the threads are tangled and difficult to use. | `A` — Amara believes the threads are tangled and difficult to use. | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `bigtom/cb702e30e9a16eeca9a9/examples/prose_control/clean-source_first_belief_toxicity_contexts_full_0150`

**Input fingerprint:** `b16a515d7ebb24572a45aebb917148e150c30736f70b77dc490729d28414155a`

| Change | Recorded version |
| --- | --- |
| Unrelated examples | No worked example (prose-control recipe) |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/social-cognition/bigtom-cb702e30e9a16eeca9a9.md).
