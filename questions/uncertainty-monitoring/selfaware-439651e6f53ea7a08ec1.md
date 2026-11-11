# Uncertainty monitoring · question 14

[Back to Uncertainty monitoring](README.md) · [All capabilities](../README.md)

**Question ID:** `selfaware/439651e6f53ea7a08ec1`  
**Source:** [SelfAware](https://github.com/yinzhangyue/SelfAware)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/uncertainty-monitoring/selfaware-439651e6f53ea7a08ec1/README.md)

## Context

> Nancy's old washing machine could only wash 9 pieces of clothing at a time. If she had to wash 19 shirts and 8 sweaters how long would she have to do?

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
  "state": "Nancy's old washing machine could only wash 9 pieces of clothing at a time. If she had to wash 19 shirts and 8 sweaters how long would she have to do?",
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
| Decider v1.1 | Answerable | Incorrect |
| Jev | Unanswerable | Correct |
| Microsoft Decision-1 | Unanswerable | Correct |
| Clef | Unanswerable | Correct |
| Luna Decisions | Unanswerable | Correct |
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
    "record": "2624",
    "kind": "source_file_record"
  },
  "source_revision": "f0bad1ff77bd42fc4eb2360281ed646c7bb7bd0c",
  "input_hash": "d5af64c6b651e1bb3867b1baf772d3d320074dc72b2434f30daafb971635b562"
}
```

</details>
