# Causal reasoning · question 29

[Back to Causal reasoning](README.md) · [All capabilities](../README.md)

**Question ID:** `cladder/a90b85ab6575b0fd6603`  
**Source:** [CLadder](https://github.com/causalNLP/cladder)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/causal-reasoning/cladder-a90b85ab6575b0fd6603/README.md)

## Context

> Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Kraz has a direct effect on pexu and rukz. Pexu has a direct effect on hwax. Hwax has a direct effect on rukz. Kraz is unobserved.
> For those who are not pexu, the probability of hwax is 43%. For those who are pexu, the probability of hwax is 92%. For those who are not pexu and are not hwax, the probability of rukz is 0%. For those who are not pexu and are hwax, the probability of rukz is 34%. For those who are pexu and are not hwax, the probability of rukz is 1%. For those who are pexu and are hwax, the probability of rukz is 33%. The overall probability of pexu is 17%.

## Question

> Does pexu negatively affect rukz through hwax?

## Answer choices

- **yes:** Yes
- **no:** No

**Reference answer:** No (`no`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Kraz has a direct effect on pexu and rukz. Pexu has a direct effect on hwax. Hwax has a direct effect on rukz. Kraz is unobserved.\nFor those who are not pexu, the probability of hwax is 43%. For those who are pexu, the probability of hwax is 92%. For those who are not pexu and are not hwax, the probability of rukz is 0%. For those who are not pexu and are hwax, the probability of rukz is 34%. For those who are pexu and are not hwax, the probability of rukz is 1%. For those who are pexu and are hwax, the probability of rukz is 33%. The overall probability of pexu is 17%.",
  "question": "Does pexu negatively affect rukz through hwax?",
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
| GLiNER2.5 Decide | No | Correct |
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
    "record": "8585",
    "kind": "source_file_record"
  },
  "source_revision": "3d2d1169b4b939a09048a6a75956c8972a93cc38",
  "input_hash": "ce0c63ba09d564674c2641209836ae4f8ad25f7fd801ea27f68c08fad1cd534d"
}
```

</details>
