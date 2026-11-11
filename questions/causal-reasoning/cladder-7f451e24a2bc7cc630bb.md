# Causal reasoning · question 40

[Back to Causal reasoning](README.md) · [All capabilities](../README.md)

**Question ID:** `cladder/7f451e24a2bc7cc630bb`  
**Source:** [CLadder](https://github.com/causalNLP/cladder)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/causal-reasoning/cladder-7f451e24a2bc7cc630bb/README.md)

## Context

> Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Liking spicy food has a direct effect on parents' social status and child's intelligence. Other unobserved factors has a direct effect on parents' social status and child's intelligence. Parents' social status has a direct effect on child's intelligence. Other unobserved factors is unobserved.
> We know that liking spicy food and confounder active causes high parental social status. liking spicy food or confounder active or high parental social status causes intelligent child. We observed confounder inactive.

## Question

> Would the child is intelligent if not liking spicy food instead of liking spicy food?

## Answer choices

- **yes:** Yes
- **no:** No

**Reference answer:** No (`no`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Liking spicy food has a direct effect on parents' social status and child's intelligence. Other unobserved factors has a direct effect on parents' social status and child's intelligence. Parents' social status has a direct effect on child's intelligence. Other unobserved factors is unobserved.\nWe know that liking spicy food and confounder active causes high parental social status. liking spicy food or confounder active or high parental social status causes intelligent child. We observed confounder inactive.",
  "question": "Would the child is intelligent if not liking spicy food instead of liking spicy food?",
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
| Clef | Yes | Incorrect |
| Luna Decisions | No | Correct |
| Clef Flash | No | Correct |
| Strands Decider | Yes | Incorrect |
| GLiNER2.5 Decide | Yes | Incorrect |
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
    "record": "9389",
    "kind": "source_file_record"
  },
  "source_revision": "3d2d1169b4b939a09048a6a75956c8972a93cc38",
  "input_hash": "5d204f9187f8e0fe191971d732c29cca228e8c23e41e058260c80eabe22d2a8f"
}
```

</details>
