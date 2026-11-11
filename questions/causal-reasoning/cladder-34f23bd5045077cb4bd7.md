# Causal reasoning · question 61

[Back to Causal reasoning](README.md) · [All capabilities](../README.md)

**Question ID:** `cladder/34f23bd5045077cb4bd7`  
**Source:** [CLadder](https://github.com/causalNLP/cladder)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/causal-reasoning/cladder-34f23bd5045077cb4bd7/README.md)

## Context

> Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Zuph has a direct effect on jyka and glimx. Zory has a direct effect on jyka and glimx. Jyka has a direct effect on glimx. Zory is unobserved.
> We know that zuph or zory causes jyka. zuph and zory and jyka causes glimx. We observed an individual is not zory.

## Question

> Would an individual is not glimx if not zuph instead of zuph?

## Answer choices

- **yes:** Yes
- **no:** No

**Reference answer:** Yes (`yes`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Zuph has a direct effect on jyka and glimx. Zory has a direct effect on jyka and glimx. Jyka has a direct effect on glimx. Zory is unobserved.\nWe know that zuph or zory causes jyka. zuph and zory and jyka causes glimx. We observed an individual is not zory.",
  "question": "Would an individual is not glimx if not zuph instead of zuph?",
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
    "record": "10517",
    "kind": "source_file_record"
  },
  "source_revision": "3d2d1169b4b939a09048a6a75956c8972a93cc38",
  "input_hash": "4cdbcd16aa3d593ca57e69d6dd2fa528ed11cc5da338a03c75250a0b87233013"
}
```

</details>
