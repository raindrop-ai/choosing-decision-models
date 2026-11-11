# Causal reasoning · question 21

[Back to Causal reasoning](README.md) · [All capabilities](../README.md)

**Question ID:** `cladder/c268eb68ed9e3d6370eb`  
**Source:** [CLadder](https://github.com/causalNLP/cladder)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/causal-reasoning/cladder-c268eb68ed9e3d6370eb/README.md)

## Context

> Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Xevo has a direct effect on tijv and gyzp. Tijv has a direct effect on gyzp.
> For those who are not xevo and are not tijv, the probability of gyzp is 75%. For those who are not xevo and are tijv, the probability of gyzp is 51%. For those who are xevo and are not tijv, the probability of gyzp is 56%. For those who are xevo and are tijv, the probability of gyzp is 21%. For those who are not xevo, the probability of tijv is 61%. For those who are xevo, the probability of tijv is 99%.

## Question

> If we disregard the mediation effect through tijv, would xevo positively affect gyzp?

## Answer choices

- **yes:** Yes
- **no:** No

**Reference answer:** No (`no`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Xevo has a direct effect on tijv and gyzp. Tijv has a direct effect on gyzp.\nFor those who are not xevo and are not tijv, the probability of gyzp is 75%. For those who are not xevo and are tijv, the probability of gyzp is 51%. For those who are xevo and are not tijv, the probability of gyzp is 56%. For those who are xevo and are tijv, the probability of gyzp is 21%. For those who are not xevo, the probability of tijv is 61%. For those who are xevo, the probability of tijv is 99%.",
  "question": "If we disregard the mediation effect through tijv, would xevo positively affect gyzp?",
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
| Strands Decider | Yes | Incorrect |
| GLiNER2.5 Decide | No | Correct |
| Laya | No | Correct |
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
    "record": "6542",
    "kind": "source_file_record"
  },
  "source_revision": "3d2d1169b4b939a09048a6a75956c8972a93cc38",
  "input_hash": "b9cde9215a965b47ced9bbdc5ef1cd89cc54bf205f8afada3490842dec43cb64"
}
```

</details>
