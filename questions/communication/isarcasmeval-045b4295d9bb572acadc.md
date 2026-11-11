# Communication · question 45

[Back to Communication](README.md) · [All capabilities](../README.md)

**Question ID:** `isarcasmeval/045b4295d9bb572acadc`  
**Source:** [iSarcasmEval](https://github.com/iabufarha/iSarcasmEval)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/communication/isarcasmeval-045b4295d9bb572acadc/README.md)

## Context

> It’s good to hear once again how the government are setting a great example when it comes to following their own COVID restrictions.....

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
  "state": "It’s good to hear once again how the government are setting a great example when it comes to following their own COVID restrictions.....",
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
| Clef Flash | Sarcastic | Correct |
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
    "record": "4568",
    "kind": "prepared_normalizer_record",
    "native_id": "isarcasmeval/task_A_En_test/1100/baseline"
  },
  "source_revision": "dfc708b53bde1bb571abfb5692f63231c2232195",
  "input_hash": "d4b24b22b9b14a8e1dc15e373d2d8a0606ab3248326a454a41692fef027fdc9f"
}
```

</details>
