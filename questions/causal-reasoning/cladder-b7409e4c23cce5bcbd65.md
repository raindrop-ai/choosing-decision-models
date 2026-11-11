# Causal reasoning · question 64

[Back to Causal reasoning](README.md) · [All capabilities](../README.md)

**Question ID:** `cladder/b7409e4c23cce5bcbd65`  
**Source:** [CLadder](https://github.com/causalNLP/cladder)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/causal-reasoning/cladder-b7409e4c23cce5bcbd65/README.md)

## Context

> Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Pexu has a direct effect on hwax. Hwax has a direct effect on rukz.
> For those who are not pexu, the probability of rukz is 52%. For those who are pexu, the probability of rukz is 52%.

## Question

> Does pexu positively affect rukz through hwax?

## Answer choices

- **yes:** Yes
- **no:** No

**Reference answer:** No (`no`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Pexu has a direct effect on hwax. Hwax has a direct effect on rukz.\nFor those who are not pexu, the probability of rukz is 52%. For those who are pexu, the probability of rukz is 52%.",
  "question": "Does pexu positively affect rukz through hwax?",
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
| Strands Decider | Yes | Incorrect |
| GLiNER2.5 Decide | Yes | Incorrect |
| Laya | Yes | Incorrect |
| CalDec v1 | Yes | Incorrect |

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
    "record": "8429",
    "kind": "source_file_record"
  },
  "source_revision": "3d2d1169b4b939a09048a6a75956c8972a93cc38",
  "input_hash": "288a73e9ceb6723240ad4993e999984632baa73689dfb10fa8480e9a4218deba"
}
```

</details>
