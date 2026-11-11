# Causal reasoning · question 22

[Back to Causal reasoning](README.md) · [All capabilities](../README.md)

**Question ID:** `cladder/c1b53611c57eb17a4fd0`  
**Source:** [CLadder](https://github.com/causalNLP/cladder)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/causal-reasoning/cladder-c1b53611c57eb17a4fd0/README.md)

## Context

> Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Alice waking up has a direct effect on Alice arriving to school. Traffic has a direct effect on Alice arriving to school.
> We know that waking up late and heavy traffic causes arriving to school on time. We observed there is heavy traffic on the road.

## Question

> Would Alice arrives at school late if waking up late instead of waking up on time?

## Answer choices

- **yes:** Yes
- **no:** No

**Reference answer:** No (`no`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Alice waking up has a direct effect on Alice arriving to school. Traffic has a direct effect on Alice arriving to school.\nWe know that waking up late and heavy traffic causes arriving to school on time. We observed there is heavy traffic on the road.",
  "question": "Would Alice arrives at school late if waking up late instead of waking up on time?",
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
    "record": "9126",
    "kind": "source_file_record"
  },
  "source_revision": "3d2d1169b4b939a09048a6a75956c8972a93cc38",
  "input_hash": "90379dec00d769ba09bf050679011ebb86e20827995494ac3cb496d41a863235"
}
```

</details>
