# Communication · question 41

[Back to Communication](README.md) · [All capabilities](../README.md)

**Question ID:** `isarcasmeval/696c52736e472e33f11e`  
**Source:** [iSarcasmEval](https://github.com/iabufarha/iSarcasmEval)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/communication/isarcasmeval-696c52736e472e33f11e/README.md)

## Context

> Really insane to think Brandon Marshall had the best season of his Hall of Fame career while in his 30s and playing with Ryan Fitzpatrick for the New York jets

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
  "state": "Really insane to think Brandon Marshall had the best season of his Hall of Fame career while in his 30s and playing with Ryan Fitzpatrick for the New York jets",
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
| Jev | Sarcastic | Incorrect |
| Microsoft Decision-1 | Not sarcastic | Correct |
| Clef | Not sarcastic | Correct |
| Luna Decisions | Sarcastic | Incorrect |
| Clef Flash | Not sarcastic | Correct |
| Strands Decider | Sarcastic | Incorrect |
| GLiNER2.5 Decide | Sarcastic | Incorrect |
| Laya | Not sarcastic | Correct |
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
    "record": "4145",
    "kind": "prepared_normalizer_record",
    "native_id": "isarcasmeval/task_A_En_test/677/baseline"
  },
  "source_revision": "dfc708b53bde1bb571abfb5692f63231c2232195",
  "input_hash": "48ece63533d87f5dac591111b9ff7dbc1f9af55657b65994f4433f8e9562485e"
}
```

</details>
