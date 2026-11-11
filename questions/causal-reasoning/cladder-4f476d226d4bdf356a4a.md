# Causal reasoning · question 39

[Back to Causal reasoning](README.md) · [All capabilities](../README.md)

**Question ID:** `cladder/4f476d226d4bdf356a4a`  
**Source:** [CLadder](https://github.com/causalNLP/cladder)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/causal-reasoning/cladder-4f476d226d4bdf356a4a/README.md)

## Context

> Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Rixq has a direct effect on zuph and xevu. Swoy has a direct effect on zuph and xevu. Zuph has a direct effect on xevu. Swoy is unobserved.
> For those who are not rixq, the probability of xevu is 71%. For those who are rixq, the probability of xevu is 47%.

## Question

> For those who are rixq, would it be less likely to see xevu if the individual was not rixq?

## Answer choices

- **yes:** Yes
- **no:** No

**Reference answer:** No (`no`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Rixq has a direct effect on zuph and xevu. Swoy has a direct effect on zuph and xevu. Zuph has a direct effect on xevu. Swoy is unobserved.\nFor those who are not rixq, the probability of xevu is 71%. For those who are rixq, the probability of xevu is 47%.",
  "question": "For those who are rixq, would it be less likely to see xevu if the individual was not rixq?",
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
    "record": "2721",
    "kind": "source_file_record"
  },
  "source_revision": "3d2d1169b4b939a09048a6a75956c8972a93cc38",
  "input_hash": "c508796856ae643bf95d8a8f94c1cc71b989ca13dcae81ab056ce86017a7711e"
}
```

</details>
