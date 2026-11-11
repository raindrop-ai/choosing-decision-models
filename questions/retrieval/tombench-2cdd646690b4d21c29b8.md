# Retrieval · question 23

[Back to Retrieval](README.md) · [All capabilities](../README.md)

**Question ID:** `tombench/2cdd646690b4d21c29b8`  
**Source:** [ToMBench](https://github.com/zhchen18/ToMBench)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/retrieval/tombench-2cdd646690b4d21c29b8/README.md)

## Context

> Xiao Li finds a storage cabinet in the study, the label on the storage cabinet is carrot, Xiao Li cannot see what is inside the storage cabinet, Xiao Li opens the storage cabinet and finds a coat, there are no carrots in the storage cabinet, Xiao Li closes the storage cabinet and puts it back in its place, Xiao Zhang enters the study and sees the storage cabinet.

## Question

> What is in the storage cabinet?

## Answer choices

- **A:** Coat
- **B:** Pencil
- **C:** Carrot
- **D:** Tape

**Reference answer:** Coat (`A`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Xiao Li finds a storage cabinet in the study, the label on the storage cabinet is carrot, Xiao Li cannot see what is inside the storage cabinet, Xiao Li opens the storage cabinet and finds a coat, there are no carrots in the storage cabinet, Xiao Li closes the storage cabinet and puts it back in its place, Xiao Zhang enters the study and sees the storage cabinet.",
  "question": "What is in the storage cabinet?",
  "choices": {
    "A": "Coat",
    "B": "Pencil",
    "C": "Carrot",
    "D": "Tape"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | Coat | Correct |
| Opus 5.5 | Coat | Correct |
| GLiDE v1.2 | Coat | Correct |
| Decider v1.1 | Coat | Correct |
| Jev | Coat | Correct |
| Microsoft Decision-1 | Coat | Correct |
| Clef | Coat | Correct |
| Luna Decisions | Coat | Correct |
| Clef Flash | Coat | Correct |
| Strands Decider | Coat | Correct |
| GLiNER2.5 Decide | Coat | Correct |
| Laya | Coat | Correct |
| CalDec v1 | Coat | Correct |

## Source and sharing

Attribution: Zhuang Chen et al.; ToMBench authors.  
Terms: **[MIT](https://opensource.org/license/mit)**. [Source sharing decision](../../docs/data-sharing.md).  
The capability assignment and choice-format normalization are part of this experiment. Source data retain their own terms.

<details>
<summary>Exact source locator and input fingerprint</summary>

```json
{
  "source_locator": {
    "path": "data/False Belief Task.jsonl",
    "record": "336",
    "kind": "source_file_record"
  },
  "source_revision": "4f491f0784ed31ef93a8837615fbc48f885cf78d",
  "input_hash": "dd74fbfa723249a32f2e0d0017b90bb43e6de58b903c524f47d1e44c5f3c24e7"
}
```

</details>
