# Uncertainty monitoring · question 22

[Back to Uncertainty monitoring](README.md) · [All capabilities](../README.md)

**Question ID:** `selfaware/38b07d3302a5fd5b77db`  
**Source:** [SelfAware](https://github.com/yinzhangyue/SelfAware)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/uncertainty-monitoring/selfaware-38b07d3302a5fd5b77db/README.md)

## Context

> At 51° 23' E, what is the easternmost point of the African continent?

## Question

> Does this question have a determinate answer?

## Answer choices

- **yes:** Answerable
- **no:** Unanswerable

**Reference answer:** Answerable (`yes`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "At 51° 23' E, what is the easternmost point of the African continent?",
  "question": "Does this question have a determinate answer?",
  "choices": {
    "yes": "Answerable",
    "no": "Unanswerable"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | Answerable | Correct |
| Opus 5.5 | Answerable | Correct |
| GLiDE v1.2 | Answerable | Correct |
| Decider v1.1 | Answerable | Correct |
| Jev | Answerable | Correct |
| Microsoft Decision-1 | Answerable | Correct |
| Clef | Answerable | Correct |
| Luna Decisions | Answerable | Correct |
| Clef Flash | Answerable | Correct |
| Strands Decider | Answerable | Correct |
| GLiNER2.5 Decide | Answerable | Correct |
| Laya | Unanswerable | Incorrect |
| CalDec v1 | Unanswerable | Incorrect |

## Source and sharing

Attribution: Zhangyue Yin, Qiushi Sun, Qipeng Guo, Jiawen Wu, Xipeng Qiu, Xuanjing Huang; SelfAware authors.  
Terms: **[CC-BY-SA-4.0](https://creativecommons.org/licenses/by-sa/4.0/)**. [Source sharing decision](../../docs/data-sharing.md).  
The capability assignment and choice-format normalization are part of this experiment. Source data retain their own terms.

<details>
<summary>Exact source locator and input fingerprint</summary>

```json
{
  "source_locator": {
    "path": "data/SelfAware.json",
    "record": "386",
    "kind": "source_file_record"
  },
  "source_revision": "f0bad1ff77bd42fc4eb2360281ed646c7bb7bd0c",
  "input_hash": "6ca55683b174ef5fc1d57a2ea74cce3840ac3130c0bbd11c01a15b9bb2808a8b"
}
```

</details>
