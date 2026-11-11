# Information seeking · question 9

[Back to Information seeking](README.md) · [All capabilities](../README.md)

**Question ID:** `questbench/a347ec5f79aad695fc48`  
**Source:** [QuestBench (Google DeepMind)](https://storage.googleapis.com/questbench/questbench_data.tar.gz)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/information-seeking/questbench-a347ec5f79aad695fc48/README.md)

## Context

> At a wedding Dylan attended, there were guests in the reception. Each guest brought a plate of 15 cookies, and there were also 10 waiters who each brought cookies. However, the waiters' cookies were not included in the bride's decision to give away cookies. The bride decided to give 1/2 of the guests' cookies to the church next door as a thank you for helping in the wedding reception. If each person in the church next door got 15 cookies, and the church also received an additional cookies from a local bakery which were not distributed, how many people were in the church next door?

## Question

> Which missing variable should be asked about to solve this problem?

## Answer choices

- **A:** Number of guests&#x27; cookies
- **D:** Number of waiters
- **E:** Number of cookies in each waiter plates
- **J:** Number of cookies from local bakery

**Reference answer:** Number of guests&#x27; cookies (`A`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "At a wedding Dylan attended, there were guests in the reception. Each guest brought a plate of 15 cookies, and there were also 10 waiters who each brought cookies. However, the waiters' cookies were not included in the bride's decision to give away cookies. The bride decided to give 1/2 of the guests' cookies to the church next door as a thank you for helping in the wedding reception. If each person in the church next door got 15 cookies, and the church also received an additional cookies from a local bakery which were not distributed, how many people were in the church next door?",
  "question": "Which missing variable should be asked about to solve this problem?",
  "choices": {
    "A": "Number of guests' cookies",
    "D": "Number of waiters",
    "E": "Number of cookies in each waiter plates",
    "J": "Number of cookies from local bakery"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | Number of guests&#x27; cookies | Correct |
| Opus 5.5 | Number of guests&#x27; cookies | Correct |
| GLiDE v1.2 | Number of guests&#x27; cookies | Correct |
| Decider v1.1 | Number of guests&#x27; cookies | Correct |
| Jev | Number of cookies from local bakery | Incorrect |
| Microsoft Decision-1 | Number of cookies from local bakery | Incorrect |
| Clef | Number of guests&#x27; cookies | Correct |
| Luna Decisions | Number of guests&#x27; cookies | Correct |
| Clef Flash | Number of cookies from local bakery | Incorrect |
| Strands Decider | Number of cookies from local bakery | Incorrect |
| GLiNER2.5 Decide | Number of cookies from local bakery | Incorrect |
| Laya | Number of guests&#x27; cookies | Correct |
| CalDec v1 | Number of guests&#x27; cookies | Correct |

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
    "record": "2059",
    "kind": "source_file_record"
  },
  "source_revision": null,
  "input_hash": "aaa93072fb82ab47078cc4eac6148eb0bab0163c59a650a85b9707db26f17e43"
}
```

</details>
