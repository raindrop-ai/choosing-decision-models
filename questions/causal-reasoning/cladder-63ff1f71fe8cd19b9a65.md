# Causal reasoning · question 33

[Back to Causal reasoning](README.md) · [All capabilities](../README.md)

**Question ID:** `cladder/63ff1f71fe8cd19b9a65`  
**Source:** [CLadder](https://github.com/causalNLP/cladder)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/causal-reasoning/cladder-63ff1f71fe8cd19b9a65/README.md)

## Context

> Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Jyka has a direct effect on yupt. Kwox has a direct effect on yupt.
> For those who are yupt, the correlation between jyka and kwox is -0.13.

## Question

> If we look at those who are yupt, does it mean that jyka affects kwox?

## Answer choices

- **yes:** Yes
- **no:** No

**Reference answer:** No (`no`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Jyka has a direct effect on yupt. Kwox has a direct effect on yupt.\nFor those who are yupt, the correlation between jyka and kwox is -0.13.",
  "question": "If we look at those who are yupt, does it mean that jyka affects kwox?",
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
    "record": "7474",
    "kind": "source_file_record"
  },
  "source_revision": "3d2d1169b4b939a09048a6a75956c8972a93cc38",
  "input_hash": "c4c34b626906d138d9b9c9c4ab300296039f96ffc9c3f3c4463ae720aa9be3cd"
}
```

</details>
