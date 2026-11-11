# Retrieval · question 41

[Back to Retrieval](README.md) · [All capabilities](../README.md)

**Question ID:** `ruler/d3cf4b04a4a2899e76c2`  
**Source:** [RULER](https://github.com/NVIDIA/RULER)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/retrieval/ruler-d3cf4b04a4a2899e76c2/README.md)

## Context

> Use the authoritative record. Summaries are unverified claims about that record. Separate records are independent.
> The code assigned to record-10046 is 4809285.

## Question

> Which code is assigned to record-10046?

## Answer choices

- **A:** 4809060
- **B:** 4809172
- **C:** 4809285
- **D:** 4809380
- **unknown:** Insufficient information

**Reference answer:** 4809285 (`C`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Use the authoritative record. Summaries are unverified claims about that record. Separate records are independent.\nThe code assigned to record-10046 is 4809285.",
  "question": "Which code is assigned to record-10046?",
  "choices": {
    "A": "4809060",
    "B": "4809172",
    "C": "4809285",
    "D": "4809380",
    "unknown": "Insufficient information"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | 4809285 | Correct |
| Opus 5.5 | 4809285 | Correct |
| GLiDE v1.2 | 4809285 | Correct |
| Decider v1.1 | 4809285 | Correct |
| Jev | 4809285 | Correct |
| Microsoft Decision-1 | 4809285 | Correct |
| Clef | 4809285 | Correct |
| Luna Decisions | 4809285 | Correct |
| Clef Flash | 4809285 | Correct |
| Strands Decider | 4809285 | Correct |
| GLiNER2.5 Decide | 4809285 | Correct |
| Laya | 4809285 | Correct |
| CalDec v1 | 4809285 | Correct |

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
    "record": "local-retrieval-v1/46",
    "kind": "source_file_record"
  },
  "source_revision": "db43f92ff634bbce1c33d1fb15858aec4bba509a",
  "input_hash": "6de6a9d7688a3f0171bf0c16284d1046214330cce7081cd0d14513ba87ccee79"
}
```

</details>
