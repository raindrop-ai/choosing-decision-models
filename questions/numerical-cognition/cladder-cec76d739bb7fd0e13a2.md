# Numerical cognition · question 25

[Back to Numerical cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `cladder/cec76d739bb7fd0e13a2`  
**Source:** [CLadder](https://github.com/causalNLP/cladder)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/numerical-cognition/cladder-cec76d739bb7fd0e13a2/README.md)

## Context

> Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Hwax has a direct effect on pexu and rukz. Pexu has a direct effect on rukz.
> The overall probability of pexu is 9%. For those who are not pexu, the probability of rukz is 79%. For those who are pexu, the probability of rukz is 56%.

## Question

> Is rukz less likely than not rukz overall?

## Answer choices

- **yes:** Yes
- **no:** No

**Reference answer:** No (`no`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Hwax has a direct effect on pexu and rukz. Pexu has a direct effect on rukz.\nThe overall probability of pexu is 9%. For those who are not pexu, the probability of rukz is 79%. For those who are pexu, the probability of rukz is 56%.",
  "question": "Is rukz less likely than not rukz overall?",
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
| Strands Decider | No | Correct |
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
    "record": "8505",
    "kind": "source_file_record"
  },
  "source_revision": "3d2d1169b4b939a09048a6a75956c8972a93cc38",
  "input_hash": "6d624d073977396c49a9ee759a0947b5fa973b5ec4b57d899881b61daa5fa7e7"
}
```

</details>
