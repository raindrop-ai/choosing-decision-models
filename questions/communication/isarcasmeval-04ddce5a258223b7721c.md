# Communication · question 27

[Back to Communication](README.md) · [All capabilities](../README.md)

**Question ID:** `isarcasmeval/04ddce5a258223b7721c`  
**Source:** [iSarcasmEval](https://github.com/iabufarha/iSarcasmEval)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/communication/isarcasmeval-04ddce5a258223b7721c/README.md)

## Context

> Don't you just love Monday mornings, they are even better when its freezing cold and you have an uncooperative child too!

## Question

> Is this message intended to be sarcastic?

## Answer choices

- **no:** Not sarcastic
- **yes:** Sarcastic

**Reference answer:** Sarcastic (`yes`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Don't you just love Monday mornings, they are even better when its freezing cold and you have an uncooperative child too!",
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
| Astra | Sarcastic | Correct |
| Opus 5.5 | Sarcastic | Correct |
| GLiDE v1.2 | Sarcastic | Correct |
| Decider v1.1 | Sarcastic | Correct |
| Jev | Sarcastic | Correct |
| Microsoft Decision-1 | Sarcastic | Correct |
| Clef | Sarcastic | Correct |
| Luna Decisions | Sarcastic | Correct |
| Clef Flash | Not sarcastic | Incorrect |
| Strands Decider | Sarcastic | Correct |
| GLiNER2.5 Decide | Sarcastic | Correct |
| Laya | Sarcastic | Correct |
| CalDec v1 | Sarcastic | Correct |

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
    "record": "4283",
    "kind": "prepared_normalizer_record",
    "native_id": "isarcasmeval/task_A_En_test/815/baseline"
  },
  "source_revision": "dfc708b53bde1bb571abfb5692f63231c2232195",
  "input_hash": "a098b8dbe9ce49626aac961a31ff48db909ec5b93f9e0d326ff7dd370b0828cc"
}
```

</details>
