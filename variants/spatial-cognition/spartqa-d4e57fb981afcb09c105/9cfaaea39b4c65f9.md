# Evidence order · Swap descriptions of sections variant

[Original question](../../../questions/spatial-cognition/spartqa-d4e57fb981afcb09c105.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> There are two blocks. We call them A and B. Block A is to the left of B. Block B has a medium yellow square and a medium black square. The medium yellow square is below the medium black square. There is also a medium blue square in this block. Below the medium black square and the medium yellow square is the medium blue square. Block A contains two medium blue squares. Medium blue square number one is below medium blue square number two.

## Question

> Which blocks have a square that is above a medium blue shape?

## Answer choices

- **A.** \[&quot;A&quot;, &quot;B&quot;\]
- **B.** \[&quot;B&quot;\]
- **C.** \[&quot;C&quot;\]
- **D.** \[&quot;A&quot;, &quot;B&quot;, &quot;C&quot;\]
- **E.** \[\]
- **F.** \[&quot;A&quot;\]
- **G.** \[&quot;A&quot;, &quot;C&quot;\]
- **H.** \[&quot;B&quot;, &quot;C&quot;\]

**Reference answer:** `A`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "There are two blocks. We call them A and B. Block A is to the left of B. Block B has a medium yellow square and a medium black square. The medium yellow square is below the medium black square. There is also a medium blue square in this block. Below the medium black square and the medium yellow square is the medium blue square. Block A contains two medium blue squares. Medium blue square number one is below medium blue square number two.",
  "question": "Which blocks have a square that is above a medium blue shape?",
  "choices": {
    "A": "[\"A\", \"B\"]",
    "B": "[\"B\"]",
    "C": "[\"C\"]",
    "D": "[\"A\", \"B\", \"C\"]",
    "E": "[]",
    "F": "[\"A\"]",
    "G": "[\"A\", \"C\"]",
    "H": "[\"B\", \"C\"]"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `A` — \[&quot;A&quot;, &quot;B&quot;\] | `A` — \[&quot;A&quot;, &quot;B&quot;\] | Same answer |
| Decider v1.1 | `A` — \[&quot;A&quot;, &quot;B&quot;\] | `A` — \[&quot;A&quot;, &quot;B&quot;\] | Same answer |
| Jev | `A` — \[&quot;A&quot;, &quot;B&quot;\] | `A` — \[&quot;A&quot;, &quot;B&quot;\] | Same answer |
| Microsoft Decision-1 | `A` — \[&quot;A&quot;, &quot;B&quot;\] | `A` — \[&quot;A&quot;, &quot;B&quot;\] | Same answer |
| Clef | `A` — \[&quot;A&quot;, &quot;B&quot;\] | `A` — \[&quot;A&quot;, &quot;B&quot;\] | Same answer |
| Luna Decisions | `A` — \[&quot;A&quot;, &quot;B&quot;\] | `A` — \[&quot;A&quot;, &quot;B&quot;\] | Same answer |
| Clef Flash | `A` — \[&quot;A&quot;, &quot;B&quot;\] | `A` — \[&quot;A&quot;, &quot;B&quot;\] | Same answer |
| Strands Decider | `A` — \[&quot;A&quot;, &quot;B&quot;\] | `B` — \[&quot;B&quot;\] | Different answer |
| GLiNER2.5 Decide | `A` — \[&quot;A&quot;, &quot;B&quot;\] | `A` — \[&quot;A&quot;, &quot;B&quot;\] | Same answer |
| Laya | `B` — \[&quot;B&quot;\] | `A` — \[&quot;A&quot;, &quot;B&quot;\] | Different answer |
| CalDec v1 | `A` — \[&quot;A&quot;, &quot;B&quot;\] | `A` — \[&quot;A&quot;, &quot;B&quot;\] | Same answer |

**Ordering comparison:** literal local or custom unit permutation. Only the exact matched comparison sets contribute to the reported ordering contrasts.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `spartqa/d4e57fb981afcb09c105/presentation_order/swap_block_descriptions/clean-source_first_spartqa_block_bundle_orders_full_0147`

**Input fingerprint:** `f3f7aea07bdeb2ddaf0ba28f7ca346a12d5e48362170e7bc0f6c3d3c97d33bbd`

| Change | Recorded version |
| --- | --- |
| Evidence order | Swap descriptions of sections |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/spatial-cognition/spartqa-d4e57fb981afcb09c105.md).
