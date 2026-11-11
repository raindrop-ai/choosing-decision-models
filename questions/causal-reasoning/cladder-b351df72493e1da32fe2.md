# Causal reasoning · question 49

[Back to Causal reasoning](README.md) · [All capabilities](../README.md)

**Question ID:** `cladder/b351df72493e1da32fe2`  
**Source:** [CLadder](https://github.com/causalNLP/cladder)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/causal-reasoning/cladder-b351df72493e1da32fe2/README.md)

## Context

> Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Gender has a direct effect on department competitiveness and admission status. Residency status has a direct effect on department competitiveness and admission status. Department competitiveness has a direct effect on admission status. Residency status is unobserved.
> For individuals who are not male, the probability of admission acceptance is 63%. For individuals who are male, the probability of admission acceptance is 55%.

## Question

> Will male gender increase the chance of admission acceptance?

## Answer choices

- **yes:** Yes
- **no:** No

**Reference answer:** No (`no`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Gender has a direct effect on department competitiveness and admission status. Residency status has a direct effect on department competitiveness and admission status. Department competitiveness has a direct effect on admission status. Residency status is unobserved.\nFor individuals who are not male, the probability of admission acceptance is 63%. For individuals who are male, the probability of admission acceptance is 55%.",
  "question": "Will male gender increase the chance of admission acceptance?",
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
    "record": "299",
    "kind": "source_file_record"
  },
  "source_revision": "3d2d1169b4b939a09048a6a75956c8972a93cc38",
  "input_hash": "c3aa439f7a5ed95b835c3e6d4c8c4bd6367186a3f64ccd40f7b6eb72f5c4dc36"
}
```

</details>
