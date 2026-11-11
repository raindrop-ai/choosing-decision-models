# Social cognition · question 57

[Back to Social cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `tombench/ba4656ab2b4426100d2f`  
**Source:** [ToMBench](https://github.com/zhchen18/ToMBench)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/social-cognition/tombench-ba4656ab2b4426100d2f/README.md)

## Context

> Xiao Li and Xiao Gang are hanging out at the bar. They see boxes and safes, and inside the box, they find a bottle. Xiao Gang leaves the bar, and Xiao Li moves the bottle to the safe.

## Question

> Xiao Gang returns to the bar, does Xiao Gang know where the bottle is now?

## Answer choices

- **A:** Does not know
- **B:** Knows, in the safe
- **C:** Knows, in the cabinet
- **D:** Knows, in the box

**Reference answer:** Does not know (`A`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Xiao Li and Xiao Gang are hanging out at the bar. They see boxes and safes, and inside the box, they find a bottle. Xiao Gang leaves the bar, and Xiao Li moves the bottle to the safe.",
  "question": "Xiao Gang returns to the bar, does Xiao Gang know where the bottle is now?",
  "choices": {
    "A": "Does not know",
    "B": "Knows, in the safe",
    "C": "Knows, in the cabinet",
    "D": "Knows, in the box"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | Does not know | Correct |
| Opus 5.5 | Does not know | Correct |
| GLiDE v1.2 | Knows, in the box | Incorrect |
| Decider v1.1 | Does not know | Correct |
| Jev | Knows, in the box | Incorrect |
| Microsoft Decision-1 | Does not know | Correct |
| Clef | Does not know | Correct |
| Luna Decisions | Does not know | Correct |
| Clef Flash | Does not know | Correct |
| Strands Decider | Knows, in the safe | Incorrect |
| GLiNER2.5 Decide | Knows, in the box | Incorrect |
| Laya | Knows, in the safe | Incorrect |
| CalDec v1 | Knows, in the safe | Incorrect |

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
    "record": "31",
    "kind": "source_file_record"
  },
  "source_revision": "4f491f0784ed31ef93a8837615fbc48f885cf78d",
  "input_hash": "7ce63b8dffd433e3facb413db019df44ecf45a4f76793947152fda307b1b0115"
}
```

</details>
