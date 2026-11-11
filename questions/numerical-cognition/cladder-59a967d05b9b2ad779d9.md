# Numerical cognition · question 9

[Back to Numerical cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `cladder/59a967d05b9b2ad779d9`  
**Source:** [CLadder](https://github.com/causalNLP/cladder)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/numerical-cognition/cladder-59a967d05b9b2ad779d9/README.md)

## Context

> Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Tanning salon treatment has a direct effect on black hair. Going to the beach has a direct effect on black hair.
> The overall probability of tanning salon treatment is 85%. The probability of no tanning salon treatment and black hair is 11%. The probability of tanning salon treatment and black hair is 30%.

## Question

> Is the chance of black hair larger when observing tanning salon treatment?

## Answer choices

- **yes:** Yes
- **no:** No

**Reference answer:** No (`no`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Tanning salon treatment has a direct effect on black hair. Going to the beach has a direct effect on black hair.\nThe overall probability of tanning salon treatment is 85%. The probability of no tanning salon treatment and black hair is 11%. The probability of tanning salon treatment and black hair is 30%.",
  "question": "Is the chance of black hair larger when observing tanning salon treatment?",
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
| Decider v1.1 | Yes | Incorrect |
| Jev | No | Correct |
| Microsoft Decision-1 | Yes | Incorrect |
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
    "record": "1965",
    "kind": "source_file_record"
  },
  "source_revision": "3d2d1169b4b939a09048a6a75956c8972a93cc38",
  "input_hash": "717057074cd86c7ec8c0904a6af1b9e1dfd4053324f33a8b76a6ca8057f9435d"
}
```

</details>
