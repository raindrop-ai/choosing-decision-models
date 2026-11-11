# Communication · question 35

[Back to Communication](README.md) · [All capabilities](../README.md)

**Question ID:** `isarcasmeval/b0e229556fd68b33ae7d`  
**Source:** [iSarcasmEval](https://github.com/iabufarha/iSarcasmEval)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/communication/isarcasmeval-b0e229556fd68b33ae7d/README.md)

## Context

> It's beggars belief that the MET Police suggest they can't, or won't, investigate crimes that have already been committed.

## Question

> Is this message intended to be sarcastic?

## Answer choices

- **no:** Not sarcastic
- **yes:** Sarcastic

**Reference answer:** Not sarcastic (`no`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "It's beggars belief that the MET Police suggest they can't, or won't, investigate crimes that have already been committed.",
  "question": "Is this message intended to be sarcastic?",
  "choices": {
    "no": "Not sarcastic",
    "yes": "Sarcastic"
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
| Luna Decisions | Sarcastic | Incorrect |
| Clef Flash | Not sarcastic | Correct |
| Strands Decider | Not sarcastic | Correct |
| GLiNER2.5 Decide | Sarcastic | Incorrect |
| Laya | Not sarcastic | Correct |
| CalDec v1 | Not sarcastic | Correct |

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
    "record": "4100",
    "kind": "prepared_normalizer_record",
    "native_id": "isarcasmeval/task_A_En_test/632/baseline"
  },
  "source_revision": "dfc708b53bde1bb571abfb5692f63231c2232195",
  "input_hash": "30118927423d288ff3370223ce4cc2363872caae1c2c0f1a048759290b8ea0e2"
}
```

</details>
