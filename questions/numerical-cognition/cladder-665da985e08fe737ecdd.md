# Numerical cognition · question 52

[Back to Numerical cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `cladder/665da985e08fe737ecdd`  
**Source:** [CLadder](https://github.com/causalNLP/cladder)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/numerical-cognition/cladder-665da985e08fe737ecdd/README.md)

## Context

> Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Zuph has a direct effect on wibl and uvzi. Vubr has a direct effect on wibl and uvzi. Wibl has a direct effect on uvzi. Vubr is unobserved.
> The overall probability of zuph is 56%. For those who are not zuph, the probability of uvzi is 26%. For those who are zuph, the probability of uvzi is 46%.

## Question

> Is uvzi less likely than not uvzi overall?

## Answer choices

- **yes:** Yes
- **no:** No

**Reference answer:** Yes (`yes`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Zuph has a direct effect on wibl and uvzi. Vubr has a direct effect on wibl and uvzi. Wibl has a direct effect on uvzi. Vubr is unobserved.\nThe overall probability of zuph is 56%. For those who are not zuph, the probability of uvzi is 26%. For those who are zuph, the probability of uvzi is 46%.",
  "question": "Is uvzi less likely than not uvzi overall?",
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
| Luna Decisions | No | Incorrect |
| Clef Flash | Yes | Correct |
| Strands Decider | No | Incorrect |
| GLiNER2.5 Decide | No | Incorrect |
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
    "record": "8289",
    "kind": "source_file_record"
  },
  "source_revision": "3d2d1169b4b939a09048a6a75956c8972a93cc38",
  "input_hash": "3f49446ca799a2c323f827036950c2542fa0017c03de05bbf70d9185f3cd1127"
}
```

</details>
