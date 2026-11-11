# Causal reasoning · question 14

[Back to Causal reasoning](README.md) · [All capabilities](../README.md)

**Question ID:** `cladder/81555bf547b2ea6266cb`  
**Source:** [CLadder](https://github.com/causalNLP/cladder)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/causal-reasoning/cladder-81555bf547b2ea6266cb/README.md)

## Context

> Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Yomx has a direct effect on gwet and xevu. Gwet has a direct effect on xevu.
> For those who are not yomx and are not gwet, the probability of xevu is 75%. For those who are not yomx and are gwet, the probability of xevu is 88%. For those who are yomx and are not gwet, the probability of xevu is 59%. For those who are yomx and are gwet, the probability of xevu is 87%. For those who are not yomx, the probability of gwet is 8%. For those who are yomx, the probability of gwet is 88%.

## Question

> Does yomx positively affect xevu through gwet?

## Answer choices

- **yes:** Yes
- **no:** No

**Reference answer:** Yes (`yes`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Yomx has a direct effect on gwet and xevu. Gwet has a direct effect on xevu.\nFor those who are not yomx and are not gwet, the probability of xevu is 75%. For those who are not yomx and are gwet, the probability of xevu is 88%. For those who are yomx and are not gwet, the probability of xevu is 59%. For those who are yomx and are gwet, the probability of xevu is 87%. For those who are not yomx, the probability of gwet is 8%. For those who are yomx, the probability of gwet is 88%.",
  "question": "Does yomx positively affect xevu through gwet?",
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
| Astra | Yes | Correct |
| Opus 5.5 | Yes | Correct |
| GLiDE v1.2 | Yes | Correct |
| Decider v1.1 | Yes | Correct |
| Jev | Yes | Correct |
| Microsoft Decision-1 | Yes | Correct |
| Clef | Yes | Correct |
| Luna Decisions | Yes | Correct |
| Clef Flash | Yes | Correct |
| Strands Decider | Yes | Correct |
| GLiNER2.5 Decide | Yes | Correct |
| Laya | No | Incorrect |
| CalDec v1 | No | Incorrect |

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
    "record": "6853",
    "kind": "source_file_record"
  },
  "source_revision": "3d2d1169b4b939a09048a6a75956c8972a93cc38",
  "input_hash": "15fc7381ef61a7e8df30a354484133746d83dcce2289f11f6d37afa6a4e61825"
}
```

</details>
