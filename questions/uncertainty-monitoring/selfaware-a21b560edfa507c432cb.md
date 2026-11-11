# Uncertainty monitoring · question 1

[Back to Uncertainty monitoring](README.md) · [All capabilities](../README.md)

**Question ID:** `selfaware/a21b560edfa507c432cb`  
**Source:** [SelfAware](https://github.com/yinzhangyue/SelfAware)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/uncertainty-monitoring/selfaware-a21b560edfa507c432cb/README.md)

## Context

> If revenge is a dish that’s best served cold, and revenge is sweet, then is revenge ice cream?

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
  "state": "If revenge is a dish that’s best served cold, and revenge is sweet, then is revenge ice cream?",
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
| Astra | Answerable | Incorrect |
| Opus 5.5 | Unanswerable | Correct |
| GLiDE v1.2 | Answerable | Incorrect |
| Decider v1.1 | Answerable | Incorrect |
| Jev | Unanswerable | Correct |
| Microsoft Decision-1 | Unanswerable | Correct |
| Clef | Unanswerable | Correct |
| Luna Decisions | Answerable | Incorrect |
| Clef Flash | Unanswerable | Correct |
| Strands Decider | Unanswerable | Correct |
| GLiNER2.5 Decide | Unanswerable | Correct |
| Laya | Answerable | Incorrect |
| CalDec v1 | Answerable | Incorrect |

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
    "record": "2681",
    "kind": "source_file_record"
  },
  "source_revision": "f0bad1ff77bd42fc4eb2360281ed646c7bb7bd0c",
  "input_hash": "3e48bf988b0a10b33cdf376ecc02469356305d3b6dca8d75674b7c67bfb0cdf5"
}
```

</details>
