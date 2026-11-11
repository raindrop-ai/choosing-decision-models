# Similar distractors · Add fewer similar but irrelevant items variant

[Original question](../../../questions/concepts-and-categorization/mnli-5310cdb49b087a272917.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** question instructions.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> On the other hand, one would hate to lose the information that might be contained in past years' selling patterns.

## Question

> Does the premise entail, contradict, or leave undetermined this statement? It would be unfortunate to lose information that shows past years' selling patterns.
>
> «The object velmin is a cedar box. Does this establish that the object velmin is wooden?»

## Answer choices

- **0.** Entailment
- **1.** Neither entailed nor contradicted
- **2.** Contradiction

**Reference answer:** `0`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "On the other hand, one would hate to lose the information that might be contained in past years' selling patterns.",
  "question": "Does the premise entail, contradict, or leave undetermined this statement? It would be unfortunate to lose information that shows past years' selling patterns.\n\n«The object velmin is a cedar box. Does this establish that the object velmin is wooden?»",
  "choices": {
    "0": "Entailment",
    "1": "Neither entailed nor contradicted",
    "2": "Contradiction"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `0` — Entailment | `0` — Entailment | Same answer |
| Decider v1.1 | `0` — Entailment | `0` — Entailment | Same answer |
| Jev | `0` — Entailment | `0` — Entailment | Same answer |
| Microsoft Decision-1 | `0` — Entailment | `1` — Neither entailed nor contradicted | Different answer |
| Clef | `0` — Entailment | `0` — Entailment | Same answer |
| Luna Decisions | `0` — Entailment | `1` — Neither entailed nor contradicted | Different answer |
| Clef Flash | `0` — Entailment | `0` — Entailment | Same answer |
| Strands Decider | `0` — Entailment | `1` — Neither entailed nor contradicted | Different answer |
| GLiNER2.5 Decide | `1` — Neither entailed nor contradicted | `1` — Neither entailed nor contradicted | Same answer |
| Laya | `0` — Entailment | `0` — Entailment | Same answer |
| CalDec v1 | `0` — Entailment | `0` — Entailment | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `mnli/5310cdb49b087a272917/similar_distractors/low/clean-source_first_wildguard_mnli_near_full_0273`

**Input fingerprint:** `bb897cf86e905174c82fdfd9508ce74ead87c40b99675cb05258ff0da0ee2272`

| Change | Recorded version |
| --- | --- |
| Similar distractors | Add fewer similar but irrelevant items |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/concepts-and-categorization/mnli-5310cdb49b087a272917.md).
