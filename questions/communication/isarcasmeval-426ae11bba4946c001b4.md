# Communication · question 15

[Back to Communication](README.md) · [All capabilities](../README.md)

**Question ID:** `isarcasmeval/426ae11bba4946c001b4`  
**Source:** [iSarcasmEval](https://github.com/iabufarha/iSarcasmEval)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/communication/isarcasmeval-426ae11bba4946c001b4/README.md)

## Context

> Game of the Year goes to Yakuza Like A Dragon, special mention to Yakuza Zero.

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
  "state": "Game of the Year goes to Yakuza Like A Dragon, special mention to Yakuza Zero.",
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
    "record": "4103",
    "kind": "prepared_normalizer_record",
    "native_id": "isarcasmeval/task_A_En_test/635/baseline"
  },
  "source_revision": "dfc708b53bde1bb571abfb5692f63231c2232195",
  "input_hash": "1e5bf8172cd0df00f7b98a6e84d1f000745742d2bb9554ddd6e6b95c9fae66e9"
}
```

</details>
