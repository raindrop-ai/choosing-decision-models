# Social cognition · question 32

[Back to Social cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `socialiqa/e855db00e65efa9913e8`  
**Source:** [Social IQa](https://storage.googleapis.com/ai2-mosaic/public/socialiqa/socialiqa-train-dev.zip)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/social-cognition/socialiqa-e855db00e65efa9913e8/README.md)

## Context

> Lee listened to Kendall's talk and took a lot of notes.

## Question

> Why did Lee do this?

## Answer choices

- **A:** understand Kendall&#x27;s words
- **B:** ruin Kai&#x27;s reputation
- **C:** tell lies about Kendall

**Reference answer:** understand Kendall&#x27;s words (`A`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Lee listened to Kendall's talk and took a lot of notes.",
  "question": "Why did Lee do this?",
  "choices": {
    "A": "understand Kendall's words",
    "B": "ruin Kai's reputation",
    "C": "tell lies about Kendall"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | understand Kendall&#x27;s words | Correct |
| Opus 5.5 | understand Kendall&#x27;s words | Correct |
| GLiDE v1.2 | understand Kendall&#x27;s words | Correct |
| Decider v1.1 | understand Kendall&#x27;s words | Correct |
| Jev | understand Kendall&#x27;s words | Correct |
| Microsoft Decision-1 | understand Kendall&#x27;s words | Correct |
| Clef | understand Kendall&#x27;s words | Correct |
| Luna Decisions | understand Kendall&#x27;s words | Correct |
| Clef Flash | understand Kendall&#x27;s words | Correct |
| Strands Decider | understand Kendall&#x27;s words | Correct |
| GLiNER2.5 Decide | understand Kendall&#x27;s words | Correct |
| Laya | understand Kendall&#x27;s words | Correct |
| CalDec v1 | understand Kendall&#x27;s words | Correct |

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
    "record": "33265",
    "kind": "source_file_record"
  },
  "source_revision": null,
  "input_hash": "45f2a47f9058faeee4cbc33b93436d0ee7b9138318beca2e4f6ec18d5b03f3b7"
}
```

</details>
