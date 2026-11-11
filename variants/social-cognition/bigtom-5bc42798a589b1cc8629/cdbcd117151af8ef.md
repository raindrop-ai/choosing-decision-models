# Similar distractors · Add fewer similar but irrelevant items variant

[Original question](../../../questions/social-cognition/bigtom-5bc42798a589b1cc8629.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> «At another observatory, an assistant checks a correctly aimed telescope.»
>
> Naledi is a young astronomer in a remote observatory in South Africa. Naledi wants to observe a distant supernova to gather data for her research. The telescope is pointed at the coordinates of the supernova, ready for observation. Naledi believes that the telescope is aimed at the correct location. A minor earthquake occurs, causing the telescope to shift its position slightly. Naledi notices the earthquake and its effect on the telescope.

## Question

> Does Naledi believe the telescope is aimed at the correct location or has shifted due to the earthquake?

## Answer choices

- **A.** Naledi believes the telescope has shifted due to the earthquake.
- **B.** Naledi believes the telescope is aimed at the correct location.

**Reference answer:** `A`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "«At another observatory, an assistant checks a correctly aimed telescope.»\n\nNaledi is a young astronomer in a remote observatory in South Africa. Naledi wants to observe a distant supernova to gather data for her research. The telescope is pointed at the coordinates of the supernova, ready for observation. Naledi believes that the telescope is aimed at the correct location. A minor earthquake occurs, causing the telescope to shift its position slightly. Naledi notices the earthquake and its effect on the telescope.",
  "question": "Does Naledi believe the telescope is aimed at the correct location or has shifted due to the earthquake?",
  "choices": {
    "A": "Naledi believes the telescope has shifted due to the earthquake.",
    "B": "Naledi believes the telescope is aimed at the correct location."
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `A` — Naledi believes the telescope has shifted due to the earthquake. | `A` — Naledi believes the telescope has shifted due to the earthquake. | Same answer |
| Decider v1.1 | `A` — Naledi believes the telescope has shifted due to the earthquake. | `A` — Naledi believes the telescope has shifted due to the earthquake. | Same answer |
| Jev | `A` — Naledi believes the telescope has shifted due to the earthquake. | `A` — Naledi believes the telescope has shifted due to the earthquake. | Same answer |
| Microsoft Decision-1 | `B` — Naledi believes the telescope is aimed at the correct location. | `A` — Naledi believes the telescope has shifted due to the earthquake. | Different answer |
| Clef | `A` — Naledi believes the telescope has shifted due to the earthquake. | `A` — Naledi believes the telescope has shifted due to the earthquake. | Same answer |
| Luna Decisions | `A` — Naledi believes the telescope has shifted due to the earthquake. | `A` — Naledi believes the telescope has shifted due to the earthquake. | Same answer |
| Clef Flash | `A` — Naledi believes the telescope has shifted due to the earthquake. | `A` — Naledi believes the telescope has shifted due to the earthquake. | Same answer |
| Strands Decider | `A` — Naledi believes the telescope has shifted due to the earthquake. | `A` — Naledi believes the telescope has shifted due to the earthquake. | Same answer |
| GLiNER2.5 Decide | `A` — Naledi believes the telescope has shifted due to the earthquake. | `A` — Naledi believes the telescope has shifted due to the earthquake. | Same answer |
| Laya | `A` — Naledi believes the telescope has shifted due to the earthquake. | `A` — Naledi believes the telescope has shifted due to the earthquake. | Same answer |
| CalDec v1 | `A` — Naledi believes the telescope has shifted due to the earthquake. | `A` — Naledi believes the telescope has shifted due to the earthquake. | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `bigtom/5bc42798a589b1cc8629/similar_distractors/low/clean-source_first_bigtom_near_scenes_full_0210`

**Input fingerprint:** `a73cef898296e452f98b28e7c069355f45c69578e4246a639bc11c176d9330fb`

| Change | Recorded version |
| --- | --- |
| Similar distractors | Add fewer similar but irrelevant items |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/social-cognition/bigtom-5bc42798a589b1cc8629.md).
