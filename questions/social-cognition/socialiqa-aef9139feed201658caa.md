# Social cognition · question 28

[Back to Social cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `socialiqa/aef9139feed201658caa`  
**Source:** [Social IQa](https://storage.googleapis.com/ai2-mosaic/public/socialiqa/socialiqa-train-dev.zip)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/social-cognition/socialiqa-aef9139feed201658caa/README.md)

## Context

> Bailey built a home for her new family and they loved it a lot.

## Question

> How would Bailey feel afterwards?

## Answer choices

- **A:** quite angry
- **B:** very sad
- **C:** at home

**Reference answer:** at home (`C`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Bailey built a home for her new family and they loved it a lot.",
  "question": "How would Bailey feel afterwards?",
  "choices": {
    "A": "quite angry",
    "B": "very sad",
    "C": "at home"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | at home | Correct |
| Opus 5.5 | at home | Correct |
| GLiDE v1.2 | at home | Correct |
| Decider v1.1 | at home | Correct |
| Jev | at home | Correct |
| Microsoft Decision-1 | at home | Correct |
| Clef | at home | Correct |
| Luna Decisions | at home | Correct |
| Clef Flash | at home | Correct |
| Strands Decider | at home | Correct |
| GLiNER2.5 Decide | at home | Correct |
| Laya | at home | Correct |
| CalDec v1 | at home | Correct |

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
    "record": "17840",
    "kind": "source_file_record"
  },
  "source_revision": null,
  "input_hash": "2308ff047f8a193371fd85fa4fc6788080595f6965a32659add0299385efc931"
}
```

</details>
