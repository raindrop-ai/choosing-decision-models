# Retrieval · question 17

[Back to Retrieval](README.md) · [All capabilities](../README.md)

**Question ID:** `tombench/b114ed34e38d91c46a6c`  
**Source:** [ToMBench](https://github.com/zhchen18/ToMBench)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/retrieval/tombench-b114ed34e38d91c46a6c/README.md)

## Context

> In the early morning, the bus is as crowded as usual. Zhao Lei gets on the bus and finds her neighbor, Mr. Zhang, is wearing casual clothes that he usually does not wear. She greets him excitedly: "Mr. Zhang, good morning! Usually, I do not see you go out at this time, do you take a day off today?" Mr. Zhang nods his head without saying much. The bus drives to the next stop, and Zhao Lei still happily continues to say: "That is a rare rest time, you must enjoy it." Mr. Zhang responds with a light "hmm", and turns his head to look out the window. Zhao Lei starts to eat the breakfast she just bought.

## Question

> What does Zhao Lei do when Mr. Zhang turns his head to look out the window?

## Answer choices

- **A:** Talks to the driver
- **B:** Flips through her magazine
- **C:** Looks out the window
- **D:** Eats breakfast

**Reference answer:** Eats breakfast (`D`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "In the early morning, the bus is as crowded as usual. Zhao Lei gets on the bus and finds her neighbor, Mr. Zhang, is wearing casual clothes that he usually does not wear. She greets him excitedly: \"Mr. Zhang, good morning! Usually, I do not see you go out at this time, do you take a day off today?\" Mr. Zhang nods his head without saying much. The bus drives to the next stop, and Zhao Lei still happily continues to say: \"That is a rare rest time, you must enjoy it.\" Mr. Zhang responds with a light \"hmm\", and turns his head to look out the window. Zhao Lei starts to eat the breakfast she just bought.",
  "question": "What does Zhao Lei do when Mr. Zhang turns his head to look out the window?",
  "choices": {
    "A": "Talks to the driver",
    "B": "Flips through her magazine",
    "C": "Looks out the window",
    "D": "Eats breakfast"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | Eats breakfast | Correct |
| Opus 5.5 | Eats breakfast | Correct |
| GLiDE v1.2 | Eats breakfast | Correct |
| Decider v1.1 | Eats breakfast | Correct |
| Jev | Eats breakfast | Correct |
| Microsoft Decision-1 | Eats breakfast | Correct |
| Clef | Eats breakfast | Correct |
| Luna Decisions | Eats breakfast | Correct |
| Clef Flash | Eats breakfast | Correct |
| Strands Decider | Eats breakfast | Correct |
| GLiNER2.5 Decide | Looks out the window | Incorrect |
| Laya | Eats breakfast | Correct |
| CalDec v1 | Eats breakfast | Correct |

## Source and sharing

Attribution: Zhuang Chen et al.; ToMBench authors.  
Terms: **[MIT](https://opensource.org/license/mit)**. [Source sharing decision](../../docs/data-sharing.md).  
The capability assignment and choice-format normalization are part of this experiment. Source data retain their own terms.

<details>
<summary>Exact source locator and input fingerprint</summary>

```json
{
  "source_locator": {
    "path": "data/Faux-pas Recognition Test.jsonl",
    "record": "210",
    "kind": "source_file_record"
  },
  "source_revision": "4f491f0784ed31ef93a8837615fbc48f885cf78d",
  "input_hash": "a46c3ae772c86a516b8d7a52c57bf047e18c97f94b1091f9da50f18a503e59d3"
}
```

</details>
