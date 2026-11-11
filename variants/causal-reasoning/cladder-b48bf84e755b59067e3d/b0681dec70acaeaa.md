# Similar distractors · Add more similar but irrelevant items variant

[Original question](../../../questions/causal-reasoning/cladder-b48bf84e755b59067e3d.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> “Does changing Nerath affect Ovelin?”
>
> “Would Zelmin still change if Travon were held fixed?”
>
> “Can Ovelin influence Zelmin through Nerath?”
>
> Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Yupt has a direct effect on xyfo and zupj. Zupj has a direct effect on muvq. Xyfo has a direct effect on muvq.
> We know that yupt causes zupj and xyfo. zupj or xyfo causes muvq.

## Question

> Would an individual is muvq if yupt instead of not yupt?

## Answer choices

- **yes.** Yes
- **no.** No

**Reference answer:** `yes`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "“Does changing Nerath affect Ovelin?”\n\n“Would Zelmin still change if Travon were held fixed?”\n\n“Can Ovelin influence Zelmin through Nerath?”\n\nImagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Yupt has a direct effect on xyfo and zupj. Zupj has a direct effect on muvq. Xyfo has a direct effect on muvq.\nWe know that yupt causes zupj and xyfo. zupj or xyfo causes muvq.",
  "question": "Would an individual is muvq if yupt instead of not yupt?",
  "choices": {
    "yes": "Yes",
    "no": "No"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `yes` — Yes | `yes` — Yes | Same answer |
| Decider v1.1 | `yes` — Yes | `yes` — Yes | Same answer |
| Jev | `yes` — Yes | `yes` — Yes | Same answer |
| Microsoft Decision-1 | `yes` — Yes | `yes` — Yes | Same answer |
| Clef | `yes` — Yes | `yes` — Yes | Same answer |
| Luna Decisions | `yes` — Yes | `yes` — Yes | Same answer |
| Clef Flash | `yes` — Yes | `yes` — Yes | Same answer |
| Strands Decider | `yes` — Yes | `yes` — Yes | Same answer |
| GLiNER2.5 Decide | `yes` — Yes | `yes` — Yes | Same answer |
| Laya | `yes` — Yes | `no` — No | Different answer |
| CalDec v1 | `no` — No | `yes` — Yes | Different answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `cladder/b48bf84e755b59067e3d/similar_distractors/high/clean-source_first_causal_near_questions_full_0211`

**Input fingerprint:** `bb2613fb56318d43168e5a02d655652d6b8d4c87f7df67f21242aed5b128de5a`

| Change | Recorded version |
| --- | --- |
| Similar distractors | Add more similar but irrelevant items |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/causal-reasoning/cladder-b48bf84e755b59067e3d.md).
