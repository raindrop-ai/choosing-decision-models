# Causal reasoning · question 46

[Back to Causal reasoning](README.md) · [All capabilities](../README.md)

**Question ID:** `cladder/02a80ff23d5499cbc69b`  
**Source:** [CLadder](https://github.com/causalNLP/cladder)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/causal-reasoning/cladder-02a80ff23d5499cbc69b/README.md)

## Context

> Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Tijw has a direct effect on xevo and gyzp. Xevo has a direct effect on tijv. Tijv has a direct effect on gyzp. Tijw is unobserved.
> For those who are not xevo and are not tijv, the probability of gyzp is 70%. For those who are not xevo and are tijv, the probability of gyzp is 28%. For those who are xevo and are not tijv, the probability of gyzp is 70%. For those who are xevo and are tijv, the probability of gyzp is 29%. For those who are not xevo, the probability of tijv is 31%. For those who are xevo, the probability of tijv is 83%.

## Question

> For those who are xevo, would it be less likely to see gyzp if the individual was not xevo?

## Answer choices

- **yes:** Yes
- **no:** No

**Reference answer:** No (`no`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Tijw has a direct effect on xevo and gyzp. Xevo has a direct effect on tijv. Tijv has a direct effect on gyzp. Tijw is unobserved.\nFor those who are not xevo and are not tijv, the probability of gyzp is 70%. For those who are not xevo and are tijv, the probability of gyzp is 28%. For those who are xevo and are not tijv, the probability of gyzp is 70%. For those who are xevo and are tijv, the probability of gyzp is 29%. For those who are not xevo, the probability of tijv is 31%. For those who are xevo, the probability of tijv is 83%.",
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
| Astra | No | Correct |
| Opus 5.5 | No | Correct |
| GLiDE v1.2 | No | Correct |
| Decider v1.1 | No | Correct |
| Jev | No | Correct |
| Microsoft Decision-1 | No | Correct |
| Clef | Yes | Incorrect |
| Luna Decisions | Yes | Incorrect |
| Clef Flash | No | Correct |
| Strands Decider | No | Correct |
| GLiNER2.5 Decide | Yes | Incorrect |
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
    "record": "6600",
    "kind": "source_file_record"
  },
  "source_revision": "3d2d1169b4b939a09048a6a75956c8972a93cc38",
  "input_hash": "514377408f80c976dc1f2668c8a695ccf46a0149841e94fb96af92a955875ec2"
}
```

</details>
