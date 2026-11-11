# Information seeking · question 63

[Back to Information seeking](README.md) · [All capabilities](../README.md)

**Question ID:** `questbench/1103c1607068c4ceb70d`  
**Source:** [QuestBench (Google DeepMind)](https://storage.googleapis.com/questbench/questbench_data.tar.gz)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/information-seeking/questbench-1103c1607068c4ceb70d/README.md)

## Context

> Janet buys a brooch for her daughter. She pays for the material to make it and then another $800 for the jeweler to construct it. After that, she pays 10% of that to get it insured. She also buys a necklace for herself, which is not related to the brooch. How much did she pay for the brooch,excluding the necklace?

## Question

> Which missing variable should be asked about to solve this problem?

## Answer choices

- **A:** the cost of the material for the brooch
- **D:** the cost of the necklace Janet bought for herself, which is unrelated to the brooch.

**Reference answer:** the cost of the material for the brooch (`A`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Janet buys a brooch for her daughter. She pays for the material to make it and then another $800 for the jeweler to construct it. After that, she pays 10% of that to get it insured. She also buys a necklace for herself, which is not related to the brooch. How much did she pay for the brooch,excluding the necklace?",
  "question": "Which missing variable should be asked about to solve this problem?",
  "choices": {
    "A": "the cost of the material for the brooch",
    "D": "the cost of the necklace Janet bought for herself, which is unrelated to the brooch."
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | the cost of the material for the brooch | Correct |
| Opus 5.5 | the cost of the material for the brooch | Correct |
| GLiDE v1.2 | the cost of the material for the brooch | Correct |
| Decider v1.1 | the cost of the material for the brooch | Correct |
| Jev | the cost of the material for the brooch | Correct |
| Microsoft Decision-1 | the cost of the material for the brooch | Correct |
| Clef | the cost of the material for the brooch | Correct |
| Luna Decisions | the cost of the material for the brooch | Correct |
| Clef Flash | the cost of the material for the brooch | Correct |
| Strands Decider | the cost of the material for the brooch | Correct |
| GLiNER2.5 Decide | the cost of the necklace Janet bought for herself, which is unrelated to the brooch. | Incorrect |
| Laya | the cost of the necklace Janet bought for herself, which is unrelated to the brooch. | Incorrect |
| CalDec v1 | the cost of the material for the brooch | Correct |

## Source and sharing

Attribution: Google LLC; QuestBench authors.  
Terms: **[CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)**. [Source sharing decision](../../docs/data-sharing.md).  
The capability assignment and choice-format normalization are part of this experiment. Source data retain their own terms.

<details>
<summary>Exact source locator and input fingerprint</summary>

```json
{
  "source_locator": {
    "path": "extracted/questbench.tar.gz/questbench_data/GSM-Q/gsm_verbal_full.csv",
    "record": "7963",
    "kind": "source_file_record"
  },
  "source_revision": null,
  "input_hash": "e100d10efbac4e38c31b0097c20e3e13382ded4734c20084a337268c090b1c95"
}
```

</details>
