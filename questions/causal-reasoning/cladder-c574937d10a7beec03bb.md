# Causal reasoning · question 47

[Back to Causal reasoning](README.md) · [All capabilities](../README.md)

**Question ID:** `cladder/c574937d10a7beec03bb`  
**Source:** [CLadder](https://github.com/causalNLP/cladder)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/causal-reasoning/cladder-c574937d10a7beec03bb/README.md)

## Context

> Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Pexu has a direct effect on kraz and hwax. Hwax has a direct effect on rukz. Kraz has a direct effect on rukz.
> For those who are not pexu, the probability of rukz is 74%. For those who are pexu, the probability of rukz is 66%.

## Question

> Does pexu negatively affect rukz through hwax and kraz?

## Answer choices

- **yes:** Yes
- **no:** No

**Reference answer:** Yes (`yes`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Pexu has a direct effect on kraz and hwax. Hwax has a direct effect on rukz. Kraz has a direct effect on rukz.\nFor those who are not pexu, the probability of rukz is 74%. For those who are pexu, the probability of rukz is 66%.",
  "question": "Does pexu negatively affect rukz through hwax and kraz?",
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
| Strands Decider | Yes | Correct |
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
    "record": "8669",
    "kind": "source_file_record"
  },
  "source_revision": "3d2d1169b4b939a09048a6a75956c8972a93cc38",
  "input_hash": "722bd57014932345d9ff7bf572f00ae21abf995c2299e27047879d6d6a6eb437"
}
```

</details>
