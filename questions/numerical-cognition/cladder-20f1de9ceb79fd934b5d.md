# Numerical cognition · question 15

[Back to Numerical cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `cladder/20f1de9ceb79fd934b5d`  
**Source:** [CLadder](https://github.com/causalNLP/cladder)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/numerical-cognition/cladder-20f1de9ceb79fd934b5d/README.md)

## Context

> Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Zuph has a direct effect on jyka and glimx. Jyka has a direct effect on glimx.
> The overall probability of zuph is 26%. For those who are not zuph, the probability of glimx is 55%. For those who are zuph, the probability of glimx is 72%.

## Question

> Is glimx more likely than not glimx overall?

## Answer choices

- **yes:** Yes
- **no:** No

**Reference answer:** Yes (`yes`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Zuph has a direct effect on jyka and glimx. Jyka has a direct effect on glimx.\nThe overall probability of zuph is 26%. For those who are not zuph, the probability of glimx is 55%. For those who are zuph, the probability of glimx is 72%.",
  "question": "Is glimx more likely than not glimx overall?",
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
| GLiNER2.5 Decide | No | Incorrect |
| Laya | Yes | Correct |
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
    "record": "5583",
    "kind": "source_file_record"
  },
  "source_revision": "3d2d1169b4b939a09048a6a75956c8972a93cc38",
  "input_hash": "078ecbb75dc05bb106d2e4d771d0e133aa396e4ae53c18482e583e4219610121"
}
```

</details>
