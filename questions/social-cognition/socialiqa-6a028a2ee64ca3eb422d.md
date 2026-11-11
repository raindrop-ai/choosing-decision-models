# Social cognition · question 60

[Back to Social cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `socialiqa/6a028a2ee64ca3eb422d`  
**Source:** [Social IQa](https://storage.googleapis.com/ai2-mosaic/public/socialiqa/socialiqa-train-dev.zip)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/social-cognition/socialiqa-6a028a2ee64ca3eb422d/README.md)

## Context

> Bailey wrote a paper for Addison's english class because he had a crush on her.

## Question

> Why did Bailey do this?

## Answer choices

- **A:** threaten Bailey and he felt pressured to do it
- **B:** wanted to mess up the english paper so he wrote it incorrectly
- **C:** impress Addison with his helpfulness and try to get on her good side

**Reference answer:** impress Addison with his helpfulness and try to get on her good side (`C`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Bailey wrote a paper for Addison's english class because he had a crush on her.",
  "question": "Why did Bailey do this?",
  "choices": {
    "A": "threaten Bailey and he felt pressured to do it",
    "B": "wanted to mess up the english paper so he wrote it incorrectly",
    "C": "impress Addison with his helpfulness and try to get on her good side"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | impress Addison with his helpfulness and try to get on her good side | Correct |
| Opus 5.5 | impress Addison with his helpfulness and try to get on her good side | Correct |
| GLiDE v1.2 | impress Addison with his helpfulness and try to get on her good side | Correct |
| Decider v1.1 | impress Addison with his helpfulness and try to get on her good side | Correct |
| Jev | impress Addison with his helpfulness and try to get on her good side | Correct |
| Microsoft Decision-1 | impress Addison with his helpfulness and try to get on her good side | Correct |
| Clef | impress Addison with his helpfulness and try to get on her good side | Correct |
| Luna Decisions | impress Addison with his helpfulness and try to get on her good side | Correct |
| Clef Flash | impress Addison with his helpfulness and try to get on her good side | Correct |
| Strands Decider | impress Addison with his helpfulness and try to get on her good side | Correct |
| GLiNER2.5 Decide | impress Addison with his helpfulness and try to get on her good side | Correct |
| Laya | wanted to mess up the english paper so he wrote it incorrectly | Incorrect |
| CalDec v1 | impress Addison with his helpfulness and try to get on her good side | Correct |

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
    "record": "26816",
    "kind": "source_file_record"
  },
  "source_revision": null,
  "input_hash": "b720cc8c1eb93539569de7358ca70a24c1ee967f7a15b2223b1c8b4d43e5cc6d"
}
```

</details>
