# Numerical cognition · question 20

[Back to Numerical cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `cladder/74ac992b64fdf90e980b`  
**Source:** [CLadder](https://github.com/causalNLP/cladder)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/numerical-cognition/cladder-74ac992b64fdf90e980b/README.md)

## Context

> Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Yupt has a direct effect on jyka and kwox. Jyka has a direct effect on kwox.
> The overall probability of jyka is 40%. The probability of not jyka and kwox is 50%. The probability of jyka and kwox is 7%.

## Question

> Is the chance of kwox larger when observing jyka?

## Answer choices

- **yes:** Yes
- **no:** No

**Reference answer:** No (`no`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Yupt has a direct effect on jyka and kwox. Jyka has a direct effect on kwox.\nThe overall probability of jyka is 40%. The probability of not jyka and kwox is 50%. The probability of jyka and kwox is 7%.",
  "question": "Is the chance of kwox larger when observing jyka?",
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
| Luna Decisions | Yes | Incorrect |
| Clef Flash | No | Correct |
| Strands Decider | Yes | Incorrect |
| GLiNER2.5 Decide | No | Correct |
| Laya | Yes | Incorrect |
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
    "record": "7500",
    "kind": "source_file_record"
  },
  "source_revision": "3d2d1169b4b939a09048a6a75956c8972a93cc38",
  "input_hash": "ffe13f963ed80512166ade23d72ac302f449ee9129b4060a33a513c8a3090429"
}
```

</details>
