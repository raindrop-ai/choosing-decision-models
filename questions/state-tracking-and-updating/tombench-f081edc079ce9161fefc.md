# State tracking and updating · question 3

[Back to State tracking and updating](README.md) · [All capabilities](../README.md)

**Question ID:** `tombench/f081edc079ce9161fefc`  
**Source:** [ToMBench](https://github.com/zhchen18/ToMBench)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/state-tracking-and-updating/tombench-f081edc079ce9161fefc/README.md)

## Context

> Xiao Ming and Zhang Wei are wandering in the hall, they see a handbag and a box, they find a sponge in the handbag, Zhang Wei leaves the hall, Xiao Ming moves the sponge to the box.

## Question

> Where is the sponge now?

## Answer choices

- **A:** Box
- **B:** Handbag
- **C:** Storage locker
- **D:** Briefcase

**Reference answer:** Box (`A`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Xiao Ming and Zhang Wei are wandering in the hall, they see a handbag and a box, they find a sponge in the handbag, Zhang Wei leaves the hall, Xiao Ming moves the sponge to the box.",
  "question": "Where is the sponge now?",
  "choices": {
    "A": "Box",
    "B": "Handbag",
    "C": "Storage locker",
    "D": "Briefcase"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | Box | Correct |
| Opus 5.5 | Box | Correct |
| GLiDE v1.2 | Box | Correct |
| Decider v1.1 | Box | Correct |
| Jev | Box | Correct |
| Microsoft Decision-1 | Box | Correct |
| Clef | Box | Correct |
| Luna Decisions | Box | Correct |
| Clef Flash | Box | Correct |
| Strands Decider | Box | Correct |
| GLiNER2.5 Decide | Box | Correct |
| Laya | Box | Correct |
| CalDec v1 | Box | Correct |

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
    "record": "270",
    "kind": "source_file_record"
  },
  "source_revision": "4f491f0784ed31ef93a8837615fbc48f885cf78d",
  "input_hash": "0dde839eb1142c00462a69f9915638eba8e5f4d9c35c92666b6b4d8304c51eb6"
}
```

</details>
