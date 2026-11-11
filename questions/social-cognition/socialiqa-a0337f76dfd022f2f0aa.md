# Social cognition · question 44

[Back to Social cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `socialiqa/a0337f76dfd022f2f0aa`  
**Source:** [Social IQa](https://storage.googleapis.com/ai2-mosaic/public/socialiqa/socialiqa-train-dev.zip)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/social-cognition/socialiqa-a0337f76dfd022f2f0aa/README.md)

## Context

> Skylar was grateful for Robin's letter of recommendation and eager to apply for the position. Furthermore, Robin knew Skylar personally.

## Question

> What will Skylar want to do next?

## Answer choices

- **A:** thank Robin for the help
- **B:** a bad idea
- **C:** avoid contact with Robin

**Reference answer:** thank Robin for the help (`A`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Skylar was grateful for Robin's letter of recommendation and eager to apply for the position. Furthermore, Robin knew Skylar personally.",
  "question": "What will Skylar want to do next?",
  "choices": {
    "A": "thank Robin for the help",
    "B": "a bad idea",
    "C": "avoid contact with Robin"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | thank Robin for the help | Correct |
| Opus 5.5 | thank Robin for the help | Correct |
| GLiDE v1.2 | thank Robin for the help | Correct |
| Decider v1.1 | thank Robin for the help | Correct |
| Jev | thank Robin for the help | Correct |
| Microsoft Decision-1 | thank Robin for the help | Correct |
| Clef | thank Robin for the help | Correct |
| Luna Decisions | thank Robin for the help | Correct |
| Clef Flash | thank Robin for the help | Correct |
| Strands Decider | thank Robin for the help | Correct |
| GLiNER2.5 Decide | thank Robin for the help | Correct |
| Laya | thank Robin for the help | Correct |
| CalDec v1 | thank Robin for the help | Correct |

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
    "record": "31104",
    "kind": "source_file_record"
  },
  "source_revision": null,
  "input_hash": "139d51a42a32f39e21ccae950ff97b628062de5225a4fcd5c80efe6b46c150b1"
}
```

</details>
