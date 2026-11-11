# Causal reasoning · question 23

[Back to Causal reasoning](README.md) · [All capabilities](../README.md)

**Question ID:** `cladder/dbc6a20f61f6d7d1a64a`  
**Source:** [CLadder](https://github.com/causalNLP/cladder)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/causal-reasoning/cladder-dbc6a20f61f6d7d1a64a/README.md)

## Context

> Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Swoy has a direct effect on rixq and xevu. Rixq has a direct effect on zuph. Zuph has a direct effect on xevu. Swoy is unobserved.
> For those who are not rixq, the probability of zuph is 61%. For those who are rixq, the probability of zuph is 34%. For those who are not rixq and are not zuph, the probability of xevu is 46%. For those who are not rixq and are zuph, the probability of xevu is 41%. For those who are rixq and are not zuph, the probability of xevu is 66%. For those who are rixq and are zuph, the probability of xevu is 60%. The overall probability of rixq is 48%.

## Question

> Does rixq negatively affect xevu through zuph?

## Answer choices

- **yes:** Yes
- **no:** No

**Reference answer:** No (`no`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Swoy has a direct effect on rixq and xevu. Rixq has a direct effect on zuph. Zuph has a direct effect on xevu. Swoy is unobserved.\nFor those who are not rixq, the probability of zuph is 61%. For those who are rixq, the probability of zuph is 34%. For those who are not rixq and are not zuph, the probability of xevu is 46%. For those who are not rixq and are zuph, the probability of xevu is 41%. For those who are rixq and are not zuph, the probability of xevu is 66%. For those who are rixq and are zuph, the probability of xevu is 60%. The overall probability of rixq is 48%.",
  "question": "Does rixq negatively affect xevu through zuph?",
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
| Decider v1.1 | Yes | Incorrect |
| Jev | No | Correct |
| Microsoft Decision-1 | Yes | Incorrect |
| Clef | No | Correct |
| Luna Decisions | Yes | Incorrect |
| Clef Flash | No | Correct |
| Strands Decider | Yes | Incorrect |
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
    "record": "2644",
    "kind": "source_file_record"
  },
  "source_revision": "3d2d1169b4b939a09048a6a75956c8972a93cc38",
  "input_hash": "6e8ade9794e228835e5bc9f88a3984ef0a2dc2bc27d3252bedce9bb40105bd76"
}
```

</details>
