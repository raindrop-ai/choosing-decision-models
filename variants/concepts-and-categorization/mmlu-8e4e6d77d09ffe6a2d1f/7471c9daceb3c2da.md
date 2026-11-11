# Extra events · Add 12 unrelated events variant

[Original question](../../../questions/concepts-and-categorization/mmlu-8e4e6d77d09ffe6a2d1f.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Nolan is the editor of a poetry catalog. Its entries are Virel, Zorven, Kesil, Nereth, Pavrel, and Sovrin.
> Nolan classifies Virel as a dialogue. Nolan classifies Zorven as a monologue. Nolan classifies Kesil as an elegy. Nolan classifies Nereth as a satire. Nolan classifies Pavrel as a fable. Nolan classifies Sovrin as a ballad. Nolan reclassifies Virel as a monologue. Nolan reclassifies Zorven as a dialogue. Nolan reclassifies Kesil as a ballad. Nolan reclassifies Nereth as a fable. Nolan reclassifies Pavrel as a satire. Nolan reclassifies Sovrin as an elegy.

## Question

> All of the following are modes of asexual reproduction EXCEPT

## Answer choices

- **A.** sporulation
- **B.** fission
- **C.** budding
- **D.** meiosis

**Reference answer:** `D`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Nolan is the editor of a poetry catalog. Its entries are Virel, Zorven, Kesil, Nereth, Pavrel, and Sovrin.\nNolan classifies Virel as a dialogue. Nolan classifies Zorven as a monologue. Nolan classifies Kesil as an elegy. Nolan classifies Nereth as a satire. Nolan classifies Pavrel as a fable. Nolan classifies Sovrin as a ballad. Nolan reclassifies Virel as a monologue. Nolan reclassifies Zorven as a dialogue. Nolan reclassifies Kesil as a ballad. Nolan reclassifies Nereth as a fable. Nolan reclassifies Pavrel as a satire. Nolan reclassifies Sovrin as an elegy.",
  "question": "All of the following are modes of asexual reproduction EXCEPT",
  "choices": {
    "A": "sporulation",
    "B": "fission",
    "C": "budding",
    "D": "meiosis"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `D` — meiosis | `D` — meiosis | Same answer |
| Decider v1.1 | `D` — meiosis | `D` — meiosis | Same answer |
| Jev | `D` — meiosis | `D` — meiosis | Same answer |
| Microsoft Decision-1 | `D` — meiosis | `D` — meiosis | Same answer |
| Clef | `D` — meiosis | `D` — meiosis | Same answer |
| Luna Decisions | `D` — meiosis | `D` — meiosis | Same answer |
| Clef Flash | `D` — meiosis | `D` — meiosis | Same answer |
| Strands Decider | `D` — meiosis | `C` — budding | Different answer |
| GLiNER2.5 Decide | `A` — sporulation | `A` — sporulation | Same answer |
| Laya | `B` — fission | `B` — fission | Same answer |
| CalDec v1 | `D` — meiosis | `B` — fission | Different answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `mmlu/8e4e6d77d09ffe6a2d1f/event_count/12/clean-source_first_mmlu_other_short_contexts_full_0100`

**Input fingerprint:** `f6fcad749738ed06a93a3946b22c990a2943318ddc031c1fa382ad8b781141df`

| Change | Recorded version |
| --- | --- |
| Extra events | Add 12 unrelated events |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/concepts-and-categorization/mmlu-8e4e6d77d09ffe6a2d1f.md).
