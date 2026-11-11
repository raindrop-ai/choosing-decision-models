# Communication · question 20

[Back to Communication](README.md) · [All capabilities](../README.md)

**Question ID:** `tombench/4e9d21af0d0ef82d333a`  
**Source:** [ToMBench](https://github.com/zhchen18/ToMBench)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/communication/tombench-4e9d21af0d0ef82d333a/README.md)

## Context

> Anming's mother spends a long time making Anming's favorite fried fish and chips. But when she brings the food to Anming, Anming watches TV, she doesn't even look up, and doesn't say thank you. Anming's mother says angrily: "You are really polite!"

## Question

> Why does the mother say this?

## Answer choices

- **A:** She thinks Anming is a very polite child
- **B:** She lies to encourage Anming to be a very polite child
- **C:** She wants to mock her own food is not delicious.
- **D:** She wants to mock Anming is a child without manners.

**Reference answer:** She wants to mock Anming is a child without manners. (`D`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Anming's mother spends a long time making Anming's favorite fried fish and chips. But when she brings the food to Anming, Anming watches TV, she doesn't even look up, and doesn't say thank you. Anming's mother says angrily: \"You are really polite!\"",
  "question": "Why does the mother say this?",
  "choices": {
    "A": "She thinks Anming is a very polite child",
    "B": "She lies to encourage Anming to be a very polite child",
    "C": "She wants to mock her own food is not delicious.",
    "D": "She wants to mock Anming is a child without manners."
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | She wants to mock Anming is a child without manners. | Correct |
| Opus 5.5 | She wants to mock Anming is a child without manners. | Correct |
| GLiDE v1.2 | She wants to mock Anming is a child without manners. | Correct |
| Decider v1.1 | She wants to mock Anming is a child without manners. | Correct |
| Jev | She wants to mock Anming is a child without manners. | Correct |
| Microsoft Decision-1 | She wants to mock Anming is a child without manners. | Correct |
| Clef | She wants to mock Anming is a child without manners. | Correct |
| Luna Decisions | She wants to mock Anming is a child without manners. | Correct |
| Clef Flash | She wants to mock Anming is a child without manners. | Correct |
| Strands Decider | She wants to mock Anming is a child without manners. | Correct |
| GLiNER2.5 Decide | She thinks Anming is a very polite child | Incorrect |
| Laya | She thinks Anming is a very polite child | Incorrect |
| CalDec v1 | She thinks Anming is a very polite child | Incorrect |

## Source and sharing

Attribution: Zhuang Chen et al.; ToMBench authors.  
Terms: **[MIT](https://opensource.org/license/mit)**. [Source sharing decision](../../docs/data-sharing.md).  
The capability assignment and choice-format normalization are part of this experiment. Source data retain their own terms.

<details>
<summary>Exact source locator and input fingerprint</summary>

```json
{
  "source_locator": {
    "path": "data/Strange Story Task.jsonl",
    "record": "3",
    "kind": "source_file_record"
  },
  "source_revision": "4f491f0784ed31ef93a8837615fbc48f885cf78d",
  "input_hash": "e490ea0bcc3a8847860b676d176009c86f5a0f2a7d244f6ae04a3090a1530820"
}
```

</details>
