# Causal reasoning · question 12

[Back to Causal reasoning](README.md) · [All capabilities](../README.md)

**Question ID:** `cladder/de5db69ca3199b264cec`  
**Source:** [CLadder](https://github.com/causalNLP/cladder)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/causal-reasoning/cladder-de5db69ca3199b264cec/README.md)

## Context

> Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Rixq has a direct effect on swoy and zuph. Zuph has a direct effect on xevu. Swoy has a direct effect on xevu.
> We know that rixq causes zuph and swoy. zuph or swoy causes xevu.

## Question

> Would an individual is not xevu if not rixq instead of rixq?

## Answer choices

- **yes:** Yes
- **no:** No

**Reference answer:** Yes (`yes`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Rixq has a direct effect on swoy and zuph. Zuph has a direct effect on xevu. Swoy has a direct effect on xevu.\nWe know that rixq causes zuph and swoy. zuph or swoy causes xevu.",
  "question": "Would an individual is not xevu if not rixq instead of rixq?",
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
    "record": "9558",
    "kind": "source_file_record"
  },
  "source_revision": "3d2d1169b4b939a09048a6a75956c8972a93cc38",
  "input_hash": "b4042ebc560da1690f9dc8924f388a2e4ba5b42a40f8e9778c4609e4818b25bd"
}
```

</details>
