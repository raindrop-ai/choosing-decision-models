# Social cognition · question 20

[Back to Social cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `socialiqa/663709fec0fa8c9ab71a`  
**Source:** [Social IQa](https://storage.googleapis.com/ai2-mosaic/public/socialiqa/socialiqa-train-dev.zip)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/social-cognition/socialiqa-663709fec0fa8c9ab71a/README.md)

## Context

> Remy was decorating their room and bought new sheets.

## Question

> How would you describe Remy?

## Answer choices

- **A:** As someone that likes to decorate
- **B:** proud
- **C:** As someone who&#x27;s asked about their room

**Reference answer:** As someone that likes to decorate (`A`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Remy was decorating their room and bought new sheets.",
  "question": "How would you describe Remy?",
  "choices": {
    "A": "As someone that likes to decorate",
    "B": "proud",
    "C": "As someone who's asked about their room"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | As someone that likes to decorate | Correct |
| Opus 5.5 | As someone that likes to decorate | Correct |
| GLiDE v1.2 | As someone that likes to decorate | Correct |
| Decider v1.1 | As someone that likes to decorate | Correct |
| Jev | As someone that likes to decorate | Correct |
| Microsoft Decision-1 | As someone that likes to decorate | Correct |
| Clef | As someone that likes to decorate | Correct |
| Luna Decisions | As someone that likes to decorate | Correct |
| Clef Flash | As someone that likes to decorate | Correct |
| Strands Decider | As someone that likes to decorate | Correct |
| GLiNER2.5 Decide | As someone that likes to decorate | Correct |
| Laya | As someone that likes to decorate | Correct |
| CalDec v1 | As someone that likes to decorate | Correct |

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
    "record": "3444",
    "kind": "source_file_record"
  },
  "source_revision": null,
  "input_hash": "004f4d2b628c3cdfe9f859422825e4b6f95ceb5f039e385c97fcf6e084118d5f"
}
```

</details>
