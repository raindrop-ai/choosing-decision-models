# Causal reasoning · question 18

[Back to Causal reasoning](README.md) · [All capabilities](../README.md)

**Question ID:** `cladder/b9d6be87c28d62330c0c`  
**Source:** [CLadder](https://github.com/causalNLP/cladder)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/causal-reasoning/cladder-b9d6be87c28d62330c0c/README.md)

## Context

> Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Jyka has a direct effect on yupt and kwox. Yupt has a direct effect on kwox.
> Method 1: We look directly at how jyka correlates with kwox in general. Method 2: We look at this correlation case by case according to yupt.

## Question

> To understand how jyka affects kwox, is it more correct to use the Method 1 than Method 2?

## Answer choices

- **yes:** Yes
- **no:** No

**Reference answer:** Yes (`yes`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Jyka has a direct effect on yupt and kwox. Yupt has a direct effect on kwox.\nMethod 1: We look directly at how jyka correlates with kwox in general. Method 2: We look at this correlation case by case according to yupt.",
  "question": "To understand how jyka affects kwox, is it more correct to use the Method 1 than Method 2?",
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
| Decider v1.1 | No | Incorrect |
| Jev | Yes | Correct |
| Microsoft Decision-1 | No | Incorrect |
| Clef | Yes | Correct |
| Luna Decisions | No | Incorrect |
| Clef Flash | Yes | Correct |
| Strands Decider | No | Incorrect |
| GLiNER2.5 Decide | Yes | Correct |
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
    "record": "4223",
    "kind": "source_file_record"
  },
  "source_revision": "3d2d1169b4b939a09048a6a75956c8972a93cc38",
  "input_hash": "f0c84ea078d153d61244e524024543f9ca97ce6f739fdf37deb1270c977bbb91"
}
```

</details>
