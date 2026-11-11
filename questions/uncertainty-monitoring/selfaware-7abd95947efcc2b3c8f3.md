# Uncertainty monitoring · question 20

[Back to Uncertainty monitoring](README.md) · [All capabilities](../README.md)

**Question ID:** `selfaware/7abd95947efcc2b3c8f3`  
**Source:** [SelfAware](https://github.com/yinzhangyue/SelfAware)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/uncertainty-monitoring/selfaware-7abd95947efcc2b3c8f3/README.md)

## Context

> How much money is there in the world?

## Question

> Does this question have a determinate answer?

## Answer choices

- **yes:** Answerable
- **no:** Unanswerable

**Reference answer:** Unanswerable (`no`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "How much money is there in the world?",
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
| Astra | Unanswerable | Correct |
| Opus 5.5 | Unanswerable | Correct |
| GLiDE v1.2 | Answerable | Incorrect |
| Decider v1.1 | Answerable | Incorrect |
| Jev | Unanswerable | Correct |
| Microsoft Decision-1 | Answerable | Incorrect |
| Clef | Answerable | Incorrect |
| Luna Decisions | Unanswerable | Correct |
| Clef Flash | Unanswerable | Correct |
| Strands Decider | Unanswerable | Correct |
| GLiNER2.5 Decide | Unanswerable | Correct |
| Laya | Answerable | Incorrect |
| CalDec v1 | Unanswerable | Correct |

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
    "record": "2504",
    "kind": "source_file_record"
  },
  "source_revision": "f0bad1ff77bd42fc4eb2360281ed646c7bb7bd0c",
  "input_hash": "c8584895bde728850eb107fd46066267b2a01d70471de69864881e56b21b8c0c"
}
```

</details>
