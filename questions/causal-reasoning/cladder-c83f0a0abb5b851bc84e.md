# Causal reasoning · question 41

[Back to Causal reasoning](README.md) · [All capabilities](../README.md)

**Question ID:** `cladder/c83f0a0abb5b851bc84e`  
**Source:** [CLadder](https://github.com/causalNLP/cladder)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/causal-reasoning/cladder-c83f0a0abb5b851bc84e/README.md)

## Context

> Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Smoking has a direct effect on effort and lactose intolerance. Effort has a direct effect on lactose intolerance.
> For nonsmokers and are lazy, the probability of being lactose intolerant is 47%. For nonsmokers and are hard-working, the probability of being lactose intolerant is 88%. For smokers and are lazy, the probability of being lactose intolerant is 23%. For smokers and are hard-working, the probability of being lactose intolerant is 54%. For nonsmokers, the probability of being hard-working is 40%. For smokers, the probability of being hard-working is 61%.

## Question

> Does smoking positively affect lactose intolerance through effort?

## Answer choices

- **yes:** Yes
- **no:** No

**Reference answer:** Yes (`yes`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Smoking has a direct effect on effort and lactose intolerance. Effort has a direct effect on lactose intolerance.\nFor nonsmokers and are lazy, the probability of being lactose intolerant is 47%. For nonsmokers and are hard-working, the probability of being lactose intolerant is 88%. For smokers and are lazy, the probability of being lactose intolerant is 23%. For smokers and are hard-working, the probability of being lactose intolerant is 54%. For nonsmokers, the probability of being hard-working is 40%. For smokers, the probability of being hard-working is 61%.",
  "question": "Does smoking positively affect lactose intolerance through effort?",
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
| Microsoft Decision-1 | No | Incorrect |
| Clef | No | Incorrect |
| Luna Decisions | No | Incorrect |
| Clef Flash | Yes | Correct |
| Strands Decider | Yes | Correct |
| GLiNER2.5 Decide | Yes | Correct |
| Laya | No | Incorrect |
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
    "record": "1640",
    "kind": "source_file_record"
  },
  "source_revision": "3d2d1169b4b939a09048a6a75956c8972a93cc38",
  "input_hash": "1046ce659f0781aaf2b5e65e26ae45d8db1ee8e34cd948daf1b4d5f8aa4cef43"
}
```

</details>
