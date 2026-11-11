# Communication · question 47

[Back to Communication](README.md) · [All capabilities](../README.md)

**Question ID:** `isarcasmeval/3abe6ec5adac85690586`  
**Source:** [iSarcasmEval](https://github.com/iabufarha/iSarcasmEval)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/communication/isarcasmeval-3abe6ec5adac85690586/README.md)

## Context

> So Boris has made a hash of Brexit, let 150,000 people die and lied through his teeth but still thinks he deserves a boozy bash! Nothing surprises me about him any more sadly.

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
  "state": "So Boris has made a hash of Brexit, let 150,000 people die and lied through his teeth but still thinks he deserves a boozy bash! Nothing surprises me about him any more sadly.",
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
| Astra | Sarcastic | Incorrect |
| Opus 5.5 | Not sarcastic | Correct |
| GLiDE v1.2 | Not sarcastic | Correct |
| Decider v1.1 | Not sarcastic | Correct |
| Jev | Not sarcastic | Correct |
| Microsoft Decision-1 | Not sarcastic | Correct |
| Clef | Not sarcastic | Correct |
| Luna Decisions | Sarcastic | Incorrect |
| Clef Flash | Not sarcastic | Correct |
| Strands Decider | Sarcastic | Incorrect |
| GLiNER2.5 Decide | Sarcastic | Incorrect |
| Laya | Sarcastic | Incorrect |
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
    "record": "4276",
    "kind": "prepared_normalizer_record",
    "native_id": "isarcasmeval/task_A_En_test/808/baseline"
  },
  "source_revision": "dfc708b53bde1bb571abfb5692f63231c2232195",
  "input_hash": "d6619c1741a3760feb1a1c0b5ea516bc6019b88db1a79355ae8279910b27d29a"
}
```

</details>
