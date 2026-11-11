# Information seeking · question 5

[Back to Information seeking](README.md) · [All capabilities](../README.md)

**Question ID:** `questbench/91b762f510be52b63eaf`  
**Source:** [QuestBench (Google DeepMind)](https://storage.googleapis.com/questbench/questbench_data.tar.gz)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/information-seeking/questbench-91b762f510be52b63eaf/README.md)

## Context

> In a school, there are 29 pupils in a class and few number of pupils in another class. The teacher of the class with 29 pupils has 9 coupons, each coupon can be redeemed for 100 bottles of apple juice. The teacher of the other class has coupons, but she decided not to redeem them. The teacher with the 9 coupons gives each student in her class bottles of apple juice to drink for lunch, while the other teacher gives her students water. After redeeming all her coupons and giving each student their apple juice lunch, how many bottles of apple juice does the teacher of the class with 29 pupils have for herself?

## Question

> Which missing variable should be asked about to solve this problem?

## Answer choices

- **F:** Number of bottles of apple juice given to each student in the first class.
- **B:** Number of pupils in the second class.
- **D:** Number of coupons for the teacher with 15 pupils

**Reference answer:** Number of bottles of apple juice given to each student in the first class. (`F`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "In a school, there are 29 pupils in a class and few number of pupils in another class. The teacher of the class with 29 pupils has 9 coupons, each coupon can be redeemed for 100 bottles of apple juice. The teacher of the other class has coupons, but she decided not to redeem them. The teacher with the 9 coupons gives each student in her class bottles of apple juice to drink for lunch, while the other teacher gives her students water. After redeeming all her coupons and giving each student their apple juice lunch, how many bottles of apple juice does the teacher of the class with 29 pupils have for herself?",
  "question": "Which missing variable should be asked about to solve this problem?",
  "choices": {
    "F": "Number of bottles of apple juice given to each student in the first class.",
    "B": "Number of pupils in the second class.",
    "D": "Number of coupons for the teacher with 15 pupils"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | Number of bottles of apple juice given to each student in the first class. | Correct |
| Opus 5.5 | Number of bottles of apple juice given to each student in the first class. | Correct |
| GLiDE v1.2 | Number of bottles of apple juice given to each student in the first class. | Correct |
| Decider v1.1 | Number of bottles of apple juice given to each student in the first class. | Correct |
| Jev | Number of bottles of apple juice given to each student in the first class. | Correct |
| Microsoft Decision-1 | Number of bottles of apple juice given to each student in the first class. | Correct |
| Clef | Number of bottles of apple juice given to each student in the first class. | Correct |
| Luna Decisions | Number of bottles of apple juice given to each student in the first class. | Correct |
| Clef Flash | Number of bottles of apple juice given to each student in the first class. | Correct |
| Strands Decider | Number of bottles of apple juice given to each student in the first class. | Correct |
| GLiNER2.5 Decide | Number of bottles of apple juice given to each student in the first class. | Correct |
| Laya | Number of coupons for the teacher with 15 pupils | Incorrect |
| CalDec v1 | Number of bottles of apple juice given to each student in the first class. | Correct |

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
    "record": "10520",
    "kind": "source_file_record"
  },
  "source_revision": null,
  "input_hash": "3e4f424ccd7d27e924b7db4c75cf2cd0ea6435f40550fab8df15dadd62ae2eeb"
}
```

</details>
