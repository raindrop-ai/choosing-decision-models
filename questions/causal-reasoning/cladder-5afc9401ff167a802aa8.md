# Causal reasoning · question 42

[Back to Causal reasoning](README.md) · [All capabilities](../README.md)

**Question ID:** `cladder/5afc9401ff167a802aa8`  
**Source:** [CLadder](https://github.com/causalNLP/cladder)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/causal-reasoning/cladder-5afc9401ff167a802aa8/README.md)

## Context

> Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Listening to jazz has a direct effect on elite institution admission status. Effort has a direct effect on elite institution admission status.
> For students accepted to elite institutions, the correlation between listening to jazz and being hard-working is -0.03.

## Question

> If we look at students accepted to elite institutions, does it mean that listening to jazz affects being hard-working?

## Answer choices

- **yes:** Yes
- **no:** No

**Reference answer:** No (`no`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Listening to jazz has a direct effect on elite institution admission status. Effort has a direct effect on elite institution admission status.\nFor students accepted to elite institutions, the correlation between listening to jazz and being hard-working is -0.03.",
  "question": "If we look at students accepted to elite institutions, does it mean that listening to jazz affects being hard-working?",
  "choices": {
    "yes": "Yes",
    "no": "No"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | No | Correct |
| Opus 5.5 | No | Correct |
| GLiDE v1.2 | No | Correct |
| Decider v1.1 | No | Correct |
| Jev | No | Correct |
| Microsoft Decision-1 | No | Correct |
| Clef | No | Correct |
| Luna Decisions | No | Correct |
| Clef Flash | No | Correct |
| Strands Decider | No | Correct |
| GLiNER2.5 Decide | No | Correct |
| Laya | No | Correct |
| CalDec v1 | No | Correct |

## Source and sharing

Attribution: CLadder original creators; see source.  
Terms: **[MIT](https://opensource.org/license/mit)**. [Source sharing decision](../../docs/data-sharing.md).  
The capability assignment and choice-format normalization are part of this experiment. Source data retain their own terms.

<details>
<summary>Exact source locator and input fingerprint</summary>

```json
{
  "source_locator": {
    "path": "data/cladder-v1-questions.json",
    "record": "1482",
    "kind": "source_file_record"
  },
  "source_revision": "3d2d1169b4b939a09048a6a75956c8972a93cc38",
  "input_hash": "1b0110ad75b44731ac4ea3851d73afd0634a6dde101d44e6c6841b1ca5ed2764"
}
```

</details>
