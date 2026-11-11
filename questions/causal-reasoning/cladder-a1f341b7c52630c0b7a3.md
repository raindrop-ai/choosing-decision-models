# Causal reasoning · question 25

[Back to Causal reasoning](README.md) · [All capabilities](../README.md)

**Question ID:** `cladder/a1f341b7c52630c0b7a3`  
**Source:** [CLadder](https://github.com/causalNLP/cladder)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/causal-reasoning/cladder-a1f341b7c52630c0b7a3/README.md)

## Context

> Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Zuph has a direct effect on wibl. Wibl has a direct effect on uvzi.
> For those who are not zuph, the probability of uvzi is 70%. For those who are zuph, the probability of uvzi is 73%.

## Question

> For those who are zuph, would it be less likely to see uvzi if the individual was not zuph?

## Answer choices

- **yes:** Yes
- **no:** No

**Reference answer:** Yes (`yes`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Zuph has a direct effect on wibl. Wibl has a direct effect on uvzi.\nFor those who are not zuph, the probability of uvzi is 70%. For those who are zuph, the probability of uvzi is 73%.",
  "question": "For those who are zuph, would it be less likely to see uvzi if the individual was not zuph?",
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
| Luna Decisions | No | Incorrect |
| Clef Flash | Yes | Correct |
| Strands Decider | No | Incorrect |
| GLiNER2.5 Decide | Yes | Correct |
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
    "record": "4794",
    "kind": "source_file_record"
  },
  "source_revision": "3d2d1169b4b939a09048a6a75956c8972a93cc38",
  "input_hash": "3f46190b6e4c793328372d00f4a6e687888d7583641bd96641fa7ec57b809a48"
}
```

</details>
