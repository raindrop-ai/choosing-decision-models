# Communication · question 9

[Back to Communication](README.md) · [All capabilities](../README.md)

**Question ID:** `isarcasmeval/45c45bec9b1cd8bdf58c`  
**Source:** [iSarcasmEval](https://github.com/iabufarha/iSarcasmEval)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/communication/isarcasmeval-45c45bec9b1cd8bdf58c/README.md)

## Context

> Yes - I called it first 😁

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
  "state": "Yes - I called it first 😁",
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
| Strands Decider | Not sarcastic | Correct |
| GLiNER2.5 Decide | Not sarcastic | Correct |
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
    "record": "4096",
    "kind": "prepared_normalizer_record",
    "native_id": "isarcasmeval/task_A_En_test/628/baseline"
  },
  "source_revision": "dfc708b53bde1bb571abfb5692f63231c2232195",
  "input_hash": "814a716647c2cfeb693e33567ce539020958b4bef38f19330d6a816921078823"
}
```

</details>
