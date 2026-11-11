# Social cognition · question 40

[Back to Social cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `socialiqa/c3e978f0dc5e7c441e01`  
**Source:** [Social IQa](https://storage.googleapis.com/ai2-mosaic/public/socialiqa/socialiqa-train-dev.zip)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/social-cognition/socialiqa-c3e978f0dc5e7c441e01/README.md)

## Context

> Sydney found Jesse a way to the store after they had gotten lost.

## Question

> What will Jesse want to do next?

## Answer choices

- **A:** get lost again
- **B:** buy a coffee at the store
- **C:** go to the store

**Reference answer:** go to the store (`C`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Sydney found Jesse a way to the store after they had gotten lost.",
  "question": "What will Jesse want to do next?",
  "choices": {
    "A": "get lost again",
    "B": "buy a coffee at the store",
    "C": "go to the store"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | go to the store | Correct |
| Opus 5.5 | go to the store | Correct |
| GLiDE v1.2 | go to the store | Correct |
| Decider v1.1 | go to the store | Correct |
| Jev | go to the store | Correct |
| Microsoft Decision-1 | go to the store | Correct |
| Clef | go to the store | Correct |
| Luna Decisions | go to the store | Correct |
| Clef Flash | go to the store | Correct |
| Strands Decider | go to the store | Correct |
| GLiNER2.5 Decide | go to the store | Correct |
| Laya | get lost again | Incorrect |
| CalDec v1 | get lost again | Incorrect |

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
    "record": "14617",
    "kind": "source_file_record"
  },
  "source_revision": null,
  "input_hash": "4b4872b68fca9ac9ec8f54ccb8c72f784fa703bcc0b42504e8c8c204fd8a38ba"
}
```

</details>
