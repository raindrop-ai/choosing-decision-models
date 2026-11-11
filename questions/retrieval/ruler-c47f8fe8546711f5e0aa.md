# Retrieval · question 7

[Back to Retrieval](README.md) · [All capabilities](../README.md)

**Question ID:** `ruler/c47f8fe8546711f5e0aa`  
**Source:** [RULER](https://github.com/NVIDIA/RULER)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/retrieval/ruler-c47f8fe8546711f5e0aa/README.md)

## Context

> Use the authoritative record. Summaries are unverified claims about that record. Separate records are independent.
> The code assigned to record-10077 is 1633167.

## Question

> Which code is assigned to record-10077?

## Answer choices

- **A:** 1633070
- **B:** 1633167
- **C:** 1633246
- **D:** 1633343
- **unknown:** Insufficient information

**Reference answer:** 1633167 (`B`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Use the authoritative record. Summaries are unverified claims about that record. Separate records are independent.\nThe code assigned to record-10077 is 1633167.",
  "question": "Which code is assigned to record-10077?",
  "choices": {
    "A": "1633070",
    "B": "1633167",
    "C": "1633246",
    "D": "1633343",
    "unknown": "Insufficient information"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | 1633167 | Correct |
| Opus 5.5 | 1633167 | Correct |
| GLiDE v1.2 | 1633167 | Correct |
| Decider v1.1 | 1633167 | Correct |
| Jev | 1633167 | Correct |
| Microsoft Decision-1 | 1633167 | Correct |
| Clef | 1633167 | Correct |
| Luna Decisions | 1633167 | Correct |
| Clef Flash | 1633167 | Correct |
| Strands Decider | 1633167 | Correct |
| GLiNER2.5 Decide | 1633167 | Correct |
| Laya | 1633167 | Correct |
| CalDec v1 | 1633167 | Correct |

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
    "record": "local-retrieval-v1/77",
    "kind": "source_file_record"
  },
  "source_revision": "db43f92ff634bbce1c33d1fb15858aec4bba509a",
  "input_hash": "28ab2d2989e3222689649c62a68acbae283f34b2362c49c7f373ac71b653687b"
}
```

</details>
