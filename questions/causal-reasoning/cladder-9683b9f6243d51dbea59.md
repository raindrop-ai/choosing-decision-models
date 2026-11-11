# Causal reasoning · question 56

[Back to Causal reasoning](README.md) · [All capabilities](../README.md)

**Question ID:** `cladder/9683b9f6243d51dbea59`  
**Source:** [CLadder](https://github.com/causalNLP/cladder)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/causal-reasoning/cladder-9683b9f6243d51dbea59/README.md)

## Context

> Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Respiratory issues has a direct effect on hospitalization status. Broken bones has a direct effect on hospitalization status.
> For hospitalized individuals, the correlation between respiratory issues and broken bones is 0.16.

## Question

> If we look at hospitalized individuals, does it mean that respiratory issues affects broken bones?

## Answer choices

- **yes:** Yes
- **no:** No

**Reference answer:** No (`no`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Respiratory issues has a direct effect on hospitalization status. Broken bones has a direct effect on hospitalization status.\nFor hospitalized individuals, the correlation between respiratory issues and broken bones is 0.16.",
  "question": "If we look at hospitalized individuals, does it mean that respiratory issues affects broken bones?",
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
| Strands Decider | No | Correct |
| GLiNER2.5 Decide | Yes | Incorrect |
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
    "record": "332",
    "kind": "source_file_record"
  },
  "source_revision": "3d2d1169b4b939a09048a6a75956c8972a93cc38",
  "input_hash": "dc9932575aeaaf32e0f8745bb8a5a5c9f792eeb32bc66593fcad1749933a5313"
}
```

</details>
