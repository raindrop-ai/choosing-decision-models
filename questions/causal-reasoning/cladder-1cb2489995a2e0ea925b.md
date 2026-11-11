# Causal reasoning · question 66

[Back to Causal reasoning](README.md) · [All capabilities](../README.md)

**Question ID:** `cladder/1cb2489995a2e0ea925b`  
**Source:** [CLadder](https://github.com/causalNLP/cladder)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/causal-reasoning/cladder-1cb2489995a2e0ea925b/README.md)

## Context

> Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Tanning salon treatment has a direct effect on skin. Going to the beach has a direct effect on skin.
> For people not using tanning salon treatments, the probability of tanned skin is 6%. For people who went to tanning salons, the probability of tanned skin is 57%.

## Question

> Will tanning salon treatment decrease the chance of tanned skin?

## Answer choices

- **yes:** Yes
- **no:** No

**Reference answer:** No (`no`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Tanning salon treatment has a direct effect on skin. Going to the beach has a direct effect on skin.\nFor people not using tanning salon treatments, the probability of tanned skin is 6%. For people who went to tanning salons, the probability of tanned skin is 57%.",
  "question": "Will tanning salon treatment decrease the chance of tanned skin?",
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
    "record": "119",
    "kind": "source_file_record"
  },
  "source_revision": "3d2d1169b4b939a09048a6a75956c8972a93cc38",
  "input_hash": "a1666533d9b6ae83b76ee2925434f14b09e6f579e3b8ee9e74ae628adee56a38"
}
```

</details>
