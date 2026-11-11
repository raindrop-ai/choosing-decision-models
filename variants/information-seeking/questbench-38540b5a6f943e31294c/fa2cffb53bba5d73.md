# Evidence order · Swap items in the given list variant

[Original question](../../../questions/information-seeking/questbench-38540b5a6f943e31294c.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Lindsay is doing the laundry, and thinks she has missed some socks. There are  socks and  pairs of trousers that need washing. If she washes 15 loose socks and 10 pairs of socks, how many socks has Lindsay missed?

## Question

> Which missing variable should be asked about to solve this problem?

## Answer choices

- **S.** Total number of socks
- **X.** Total pairs of trousers

**Reference answer:** `S`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Lindsay is doing the laundry, and thinks she has missed some socks. There are  socks and  pairs of trousers that need washing. If she washes 15 loose socks and 10 pairs of socks, how many socks has Lindsay missed?",
  "question": "Which missing variable should be asked about to solve this problem?",
  "choices": {
    "S": "Total number of socks",
    "X": "Total pairs of trousers"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `S` — Total number of socks | `S` — Total number of socks | Same answer |
| Decider v1.1 | `S` — Total number of socks | `S` — Total number of socks | Same answer |
| Jev | `S` — Total number of socks | `S` — Total number of socks | Same answer |
| Microsoft Decision-1 | `S` — Total number of socks | `S` — Total number of socks | Same answer |
| Clef | `S` — Total number of socks | `S` — Total number of socks | Same answer |
| Luna Decisions | `S` — Total number of socks | `S` — Total number of socks | Same answer |
| Clef Flash | `S` — Total number of socks | `S` — Total number of socks | Same answer |
| Strands Decider | `S` — Total number of socks | `S` — Total number of socks | Same answer |
| GLiNER2.5 Decide | `S` — Total number of socks | `S` — Total number of socks | Same answer |
| Laya | `S` — Total number of socks | `S` — Total number of socks | Same answer |
| CalDec v1 | `S` — Total number of socks | `S` — Total number of socks | Same answer |

**Ordering comparison:** literal local or custom unit permutation. Only the exact matched comparison sets contribute to the reported ordering contrasts.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `questbench/38540b5a6f943e31294c/presentation_order/swap_given_inventory/clean-source_first_parallel_b_financial_orders_0305`

**Input fingerprint:** `e04b40d84a412f2c3a59a929082a93ecd88457a63fd4ba115921c800b7229be5`

| Change | Recorded version |
| --- | --- |
| Evidence order | Swap items in the given list |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/information-seeking/questbench-38540b5a6f943e31294c.md).
