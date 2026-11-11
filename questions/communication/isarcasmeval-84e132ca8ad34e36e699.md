# Communication · question 18

[Back to Communication](README.md) · [All capabilities](../README.md)

**Question ID:** `isarcasmeval/84e132ca8ad34e36e699`  
**Source:** [iSarcasmEval](https://github.com/iabufarha/iSarcasmEval)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/communication/isarcasmeval-84e132ca8ad34e36e699/README.md)

## Context

> oh great, we have to wear masks and constant tests to protect our loved ones and others around us. being a human is so hard

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
  "state": "oh great, we have to wear masks and constant tests to protect our loved ones and others around us. being a human is so hard",
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
    "record": "4628",
    "kind": "prepared_normalizer_record",
    "native_id": "isarcasmeval/task_A_En_test/1160/baseline"
  },
  "source_revision": "dfc708b53bde1bb571abfb5692f63231c2232195",
  "input_hash": "d2045c9762c406d01eb1cb65737ed367b92d812392549d508e376304663a66c7"
}
```

</details>
