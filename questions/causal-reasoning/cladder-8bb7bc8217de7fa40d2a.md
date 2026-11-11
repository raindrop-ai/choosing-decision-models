# Causal reasoning · question 16

[Back to Causal reasoning](README.md) · [All capabilities](../README.md)

**Question ID:** `cladder/8bb7bc8217de7fa40d2a`  
**Source:** [CLadder](https://github.com/causalNLP/cladder)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/causal-reasoning/cladder-8bb7bc8217de7fa40d2a/README.md)

## Context

> Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Jyka has a direct effect on hwax and lirg. Gyzp has a direct effect on hwax and lirg. Hwax has a direct effect on lirg. Gyzp is unobserved.
> For those who are not jyka, the probability of lirg is 97%. For those who are jyka, the probability of lirg is 51%.

## Question

> For those who are jyka, would it be less likely to see lirg if the individual was not jyka?

## Answer choices

- **yes:** Yes
- **no:** No

**Reference answer:** No (`no`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Jyka has a direct effect on hwax and lirg. Gyzp has a direct effect on hwax and lirg. Hwax has a direct effect on lirg. Gyzp is unobserved.\nFor those who are not jyka, the probability of lirg is 97%. For those who are jyka, the probability of lirg is 51%.",
  "question": "For those who are jyka, would it be less likely to see lirg if the individual was not jyka?",
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
| Strands Decider | Yes | Incorrect |
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
    "record": "7288",
    "kind": "source_file_record"
  },
  "source_revision": "3d2d1169b4b939a09048a6a75956c8972a93cc38",
  "input_hash": "01a8af99ad4af2e51a409deabc11aea272f8fa1e3d4a0d1419301073a1f84a52"
}
```

</details>
