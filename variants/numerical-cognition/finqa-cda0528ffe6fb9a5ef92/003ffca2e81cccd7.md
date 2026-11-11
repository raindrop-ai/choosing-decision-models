# Repetition · Present the same evidence twice variant

[Original question](../../../questions/numerical-cognition/finqa-cda0528ffe6fb9a5ef92.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** question instructions.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> {"pre\_text": \["performance graph the following graph compares the total return , assuming reinvestment of dividends , on an investment in the company , based on performance of the company's common stock , with the total return of the standard &amp; poor's 500 composite stock index and the dow jones united states travel and leisure index for a five year period by measuring the changes in common stock prices from december 31 , 2012 to december 31 , 2017. ."\], "table": \[\["", "12/12", "12/13", "12/14", "12/15", "12/16", "12/17"\], \["royal caribbean cruises ltd .", "100.00", "142.11", "251.44", "313.65", "260.04", "385.47"\], \["s&amp;p 500", "100.00", "132.39", "150.51", "152.59", "170.84", "208.14"\], \["dow jones us travel &amp; leisure", "100.00", "145.48", "169.28", "179.27", "192.85", "238.77"\]\], "post\_text": \["the stock performance graph assumes for comparison that the value of the company's common stock and of each index was $ 100 on december 31 , 2012 and that all dividends were reinvested .", "past performance is not necessarily an indicator of future results. ."\]}

## Question

> what is the mathematical mean for all three investments as of dec 31 , 2017?
>
> «{"pre\_text": \["performance graph the following graph compares the total return , assuming reinvestment of dividends , on an investment in the company , based on performance of the company's common stock , with the total return of the standard &amp; poor's 500 composite stock index and the dow jones united states travel and leisure index for a five year period by measuring the changes in common stock prices from december 31 , 2012 to december 31 , 2017. ."\], "table": \[\["", "12/12", "12/13", "12/14", "12/15", "12/16", "12/17"\], \["royal caribbean cruises ltd .", "100.00", "142.11", "251.44", "313.65", "260.04", "385.47"\], \["s&amp;p 500", "100.00", "132.39", "150.51", "152.59", "170.84", "208.14"\], \["dow jones us travel &amp; leisure", "100.00", "145.48", "169.28", "179.27", "192.85", "238.77"\]\], "post\_text": \["the stock performance graph assumes for comparison that the value of the company's common stock and of each index was $ 100 on december 31 , 2012 and that all dividends were reinvested .", "past performance is not necessarily an indicator of future results. ."\]}»

## Answer choices

- **A.** 385.47
- **B.** 2.77
- **C.** 277.46
- **D.** 118.28

**Reference answer:** `C`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "{\"pre_text\": [\"performance graph the following graph compares the total return , assuming reinvestment of dividends , on an investment in the company , based on performance of the company's common stock , with the total return of the standard & poor's 500 composite stock index and the dow jones united states travel and leisure index for a five year period by measuring the changes in common stock prices from december 31 , 2012 to december 31 , 2017. .\"], \"table\": [[\"\", \"12/12\", \"12/13\", \"12/14\", \"12/15\", \"12/16\", \"12/17\"], [\"royal caribbean cruises ltd .\", \"100.00\", \"142.11\", \"251.44\", \"313.65\", \"260.04\", \"385.47\"], [\"s&p 500\", \"100.00\", \"132.39\", \"150.51\", \"152.59\", \"170.84\", \"208.14\"], [\"dow jones us travel & leisure\", \"100.00\", \"145.48\", \"169.28\", \"179.27\", \"192.85\", \"238.77\"]], \"post_text\": [\"the stock performance graph assumes for comparison that the value of the company's common stock and of each index was $ 100 on december 31 , 2012 and that all dividends were reinvested .\", \"past performance is not necessarily an indicator of future results. .\"]}",
  "question": "what is the mathematical mean for all three investments as of dec 31 , 2017?\n\n«{\"pre_text\": [\"performance graph the following graph compares the total return , assuming reinvestment of dividends , on an investment in the company , based on performance of the company's common stock , with the total return of the standard & poor's 500 composite stock index and the dow jones united states travel and leisure index for a five year period by measuring the changes in common stock prices from december 31 , 2012 to december 31 , 2017. .\"], \"table\": [[\"\", \"12/12\", \"12/13\", \"12/14\", \"12/15\", \"12/16\", \"12/17\"], [\"royal caribbean cruises ltd .\", \"100.00\", \"142.11\", \"251.44\", \"313.65\", \"260.04\", \"385.47\"], [\"s&p 500\", \"100.00\", \"132.39\", \"150.51\", \"152.59\", \"170.84\", \"208.14\"], [\"dow jones us travel & leisure\", \"100.00\", \"145.48\", \"169.28\", \"179.27\", \"192.85\", \"238.77\"]], \"post_text\": [\"the stock performance graph assumes for comparison that the value of the company's common stock and of each index was $ 100 on december 31 , 2012 and that all dividends were reinvested .\", \"past performance is not necessarily an indicator of future results. .\"]}»",
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

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `C` — 277.46 | `C` — 277.46 | Same answer |
| Decider v1.1 | `C` — 277.46 | `C` — 277.46 | Same answer |
| Jev | `C` — 277.46 | `C` — 277.46 | Same answer |
| Microsoft Decision-1 | `C` — 277.46 | `C` — 277.46 | Same answer |
| Clef | `C` — 277.46 | `C` — 277.46 | Same answer |
| Luna Decisions | `C` — 277.46 | `C` — 277.46 | Same answer |
| Clef Flash | `C` — 277.46 | `C` — 277.46 | Same answer |
| Strands Decider | `C` — 277.46 | `C` — 277.46 | Same answer |
| GLiNER2.5 Decide | `A` — 385.47 | `A` — 385.47 | Same answer |
| Laya | `A` — 385.47 | `A` — 385.47 | Same answer |
| CalDec v1 | `A` — 385.47 | `A` — 385.47 | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `finqa/cda0528ffe6fb9a5ef92/evidence_repetition/2/clean-source_first_parallel_b_financial_orders_0305`

**Input fingerprint:** `c9b60ec4802207d934f35bb5dbb2049aa47570dda83983c34640bc8758216095`

| Change | Recorded version |
| --- | --- |
| Repetition | Present the same evidence twice |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/numerical-cognition/finqa-cda0528ffe6fb9a5ef92.md).
