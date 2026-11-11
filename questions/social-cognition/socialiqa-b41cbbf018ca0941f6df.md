# Social cognition · question 48

[Back to Social cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `socialiqa/b41cbbf018ca0941f6df`  
**Source:** [Social IQa](https://storage.googleapis.com/ai2-mosaic/public/socialiqa/socialiqa-train-dev.zip)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/social-cognition/socialiqa-b41cbbf018ca0941f6df/README.md)

## Context

> Casey used their car to get to work and made it to work on  time.

## Question

> How would Casey feel afterwards?

## Answer choices

- **A:** Glad they were on time
- **B:** a smart worker
- **C:** Like they need to get to work

**Reference answer:** Glad they were on time (`A`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Casey used their car to get to work and made it to work on  time.",
  "question": "How would Casey feel afterwards?",
  "choices": {
    "A": "Glad they were on time",
    "B": "a smart worker",
    "C": "Like they need to get to work"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | Glad they were on time | Correct |
| Opus 5.5 | Glad they were on time | Correct |
| GLiDE v1.2 | Glad they were on time | Correct |
| Decider v1.1 | Glad they were on time | Correct |
| Jev | Glad they were on time | Correct |
| Microsoft Decision-1 | Glad they were on time | Correct |
| Clef | Glad they were on time | Correct |
| Luna Decisions | Glad they were on time | Correct |
| Clef Flash | Glad they were on time | Correct |
| Strands Decider | Glad they were on time | Correct |
| GLiNER2.5 Decide | Glad they were on time | Correct |
| Laya | Glad they were on time | Correct |
| CalDec v1 | Glad they were on time | Correct |

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
    "record": "32800",
    "kind": "source_file_record"
  },
  "source_revision": null,
  "input_hash": "76e917cdc63f0c437ab7f5cb9e3cc37dfe5007c73c039c7eacf429dc4f2516d9"
}
```

</details>
