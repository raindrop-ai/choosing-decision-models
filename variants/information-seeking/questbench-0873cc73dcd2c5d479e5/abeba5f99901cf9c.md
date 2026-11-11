# Evidence order · Ask about the object before presenting the facts variant

[Original question](../../../questions/information-seeking/questbench-0873cc73dcd2c5d479e5.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> If John works a full 7 day week, how much does he make? John is a diligent worker who completes cycles of work each day. Each cycle consists of different tasks. Each task pays $1.20. However, John also spends on a cup of coffee after every 10 cycles to keep himself energized, but his employer reimburses him for these coffee breaks.

## Question

> Which missing variable should be asked about to solve this problem?

## Answer choices

- **T.** Number of tasks per cycle
- **C1.** Cost of a cup of coffee

**Reference answer:** `T`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "If John works a full 7 day week, how much does he make? John is a diligent worker who completes cycles of work each day. Each cycle consists of different tasks. Each task pays $1.20. However, John also spends on a cup of coffee after every 10 cycles to keep himself energized, but his employer reimburses him for these coffee breaks.",
  "question": "Which missing variable should be asked about to solve this problem?",
  "choices": {
    "T": "Number of tasks per cycle",
    "C1": "Cost of a cup of coffee"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `T` — Number of tasks per cycle | `T` — Number of tasks per cycle | Same answer |
| Decider v1.1 | `T` — Number of tasks per cycle | `T` — Number of tasks per cycle | Same answer |
| Jev | `T` — Number of tasks per cycle | `T` — Number of tasks per cycle | Same answer |
| Microsoft Decision-1 | `T` — Number of tasks per cycle | `T` — Number of tasks per cycle | Same answer |
| Clef | `T` — Number of tasks per cycle | `T` — Number of tasks per cycle | Same answer |
| Luna Decisions | `T` — Number of tasks per cycle | `T` — Number of tasks per cycle | Same answer |
| Clef Flash | `T` — Number of tasks per cycle | `T` — Number of tasks per cycle | Same answer |
| Strands Decider | `T` — Number of tasks per cycle | `T` — Number of tasks per cycle | Same answer |
| GLiNER2.5 Decide | `C1` — Cost of a cup of coffee | `C1` — Cost of a cup of coffee | Same answer |
| Laya | `T` — Number of tasks per cycle | `T` — Number of tasks per cycle | Same answer |
| CalDec v1 | `C1` — Cost of a cup of coffee | `C1` — Cost of a cup of coffee | Same answer |

**Ordering comparison:** literal local or custom unit permutation. Only the exact matched comparison sets contribute to the reported ordering contrasts.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `questbench/0873cc73dcd2c5d479e5/presentation_order/native_object_query_before_givens/clean-source_first_parallel_b_intrinsic_query_orders_0334`

**Input fingerprint:** `95b4787d5b2fe12af4a1078199191c156bfb1198040df1201270fcb763c3e949`

| Change | Recorded version |
| --- | --- |
| Evidence order | Ask about the object before presenting the facts |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/information-seeking/questbench-0873cc73dcd2c5d479e5.md).
