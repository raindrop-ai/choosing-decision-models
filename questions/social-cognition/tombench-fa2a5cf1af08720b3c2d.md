# Social cognition · question 10

[Back to Social cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `tombench/fa2a5cf1af08720b3c2d`  
**Source:** [ToMBench](https://github.com/zhchen18/ToMBench)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/social-cognition/tombench-fa2a5cf1af08720b3c2d/README.md)

## Context

> Xinxin, Jiayi, and Qiaoqiao are in a group, preparing for the end-of-term project meeting. Qiaoqiao chats with other classmates on the side, while Xinxin and Jiayi dedicate themselves to this project. Seeing Jiayi completes a task, Xinxin gives Jiayi an appreciative smile, then gently points at Qiaoqiao who is chatting, and then looks at Jiayi with her eyes. After smiling at Jiayi, Xinxin's face suddenly becomes serious. Qiaoqiao sees Xinxin's pointing and the change in her face.

## Question

> Why does Xinxin's face become serious after looking at Qiaoqiao?

## Answer choices

- **A:** Xinxin shows her appreciation for Jiayi in front of Qiaoqiao to stimulate Qiaoqiao&#x27;s envy.
- **B:** Xinxin is dissatisfied with Qiaoqiao not participating in the project work.
- **C:** Xinxin sees Qiaoqiao chatting and thinks their topic is stupid.
- **D:** Xinxin wants Jiayi to join her in blaming Qiaoqiao who does not work.

**Reference answer:** Xinxin is dissatisfied with Qiaoqiao not participating in the project work. (`B`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Xinxin, Jiayi, and Qiaoqiao are in a group, preparing for the end-of-term project meeting. Qiaoqiao chats with other classmates on the side, while Xinxin and Jiayi dedicate themselves to this project. Seeing Jiayi completes a task, Xinxin gives Jiayi an appreciative smile, then gently points at Qiaoqiao who is chatting, and then looks at Jiayi with her eyes. After smiling at Jiayi, Xinxin's face suddenly becomes serious. Qiaoqiao sees Xinxin's pointing and the change in her face.",
  "question": "Why does Xinxin's face become serious after looking at Qiaoqiao?",
  "choices": {
    "A": "Xinxin shows her appreciation for Jiayi in front of Qiaoqiao to stimulate Qiaoqiao's envy.",
    "B": "Xinxin is dissatisfied with Qiaoqiao not participating in the project work.",
    "C": "Xinxin sees Qiaoqiao chatting and thinks their topic is stupid.",
    "D": "Xinxin wants Jiayi to join her in blaming Qiaoqiao who does not work."
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | Xinxin is dissatisfied with Qiaoqiao not participating in the project work. | Correct |
| Opus 5.5 | Xinxin is dissatisfied with Qiaoqiao not participating in the project work. | Correct |
| GLiDE v1.2 | Xinxin is dissatisfied with Qiaoqiao not participating in the project work. | Correct |
| Decider v1.1 | Xinxin is dissatisfied with Qiaoqiao not participating in the project work. | Correct |
| Jev | Xinxin is dissatisfied with Qiaoqiao not participating in the project work. | Correct |
| Microsoft Decision-1 | Xinxin is dissatisfied with Qiaoqiao not participating in the project work. | Correct |
| Clef | Xinxin is dissatisfied with Qiaoqiao not participating in the project work. | Correct |
| Luna Decisions | Xinxin is dissatisfied with Qiaoqiao not participating in the project work. | Correct |
| Clef Flash | Xinxin is dissatisfied with Qiaoqiao not participating in the project work. | Correct |
| Strands Decider | Xinxin is dissatisfied with Qiaoqiao not participating in the project work. | Correct |
| GLiNER2.5 Decide | Xinxin shows her appreciation for Jiayi in front of Qiaoqiao to stimulate Qiaoqiao&#x27;s envy. | Incorrect |
| Laya | Xinxin is dissatisfied with Qiaoqiao not participating in the project work. | Correct |
| CalDec v1 | Xinxin shows her appreciation for Jiayi in front of Qiaoqiao to stimulate Qiaoqiao&#x27;s envy. | Incorrect |

## Source and sharing

Attribution: Zhuang Chen et al.; ToMBench authors.  
Terms: **[MIT](https://opensource.org/license/mit)**. [Source sharing decision](../../docs/data-sharing.md).  
The capability assignment and choice-format normalization are part of this experiment. Source data retain their own terms.

<details>
<summary>Exact source locator and input fingerprint</summary>

```json
{
  "source_locator": {
    "path": "data/Ambiguous Story Task.jsonl",
    "record": "94",
    "kind": "source_file_record"
  },
  "source_revision": "4f491f0784ed31ef93a8837615fbc48f885cf78d",
  "input_hash": "9c412f1f578283a2a26131ac9f6eea6fd647b4beaed59a3dc2b6c382d862679e"
}
```

</details>
