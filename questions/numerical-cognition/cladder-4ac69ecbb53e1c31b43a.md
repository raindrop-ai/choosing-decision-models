# Numerical cognition · question 56

[Back to Numerical cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `cladder/4ac69ecbb53e1c31b43a`  
**Source:** [CLadder](https://github.com/causalNLP/cladder)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/numerical-cognition/cladder-4ac69ecbb53e1c31b43a/README.md)

## Context

> Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Jyka has a direct effect on yupt. Kwox has a direct effect on yupt.
> The overall probability of jyka is 77%. For those who are not jyka, the probability of kwox is 67%. For those who are jyka, the probability of kwox is 67%.

## Question

> Is kwox less likely than not kwox overall?

## Answer choices

- **yes:** Yes
- **no:** No

**Reference answer:** No (`no`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Jyka has a direct effect on yupt. Kwox has a direct effect on yupt.\nThe overall probability of jyka is 77%. For those who are not jyka, the probability of kwox is 67%. For those who are jyka, the probability of kwox is 67%.",
  "question": "Is kwox less likely than not kwox overall?",
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
| GLiNER2.5 Decide | No | Correct |
| Laya | No | Correct |
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
    "record": "7470",
    "kind": "source_file_record"
  },
  "source_revision": "3d2d1169b4b939a09048a6a75956c8972a93cc38",
  "input_hash": "506a9dab399482564045ebac9b2db532dccd82e3cca352ff936a971a8b2d1b37"
}
```

</details>
