# Retrieval · question 47

[Back to Retrieval](README.md) · [All capabilities](../README.md)

**Question ID:** `ruler/0ed1cdaeb2c88c1e9527`  
**Source:** [RULER](https://github.com/NVIDIA/RULER)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/retrieval/ruler-0ed1cdaeb2c88c1e9527/README.md)

## Context

> Use the authoritative record. Summaries are unverified claims about that record. Separate records are independent.
> The code assigned to record-10029 is 6530135.

## Question

> Which code is assigned to record-10029?

## Answer choices

- **A:** 6530014
- **B:** 6530135
- **C:** 6530250
- **D:** 6530368
- **unknown:** Insufficient information

**Reference answer:** 6530135 (`B`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Use the authoritative record. Summaries are unverified claims about that record. Separate records are independent.\nThe code assigned to record-10029 is 6530135.",
  "question": "Which code is assigned to record-10029?",
  "choices": {
    "A": "6530014",
    "B": "6530135",
    "C": "6530250",
    "D": "6530368",
    "unknown": "Insufficient information"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | 6530135 | Correct |
| Opus 5.5 | 6530135 | Correct |
| GLiDE v1.2 | 6530135 | Correct |
| Decider v1.1 | 6530135 | Correct |
| Jev | 6530135 | Correct |
| Microsoft Decision-1 | 6530135 | Correct |
| Clef | 6530135 | Correct |
| Luna Decisions | 6530135 | Correct |
| Clef Flash | 6530135 | Correct |
| Strands Decider | 6530135 | Correct |
| GLiNER2.5 Decide | 6530135 | Correct |
| Laya | 6530135 | Correct |
| CalDec v1 | 6530135 | Correct |

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
    "record": "local-retrieval-v1/29",
    "kind": "source_file_record"
  },
  "source_revision": "db43f92ff634bbce1c33d1fb15858aec4bba509a",
  "input_hash": "db834a81232579e8f1c896f19defa91d7d67e47d96c519f61b532f9de0ef4238"
}
```

</details>
