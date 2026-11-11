# Social cognition · question 53

[Back to Social cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `tombench/ea74a3f3e4d59cb62974`  
**Source:** [ToMBench](https://github.com/zhchen18/ToMBench)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/social-cognition/tombench-ea74a3f3e4d59cb62974/README.md)

## Context

> Liu Jing finds that her best friend Zhang Hong does not invite her to the birthday party.

## Question

> What emotion does Liu Jing possibly have?

## Answer choices

- **A:** Embarrassed
- **B:** Disappointed
- **C:** Ashamed
- **D:** Contempt

**Reference answer:** Disappointed (`B`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Liu Jing finds that her best friend Zhang Hong does not invite her to the birthday party.",
  "question": "What emotion does Liu Jing possibly have?",
  "choices": {
    "A": "Embarrassed",
    "B": "Disappointed",
    "C": "Ashamed",
    "D": "Contempt"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | Disappointed | Correct |
| Opus 5.5 | Disappointed | Correct |
| GLiDE v1.2 | Disappointed | Correct |
| Decider v1.1 | Disappointed | Correct |
| Jev | Disappointed | Correct |
| Microsoft Decision-1 | Disappointed | Correct |
| Clef | Disappointed | Correct |
| Luna Decisions | Disappointed | Correct |
| Clef Flash | Disappointed | Correct |
| Strands Decider | Disappointed | Correct |
| GLiNER2.5 Decide | Disappointed | Correct |
| Laya | Embarrassed | Incorrect |
| CalDec v1 | Disappointed | Correct |

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
    "record": "15",
    "kind": "source_file_record"
  },
  "source_revision": "4f491f0784ed31ef93a8837615fbc48f885cf78d",
  "input_hash": "3ef47cf4e828dc568bf0c961e718505b1da9d1bc8a846fbeaf0561bb38e9aed3"
}
```

</details>
