# Communication · question 7

[Back to Communication](README.md) · [All capabilities](../README.md)

**Question ID:** `pub/38325ecb2eba1a31d6c7`  
**Source:** [PUB](https://huggingface.co/datasets/cfilt/PUB)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/communication/pub-38325ecb2eba1a31d6c7/README.md)

## Context

> Context: X and Y are colleagues who are leaving work on a Friday at the same time.
> X: Do you want to go see a movie tonight?
> Y: I'd rather do something physical.

## Question

> Choose the interpretation or answer requested by the text.

## Answer choices

- **A:** Yes
- **B:** No
- **C:** Yes, subject to some conditions
- **D:** In the middle, neither yes nor no
- **E:** Other

**Reference answer:** No (`B`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Context: X and Y are colleagues who are leaving work on a Friday at the same time.\nX: Do you want to go see a movie tonight?\nY: I'd rather do something physical.\n",
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
| Astra | No | Correct |
| Opus 5.5 | No | Correct |
| GLiDE v1.2 | No | Correct |
| Decider v1.1 | No | Correct |
| Jev | No | Correct |
| Microsoft Decision-1 | No | Correct |
| Clef | No | Correct |
| Luna Decisions | Other | Incorrect |
| Clef Flash | No | Correct |
| Strands Decider | No | Correct |
| GLiNER2.5 Decide | Other | Incorrect |
| Laya | No | Correct |
| CalDec v1 | No | Correct |

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
    "record": "2502",
    "kind": "source_file_record"
  },
  "source_revision": "65a6a87359fe4aa5278952741d5ed7e0ecb0f0ff",
  "input_hash": "610c7fc4468f33054117cd5920c3a813e20b3ce5ca0dad93fab9888ea2a36261"
}
```

</details>
