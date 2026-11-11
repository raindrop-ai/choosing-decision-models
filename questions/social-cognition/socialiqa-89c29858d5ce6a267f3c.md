# Social cognition · question 16

[Back to Social cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `socialiqa/89c29858d5ce6a267f3c`  
**Source:** [Social IQa](https://storage.googleapis.com/ai2-mosaic/public/socialiqa/socialiqa-train-dev.zip)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/social-cognition/socialiqa-89c29858d5ce6a267f3c/README.md)

## Context

> Jan refused to follow the rules at school. When Jan's parent's tried to talk to them, Jan gave them a hard time.

## Question

> How would Jan's parents feel as a result?

## Answer choices

- **A:** disaffected
- **B:** disrespected
- **C:** feeling depressed

**Reference answer:** disrespected (`B`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Jan refused to follow the rules at school. When Jan's parent's tried to talk to them, Jan gave them a hard time.",
  "question": "How would Jan's parents feel as a result?",
  "choices": {
    "A": "disaffected",
    "B": "disrespected",
    "C": "feeling depressed"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | disrespected | Correct |
| Opus 5.5 | disrespected | Correct |
| GLiDE v1.2 | disrespected | Correct |
| Decider v1.1 | disrespected | Correct |
| Jev | disrespected | Correct |
| Microsoft Decision-1 | disrespected | Correct |
| Clef | disrespected | Correct |
| Luna Decisions | disrespected | Correct |
| Clef Flash | disrespected | Correct |
| Strands Decider | disrespected | Correct |
| GLiNER2.5 Decide | disrespected | Correct |
| Laya | disaffected | Incorrect |
| CalDec v1 | disaffected | Incorrect |

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
    "record": "21784",
    "kind": "source_file_record"
  },
  "source_revision": null,
  "input_hash": "f05918808858e33645b7137e7aca9d23c0c35f71e9599894b7460e848e18c308"
}
```

</details>
