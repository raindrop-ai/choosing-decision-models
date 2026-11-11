# State tracking and updating · question 62

[Back to State tracking and updating](README.md) · [All capabilities](../README.md)

**Question ID:** `bbh/e9d5fa0fe20ed7cd4ead`  
**Source:** [BIG-Bench Hard selected tasks](https://github.com/suzgunmirac/BIG-Bench-Hard)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/state-tracking-and-updating/bbh-e9d5fa0fe20ed7cd4ead/README.md)

## Question

> Alice, Bob, and Claire are holding a white elephant gift exchange. At the start of the event, they are each holding a present of a different color: Alice has a orange ball, Bob has a green present, and Claire has a red present.
> As the event progresses, pairs of people swap gifts. First, Bob and Alice swap their gifts. Then, Bob and Claire swap their gifts. Finally, Alice and Claire swap their gifts. At the end of the event, Alice has the

## Answer choices

- **A:** orange ball
- **B:** green present
- **C:** red present

**Reference answer:** orange ball (`A`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "",
  "question": "Alice, Bob, and Claire are holding a white elephant gift exchange. At the start of the event, they are each holding a present of a different color: Alice has a orange ball, Bob has a green present, and Claire has a red present.\nAs the event progresses, pairs of people swap gifts. First, Bob and Alice swap their gifts. Then, Bob and Claire swap their gifts. Finally, Alice and Claire swap their gifts. At the end of the event, Alice has the",
  "choices": {
    "A": "orange ball",
    "B": "green present",
    "C": "red present"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | orange ball | Correct |
| Opus 5.5 | orange ball | Correct |
| GLiDE v1.2 | orange ball | Correct |
| Decider v1.1 | red present | Incorrect |
| Jev | orange ball | Correct |
| Microsoft Decision-1 | orange ball | Correct |
| Clef | red present | Incorrect |
| Luna Decisions | green present | Incorrect |
| Clef Flash | red present | Incorrect |
| Strands Decider | red present | Incorrect |
| GLiNER2.5 Decide | orange ball | Correct |
| Laya | orange ball | Correct |
| CalDec v1 | orange ball | Correct |

## Source and sharing

Attribution: Mirac Suzgun and BIG-Bench Hard authors; BIG-bench contributors.  
Terms: **[MIT AND Apache-2.0](https://opensource.org/license/mit)**. [Source sharing decision](../../docs/data-sharing.md).  
The capability assignment and choice-format normalization are part of this experiment. Source data retain their own terms.

<details>
<summary>Exact source locator and input fingerprint</summary>

```json
{
  "source_locator": {
    "path": "bbh/tracking_shuffled_objects_three_objects.json",
    "record": "230",
    "kind": "source_file_record"
  },
  "source_revision": "9ee07bd481feebf959a6b59d61ea57bdcf30964d",
  "input_hash": "061f697b1d3395c34adfef22f128581fa301c8442253ce03bd67e386d781191e"
}
```

</details>
