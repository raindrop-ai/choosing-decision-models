# Concepts and categorization · question 40

[Back to Concepts and categorization](README.md) · [All capabilities](../README.md)

**Question ID:** `emowoz/6655f90bafecb88cc636`  
**Source:** [EmoWOZ](https://zenodo.org/records/6506504)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/concepts-and-categorization/emowoz-6655f90bafecb88cc636/README.md)

## Context

> User: I need a train departing from Cambridge, leaving after 21:30. 
> Assistant: What time were you looking to arrive and what is your destination?
> User: I need to go to Peterborough on Tuesday please
> Assistant: The TR7663 departs at 21:34 and arrives in Peterborough at 22:24. Shall I book this for you?
> User: Yes, for 7 people please.  I need the reference number.
> Assistant: Booking was successful, the total fee is 115.5 GBP payable at the station. Reference number is : NBX6ZT2O.
> User: I'm also looking for a restaurant in the south on the expensive side. 
> Assistant: I have 5 results for expensive restaurants in the south. Are you in the mood for Chinese, Indian, Italian or Mexican food?
> User: We are looking for indian food.
> Assistant: The Taj Tandoori is an expensive restaurant in the south.  It is located at 64 Cherry Hinton Road.  Would you like me to book it?
> User: Yes, for 7 people at 10:30 on Tuesday.
> Assistant: Unfortunately the restaurant is full at that time. Would you like to try another time or day?
> User: How about 9:30? 
> Assistant: I'm sorry, they don't offer that time. Would you like to try a later time?
> User: They have no 9:30?
> Assistant: They have no bookings available Tuesday morning. Would you like to try afternoon or another restaurant?
> User: Let's try again. An expensive Indian restaurant in the south - Tuesday, 9:30, 7 people.

## Question

> What emotion does the final user message express, taking the conversation into account?

## Answer choices

- **4:** Abusive
- **5:** Excited
- **1:** Fearful
- **6:** Satisfied
- **0:** Neutral
- **2:** Dissatisfied
- **3:** Apologetic

**Reference answer:** Dissatisfied (`2`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "User: I need a train departing from Cambridge, leaving after 21:30. \nAssistant: What time were you looking to arrive and what is your destination?\nUser: I need to go to Peterborough on Tuesday please\nAssistant: The TR7663 departs at 21:34 and arrives in Peterborough at 22:24. Shall I book this for you?\nUser: Yes, for 7 people please.  I need the reference number.\nAssistant: Booking was successful, the total fee is 115.5 GBP payable at the station. Reference number is : NBX6ZT2O.\nUser: I'm also looking for a restaurant in the south on the expensive side. \nAssistant: I have 5 results for expensive restaurants in the south. Are you in the mood for Chinese, Indian, Italian or Mexican food?\nUser: We are looking for indian food.\nAssistant: The Taj Tandoori is an expensive restaurant in the south.  It is located at 64 Cherry Hinton Road.  Would you like me to book it?\nUser: Yes, for 7 people at 10:30 on Tuesday.\nAssistant: Unfortunately the restaurant is full at that time. Would you like to try another time or day?\nUser: How about 9:30? \nAssistant: I'm sorry, they don't offer that time. Would you like to try a later time?\nUser: They have no 9:30?\nAssistant: They have no bookings available Tuesday morning. Would you like to try afternoon or another restaurant?\nUser: Let's try again. An expensive Indian restaurant in the south - Tuesday, 9:30, 7 people.",
  "question": "What emotion does the final user message express, taking the conversation into account?",
  "choices": {
    "4": "Abusive",
    "5": "Excited",
    "1": "Fearful",
    "6": "Satisfied",
    "0": "Neutral",
    "2": "Dissatisfied",
    "3": "Apologetic"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | Dissatisfied | Correct |
| Opus 5.5 | Dissatisfied | Correct |
| GLiDE v1.2 | Neutral | Incorrect |
| Decider v1.1 | Neutral | Incorrect |
| Jev | Dissatisfied | Correct |
| Microsoft Decision-1 | Neutral | Incorrect |
| Clef | Neutral | Incorrect |
| Luna Decisions | Dissatisfied | Correct |
| Clef Flash | Neutral | Incorrect |
| Strands Decider | Neutral | Incorrect |
| GLiNER2.5 Decide | Dissatisfied | Correct |
| Laya | Satisfied | Incorrect |
| CalDec v1 | Satisfied | Incorrect |

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
    "record": "10190",
    "kind": "prepared_normalizer_record",
    "native_id": "emowoz/MUL0370.json/16/baseline"
  },
  "source_revision": "6506504",
  "input_hash": "9905fbdb73f13d669c8cc40988afb3d9b6169f2a058f7d951815a6fe662a6763"
}
```

</details>
