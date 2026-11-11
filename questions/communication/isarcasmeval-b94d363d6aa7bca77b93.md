# Communication · question 65

[Back to Communication](README.md) · [All capabilities](../README.md)

**Question ID:** `isarcasmeval/b94d363d6aa7bca77b93`  
**Source:** [iSarcasmEval](https://github.com/iabufarha/iSarcasmEval)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/communication/isarcasmeval-b94d363d6aa7bca77b93/README.md)

## Context

> Just download the Researcher app - if anyone has tips please let me know 🙏

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
  "state": "Just download the Researcher app - if anyone has tips please let me know 🙏",
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
    "record": "3118",
    "kind": "prepared_normalizer_record",
    "native_id": "isarcasmeval/train.En/3118/baseline"
  },
  "source_revision": "dfc708b53bde1bb571abfb5692f63231c2232195",
  "input_hash": "c7ceb87cb374f72b624e20a6d8ac0b2e5fb4bc829f3df02fc4342a1d363bbe34"
}
```

</details>
