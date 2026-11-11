# Extra events · Add 2 unrelated events variant

[Original question](../../../questions/concepts-and-categorization/mmlu-8ccc30df4a8c7233ef17.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Nolan is the editor of a poetry catalog. Its entries are Virel, Zorven, Kesil, Nereth, Pavrel, and Sovrin.
> Nolan classifies Virel as a dialogue. Nolan classifies Zorven as a monologue.

## Question

> The idea that you identify with, and give allegiance, to a nation-state is

## Answer choices

- **A.** regionalism.
- **B.** diffusion.
- **C.** iconography.
- **D.** nationalism.

**Reference answer:** `D`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Nolan is the editor of a poetry catalog. Its entries are Virel, Zorven, Kesil, Nereth, Pavrel, and Sovrin.\nNolan classifies Virel as a dialogue. Nolan classifies Zorven as a monologue.",
  "question": "The idea that you identify with, and give allegiance, to a nation-state is",
  "choices": {
    "A": "regionalism.",
    "B": "diffusion.",
    "C": "iconography.",
    "D": "nationalism."
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `D` — nationalism. | `D` — nationalism. | Same answer |
| Decider v1.1 | `D` — nationalism. | `D` — nationalism. | Same answer |
| Jev | `D` — nationalism. | `D` — nationalism. | Same answer |
| Microsoft Decision-1 | `D` — nationalism. | `D` — nationalism. | Same answer |
| Clef | `D` — nationalism. | `D` — nationalism. | Same answer |
| Luna Decisions | `D` — nationalism. | `D` — nationalism. | Same answer |
| Clef Flash | `D` — nationalism. | `D` — nationalism. | Same answer |
| Strands Decider | `D` — nationalism. | `D` — nationalism. | Same answer |
| GLiNER2.5 Decide | `D` — nationalism. | `B` — diffusion. | Different answer |
| Laya | `D` — nationalism. | `C` — iconography. | Different answer |
| CalDec v1 | `D` — nationalism. | `B` — diffusion. | Different answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `mmlu/8ccc30df4a8c7233ef17/event_count/2/clean-source_first_mmlu_other_short_contexts_full_0100`

**Input fingerprint:** `220a88c357ceb6a8244f594729ecfe4505446c74ed89075b9f27ed97750ba02f`

| Change | Recorded version |
| --- | --- |
| Extra events | Add 2 unrelated events |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/concepts-and-categorization/mmlu-8ccc30df4a8c7233ef17.md).
