# Communication · question 61

[Back to Communication](README.md) · [All capabilities](../README.md)

**Question ID:** `isarcasmeval/6805cca11e8ee9bf3dcc`  
**Source:** [iSarcasmEval](https://github.com/iabufarha/iSarcasmEval)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/communication/isarcasmeval-6805cca11e8ee9bf3dcc/README.md)

## Context

> using loops, building an idea on that loop, and then deleting the loop has been a fun little exercise recently

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
  "state": "using loops, building an idea on that loop, and then deleting the loop has been a fun little exercise recently",
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
| Luna Decisions | Not sarcastic | Correct |
| Clef Flash | Not sarcastic | Correct |
| Strands Decider | Not sarcastic | Correct |
| GLiNER2.5 Decide | Not sarcastic | Correct |
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
    "record": "1984",
    "kind": "prepared_normalizer_record",
    "native_id": "isarcasmeval/train.En/1984/baseline"
  },
  "source_revision": "dfc708b53bde1bb571abfb5692f63231c2232195",
  "input_hash": "f237b0dd998aa5204043ebcafff3584f51e2878a907d02d0830c8eedf3337232"
}
```

</details>
