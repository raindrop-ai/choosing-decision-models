# Social cognition · question 11

[Back to Social cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `socialiqa/caf4d3dd24a4cd57690e`  
**Source:** [Social IQa](https://storage.googleapis.com/ai2-mosaic/public/socialiqa/socialiqa-train-dev.zip)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/social-cognition/socialiqa-caf4d3dd24a4cd57690e/README.md)

## Context

> Addison identified an asset at risk of failure and found a way to fix it.

## Question

> What will Others want to do next?

## Answer choices

- **A:** look for risks
- **B:** think about the risks
- **C:** thank Addison for their hard work

**Reference answer:** thank Addison for their hard work (`C`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Addison identified an asset at risk of failure and found a way to fix it.",
  "question": "What will Others want to do next?",
  "choices": {
    "A": "look for risks",
    "B": "think about the risks",
    "C": "thank Addison for their hard work"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | thank Addison for their hard work | Correct |
| Opus 5.5 | thank Addison for their hard work | Correct |
| GLiDE v1.2 | thank Addison for their hard work | Correct |
| Decider v1.1 | thank Addison for their hard work | Correct |
| Jev | thank Addison for their hard work | Correct |
| Microsoft Decision-1 | thank Addison for their hard work | Correct |
| Clef | thank Addison for their hard work | Correct |
| Luna Decisions | thank Addison for their hard work | Correct |
| Clef Flash | thank Addison for their hard work | Correct |
| Strands Decider | thank Addison for their hard work | Correct |
| GLiNER2.5 Decide | thank Addison for their hard work | Correct |
| Laya | look for risks | Incorrect |
| CalDec v1 | look for risks | Incorrect |

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
    "record": "15759",
    "kind": "source_file_record"
  },
  "source_revision": null,
  "input_hash": "5cfffd3697cc6e152b2ba32ff8b8c6bb4aa4b4dd58c878d8a1cdcce1a28fc10f"
}
```

</details>
