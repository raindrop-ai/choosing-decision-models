# Social cognition · question 33

[Back to Social cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `tombench/af01864109c5ac190db3`  
**Source:** [ToMBench](https://github.com/zhchen18/ToMBench)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/social-cognition/tombench-af01864109c5ac190db3/README.md)

## Context

> Xiao Li and Li Lei are strolling in the hallway. They see cabinets and boxes, and inside the cabinet, they find a vest. Li Lei leaves the hallway, and Xiao Li moves the vest to the box.

## Question

> Does Li Lei see anything in the box?

## Answer choices

- **A:** A vest
- **B:** Does not see
- **C:** Lockers
- **D:** Boxes

**Reference answer:** Does not see (`B`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Xiao Li and Li Lei are strolling in the hallway. They see cabinets and boxes, and inside the cabinet, they find a vest. Li Lei leaves the hallway, and Xiao Li moves the vest to the box.",
  "question": "Does Li Lei see anything in the box?",
  "choices": {
    "A": "A vest",
    "B": "Does not see",
    "C": "Lockers",
    "D": "Boxes"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | Does not see | Correct |
| Opus 5.5 | Does not see | Correct |
| GLiDE v1.2 | Does not see | Correct |
| Decider v1.1 | Does not see | Correct |
| Jev | Does not see | Correct |
| Microsoft Decision-1 | Does not see | Correct |
| Clef | Does not see | Correct |
| Luna Decisions | Does not see | Correct |
| Clef Flash | Does not see | Correct |
| Strands Decider | A vest | Incorrect |
| GLiNER2.5 Decide | A vest | Incorrect |
| Laya | A vest | Incorrect |
| CalDec v1 | A vest | Incorrect |

## Source and sharing

Attribution: Zhuang Chen et al.; ToMBench authors.  
Terms: **[MIT](https://opensource.org/license/mit)**. [Source sharing decision](../../docs/data-sharing.md).  
The capability assignment and choice-format normalization are part of this experiment. Source data retain their own terms.

<details>
<summary>Exact source locator and input fingerprint</summary>

```json
{
  "source_locator": {
    "path": "data/Percepts-Knowledge Links.jsonl",
    "record": "36",
    "kind": "source_file_record"
  },
  "source_revision": "4f491f0784ed31ef93a8837615fbc48f885cf78d",
  "input_hash": "8e646ba8edbaa2346c7d8abc61d6521b8f746e207783645155e5e7a77e4df0ca"
}
```

</details>
