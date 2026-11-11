# Causal reasoning · question 20

[Back to Causal reasoning](README.md) · [All capabilities](../README.md)

**Question ID:** `cladder/fed7df3f6e4f44404358`  
**Source:** [CLadder](https://github.com/causalNLP/cladder)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/causal-reasoning/cladder-fed7df3f6e4f44404358/README.md)

## Context

> Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Personality has a direct effect on relationship status. Appearance has a direct effect on relationship status.
> For people in a relationship, the correlation between kindness and attractive appearance is -0.03.

## Question

> If we look at people in a relationship, does it mean that kindness affects attractive appearance?

## Answer choices

- **yes:** Yes
- **no:** No

**Reference answer:** No (`no`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Personality has a direct effect on relationship status. Appearance has a direct effect on relationship status.\nFor people in a relationship, the correlation between kindness and attractive appearance is -0.03.",
  "question": "If we look at people in a relationship, does it mean that kindness affects attractive appearance?",
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
    "record": "350",
    "kind": "source_file_record"
  },
  "source_revision": "3d2d1169b4b939a09048a6a75956c8972a93cc38",
  "input_hash": "99e8059bb0e731229a469813bb4720b77da910f154b4f24083a43ad201dab2e1"
}
```

</details>
