# Misleading details · Add an unverified claim that conflicts with the evidence variant

[Original question](../../../questions/concepts-and-categorization/mnli-9f29122b74e1dbd1b45d.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** question instructions.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Rukeyser's Sphinx was not very affable, either.)

## Question

> A reader thinks the relation between «Rukeyser's Sphinx was not very affable, either.)» and «The Sphinx wasn't very friendly.» is Contradiction.
>
> Does the premise entail, contradict, or leave undetermined this statement? The Sphinx wasn't very friendly.

## Answer choices

- **0.** Entailment
- **1.** Neither entailed nor contradicted
- **2.** Contradiction

**Reference answer:** `0`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Rukeyser's Sphinx was not very affable, either.)",
  "question": "A reader thinks the relation between «Rukeyser's Sphinx was not very affable, either.)» and «The Sphinx wasn't very friendly.» is Contradiction.\n\nDoes the premise entail, contradict, or leave undetermined this statement? The Sphinx wasn't very friendly.",
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
| Microsoft Decision-1 | `0` — Entailment | `0` — Entailment | Same answer |
| Clef | `0` — Entailment | `0` — Entailment | Same answer |
| Luna Decisions | `0` — Entailment | `0` — Entailment | Same answer |
| Clef Flash | `0` — Entailment | `0` — Entailment | Same answer |
| Strands Decider | `0` — Entailment | `0` — Entailment | Same answer |
| GLiNER2.5 Decide | `1` — Neither entailed nor contradicted | `2` — Contradiction | Different answer |
| Laya | `0` — Entailment | `0` — Entailment | Same answer |
| CalDec v1 | `0` — Entailment | `0` — Entailment | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `mnli/9f29122b74e1dbd1b45d/misleading_summary/misleading/clean-source_first_residual_classification_contexts_full_0219`

**Input fingerprint:** `41831057e8e19a8c063fd6968349e2a195a29881147d1e55c6c2168d62fe4cb3`

| Change | Recorded version |
| --- | --- |
| Misleading details | Add an unverified claim that conflicts with the evidence |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/concepts-and-categorization/mnli-9f29122b74e1dbd1b45d.md).
