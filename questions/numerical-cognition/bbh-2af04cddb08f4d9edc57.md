# Numerical cognition · question 57

[Back to Numerical cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `bbh/2af04cddb08f4d9edc57`  
**Source:** [BIG-Bench Hard selected tasks](https://github.com/suzgunmirac/BIG-Bench-Hard)  
**Input format:** adapted choices

[Explore this question’s altered versions](../../variants/numerical-cognition/bbh-2af04cddb08f4d9edc57/README.md)

## Question

> ((-1 - -9 \* 8 - -9) + (-9 - 2 \* -6 + -6)) =

## Answer choices

- **A:** -77
- **B:** -12
- **C:** 77
- **D:** -3

**Reference answer:** 77 (`C`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "",
  "question": "((-1 - -9 * 8 - -9) + (-9 - 2 * -6 + -6)) =",
  "choices": {
    "A": "-77",
    "B": "-12",
    "C": "77",
    "D": "-3"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | 77 | Correct |
| Opus 5.5 | 77 | Correct |
| GLiDE v1.2 | 77 | Correct |
| Decider v1.1 | 77 | Correct |
| Jev | 77 | Correct |
| Microsoft Decision-1 | 77 | Correct |
| Clef | -12 | Incorrect |
| Luna Decisions | 77 | Correct |
| Clef Flash | -12 | Incorrect |
| Strands Decider | -77 | Incorrect |
| GLiNER2.5 Decide | -77 | Incorrect |
| Laya | -77 | Incorrect |
| CalDec v1 | -77 | Incorrect |

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
    "record": "62",
    "kind": "source_file_record"
  },
  "source_revision": "9ee07bd481feebf959a6b59d61ea57bdcf30964d",
  "input_hash": "6606aac39a2f4ab9f5ae4f19e8bdb3f4386034f56392efc1d6e4805ffcbea8fd"
}
```

</details>
