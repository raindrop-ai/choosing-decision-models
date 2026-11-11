# Spatial cognition · question 9

[Back to Spatial cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `babi/f23876e41cd917cc4bba`  
**Source:** [bAbI](https://dl.fbaipublicfiles.com/babi/tasks_1-20_v1-2.tar.gz)  
**Input format:** adapted choices

[Explore this question’s altered versions](../../variants/spatial-cognition/babi-f23876e41cd917cc4bba/README.md)

## Context

> The red sphere is below the triangle.
> The blue square is below the red sphere.

## Question

> Is the triangle above the blue square?

## Answer choices

- **yes:** yes
- **no:** no

**Reference answer:** yes (`yes`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "The red sphere is below the triangle.\nThe blue square is below the red sphere.",
  "question": "Is the triangle above the blue square?",
  "choices": {
    "yes": "yes",
    "no": "no"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | yes | Correct |
| Opus 5.5 | yes | Correct |
| GLiDE v1.2 | yes | Correct |
| Decider v1.1 | yes | Correct |
| Jev | yes | Correct |
| Microsoft Decision-1 | yes | Correct |
| Clef | yes | Correct |
| Luna Decisions | yes | Correct |
| Clef Flash | yes | Correct |
| Strands Decider | yes | Correct |
| GLiNER2.5 Decide | yes | Correct |
| Laya | no | Incorrect |
| CalDec v1 | no | Incorrect |

## Source and sharing

Attribution: Facebook, Inc.; bAbI authors.  
Terms: **[CC-BY-3.0](https://creativecommons.org/licenses/by/3.0/)**. [Source sharing decision](../../docs/data-sharing.md).  
The capability assignment and choice-format normalization are part of this experiment. Source data retain their own terms.

<details>
<summary>Exact source locator and input fingerprint</summary>

```json
{
  "source_locator": {
    "path": "extracted/tasks.tar.gz/tasks_1-20_v1-2/en/qa17_positional-reasoning_test.txt",
    "record": "116",
    "kind": "source_file_record"
  },
  "source_revision": null,
  "input_hash": "3c340e35d5e299b0bf0e8a24c6222898cc761fa5772472d55985d5fcbea5e962"
}
```

</details>
