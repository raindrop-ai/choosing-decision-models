# Communication · question 21

[Back to Communication](README.md) · [All capabilities](../README.md)

**Question ID:** `isarcasmeval/a1521ecf9b0e44a2bc78`  
**Source:** [iSarcasmEval](https://github.com/iabufarha/iSarcasmEval)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/communication/isarcasmeval-a1521ecf9b0e44a2bc78/README.md)

## Context

> Really looking forward to going Christmas shopping with my anti-vax, anti-mask, global conspiracy believing sister this weekend. 

## Question

> Is this message intended to be sarcastic?

## Answer choices

- **yes:** Sarcastic
- **no:** Not sarcastic

**Reference answer:** Sarcastic (`yes`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Really looking forward to going Christmas shopping with my anti-vax, anti-mask, global conspiracy believing sister this weekend. ",
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
| Astra | Sarcastic | Correct |
| Opus 5.5 | Sarcastic | Correct |
| GLiDE v1.2 | Sarcastic | Correct |
| Decider v1.1 | Sarcastic | Correct |
| Jev | Sarcastic | Correct |
| Microsoft Decision-1 | Sarcastic | Correct |
| Clef | Sarcastic | Correct |
| Luna Decisions | Sarcastic | Correct |
| Clef Flash | Not sarcastic | Incorrect |
| Strands Decider | Not sarcastic | Incorrect |
| GLiNER2.5 Decide | Not sarcastic | Incorrect |
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
    "record": "4386",
    "kind": "prepared_normalizer_record",
    "native_id": "isarcasmeval/task_A_En_test/918/baseline"
  },
  "source_revision": "dfc708b53bde1bb571abfb5692f63231c2232195",
  "input_hash": "75b18037e0b671fcaa59645e86e5aa427d622fcb6daa587d94cc29d36a33d4b9"
}
```

</details>
