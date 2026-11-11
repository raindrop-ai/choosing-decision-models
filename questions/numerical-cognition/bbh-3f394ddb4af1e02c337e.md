# Numerical cognition · question 58

[Back to Numerical cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `bbh/3f394ddb4af1e02c337e`  
**Source:** [BIG-Bench Hard selected tasks](https://github.com/suzgunmirac/BIG-Bench-Hard)  
**Input format:** adapted choices

[Explore this question’s altered versions](../../variants/numerical-cognition/bbh-3f394ddb4af1e02c337e/README.md)

## Question

> ((4 \* -4 + -6 - -2) - (9 + -7 + -8 \* 6)) =

## Answer choices

- **A:** 26
- **B:** 0
- **C:** 2
- **D:** -46

**Reference answer:** 26 (`A`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "",
  "question": "((4 * -4 + -6 - -2) - (9 + -7 + -8 * 6)) =",
  "choices": {
    "A": "26",
    "B": "0",
    "C": "2",
    "D": "-46"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | 26 | Correct |
| Opus 5.5 | 26 | Correct |
| GLiDE v1.2 | 26 | Correct |
| Decider v1.1 | 26 | Correct |
| Jev | 26 | Correct |
| Microsoft Decision-1 | 26 | Correct |
| Clef | -46 | Incorrect |
| Luna Decisions | 26 | Correct |
| Clef Flash | -46 | Incorrect |
| Strands Decider | -46 | Incorrect |
| GLiNER2.5 Decide | 26 | Correct |
| Laya | 0 | Incorrect |
| CalDec v1 | 2 | Incorrect |

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
    "record": "166",
    "kind": "source_file_record"
  },
  "source_revision": "9ee07bd481feebf959a6b59d61ea57bdcf30964d",
  "input_hash": "326329fe3bd5b548903819605d390193a61976d52d4f57a19d011b95924307eb"
}
```

</details>
