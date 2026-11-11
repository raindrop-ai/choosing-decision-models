# Option order · Move the first answer choice to the end variant

[Original question](../../../questions/retrieval/spartqa-55c71aa18eb52489daf1.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** answer choices or their order.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> We have three blocks. Lets call them A, B and C. Block A is below B. Block C is above A. Block A contains one medium blue square. Block B has one medium black square. And block C has two medium blue squares. Medium blue square number one is touching the bottom edge of this block. There is also a medium black square in this block. It is below medium blue square number two. Below the medium black square and medium blue square number two is medium blue square number one.

## Question

> Which blocks have a medium blue square?

## Answer choices

- **B.** [&quot;A&quot;]
- **C.** [&quot;C&quot;]
- **D.** []
- **E.** [&quot;B&quot;, &quot;C&quot;]
- **F.** [&quot;A&quot;, &quot;B&quot;]
- **G.** [&quot;B&quot;]
- **H.** [&quot;A&quot;, &quot;B&quot;, &quot;C&quot;]
- **A.** [&quot;A&quot;, &quot;C&quot;]

**Reference answer:** `A`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "We have three blocks. Lets call them A, B and C. Block A is below B. Block C is above A. Block A contains one medium blue square. Block B has one medium black square. And block C has two medium blue squares. Medium blue square number one is touching the bottom edge of this block. There is also a medium black square in this block. It is below medium blue square number two. Below the medium black square and medium blue square number two is medium blue square number one.",
  "question": "Which blocks have a medium blue square?",
  "choices": {
    "B": "[\"A\"]",
    "C": "[\"C\"]",
    "D": "[]",
    "E": "[\"B\", \"C\"]",
    "F": "[\"A\", \"B\"]",
    "G": "[\"B\"]",
    "H": "[\"A\", \"B\", \"C\"]",
    "A": "[\"A\", \"C\"]"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `A` — \[&quot;A&quot;, &quot;C&quot;\] | `A` — \[&quot;A&quot;, &quot;C&quot;\] | Same answer |
| Decider v1.1 | `A` — \[&quot;A&quot;, &quot;C&quot;\] | `A` — \[&quot;A&quot;, &quot;C&quot;\] | Same answer |
| Jev | `A` — \[&quot;A&quot;, &quot;C&quot;\] | `A` — \[&quot;A&quot;, &quot;C&quot;\] | Same answer |
| Microsoft Decision-1 | `A` — \[&quot;A&quot;, &quot;C&quot;\] | `A` — \[&quot;A&quot;, &quot;C&quot;\] | Same answer |
| Clef | `A` — \[&quot;A&quot;, &quot;C&quot;\] | `A` — \[&quot;A&quot;, &quot;C&quot;\] | Same answer |
| Luna Decisions | `H` — \[&quot;A&quot;, &quot;B&quot;, &quot;C&quot;\] | `A` — \[&quot;A&quot;, &quot;C&quot;\] | Different answer |
| Clef Flash | `A` — \[&quot;A&quot;, &quot;C&quot;\] | `A` — \[&quot;A&quot;, &quot;C&quot;\] | Same answer |
| Strands Decider | `A` — \[&quot;A&quot;, &quot;C&quot;\] | `A` — \[&quot;A&quot;, &quot;C&quot;\] | Same answer |
| GLiNER2.5 Decide | `H` — \[&quot;A&quot;, &quot;B&quot;, &quot;C&quot;\] | `H` — \[&quot;A&quot;, &quot;B&quot;, &quot;C&quot;\] | Same answer |
| Laya | `C` — \[&quot;C&quot;\] | `C` — \[&quot;C&quot;\] | Same answer |
| CalDec v1 | `C` — \[&quot;C&quot;\] | `C` — \[&quot;C&quot;\] | Same answer |

Clef and Clef Flash sort answer choices in their published input-processing code. Their choice-order results describe that preprocessing.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `spartqa/55c71aa18eb52489daf1/option_order/rotate_1`

**Input fingerprint:** `8fe66825881eb5f38778bca4ac6ea03a9be7c962519bd099c4cf30f6a50d5911`

| Change | Recorded version |
| --- | --- |
| Option order | Move the first answer choice to the end |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/retrieval/spartqa-55c71aa18eb52489daf1.md).
