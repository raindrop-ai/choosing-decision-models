# Numerical cognition · question 54

[Back to Numerical cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `cladder/bb3595c6eadc9b7b7a2a`  
**Source:** [CLadder](https://github.com/causalNLP/cladder)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/numerical-cognition/cladder-bb3595c6eadc9b7b7a2a/README.md)

## Context

> Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Zuph has a direct effect on vubr and wibl. Wibl has a direct effect on uvzi. Vubr has a direct effect on uvzi.
> The overall probability of zuph is 33%. For those who are not zuph, the probability of uvzi is 47%. For those who are zuph, the probability of uvzi is 31%.

## Question

> Is uvzi more likely than not uvzi overall?

## Answer choices

- **yes:** Yes
- **no:** No

**Reference answer:** No (`no`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Zuph has a direct effect on vubr and wibl. Wibl has a direct effect on uvzi. Vubr has a direct effect on uvzi.\nThe overall probability of zuph is 33%. For those who are not zuph, the probability of uvzi is 47%. For those who are zuph, the probability of uvzi is 31%.",
  "question": "Is uvzi more likely than not uvzi overall?",
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
| Microsoft Decision-1 | Yes | Incorrect |
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
    "record": "8349",
    "kind": "source_file_record"
  },
  "source_revision": "3d2d1169b4b939a09048a6a75956c8972a93cc38",
  "input_hash": "c89294e414b34bb80462ac1102b4725d960a2cf5ca188fd29005ec15bfdb11cc"
}
```

</details>
