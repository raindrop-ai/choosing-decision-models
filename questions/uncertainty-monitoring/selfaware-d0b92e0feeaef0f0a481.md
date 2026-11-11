# Uncertainty monitoring · question 46

[Back to Uncertainty monitoring](README.md) · [All capabilities](../README.md)

**Question ID:** `selfaware/d0b92e0feeaef0f0a481`  
**Source:** [SelfAware](https://github.com/yinzhangyue/SelfAware)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/uncertainty-monitoring/selfaware-d0b92e0feeaef0f0a481/README.md)

## Context

> Is a turtle homeless or naked, without a shell?

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
  "state": "Is a turtle homeless or naked, without a shell?",
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
| Jev | Answerable | Incorrect |
| Microsoft Decision-1 | Answerable | Incorrect |
| Clef | Answerable | Incorrect |
| Luna Decisions | Answerable | Incorrect |
| Clef Flash | Answerable | Incorrect |
| Strands Decider | Unanswerable | Correct |
| GLiNER2.5 Decide | Unanswerable | Correct |
| Laya | Unanswerable | Correct |
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
    "record": "2491",
    "kind": "source_file_record"
  },
  "source_revision": "f0bad1ff77bd42fc4eb2360281ed646c7bb7bd0c",
  "input_hash": "0b0ba6ed9b3e92b097e3491c553308f27ad7e7e57c031bc8263efc2884ecb0c7"
}
```

</details>
