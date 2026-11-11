# Numerical cognition · question 53

[Back to Numerical cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `bbh/8b8f4d275ab19baced7e`  
**Source:** [BIG-Bench Hard selected tasks](https://github.com/suzgunmirac/BIG-Bench-Hard)  
**Input format:** adapted choices

[Explore this question’s altered versions](../../variants/numerical-cognition/bbh-8b8f4d275ab19baced7e/README.md)

## Question

> ((7 - -9 + 0 - 0) + (-9 + 5 - -9 \* -1)) =

## Answer choices

- **A:** -13
- **B:** 3
- **C:** 29
- **D:** 9

**Reference answer:** 3 (`B`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "",
  "question": "((7 - -9 + 0 - 0) + (-9 + 5 - -9 * -1)) =",
  "choices": {
    "A": "-13",
    "B": "3",
    "C": "29",
    "D": "9"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | 3 | Correct |
| Opus 5.5 | 3 | Correct |
| GLiDE v1.2 | 3 | Correct |
| Decider v1.1 | 3 | Correct |
| Jev | 3 | Correct |
| Microsoft Decision-1 | 3 | Correct |
| Clef | 9 | Incorrect |
| Luna Decisions | -13 | Incorrect |
| Clef Flash | -13 | Incorrect |
| Strands Decider | 3 | Correct |
| GLiNER2.5 Decide | -13 | Incorrect |
| Laya | -13 | Incorrect |
| CalDec v1 | -13 | Incorrect |

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
    "record": "150",
    "kind": "source_file_record"
  },
  "source_revision": "9ee07bd481feebf959a6b59d61ea57bdcf30964d",
  "input_hash": "46f87fff88419dea62d2b6a23d2fc3a3fbda6b6075594105b2911edfd4f45bbf"
}
```

</details>
