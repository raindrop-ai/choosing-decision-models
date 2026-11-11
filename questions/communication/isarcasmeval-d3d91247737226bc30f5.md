# Communication · question 31

[Back to Communication](README.md) · [All capabilities](../README.md)

**Question ID:** `isarcasmeval/d3d91247737226bc30f5`  
**Source:** [iSarcasmEval](https://github.com/iabufarha/iSarcasmEval)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/communication/isarcasmeval-d3d91247737226bc30f5/README.md)

## Context

> Boy, I sure do love being constantly misgendered by my cis relatives at family gatherings 🙃

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
  "state": "Boy, I sure do love being constantly misgendered by my cis relatives at family gatherings 🙃",
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
| Clef | Not sarcastic | Incorrect |
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
    "record": "4716",
    "kind": "prepared_normalizer_record",
    "native_id": "isarcasmeval/task_A_En_test/1248/baseline"
  },
  "source_revision": "dfc708b53bde1bb571abfb5692f63231c2232195",
  "input_hash": "86af066ac2ec28fde98b9ce7ccf9e30e05012fa39f1462352b940381999e20c3"
}
```

</details>
