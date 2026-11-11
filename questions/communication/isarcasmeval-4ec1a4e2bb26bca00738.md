# Communication · question 49

[Back to Communication](README.md) · [All capabilities](../README.md)

**Question ID:** `isarcasmeval/4ec1a4e2bb26bca00738`  
**Source:** [iSarcasmEval](https://github.com/iabufarha/iSarcasmEval)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/communication/isarcasmeval-4ec1a4e2bb26bca00738/README.md)

## Context

> Politicians are nothing more than a corrupt, vile, self-serving wastes of thieves with a contempt for the electorate they purport to serve.

## Question

> Is this message intended to be sarcastic?

## Answer choices

- **yes:** Sarcastic
- **no:** Not sarcastic

**Reference answer:** Not sarcastic (`no`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Politicians are nothing more than a corrupt, vile, self-serving wastes of thieves with a contempt for the electorate they purport to serve.",
  "question": "Is this message intended to be sarcastic?",
  "choices": {
    "yes": "Sarcastic",
    "no": "Not sarcastic"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | Not sarcastic | Correct |
| Opus 5.5 | Not sarcastic | Correct |
| GLiDE v1.2 | Not sarcastic | Correct |
| Decider v1.1 | Not sarcastic | Correct |
| Jev | Not sarcastic | Correct |
| Microsoft Decision-1 | Not sarcastic | Correct |
| Clef | Not sarcastic | Correct |
| Luna Decisions | Not sarcastic | Correct |
| Clef Flash | Not sarcastic | Correct |
| Strands Decider | Sarcastic | Incorrect |
| GLiNER2.5 Decide | Sarcastic | Incorrect |
| Laya | Sarcastic | Incorrect |
| CalDec v1 | Sarcastic | Incorrect |

## Source and sharing

Attribution: Ibrahim Abu Farha et al.; iSarcasmEval authors.  
Terms: **[MIT](https://opensource.org/license/mit)**. [Source sharing decision](../../docs/data-sharing.md).  
The capability assignment and choice-format normalization are part of this experiment. Source data retain their own terms.

<details>
<summary>Exact source locator and input fingerprint</summary>

```json
{
  "source_locator": {
    "path": "data/prepared/isarcasmeval.jsonl",
    "record": "4114",
    "kind": "prepared_normalizer_record",
    "native_id": "isarcasmeval/task_A_En_test/646/baseline"
  },
  "source_revision": "dfc708b53bde1bb571abfb5692f63231c2232195",
  "input_hash": "3f360ec0f31ad47439a9e4631cb0b19a6facd8dfdc21fcee0e3c5f266f85b492"
}
```

</details>
