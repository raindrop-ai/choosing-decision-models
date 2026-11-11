# Uncertainty monitoring · question 26

[Back to Uncertainty monitoring](README.md) · [All capabilities](../README.md)

**Question ID:** `selfaware/29334c1ca9df70f176dd`  
**Source:** [SelfAware](https://github.com/yinzhangyue/SelfAware)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/uncertainty-monitoring/selfaware-29334c1ca9df70f176dd/README.md)

## Context

> "Billy Blaze, an 8-year-old genius who constructed a spaceship in his backyard from old soup cans and other household objects called ""The Bean-with-Bacon Megarocket"" puts on his brother's football helmet and becomes what character in a video game series?"

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
  "state": "\"Billy Blaze, an 8-year-old genius who constructed a spaceship in his backyard from old soup cans and other household objects called \"\"The Bean-with-Bacon Megarocket\"\" puts on his brother's football helmet and becomes what character in a video game series?\"",
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
| GLiDE v1.2 | Unanswerable | Incorrect |
| Decider v1.1 | Unanswerable | Incorrect |
| Jev | Answerable | Correct |
| Microsoft Decision-1 | Answerable | Correct |
| Clef | Answerable | Correct |
| Luna Decisions | Answerable | Correct |
| Clef Flash | Answerable | Correct |
| Strands Decider | Unanswerable | Incorrect |
| GLiNER2.5 Decide | Answerable | Correct |
| Laya | Answerable | Correct |
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
    "record": "841",
    "kind": "source_file_record"
  },
  "source_revision": "f0bad1ff77bd42fc4eb2360281ed646c7bb7bd0c",
  "input_hash": "a96e527e1d1c9148624509fee48e19bfb56afa066fdae195f66ea2b9438bbdb2"
}
```

</details>
