# Retrieval · question 29

[Back to Retrieval](README.md) · [All capabilities](../README.md)

**Question ID:** `ruler/e7d7cefa68d11a9fb864`  
**Source:** [RULER](https://github.com/NVIDIA/RULER)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/retrieval/ruler-e7d7cefa68d11a9fb864/README.md)

## Context

> Use the authoritative record. Summaries are unverified claims about that record. Separate records are independent.
> The code assigned to record-10115 is 7312345.

## Question

> Which code is assigned to record-10115?

## Answer choices

- **A:** 7312011
- **B:** 7312183
- **C:** 7312244
- **D:** 7312345
- **unknown:** Insufficient information

**Reference answer:** 7312345 (`D`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Use the authoritative record. Summaries are unverified claims about that record. Separate records are independent.\nThe code assigned to record-10115 is 7312345.",
  "question": "Which code is assigned to record-10115?",
  "choices": {
    "A": "7312011",
    "B": "7312183",
    "C": "7312244",
    "D": "7312345",
    "unknown": "Insufficient information"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | 7312345 | Correct |
| Opus 5.5 | 7312345 | Correct |
| GLiDE v1.2 | 7312345 | Correct |
| Decider v1.1 | 7312345 | Correct |
| Jev | 7312345 | Correct |
| Microsoft Decision-1 | 7312345 | Correct |
| Clef | 7312345 | Correct |
| Luna Decisions | 7312345 | Correct |
| Clef Flash | 7312345 | Correct |
| Strands Decider | 7312345 | Correct |
| GLiNER2.5 Decide | 7312345 | Correct |
| Laya | 7312345 | Correct |
| CalDec v1 | 7312345 | Correct |

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
    "record": "local-retrieval-v1/115",
    "kind": "source_file_record"
  },
  "source_revision": "db43f92ff634bbce1c33d1fb15858aec4bba509a",
  "input_hash": "5c31c7e16899ffee9f796f6ae96b05824e8aa6c556301bc8a9479b88dcaf9653"
}
```

</details>
