# Numerical cognition · question 16

[Back to Numerical cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `bbh/9c6be9457cec8a333e0a`  
**Source:** [BIG-Bench Hard selected tasks](https://github.com/suzgunmirac/BIG-Bench-Hard)  
**Input format:** adapted choices

[Explore this question’s altered versions](../../variants/numerical-cognition/bbh-9c6be9457cec8a333e0a/README.md)

## Question

> ((-5 - 6 \* 2 + 4) - (1 - 9 - 0 \* 5)) =

## Answer choices

- **A:** 1
- **B:** 5
- **C:** -5
- **D:** -29

**Reference answer:** -5 (`C`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "",
  "question": "((-5 - 6 * 2 + 4) - (1 - 9 - 0 * 5)) =",
  "choices": {
    "A": "1",
    "B": "5",
    "C": "-5",
    "D": "-29"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | -5 | Correct |
| Opus 5.5 | -5 | Correct |
| GLiDE v1.2 | -5 | Correct |
| Decider v1.1 | -5 | Correct |
| Jev | -5 | Correct |
| Microsoft Decision-1 | 1 | Incorrect |
| Clef | 5 | Incorrect |
| Luna Decisions | -29 | Incorrect |
| Clef Flash | 5 | Incorrect |
| Strands Decider | -29 | Incorrect |
| GLiNER2.5 Decide | 1 | Incorrect |
| Laya | 1 | Incorrect |
| CalDec v1 | 1 | Incorrect |

## Source and sharing

Attribution: Mirac Suzgun and BIG-Bench Hard authors; BIG-bench contributors.  
Terms: **[MIT AND Apache-2.0](https://opensource.org/license/mit)**. [Source sharing decision](../../docs/data-sharing.md).  
The capability assignment and choice-format normalization are part of this experiment. Source data retain their own terms.

<details>
<summary>Exact source locator and input fingerprint</summary>

```json
{
  "source_locator": {
    "path": "bbh/multistep_arithmetic_two.json",
    "record": "182",
    "kind": "source_file_record"
  },
  "source_revision": "9ee07bd481feebf959a6b59d61ea57bdcf30964d",
  "input_hash": "c081622f23ff917a7141280e2a47e03971791ac3d615264195e0b0b68d05b03e"
}
```

</details>
