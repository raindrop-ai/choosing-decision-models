# Uncertainty monitoring · question 58

[Back to Uncertainty monitoring](README.md) · [All capabilities](../README.md)

**Question ID:** `selfaware/78e32e9988edd5bb8db5`  
**Source:** [SelfAware](https://github.com/yinzhangyue/SelfAware)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/uncertainty-monitoring/selfaware-78e32e9988edd5bb8db5/README.md)

## Context

> Would you rather have to wear a bib every time you go out to eat or drink from a sippy cup every time you're at a bar?

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
  "state": "Would you rather have to wear a bib every time you go out to eat or drink from a sippy cup every time you're at a bar?",
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
| GLiDE v1.2 | Unanswerable | Correct |
| Decider v1.1 | Unanswerable | Correct |
| Jev | Unanswerable | Correct |
| Microsoft Decision-1 | Unanswerable | Correct |
| Clef | Unanswerable | Correct |
| Luna Decisions | Answerable | Incorrect |
| Clef Flash | Unanswerable | Correct |
| Strands Decider | Answerable | Incorrect |
| GLiNER2.5 Decide | Unanswerable | Correct |
| Laya | Unanswerable | Correct |
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
    "record": "2708",
    "kind": "source_file_record"
  },
  "source_revision": "f0bad1ff77bd42fc4eb2360281ed646c7bb7bd0c",
  "input_hash": "f4088f07e71336f3a8933a8a528506cf6e68712c97838dfc082d5a97e70ae742"
}
```

</details>
