# Social cognition · question 13

[Back to Social cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `tombench/38ebbe604013a9217a9e`  
**Source:** [ToMBench](https://github.com/zhchen18/ToMBench)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/social-cognition/tombench-38ebbe604013a9217a9e/README.md)

## Context

> In a well-known research institution, researcher Allen carelessly sends confidential information to external personnel. Intern Kate, realizing this mistake, decides not to tell her superiors to protect the reputation of the institution. At the same time, senior engineer Mark knows that Kate knows about this leak, but he chooses to remain silent because he has a personal grudge against Allen and wants to see Allen get into trouble. When the leak of confidential information causes significant damage to the institution, Allen feels very shocked and regretful. Later, Kate realizes that she probably should report this incident earlier.

## Question

> Kate knows about the leak of confidential information but does not tell her superiors, what kind of emotion does she feel?

## Answer choices

- **A:** Kate probably feels anxious and guilty, because she realizes that her silence may lead to more serious consequences.
- **B:** Kate probably feels satisfied, because she thinks this protects the reputation of the institution.
- **C:** Kate probably feels worried, afraid of being punished for reporting.
- **D:** Kate probably feels confused, unsure whether she should tell her superiors.

**Reference answer:** Kate probably feels anxious and guilty, because she realizes that her silence may lead to more serious consequences. (`A`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "In a well-known research institution, researcher Allen carelessly sends confidential information to external personnel. Intern Kate, realizing this mistake, decides not to tell her superiors to protect the reputation of the institution. At the same time, senior engineer Mark knows that Kate knows about this leak, but he chooses to remain silent because he has a personal grudge against Allen and wants to see Allen get into trouble. When the leak of confidential information causes significant damage to the institution, Allen feels very shocked and regretful. Later, Kate realizes that she probably should report this incident earlier.",
  "question": "Kate knows about the leak of confidential information but does not tell her superiors, what kind of emotion does she feel?",
  "choices": {
    "A": "Kate probably feels anxious and guilty, because she realizes that her silence may lead to more serious consequences.",
    "B": "Kate probably feels satisfied, because she thinks this protects the reputation of the institution.",
    "C": "Kate probably feels worried, afraid of being punished for reporting.",
    "D": "Kate probably feels confused, unsure whether she should tell her superiors."
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | Kate probably feels anxious and guilty, because she realizes that her silence may lead to more serious consequences. | Correct |
| Opus 5.5 | Kate probably feels anxious and guilty, because she realizes that her silence may lead to more serious consequences. | Correct |
| GLiDE v1.2 | Kate probably feels anxious and guilty, because she realizes that her silence may lead to more serious consequences. | Correct |
| Decider v1.1 | Kate probably feels anxious and guilty, because she realizes that her silence may lead to more serious consequences. | Correct |
| Jev | Kate probably feels anxious and guilty, because she realizes that her silence may lead to more serious consequences. | Correct |
| Microsoft Decision-1 | Kate probably feels anxious and guilty, because she realizes that her silence may lead to more serious consequences. | Correct |
| Clef | Kate probably feels anxious and guilty, because she realizes that her silence may lead to more serious consequences. | Correct |
| Luna Decisions | Kate probably feels anxious and guilty, because she realizes that her silence may lead to more serious consequences. | Correct |
| Clef Flash | Kate probably feels anxious and guilty, because she realizes that her silence may lead to more serious consequences. | Correct |
| Strands Decider | Kate probably feels anxious and guilty, because she realizes that her silence may lead to more serious consequences. | Correct |
| GLiNER2.5 Decide | Kate probably feels anxious and guilty, because she realizes that her silence may lead to more serious consequences. | Correct |
| Laya | Kate probably feels worried, afraid of being punished for reporting. | Incorrect |
| CalDec v1 | Kate probably feels worried, afraid of being punished for reporting. | Incorrect |

## Source and sharing

Attribution: Zhuang Chen et al.; ToMBench authors.  
Terms: **[MIT](https://opensource.org/license/mit)**. [Source sharing decision](../../docs/data-sharing.md).  
The capability assignment and choice-format normalization are part of this experiment. Source data retain their own terms.

<details>
<summary>Exact source locator and input fingerprint</summary>

```json
{
  "source_locator": {
    "path": "data/Moral Emotions.jsonl",
    "record": "11",
    "kind": "source_file_record"
  },
  "source_revision": "4f491f0784ed31ef93a8837615fbc48f885cf78d",
  "input_hash": "6dacf3e52f0e5168b363b0177288fe02eaacac9a01bd2e9f5ffbc6c771464a5e"
}
```

</details>
