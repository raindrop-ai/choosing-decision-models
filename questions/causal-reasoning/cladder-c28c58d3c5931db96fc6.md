# Causal reasoning · question 30

[Back to Causal reasoning](README.md) · [All capabilities](../README.md)

**Question ID:** `cladder/c28c58d3c5931db96fc6`  
**Source:** [CLadder](https://github.com/causalNLP/cladder)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/causal-reasoning/cladder-c28c58d3c5931db96fc6/README.md)

## Context

> Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Full moon has a direct effect on sprinkler and weather. Weather has a direct effect on ground. Sprinkler has a direct effect on ground.
> For situations where there is no full moon, the probability of wet ground is 37%. For situations where there is a full moon, the probability of wet ground is 42%.

## Question

> Will full moon increase the chance of wet ground?

## Answer choices

- **yes:** Yes
- **no:** No

**Reference answer:** Yes (`yes`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Full moon has a direct effect on sprinkler and weather. Weather has a direct effect on ground. Sprinkler has a direct effect on ground.\nFor situations where there is no full moon, the probability of wet ground is 37%. For situations where there is a full moon, the probability of wet ground is 42%.",
  "question": "Will full moon increase the chance of wet ground?",
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
| Luna Decisions | Yes | Correct |
| Clef Flash | Yes | Correct |
| Strands Decider | Yes | Correct |
| GLiNER2.5 Decide | No | Incorrect |
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
    "record": "1304",
    "kind": "source_file_record"
  },
  "source_revision": "3d2d1169b4b939a09048a6a75956c8972a93cc38",
  "input_hash": "591c20467f337ad9417cabe72ee8f9ae0ca5c1814259f374f67535cac39bdb16"
}
```

</details>
