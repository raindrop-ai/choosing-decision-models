# Option order · Move the first answer choice to the end variant

[Original question](../../../questions/numerical-cognition/finqa-1e239367f3767bf0a849.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** answer choices or their order.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

<details>
<summary>Read the full context</summary>

> {"pre\_text": \["stock performance graph the following performance graph compares the cumulative total return ( including dividends ) to the holders of our common stock from december 31 , 2002 through december 31 , 2007 , with the cumulative total returns of the nyse composite index , the ftse nareit composite reit index ( the 201call reit index 201d ) , the ftse nareit healthcare equity reit index ( the 201chealthcare reit index 201d ) and the russell 1000 index over the same period .", "the comparison assumes $ 100 was invested on december 31 , 2002 in our common stock and in each of the foregoing indices and assumes reinvestment of dividends , as applicable .", "we have included the nyse composite index in the performance graph because our common stock is listed on the nyse .", "we have included the other indices because we believe that they are either most representative of the industry in which we compete , or otherwise provide a fair basis for comparison with ventas , and are therefore particularly relevant to an assessment of our performance .", "the figures in the table below are rounded to the nearest dollar. ."\], "table": \[\["", "12/31/2002", "12/31/2003", "12/31/2004", "12/31/2005", "12/31/2006", "12/31/2007"\], \["ventas", "$ 100", "$ 206", "$ 270", "$ 331", "$ 457", "$ 512"\], \["nyse composite index", "$ 100", "$ 132", "$ 151", "$ 166", "$ 200", "$ 217"\], \["all reit index", "$ 100", "$ 138", "$ 181", "$ 196", "$ 262", "$ 215"\], \["healthcare reit index", "$ 100", "$ 154", "$ 186", "$ 189", "$ 273", "$ 279"\], \["russell 1000 index", "$ 100", "$ 130", "$ 145", "$ 154", "$ 178", "$ 188"\]\], "post\_text": \["ventas nyse composite index all reit index healthcare reit index russell 1000 index ."\]}

</details>

## Question

> what was the 5 year return on ventas common stock?

## Answer choices

- **B.** 412%
- **C.** 51200%
- **D.** 31200%
- **A.** 4120000%

**Reference answer:** `B`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "{\"pre_text\": [\"stock performance graph the following performance graph compares the cumulative total return ( including dividends ) to the holders of our common stock from december 31 , 2002 through december 31 , 2007 , with the cumulative total returns of the nyse composite index , the ftse nareit composite reit index ( the 201call reit index 201d ) , the ftse nareit healthcare equity reit index ( the 201chealthcare reit index 201d ) and the russell 1000 index over the same period .\", \"the comparison assumes $ 100 was invested on december 31 , 2002 in our common stock and in each of the foregoing indices and assumes reinvestment of dividends , as applicable .\", \"we have included the nyse composite index in the performance graph because our common stock is listed on the nyse .\", \"we have included the other indices because we believe that they are either most representative of the industry in which we compete , or otherwise provide a fair basis for comparison with ventas , and are therefore particularly relevant to an assessment of our performance .\", \"the figures in the table below are rounded to the nearest dollar. .\"], \"table\": [[\"\", \"12/31/2002\", \"12/31/2003\", \"12/31/2004\", \"12/31/2005\", \"12/31/2006\", \"12/31/2007\"], [\"ventas\", \"$ 100\", \"$ 206\", \"$ 270\", \"$ 331\", \"$ 457\", \"$ 512\"], [\"nyse composite index\", \"$ 100\", \"$ 132\", \"$ 151\", \"$ 166\", \"$ 200\", \"$ 217\"], [\"all reit index\", \"$ 100\", \"$ 138\", \"$ 181\", \"$ 196\", \"$ 262\", \"$ 215\"], [\"healthcare reit index\", \"$ 100\", \"$ 154\", \"$ 186\", \"$ 189\", \"$ 273\", \"$ 279\"], [\"russell 1000 index\", \"$ 100\", \"$ 130\", \"$ 145\", \"$ 154\", \"$ 178\", \"$ 188\"]], \"post_text\": [\"ventas nyse composite index all reit index healthcare reit index russell 1000 index .\"]}",
  "question": "what was the 5 year return on ventas common stock?",
  "choices": {
    "B": "412%",
    "C": "51200%",
    "D": "31200%",
    "A": "4120000%"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `B` — 412% | `B` — 412% | Same answer |
| Decider v1.1 | `B` — 412% | `B` — 412% | Same answer |
| Jev | `B` — 412% | `B` — 412% | Same answer |
| Microsoft Decision-1 | `B` — 412% | `B` — 412% | Same answer |
| Clef | `B` — 412% | `B` — 412% | Same answer |
| Luna Decisions | `B` — 412% | `B` — 412% | Same answer |
| Clef Flash | `B` — 412% | `B` — 412% | Same answer |
| Strands Decider | `B` — 412% | `B` — 412% | Same answer |
| GLiNER2.5 Decide | `A` — 4120000% | `A` — 4120000% | Same answer |
| Laya | `C` — 51200% | `C` — 51200% | Same answer |
| CalDec v1 | `C` — 51200% | `C` — 51200% | Same answer |

Clef and Clef Flash sort answer choices in their published input-processing code. Their choice-order results describe that preprocessing.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `finqa/1e239367f3767bf0a849/option_order/rotate_1`

**Input fingerprint:** `3820d045a08ebd770dcbb5e5f026d724ced9cfbeba53c5134f3737480e9b08fd`

| Change | Recorded version |
| --- | --- |
| Option order | Move the first answer choice to the end |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/numerical-cognition/finqa-1e239367f3767bf0a849.md).
