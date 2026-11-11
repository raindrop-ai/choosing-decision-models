# Causal reasoning · question 27

[Back to Causal reasoning](README.md) · [All capabilities](../README.md)

**Question ID:** `cladder/38b3bb9d4f17a6fed2bf`  
**Source:** [CLadder](https://github.com/causalNLP/cladder)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/causal-reasoning/cladder-38b3bb9d4f17a6fed2bf/README.md)

## Context

> Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Wibl has a direct effect on zuph and uvzi. Zuph has a direct effect on uvzi.
> We know that wibl causes not zuph. wibl and zuph causes uvzi. We observed an individual is wibl.

## Question

> Would an individual is uvzi if zuph instead of not zuph?

## Answer choices

- **yes:** Yes
- **no:** No

**Reference answer:** Yes (`yes`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Wibl has a direct effect on zuph and uvzi. Zuph has a direct effect on uvzi.\nWe know that wibl causes not zuph. wibl and zuph causes uvzi. We observed an individual is wibl.",
  "question": "Would an individual is uvzi if zuph instead of not zuph?",
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
| Clef | No | Incorrect |
| Luna Decisions | Yes | Correct |
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
    "record": "10256",
    "kind": "source_file_record"
  },
  "source_revision": "3d2d1169b4b939a09048a6a75956c8972a93cc38",
  "input_hash": "10f015e05b2d47c4425285d3bf4a364365d88588daf0475b00bc7d4df4373d81"
}
```

</details>
