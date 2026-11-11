# Communication · question 44

[Back to Communication](README.md) · [All capabilities](../README.md)

**Question ID:** `pub/022a4c7f5dee09eaf4b8`  
**Source:** [PUB](https://huggingface.co/datasets/cfilt/PUB)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/communication/pub-022a4c7f5dee09eaf4b8/README.md)

## Context

> Context: Y has just told X that he/she is considering switching his/her job.
> X: Do you prefer a different career?
> Y: Only if the promotion opportunities are better.

## Question

> Choose the interpretation or answer requested by the text.

## Answer choices

- **A:** Yes
- **B:** No
- **C:** Yes, subject to some conditions
- **D:** In the middle, neither yes nor no
- **E:** Other

**Reference answer:** Yes, subject to some conditions (`C`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Context: Y has just told X that he/she is considering switching his/her job.\nX: Do you prefer a different career?\nY: Only if the promotion opportunities are better.\n",
  "question": "Choose the interpretation or answer requested by the text.",
  "choices": {
    "A": "Yes",
    "B": "No",
    "C": "Yes, subject to some conditions",
    "D": "In the middle, neither yes nor no",
    "E": "Other"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | Yes, subject to some conditions | Correct |
| Opus 5.5 | Yes, subject to some conditions | Correct |
| GLiDE v1.2 | Yes, subject to some conditions | Correct |
| Decider v1.1 | Yes, subject to some conditions | Correct |
| Jev | Yes, subject to some conditions | Correct |
| Microsoft Decision-1 | Yes, subject to some conditions | Correct |
| Clef | Yes, subject to some conditions | Correct |
| Luna Decisions | Yes, subject to some conditions | Correct |
| Clef Flash | Yes, subject to some conditions | Correct |
| Strands Decider | Yes, subject to some conditions | Correct |
| GLiNER2.5 Decide | Other | Incorrect |
| Laya | Yes | Incorrect |
| CalDec v1 | Yes | Incorrect |

## Source and sharing

Attribution: CFILT, IIT Bombay; PUB authors.  
Terms: **[MIT](https://opensource.org/license/mit)**. [Source sharing decision](../../docs/data-sharing.md).  
The capability assignment and choice-format normalization are part of this experiment. Source data retain their own terms.

<details>
<summary>Exact source locator and input fingerprint</summary>

```json
{
  "source_locator": {
    "path": "extracted/task_2.zip/task_2.jsonl",
    "record": "2096",
    "kind": "source_file_record"
  },
  "source_revision": "65a6a87359fe4aa5278952741d5ed7e0ecb0f0ff",
  "input_hash": "922c987a6a999f0da2cd6f474bf97d52e65cf95ee54c0c25ebe2071c8f00e0a6"
}
```

</details>
