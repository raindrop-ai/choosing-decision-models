# Social cognition · question 25

[Back to Social cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `tombench/c45771fa2bf4b87022a8`  
**Source:** [ToMBench](https://github.com/zhchen18/ToMBench)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/social-cognition/tombench-c45771fa2bf4b87022a8/README.md)

## Context

> Zhang Lei goes to Paris for the first time, she stands under the Eiffel Tower, looking up at this world-famous landmark.

## Question

> What is Zhang Lei's feeling under the Eiffel Tower?

## Answer choices

- **A:** Angry
- **B:** Fear
- **C:** Curious
- **D:** Sadness

**Reference answer:** Curious (`C`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Zhang Lei goes to Paris for the first time, she stands under the Eiffel Tower, looking up at this world-famous landmark.",
  "question": "What is Zhang Lei's feeling under the Eiffel Tower?",
  "choices": {
    "A": "Angry",
    "B": "Fear",
    "C": "Curious",
    "D": "Sadness"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | Curious | Correct |
| Opus 5.5 | Curious | Correct |
| GLiDE v1.2 | Curious | Correct |
| Decider v1.1 | Curious | Correct |
| Jev | Curious | Correct |
| Microsoft Decision-1 | Curious | Correct |
| Clef | Curious | Correct |
| Luna Decisions | Curious | Correct |
| Clef Flash | Curious | Correct |
| Strands Decider | Curious | Correct |
| GLiNER2.5 Decide | Curious | Correct |
| Laya | Curious | Correct |
| CalDec v1 | Curious | Correct |

## Source and sharing

Attribution: Zhuang Chen et al.; ToMBench authors.  
Terms: **[MIT](https://opensource.org/license/mit)**. [Source sharing decision](../../docs/data-sharing.md).  
The capability assignment and choice-format normalization are part of this experiment. Source data retain their own terms.

<details>
<summary>Exact source locator and input fingerprint</summary>

```json
{
  "source_locator": {
    "path": "data/Unexpected Outcome Test.jsonl",
    "record": "153",
    "kind": "source_file_record"
  },
  "source_revision": "4f491f0784ed31ef93a8837615fbc48f885cf78d",
  "input_hash": "65c38fdd4cd1ffe78d7345eddf83fe6e32e66d260c669da779046755567c1db1"
}
```

</details>
