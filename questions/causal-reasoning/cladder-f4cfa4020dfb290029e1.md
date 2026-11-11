# Causal reasoning · question 52

[Back to Causal reasoning](README.md) · [All capabilities](../README.md)

**Question ID:** `cladder/f4cfa4020dfb290029e1`  
**Source:** [CLadder](https://github.com/causalNLP/cladder)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/causal-reasoning/cladder-f4cfa4020dfb290029e1/README.md)

## Context

> Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: The captain has a direct effect on the private and the corporal. The corporal has a direct effect on prisoner. The private has a direct effect on prisoner.
> For captains who release prisoners, the probability of the prisoner's death is 33%. For captains who execute prisoners, the probability of the prisoner's death is 81%.

## Question

> For captains who execute prisoners, would it be less likely to see the prisoner's death if the captain had ordered the release of the prisoner?

## Answer choices

- **yes:** Yes
- **no:** No

**Reference answer:** Yes (`yes`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: The captain has a direct effect on the private and the corporal. The corporal has a direct effect on prisoner. The private has a direct effect on prisoner.\nFor captains who release prisoners, the probability of the prisoner's death is 33%. For captains who execute prisoners, the probability of the prisoner's death is 81%.",
  "question": "For captains who execute prisoners, would it be less likely to see the prisoner's death if the captain had ordered the release of the prisoner?",
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
| Strands Decider | No | Incorrect |
| GLiNER2.5 Decide | Yes | Correct |
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
    "record": "649",
    "kind": "source_file_record"
  },
  "source_revision": "3d2d1169b4b939a09048a6a75956c8972a93cc38",
  "input_hash": "662cbdc120b3e41ada063da054b8266c02d2171b4695e99d34458d2380abaa7f"
}
```

</details>
