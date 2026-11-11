# Retrieval · question 38

[Back to Retrieval](README.md) · [All capabilities](../README.md)

**Question ID:** `ruler/48cc91ae8cacf7540843`  
**Source:** [RULER](https://github.com/NVIDIA/RULER)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/retrieval/ruler-48cc91ae8cacf7540843/README.md)

## Context

> Use the authoritative record. Summaries are unverified claims about that record. Separate records are independent.
> The code assigned to record-10089 is 4278122.

## Question

> Which code is assigned to record-10089?

## Answer choices

- **A:** 4278078
- **B:** 4278122
- **C:** 4278275
- **D:** 4278318
- **unknown:** Insufficient information

**Reference answer:** 4278122 (`B`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Use the authoritative record. Summaries are unverified claims about that record. Separate records are independent.\nThe code assigned to record-10089 is 4278122.",
  "question": "Which code is assigned to record-10089?",
  "choices": {
    "A": "4278078",
    "B": "4278122",
    "C": "4278275",
    "D": "4278318",
    "unknown": "Insufficient information"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | 4278122 | Correct |
| Opus 5.5 | 4278122 | Correct |
| GLiDE v1.2 | 4278122 | Correct |
| Decider v1.1 | 4278122 | Correct |
| Jev | 4278122 | Correct |
| Microsoft Decision-1 | 4278122 | Correct |
| Clef | 4278122 | Correct |
| Luna Decisions | 4278122 | Correct |
| Clef Flash | 4278122 | Correct |
| Strands Decider | 4278122 | Correct |
| GLiNER2.5 Decide | 4278122 | Correct |
| Laya | 4278122 | Correct |
| CalDec v1 | 4278122 | Correct |

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
    "record": "local-retrieval-v1/89",
    "kind": "source_file_record"
  },
  "source_revision": "db43f92ff634bbce1c33d1fb15858aec4bba509a",
  "input_hash": "1a2c6e582c18908b16e4af5238ef7923b0caac07cc5d20c100624c797abfdde8"
}
```

</details>
