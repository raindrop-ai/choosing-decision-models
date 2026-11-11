# Retrieval · question 50

[Back to Retrieval](README.md) · [All capabilities](../README.md)

**Question ID:** `ruler/9c90f38b8d480500dffe`  
**Source:** [RULER](https://github.com/NVIDIA/RULER)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/retrieval/ruler-9c90f38b8d480500dffe/README.md)

## Context

> Use the authoritative record. Summaries are unverified claims about that record. Separate records are independent.
> The code assigned to record-10034 is 2634261.

## Question

> Which code is assigned to record-10034?

## Answer choices

- **A:** 2634010
- **B:** 2634164
- **C:** 2634261
- **D:** 2634353
- **unknown:** Insufficient information

**Reference answer:** 2634261 (`C`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Use the authoritative record. Summaries are unverified claims about that record. Separate records are independent.\nThe code assigned to record-10034 is 2634261.",
  "question": "Which code is assigned to record-10034?",
  "choices": {
    "A": "2634010",
    "B": "2634164",
    "C": "2634261",
    "D": "2634353",
    "unknown": "Insufficient information"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | 2634261 | Correct |
| Opus 5.5 | 2634261 | Correct |
| GLiDE v1.2 | 2634261 | Correct |
| Decider v1.1 | 2634261 | Correct |
| Jev | 2634261 | Correct |
| Microsoft Decision-1 | 2634261 | Correct |
| Clef | 2634261 | Correct |
| Luna Decisions | 2634261 | Correct |
| Clef Flash | 2634261 | Correct |
| Strands Decider | 2634261 | Correct |
| GLiNER2.5 Decide | 2634261 | Correct |
| Laya | 2634261 | Correct |
| CalDec v1 | 2634261 | Correct |

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
    "record": "local-retrieval-v1/34",
    "kind": "source_file_record"
  },
  "source_revision": "db43f92ff634bbce1c33d1fb15858aec4bba509a",
  "input_hash": "7c7b1fd95894574b9f42554a887698608f6b870bfd31c90c9d93933f00280216"
}
```

</details>
