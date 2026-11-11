# Numerical cognition · question 10

[Back to Numerical cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `bbh/8d08bff83bb06db3cc2c`  
**Source:** [BIG-Bench Hard selected tasks](https://github.com/suzgunmirac/BIG-Bench-Hard)  
**Input format:** adapted choices

[Explore this question’s altered versions](../../variants/numerical-cognition/bbh-8d08bff83bb06db3cc2c/README.md)

## Question

> ((-5 + 6 + -6 \* -1) + (-5 + -5 + 9 + -2)) =

## Answer choices

- **A:** -3
- **B:** -9
- **C:** -4
- **D:** 4

**Reference answer:** 4 (`D`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "",
  "question": "((-5 + 6 + -6 * -1) + (-5 + -5 + 9 + -2)) =",
  "choices": {
    "A": "-3",
    "B": "-9",
    "C": "-4",
    "D": "4"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | 4 | Correct |
| Opus 5.5 | 4 | Correct |
| GLiDE v1.2 | 4 | Correct |
| Decider v1.1 | 4 | Correct |
| Jev | 4 | Correct |
| Microsoft Decision-1 | -3 | Incorrect |
| Clef | -4 | Incorrect |
| Luna Decisions | -3 | Incorrect |
| Clef Flash | -4 | Incorrect |
| Strands Decider | -4 | Incorrect |
| GLiNER2.5 Decide | -3 | Incorrect |
| Laya | -3 | Incorrect |
| CalDec v1 | -3 | Incorrect |

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
    "record": "63",
    "kind": "source_file_record"
  },
  "source_revision": "9ee07bd481feebf959a6b59d61ea57bdcf30964d",
  "input_hash": "31964ad982a1c1b8ee7add51e3f145094bf329ad123c92e6fc4e98128de8f9ec"
}
```

</details>
