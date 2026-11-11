# Numerical cognition · question 47

[Back to Numerical cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `finqa/cda0528ffe6fb9a5ef92`  
**Source:** [FinQA](https://github.com/czyssrs/FinQA)  
**Input format:** adapted choices

[Explore this question’s altered versions](../../variants/numerical-cognition/finqa-cda0528ffe6fb9a5ef92/README.md)

## Context

> {"pre\_text": \["performance graph the following graph compares the total return , assuming reinvestment of dividends , on an investment in the company , based on performance of the company's common stock , with the total return of the standard &amp; poor's 500 composite stock index and the dow jones united states travel and leisure index for a five year period by measuring the changes in common stock prices from december 31 , 2012 to december 31 , 2017. ."\], "table": \[\["", "12/12", "12/13", "12/14", "12/15", "12/16", "12/17"\], \["royal caribbean cruises ltd .", "100.00", "142.11", "251.44", "313.65", "260.04", "385.47"\], \["s&amp;p 500", "100.00", "132.39", "150.51", "152.59", "170.84", "208.14"\], \["dow jones us travel &amp; leisure", "100.00", "145.48", "169.28", "179.27", "192.85", "238.77"\]\], "post\_text": \["the stock performance graph assumes for comparison that the value of the company's common stock and of each index was $ 100 on december 31 , 2012 and that all dividends were reinvested .", "past performance is not necessarily an indicator of future results. ."\]}

## Question

> what is the mathematical mean for all three investments as of dec 31 , 2017?

## Answer choices

- **A:** 385.47
- **B:** 2.77
- **C:** 277.46
- **D:** 118.28

**Reference answer:** 277.46 (`C`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "{\"pre_text\": [\"performance graph the following graph compares the total return , assuming reinvestment of dividends , on an investment in the company , based on performance of the company's common stock , with the total return of the standard & poor's 500 composite stock index and the dow jones united states travel and leisure index for a five year period by measuring the changes in common stock prices from december 31 , 2012 to december 31 , 2017. .\"], \"table\": [[\"\", \"12/12\", \"12/13\", \"12/14\", \"12/15\", \"12/16\", \"12/17\"], [\"royal caribbean cruises ltd .\", \"100.00\", \"142.11\", \"251.44\", \"313.65\", \"260.04\", \"385.47\"], [\"s&p 500\", \"100.00\", \"132.39\", \"150.51\", \"152.59\", \"170.84\", \"208.14\"], [\"dow jones us travel & leisure\", \"100.00\", \"145.48\", \"169.28\", \"179.27\", \"192.85\", \"238.77\"]], \"post_text\": [\"the stock performance graph assumes for comparison that the value of the company's common stock and of each index was $ 100 on december 31 , 2012 and that all dividends were reinvested .\", \"past performance is not necessarily an indicator of future results. .\"]}",
  "question": "what is the mathematical mean for all three investments as of dec 31 , 2017?",
  "choices": {
    "A": "385.47",
    "B": "2.77",
    "C": "277.46",
    "D": "118.28"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | 277.46 | Correct |
| Opus 5.5 | 277.46 | Correct |
| GLiDE v1.2 | 277.46 | Correct |
| Decider v1.1 | 277.46 | Correct |
| Jev | 277.46 | Correct |
| Microsoft Decision-1 | 277.46 | Correct |
| Clef | 277.46 | Correct |
| Luna Decisions | 277.46 | Correct |
| Clef Flash | 277.46 | Correct |
| Strands Decider | 277.46 | Correct |
| GLiNER2.5 Decide | 385.47 | Incorrect |
| Laya | 385.47 | Incorrect |
| CalDec v1 | 385.47 | Incorrect |

## Source and sharing

Attribution: Zhiyu Chen et al.; FinQA authors.  
Terms: **[MIT](https://opensource.org/license/mit)**. [Source sharing decision](../../docs/data-sharing.md).  
The capability assignment and choice-format normalization are part of this experiment. Source data retain their own terms.

<details>
<summary>Exact source locator and input fingerprint</summary>

```json
{
  "source_locator": {
    "path": "dataset/train.json",
    "record": "2215",
    "kind": "source_file_record"
  },
  "source_revision": "0f16e2867befa6840783e58be38c9efb9229d742",
  "input_hash": "fee3dfb942769497aecaf127c5a3eb75adfc05cda04da7ac47cdb6a42d9ec7e9"
}
```

</details>
