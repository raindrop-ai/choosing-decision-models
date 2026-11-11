# Numerical cognition · question 62

[Back to Numerical cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `bbh/40eceedeab129fcf9d44`  
**Source:** [BIG-Bench Hard selected tasks](https://github.com/suzgunmirac/BIG-Bench-Hard)  
**Input format:** adapted choices

[Explore this question’s altered versions](../../variants/numerical-cognition/bbh-40eceedeab129fcf9d44/README.md)

## Question

> ((3 + 3 - -4 - 2) + (-2 - -7 \* -2 \* 1)) =

## Answer choices

- **A:** 8
- **B:** 14
- **C:** -1
- **D:** -8

**Reference answer:** -8 (`D`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "",
  "question": "((3 + 3 - -4 - 2) + (-2 - -7 * -2 * 1)) =",
  "choices": {
    "A": "8",
    "B": "14",
    "C": "-1",
    "D": "-8"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | -8 | Correct |
| Opus 5.5 | -8 | Correct |
| GLiDE v1.2 | -8 | Correct |
| Decider v1.1 | -8 | Correct |
| Jev | -8 | Correct |
| Microsoft Decision-1 | -8 | Correct |
| Clef | -1 | Incorrect |
| Luna Decisions | -1 | Incorrect |
| Clef Flash | -1 | Incorrect |
| Strands Decider | 8 | Incorrect |
| GLiNER2.5 Decide | 8 | Incorrect |
| Laya | -8 | Correct |
| CalDec v1 | -1 | Incorrect |

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
    "record": "121",
    "kind": "source_file_record"
  },
  "source_revision": "9ee07bd481feebf959a6b59d61ea57bdcf30964d",
  "input_hash": "36f8f7faafb259738d8fd2ae60af7fdee4c67d4d650b29b32c8e511266ce95c6"
}
```

</details>
