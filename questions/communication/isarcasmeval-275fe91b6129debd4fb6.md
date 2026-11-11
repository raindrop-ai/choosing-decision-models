# Communication · question 57

[Back to Communication](README.md) · [All capabilities](../README.md)

**Question ID:** `isarcasmeval/275fe91b6129debd4fb6`  
**Source:** [iSarcasmEval](https://github.com/iabufarha/iSarcasmEval)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/communication/isarcasmeval-275fe91b6129debd4fb6/README.md)

## Context

> James Harden is allowed to travel every time he drives apparently

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
  "state": "James Harden is allowed to travel every time he drives apparently",
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
| Clef | Not sarcastic | Incorrect |
| Luna Decisions | Sarcastic | Correct |
| Clef Flash | Not sarcastic | Incorrect |
| Strands Decider | Not sarcastic | Incorrect |
| GLiNER2.5 Decide | Sarcastic | Correct |
| Laya | Not sarcastic | Incorrect |
| CalDec v1 | Not sarcastic | Incorrect |

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
    "record": "527",
    "kind": "prepared_normalizer_record",
    "native_id": "isarcasmeval/train.En/527/baseline"
  },
  "source_revision": "dfc708b53bde1bb571abfb5692f63231c2232195",
  "input_hash": "6dd49fa6e37e5eca473fb399fad2db0e4fe6069fb4ac39eda658c3203e872d19"
}
```

</details>
