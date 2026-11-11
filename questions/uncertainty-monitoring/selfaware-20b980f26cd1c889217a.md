# Uncertainty monitoring · question 64

[Back to Uncertainty monitoring](README.md) · [All capabilities](../README.md)

**Question ID:** `selfaware/20b980f26cd1c889217a`  
**Source:** [SelfAware](https://github.com/yinzhangyue/SelfAware)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/uncertainty-monitoring/selfaware-20b980f26cd1c889217a/README.md)

## Context

> Who invented the art of milking a cow?

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
  "state": "Who invented the art of milking a cow?",
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
| Luna Decisions | Unanswerable | Correct |
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
    "record": "2999",
    "kind": "source_file_record"
  },
  "source_revision": "f0bad1ff77bd42fc4eb2360281ed646c7bb7bd0c",
  "input_hash": "9f2f7bd4b6d4a2d064c593e91ae548de2a561d2af5b7f2fc300aad39e746100b"
}
```

</details>
