# Numerical cognition · question 37

[Back to Numerical cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `cladder/2ffc9b4a2bdc38318b16`  
**Source:** [CLadder](https://github.com/causalNLP/cladder)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/numerical-cognition/cladder-2ffc9b4a2bdc38318b16/README.md)

## Context

> Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Rixq has a direct effect on zuph. Zuph has a direct effect on xevu.
> The overall probability of rixq is 81%. For those who are not rixq, the probability of xevu is 62%. For those who are rixq, the probability of xevu is 44%.

## Question

> Is xevu less likely than not xevu overall?

## Answer choices

- **yes:** Yes
- **no:** No

**Reference answer:** Yes (`yes`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Rixq has a direct effect on zuph. Zuph has a direct effect on xevu.\nThe overall probability of rixq is 81%. For those who are not rixq, the probability of xevu is 62%. For those who are rixq, the probability of xevu is 44%.",
  "question": "Is xevu less likely than not xevu overall?",
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
| Microsoft Decision-1 | No | Incorrect |
| Clef | Yes | Correct |
| Luna Decisions | Yes | Correct |
| Clef Flash | No | Incorrect |
| Strands Decider | No | Incorrect |
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
    "record": "2493",
    "kind": "source_file_record"
  },
  "source_revision": "3d2d1169b4b939a09048a6a75956c8972a93cc38",
  "input_hash": "1b8b3ebc21c98188e6d804304149a51b11b3312dcfbe334f1effb6782a4c1515"
}
```

</details>
