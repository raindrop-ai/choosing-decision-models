# Communication · question 60

[Back to Communication](README.md) · [All capabilities](../README.md)

**Question ID:** `pub/af91d0e3d83ed05469bf`  
**Source:** [PUB](https://huggingface.co/datasets/cfilt/PUB)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/communication/pub-af91d0e3d83ed05469bf/README.md)

## Context

> Context: Y has just told X that he/she is thinking of buying a flat in New York.
> X: Can you afford an apartment?
> Y: I've been saving for a long time.

## Question

> Choose the interpretation or answer requested by the text.

## Answer choices

- **A:** Yes
- **B:** No
- **C:** Yes, subject to some conditions
- **D:** In the middle, neither yes nor no
- **E:** Other

**Reference answer:** Yes (`A`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Context: Y has just told X that he/she is thinking of buying a flat in New York.\nX: Can you afford an apartment?\nY: I've been saving for a long time.\n",
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
| Astra | Yes | Correct |
| Opus 5.5 | Yes | Correct |
| GLiDE v1.2 | Yes | Correct |
| Decider v1.1 | Yes | Correct |
| Jev | Yes | Correct |
| Microsoft Decision-1 | Yes | Correct |
| Clef | Yes | Correct |
| Luna Decisions | Yes, subject to some conditions | Incorrect |
| Clef Flash | Yes | Correct |
| Strands Decider | Yes | Correct |
| GLiNER2.5 Decide | Other | Incorrect |
| Laya | Yes | Correct |
| CalDec v1 | Yes | Correct |

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
    "record": "2302",
    "kind": "source_file_record"
  },
  "source_revision": "65a6a87359fe4aa5278952741d5ed7e0ecb0f0ff",
  "input_hash": "0bf210cbac614d4c86861606ffdbe59db567b911a325f94557e4b753951ae971"
}
```

</details>
