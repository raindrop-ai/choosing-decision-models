# Concepts and categorization · question 18

[Back to Concepts and categorization](README.md) · [All capabilities](../README.md)

**Question ID:** `emowoz/dd3062c48be0c7478cd2`  
**Source:** [EmoWOZ](https://zenodo.org/records/6506504)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/concepts-and-categorization/emowoz-dd3062c48be0c7478cd2/README.md)

## Context

> User: Do you have any recommendations for restaurants in Cambridge?
> Assistant: There are 110 restaurants in Cambridge, is there a specific cuisine you're looking for?
> User: I'm sorry, it is actually a train that I'm looking for. I need to depart from Cambridge on Saturday.

## Question

> What emotion does the final user message express, taking the conversation into account?

## Answer choices

- **5:** Excited
- **1:** Fearful
- **0:** Neutral
- **6:** Satisfied
- **2:** Dissatisfied
- **3:** Apologetic
- **4:** Abusive

**Reference answer:** Apologetic (`3`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "User: Do you have any recommendations for restaurants in Cambridge?\nAssistant: There are 110 restaurants in Cambridge, is there a specific cuisine you're looking for?\nUser: I'm sorry, it is actually a train that I'm looking for. I need to depart from Cambridge on Saturday.",
  "question": "What emotion does the final user message express, taking the conversation into account?",
  "choices": {
    "5": "Excited",
    "1": "Fearful",
    "0": "Neutral",
    "6": "Satisfied",
    "2": "Dissatisfied",
    "3": "Apologetic",
    "4": "Abusive"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | Apologetic | Correct |
| Opus 5.5 | Apologetic | Correct |
| GLiDE v1.2 | Apologetic | Correct |
| Decider v1.1 | Apologetic | Correct |
| Jev | Apologetic | Correct |
| Microsoft Decision-1 | Apologetic | Correct |
| Clef | Apologetic | Correct |
| Luna Decisions | Apologetic | Correct |
| Clef Flash | Apologetic | Correct |
| Strands Decider | Apologetic | Correct |
| GLiNER2.5 Decide | Apologetic | Correct |
| Laya | Apologetic | Correct |
| CalDec v1 | Neutral | Incorrect |

## Source and sharing

Attribution: Shutong Feng, Nurul Lubis, Christian Geishauser, Hsien-chin Lin, Michael Heck, Carel van Niekerk, Milica Gasic.  
Terms: **[CC-BY-NC-4.0](https://creativecommons.org/licenses/by-nc/4.0/)**. [Source sharing decision](../../docs/data-sharing.md).  
The capability assignment and choice-format normalization are part of this experiment. Source data retain their own terms.

<details>
<summary>Exact source locator and input fingerprint</summary>

```json
{
  "source_locator": {
    "path": "data/prepared/emowoz.jsonl",
    "record": "4420",
    "kind": "prepared_normalizer_record",
    "native_id": "emowoz/PMUL0690.json/2/baseline"
  },
  "source_revision": "6506504",
  "input_hash": "45aedba0b3e977188564bcf2688345dfbf481234dc64bf68553ee68132ebfd9c"
}
```

</details>
