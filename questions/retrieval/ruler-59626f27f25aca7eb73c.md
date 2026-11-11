# Retrieval · question 62

[Back to Retrieval](README.md) · [All capabilities](../README.md)

**Question ID:** `ruler/59626f27f25aca7eb73c`  
**Source:** [RULER](https://github.com/NVIDIA/RULER)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/retrieval/ruler-59626f27f25aca7eb73c/README.md)

## Context

> Use the authoritative record. Summaries are unverified claims about that record. Separate records are independent.
> The code assigned to record-10065 is 1373173.

## Question

> Which code is assigned to record-10065?

## Answer choices

- **A:** 1373028
- **B:** 1373173
- **C:** 1373272
- **D:** 1373353
- **unknown:** Insufficient information

**Reference answer:** 1373173 (`B`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Use the authoritative record. Summaries are unverified claims about that record. Separate records are independent.\nThe code assigned to record-10065 is 1373173.",
  "question": "Which code is assigned to record-10065?",
  "choices": {
    "A": "1373028",
    "B": "1373173",
    "C": "1373272",
    "D": "1373353",
    "unknown": "Insufficient information"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | 1373173 | Correct |
| Opus 5.5 | 1373173 | Correct |
| GLiDE v1.2 | 1373173 | Correct |
| Decider v1.1 | 1373173 | Correct |
| Jev | 1373173 | Correct |
| Microsoft Decision-1 | 1373173 | Correct |
| Clef | 1373173 | Correct |
| Luna Decisions | 1373173 | Correct |
| Clef Flash | 1373173 | Correct |
| Strands Decider | 1373173 | Correct |
| GLiNER2.5 Decide | 1373173 | Correct |
| Laya | 1373173 | Correct |
| CalDec v1 | 1373173 | Correct |

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
    "record": "local-retrieval-v1/65",
    "kind": "source_file_record"
  },
  "source_revision": "db43f92ff634bbce1c33d1fb15858aec4bba509a",
  "input_hash": "c91c96266aca4b71a517d0760a430c25c29830aad61bc06af33411b8b8f56ad4"
}
```

</details>
