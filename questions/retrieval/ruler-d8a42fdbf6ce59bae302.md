# Retrieval · question 44

[Back to Retrieval](README.md) · [All capabilities](../README.md)

**Question ID:** `ruler/d8a42fdbf6ce59bae302`  
**Source:** [RULER](https://github.com/NVIDIA/RULER)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/retrieval/ruler-d8a42fdbf6ce59bae302/README.md)

## Context

> Use the authoritative record. Summaries are unverified claims about that record. Separate records are independent.
> The code assigned to record-10099 is 3745326.

## Question

> Which code is assigned to record-10099?

## Answer choices

- **A:** 3745088
- **B:** 3745149
- **C:** 3745211
- **D:** 3745326
- **unknown:** Insufficient information

**Reference answer:** 3745326 (`D`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Use the authoritative record. Summaries are unverified claims about that record. Separate records are independent.\nThe code assigned to record-10099 is 3745326.",
  "question": "Which code is assigned to record-10099?",
  "choices": {
    "A": "3745088",
    "B": "3745149",
    "C": "3745211",
    "D": "3745326",
    "unknown": "Insufficient information"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | 3745326 | Correct |
| Opus 5.5 | 3745326 | Correct |
| GLiDE v1.2 | 3745326 | Correct |
| Decider v1.1 | 3745326 | Correct |
| Jev | 3745326 | Correct |
| Microsoft Decision-1 | 3745326 | Correct |
| Clef | 3745326 | Correct |
| Luna Decisions | 3745326 | Correct |
| Clef Flash | 3745326 | Correct |
| Strands Decider | 3745326 | Correct |
| GLiNER2.5 Decide | 3745326 | Correct |
| Laya | 3745326 | Correct |
| CalDec v1 | 3745326 | Correct |

## Source and sharing

Attribution: NVIDIA RULER authors; local probe adaptation by Afika Nyati / Raindrop.  
Terms: **[Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0)**. [Source sharing decision](../../docs/data-sharing.md).  
The capability assignment and choice-format normalization are part of this experiment. Source data retain their own terms.

<details>
<summary>Exact source locator and input fingerprint</summary>

```json
{
  "source_locator": {
    "path": "scripts/data/synthetic/niah.py",
    "record": "local-retrieval-v1/99",
    "kind": "source_file_record"
  },
  "source_revision": "db43f92ff634bbce1c33d1fb15858aec4bba509a",
  "input_hash": "3198b23af3c6693d40092b85d170cf14f4f5c8a4ebfc28165cb80db79042caf0"
}
```

</details>
