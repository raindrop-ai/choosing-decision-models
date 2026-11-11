# Social cognition · question 17

[Back to Social cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `tombench/22239a3652a340bfad6e`  
**Source:** [ToMBench](https://github.com/zhchen18/ToMBench)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/social-cognition/tombench-22239a3652a340bfad6e/README.md)

## Context

> Xiao Bei and Xiao Li are wandering in the parking lot, they see boxes and baskets, they find bananas in the box, Xiao Li leaves the parking lot, Xiao Bei moves the bananas to the basket.

## Question

> After Xiao Li returns to the parking lot, where does Xiao Bei think Xiao Li looks for the bananas?

## Answer choices

- **A:** Briefcase
- **B:** Box
- **C:** Basket
- **D:** Cabinet

**Reference answer:** Box (`B`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Xiao Bei and Xiao Li are wandering in the parking lot, they see boxes and baskets, they find bananas in the box, Xiao Li leaves the parking lot, Xiao Bei moves the bananas to the basket.",
  "question": "After Xiao Li returns to the parking lot, where does Xiao Bei think Xiao Li looks for the bananas?",
  "choices": {
    "A": "Briefcase",
    "B": "Box",
    "C": "Basket",
    "D": "Cabinet"
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
| GLiNER2.5 Decide | Basket | Incorrect |
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
    "record": "286",
    "kind": "source_file_record"
  },
  "source_revision": "4f491f0784ed31ef93a8837615fbc48f885cf78d",
  "input_hash": "99e9b90aec512e5e5fb92da234eb4ab2c57182747d1a45b9e94439dc5ece039c"
}
```

</details>
