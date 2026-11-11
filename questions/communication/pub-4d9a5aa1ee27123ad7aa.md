# Communication · question 30

[Back to Communication](README.md) · [All capabilities](../README.md)

**Question ID:** `pub/4d9a5aa1ee27123ad7aa`  
**Source:** [PUB](https://huggingface.co/datasets/cfilt/PUB)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/communication/pub-4d9a5aa1ee27123ad7aa/README.md)

## Context

> Speaker\_1: He shares as much as scrooge.
> Speaker\_2: He doesn't share much at all.

## Question

> Choose the interpretation or answer requested by the text.

## Answer choices

- **A:** Agrees
- **B:** Disagrees

**Reference answer:** Agrees (`A`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Speaker_1: He shares as much as scrooge.\nSpeaker_2: He doesn't share much at all.",
  "question": "Choose the interpretation or answer requested by the text.",
  "choices": {
    "A": "Agrees",
    "B": "Disagrees"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | Agrees | Correct |
| Opus 5.5 | Agrees | Correct |
| GLiDE v1.2 | Agrees | Correct |
| Decider v1.1 | Agrees | Correct |
| Jev | Agrees | Correct |
| Microsoft Decision-1 | Agrees | Correct |
| Clef | Disagrees | Incorrect |
| Luna Decisions | Agrees | Correct |
| Clef Flash | Agrees | Correct |
| Strands Decider | Disagrees | Incorrect |
| GLiNER2.5 Decide | Disagrees | Incorrect |
| Laya | Disagrees | Incorrect |
| CalDec v1 | Disagrees | Incorrect |

## Source and sharing

Attribution: CFILT, IIT Bombay; PUB authors.  
Terms: **[MIT](https://opensource.org/license/mit)**. [Source sharing decision](../../docs/data-sharing.md).  
The capability assignment and choice-format normalization are part of this experiment. Source data retain their own terms.

<details>
<summary>Exact source locator and input fingerprint</summary>

```json
{
  "source_locator": {
    "path": "extracted/task_5.zip/task_5.jsonl",
    "record": "706",
    "kind": "source_file_record"
  },
  "source_revision": "65a6a87359fe4aa5278952741d5ed7e0ecb0f0ff",
  "input_hash": "897b95ad9aac51a5b4407b83dd6e1fdba07442cce47ef17813016d046c281e1c"
}
```

</details>
