# Causal reasoning · question 53

[Back to Causal reasoning](README.md) · [All capabilities](../README.md)

**Question ID:** `cladder/12c8d26f5c4560a727ba`  
**Source:** [CLadder](https://github.com/causalNLP/cladder)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/causal-reasoning/cladder-12c8d26f5c4560a727ba/README.md)

## Context

> Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Jyka has a direct effect on qwiu and yupt. Yupt has a direct effect on kwox. Qwiu has a direct effect on kwox.
> For those who are not jyka, the probability of kwox is 55%. For those who are jyka, the probability of kwox is 84%.

## Question

> Does jyka positively affect kwox through yupt and qwiu?

## Answer choices

- **yes:** Yes
- **no:** No

**Reference answer:** Yes (`yes`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Jyka has a direct effect on qwiu and yupt. Yupt has a direct effect on kwox. Qwiu has a direct effect on kwox.\nFor those who are not jyka, the probability of kwox is 55%. For those who are jyka, the probability of kwox is 84%.",
  "question": "Does jyka positively affect kwox through yupt and qwiu?",
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
| CalDec v1 | Yes | Correct |

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
    "record": "7673",
    "kind": "source_file_record"
  },
  "source_revision": "3d2d1169b4b939a09048a6a75956c8972a93cc38",
  "input_hash": "3c7d25ea84192f2328e4c39cc843b6844b9f3514f4a2e0f06e8120c7a6ba6ea6"
}
```

</details>
