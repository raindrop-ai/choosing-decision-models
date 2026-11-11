# Causal reasoning · question 36

[Back to Causal reasoning](README.md) · [All capabilities](../README.md)

**Question ID:** `cladder/2f42ba0ce24a35eaa5b5`  
**Source:** [CLadder](https://github.com/causalNLP/cladder)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/causal-reasoning/cladder-2f42ba0ce24a35eaa5b5/README.md)

## Context

> Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Qwiu has a direct effect on jyka and kwox. Jyka has a direct effect on yupt. Yupt has a direct effect on kwox. Qwiu is unobserved.
> For those who are not jyka, the probability of yupt is 96%. For those who are jyka, the probability of yupt is 37%. For those who are not jyka and are not yupt, the probability of kwox is 49%. For those who are not jyka and are yupt, the probability of kwox is 82%. For those who are jyka and are not yupt, the probability of kwox is 44%. For those who are jyka and are yupt, the probability of kwox is 84%. The overall probability of jyka is 32%.

## Question

> Will jyka decrease the chance of kwox?

## Answer choices

- **yes:** Yes
- **no:** No

**Reference answer:** Yes (`yes`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Qwiu has a direct effect on jyka and kwox. Jyka has a direct effect on yupt. Yupt has a direct effect on kwox. Qwiu is unobserved.\nFor those who are not jyka, the probability of yupt is 96%. For those who are jyka, the probability of yupt is 37%. For those who are not jyka and are not yupt, the probability of kwox is 49%. For those who are not jyka and are yupt, the probability of kwox is 82%. For those who are jyka and are not yupt, the probability of kwox is 44%. For those who are jyka and are yupt, the probability of kwox is 84%. The overall probability of jyka is 32%.",
  "question": "Will jyka decrease the chance of kwox?",
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
| GLiNER2.5 Decide | No | Incorrect |
| Laya | No | Incorrect |
| CalDec v1 | No | Incorrect |

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
    "record": "4289",
    "kind": "source_file_record"
  },
  "source_revision": "3d2d1169b4b939a09048a6a75956c8972a93cc38",
  "input_hash": "f960dabe94f918339c64aa8230bf2de9a68494011e547a6447339058e2410f55"
}
```

</details>
