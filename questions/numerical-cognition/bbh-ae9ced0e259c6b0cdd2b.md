# Numerical cognition · question 67

[Back to Numerical cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `bbh/ae9ced0e259c6b0cdd2b`  
**Source:** [BIG-Bench Hard selected tasks](https://github.com/suzgunmirac/BIG-Bench-Hard)  
**Input format:** adapted choices

[Explore this question’s altered versions](../../variants/numerical-cognition/bbh-ae9ced0e259c6b0cdd2b/README.md)

## Question

> ((-8 - -6 \* 7 \* 0) \* (0 + -5 \* -8 - 0)) =

## Answer choices

- **A:** -1
- **B:** -320
- **C:** 40
- **D:** 1

**Reference answer:** -320 (`B`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "",
  "question": "((-8 - -6 * 7 * 0) * (0 + -5 * -8 - 0)) =",
  "choices": {
    "A": "-1",
    "B": "-320",
    "C": "40",
    "D": "1"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | -320 | Correct |
| Opus 5.5 | -320 | Correct |
| GLiDE v1.2 | -320 | Correct |
| Decider v1.1 | -320 | Correct |
| Jev | -320 | Correct |
| Microsoft Decision-1 | -320 | Correct |
| Clef | -320 | Correct |
| Luna Decisions | -320 | Correct |
| Clef Flash | 40 | Incorrect |
| Strands Decider | -320 | Correct |
| GLiNER2.5 Decide | -1 | Incorrect |
| Laya | -1 | Incorrect |
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
    "record": "76",
    "kind": "source_file_record"
  },
  "source_revision": "9ee07bd481feebf959a6b59d61ea57bdcf30964d",
  "input_hash": "7f72ccb947b93d2365f5b451525e5746c40374fa85ba0b09431593aa92257323"
}
```

</details>
