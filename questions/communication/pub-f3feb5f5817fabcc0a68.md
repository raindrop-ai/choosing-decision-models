# Communication · question 19

[Back to Communication](README.md) · [All capabilities](../README.md)

**Question ID:** `pub/f3feb5f5817fabcc0a68`  
**Source:** [PUB](https://huggingface.co/datasets/cfilt/PUB)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/communication/pub-f3feb5f5817fabcc0a68/README.md)

## Context

> Premise: Jill doesn't conceal why the girls do scratch.
> Hypothesis: The girls do scratch

## Question

> Choose the interpretation or answer requested by the text.

## Answer choices

- **A:** Hypothesis is definitely true given premise
- **B:** Hypothesis might be true given premise
- **C:** Hypothesis is definitely not true given premise

**Reference answer:** Hypothesis is definitely true given premise (`A`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Premise: Jill doesn't conceal why the girls do scratch.\nHypothesis: The girls do scratch",
  "question": "Choose the interpretation or answer requested by the text.",
  "choices": {
    "A": "Hypothesis is definitely true given premise",
    "B": "Hypothesis might be true given premise",
    "C": "Hypothesis is definitely not true given premise"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | Hypothesis is definitely true given premise | Correct |
| Opus 5.5 | Hypothesis is definitely true given premise | Correct |
| GLiDE v1.2 | Hypothesis is definitely true given premise | Correct |
| Decider v1.1 | Hypothesis is definitely true given premise | Correct |
| Jev | Hypothesis is definitely true given premise | Correct |
| Microsoft Decision-1 | Hypothesis is definitely true given premise | Correct |
| Clef | Hypothesis is definitely true given premise | Correct |
| Luna Decisions | Hypothesis might be true given premise | Incorrect |
| Clef Flash | Hypothesis is definitely true given premise | Correct |
| Strands Decider | Hypothesis is definitely true given premise | Correct |
| GLiNER2.5 Decide | Hypothesis is definitely true given premise | Correct |
| Laya | Hypothesis is definitely true given premise | Correct |
| CalDec v1 | Hypothesis is definitely true given premise | Correct |

## Source and sharing

Attribution: CFILT, IIT Bombay; PUB authors.  
Terms: **[MIT](https://opensource.org/license/mit)**. [Source sharing decision](../../docs/data-sharing.md).  
The capability assignment and choice-format normalization are part of this experiment. Source data retain their own terms.

<details>
<summary>Exact source locator and input fingerprint</summary>

```json
{
  "source_locator": {
    "path": "extracted/task_11.zip/task_11.jsonl",
    "record": "122",
    "kind": "source_file_record"
  },
  "source_revision": "65a6a87359fe4aa5278952741d5ed7e0ecb0f0ff",
  "input_hash": "8ddca03f11faac8fbe6d8d1dde2c7f078a1bc7262b02a9989a84623646d3e2a2"
}
```

</details>
