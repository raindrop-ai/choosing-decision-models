# Causal reasoning · question 63

[Back to Causal reasoning](README.md) · [All capabilities](../README.md)

**Question ID:** `cladder/79272deaabce2ac8daa1`  
**Source:** [CLadder](https://github.com/causalNLP/cladder)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/causal-reasoning/cladder-79272deaabce2ac8daa1/README.md)

## Context

> Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Xevo has a direct effect on tijv. Tijv has a direct effect on gyzp.
> For those who are not xevo, the probability of gyzp is 43%. For those who are xevo, the probability of gyzp is 49%.

## Question

> For those who are xevo, would it be less likely to see gyzp if the individual was not xevo?

## Answer choices

- **yes:** Yes
- **no:** No

**Reference answer:** Yes (`yes`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Xevo has a direct effect on tijv. Tijv has a direct effect on gyzp.\nFor those who are not xevo, the probability of gyzp is 43%. For those who are xevo, the probability of gyzp is 49%.",
  "question": "For those who are xevo, would it be less likely to see gyzp if the individual was not xevo?",
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
    "record": "6435",
    "kind": "source_file_record"
  },
  "source_revision": "3d2d1169b4b939a09048a6a75956c8972a93cc38",
  "input_hash": "4cdbe1c6c6484068c5b7b0baaaa6e828537ca89ed79e4ea68b4f045acae811b3"
}
```

</details>
