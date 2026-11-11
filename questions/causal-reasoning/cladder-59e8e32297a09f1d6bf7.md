# Causal reasoning · question 50

[Back to Causal reasoning](README.md) · [All capabilities](../README.md)

**Question ID:** `cladder/59e8e32297a09f1d6bf7`  
**Source:** [CLadder](https://github.com/causalNLP/cladder)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/causal-reasoning/cladder-59e8e32297a09f1d6bf7/README.md)

## Context

> Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Yomx has a direct effect on gwet. Xevu has a direct effect on gwet.
> For those who are gwet, the correlation between yomx and xevu is 0.10.

## Question

> If we look at those who are gwet, does it mean that yomx affects xevu?

## Answer choices

- **yes:** Yes
- **no:** No

**Reference answer:** No (`no`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Yomx has a direct effect on gwet. Xevu has a direct effect on gwet.\nFor those who are gwet, the correlation between yomx and xevu is 0.10.",
  "question": "If we look at those who are gwet, does it mean that yomx affects xevu?",
  "choices": {
    "yes": "Yes",
    "no": "No"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | No | Correct |
| Opus 5.5 | No | Correct |
| GLiDE v1.2 | No | Correct |
| Decider v1.1 | No | Correct |
| Jev | No | Correct |
| Microsoft Decision-1 | No | Correct |
| Clef | No | Correct |
| Luna Decisions | No | Correct |
| Clef Flash | No | Correct |
| Strands Decider | No | Correct |
| GLiNER2.5 Decide | Yes | Incorrect |
| Laya | No | Correct |
| CalDec v1 | No | Correct |

## Source and sharing

Attribution: CLadder original creators; see source.  
Terms: **[MIT](https://opensource.org/license/mit)**. [Source sharing decision](../../docs/data-sharing.md).  
The capability assignment and choice-format normalization are part of this experiment. Source data retain their own terms.

<details>
<summary>Exact source locator and input fingerprint</summary>

```json
{
  "source_locator": {
    "path": "data/cladder-v1-questions.json",
    "record": "3538",
    "kind": "source_file_record"
  },
  "source_revision": "3d2d1169b4b939a09048a6a75956c8972a93cc38",
  "input_hash": "fbd669813a5f4227bd50642ffd256262fe220af50366d7f21e0cbf54ae3eaa3c"
}
```

</details>
