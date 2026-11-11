# Communication · question 1

[Back to Communication](README.md) · [All capabilities](../README.md)

**Question ID:** `isarcasmeval/50039007b81a935b1eb9`  
**Source:** [iSarcasmEval](https://github.com/iabufarha/iSarcasmEval)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/communication/isarcasmeval-50039007b81a935b1eb9/README.md)

## Context

> Michael Carricks interview after the Chelsea game, "i thought we were unlucky not to get the 3 points today" 3 Points, i am sure you have to start shooting to score goals to win games !!!

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
  "state": "Michael Carricks interview after the Chelsea game, \"i thought we were unlucky not to get the 3 points today\" 3 Points, i am sure you have to start shooting to score goals to win games !!!",
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
    "record": "3802",
    "kind": "prepared_normalizer_record",
    "native_id": "isarcasmeval/task_A_En_test/334/baseline"
  },
  "source_revision": "dfc708b53bde1bb571abfb5692f63231c2232195",
  "input_hash": "c035828537ce3db64435e1014a5164534a1f1d25f20ab8d989aaef49f7df7182"
}
```

</details>
