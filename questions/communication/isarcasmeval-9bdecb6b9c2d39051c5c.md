# Communication · question 12

[Back to Communication](README.md) · [All capabilities](../README.md)

**Question ID:** `isarcasmeval/9bdecb6b9c2d39051c5c`  
**Source:** [iSarcasmEval](https://github.com/iabufarha/iSarcasmEval)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/communication/isarcasmeval-9bdecb6b9c2d39051c5c/README.md)

## Context

> Why does Ramish think he can  stop my kitchen rennovation because of the noise? His kids are not exactly quiet or competent when they play their musical instruments, lets just say my dog makes a better sound.

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
  "state": "Why does Ramish think he can  stop my kitchen rennovation because of the noise? His kids are not exactly quiet or competent when they play their musical instruments, lets just say my dog makes a better sound.",
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
| GLiDE v1.2 | Not sarcastic | Incorrect |
| Decider v1.1 | Not sarcastic | Incorrect |
| Jev | Sarcastic | Correct |
| Microsoft Decision-1 | Not sarcastic | Incorrect |
| Clef | Not sarcastic | Incorrect |
| Luna Decisions | Sarcastic | Correct |
| Clef Flash | Not sarcastic | Incorrect |
| Strands Decider | Sarcastic | Correct |
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
    "record": "4112",
    "kind": "prepared_normalizer_record",
    "native_id": "isarcasmeval/task_A_En_test/644/baseline"
  },
  "source_revision": "dfc708b53bde1bb571abfb5692f63231c2232195",
  "input_hash": "f7ade53c9c682e757141a4fc00c0fcad308fee96954ebddfb1f215bc36465fb2"
}
```

</details>
