# Social cognition · question 52

[Back to Social cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `socialiqa/97bd80503bfec4f09f9f`  
**Source:** [Social IQa](https://storage.googleapis.com/ai2-mosaic/public/socialiqa/socialiqa-train-dev.zip)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/social-cognition/socialiqa-97bd80503bfec4f09f9f/README.md)

## Context

> Quinn stuck her head in the sand at the beach to make her brother laugh.

## Question

> What will Quinn want to do next?

## Answer choices

- **A:** start crying
- **B:** hit her brother
- **C:** brush off the sand

**Reference answer:** brush off the sand (`C`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Quinn stuck her head in the sand at the beach to make her brother laugh.",
  "question": "What will Quinn want to do next?",
  "choices": {
    "A": "start crying",
    "B": "hit her brother",
    "C": "brush off the sand"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | brush off the sand | Correct |
| Opus 5.5 | brush off the sand | Correct |
| GLiDE v1.2 | brush off the sand | Correct |
| Decider v1.1 | brush off the sand | Correct |
| Jev | brush off the sand | Correct |
| Microsoft Decision-1 | brush off the sand | Correct |
| Clef | brush off the sand | Correct |
| Luna Decisions | brush off the sand | Correct |
| Clef Flash | brush off the sand | Correct |
| Strands Decider | brush off the sand | Correct |
| GLiNER2.5 Decide | hit her brother | Incorrect |
| Laya | hit her brother | Incorrect |
| CalDec v1 | brush off the sand | Correct |

## Source and sharing

Attribution: Maarten Sap, Hannah Rashkin, Derek Chen, Ronan LeBras, Yejin Choi.  
Terms: **[CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)**. [Source sharing decision](../../docs/data-sharing.md).  
The capability assignment and choice-format normalization are part of this experiment. Source data retain their own terms.

<details>
<summary>Exact source locator and input fingerprint</summary>

```json
{
  "source_locator": {
    "path": "extracted/socialiqa.zip/socialiqa-train-dev/train.jsonl",
    "record": "20667",
    "kind": "source_file_record"
  },
  "source_revision": null,
  "input_hash": "f7d08311eb11942f5b0d070143bf183de402cd27555056740546083a68d2e8f0"
}
```

</details>
