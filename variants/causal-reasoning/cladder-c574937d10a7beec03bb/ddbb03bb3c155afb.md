# Paraphrasing · Change individual words and phrases variant

[Original question](../../../questions/causal-reasoning/cladder-c574937d10a7beec03bb.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Pexu directly affects kraz and hwax. Hwax directly affects rukz. Kraz directly affects rukz.
> For those who are not pexu, the probability of rukz is 74%. For those who are pexu, the probability of rukz is 66%.

## Question

> Does pexu negatively affect rukz through hwax and kraz?

## Answer choices

- **yes.** Yes
- **no.** No

**Reference answer:** `yes`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Pexu directly affects kraz and hwax. Hwax directly affects rukz. Kraz directly affects rukz.\nFor those who are not pexu, the probability of rukz is 74%. For those who are pexu, the probability of rukz is 66%.",
  "question": "Does pexu negatively affect rukz through hwax and kraz?",
  "choices": {
    "yes": "Yes",
    "no": "No"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `yes` — Yes | `yes` — Yes | Same answer |
| Decider v1.1 | `yes` — Yes | `no` — No | Different answer |
| Jev | `yes` — Yes | `yes` — Yes | Same answer |
| Microsoft Decision-1 | `yes` — Yes | `yes` — Yes | Same answer |
| Clef | `yes` — Yes | `yes` — Yes | Same answer |
| Luna Decisions | `no` — No | `no` — No | Same answer |
| Clef Flash | `yes` — Yes | `yes` — Yes | Same answer |
| Strands Decider | `yes` — Yes | `yes` — Yes | Same answer |
| GLiNER2.5 Decide | `yes` — Yes | `yes` — Yes | Same answer |
| Laya | `yes` — Yes | `no` — No | Different answer |
| CalDec v1 | `yes` — Yes | `yes` — Yes | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `cladder/c574937d10a7beec03bb/paraphrasing/surface`

**Input fingerprint:** `18625feda584f32070a0bf4fe1899b9582ca39550ecc297765986d0b6382d0e1`

| Change | Recorded version |
| --- | --- |
| Paraphrasing | Change individual words and phrases |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/causal-reasoning/cladder-c574937d10a7beec03bb.md).
