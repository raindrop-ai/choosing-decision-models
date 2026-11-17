# Option order · Move the first answer choice to the end variant

[Original question](../../../questions/spatial-cognition/spartqa-d1358533de5389e13e27.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** answer choices or their order.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> We have three blocks, A, B and C. Block A has one medium blue square. Then, there is block B. It has a medium blue square. This block also has a medium black square. The medium blue square is below the medium black square. Finally, to the right of block A we have block C. It is above block B. It contains two medium blue squares. One medium yellow square is also in this block. Medium blue square number one is touching the bottom edge of this block. Medium blue square number two is below the medium yellow square. Medium blue square number one is below the medium yellow square and medium blue square number two.

## Question

> Which blocks have a medium square that is above a blue square?

## Answer choices

- **B.** \[&quot;B&quot;, &quot;C&quot;\]
- **C.** \[&quot;C&quot;\]
- **D.** \[\]
- **E.** \[&quot;A&quot;, &quot;B&quot;, &quot;C&quot;\]
- **F.** \[&quot;A&quot;\]
- **G.** \[&quot;A&quot;, &quot;C&quot;\]
- **H.** \[&quot;A&quot;, &quot;B&quot;\]
- **A.** \[&quot;B&quot;\]

**Reference answer:** `B`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "We have three blocks, A, B and C. Block A has one medium blue square. Then, there is block B. It has a medium blue square. This block also has a medium black square. The medium blue square is below the medium black square. Finally, to the right of block A we have block C. It is above block B. It contains two medium blue squares. One medium yellow square is also in this block. Medium blue square number one is touching the bottom edge of this block. Medium blue square number two is below the medium yellow square. Medium blue square number one is below the medium yellow square and medium blue square number two.",
  "question": "Which blocks have a medium square that is above a blue square?",
  "choices": {
    "B": "[\"B\", \"C\"]",
    "C": "[\"C\"]",
    "D": "[]",
    "E": "[\"A\", \"B\", \"C\"]",
    "F": "[\"A\"]",
    "G": "[\"A\", \"C\"]",
    "H": "[\"A\", \"B\"]",
    "A": "[\"B\"]"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `B` — \[&quot;B&quot;, &quot;C&quot;\] | `B` — \[&quot;B&quot;, &quot;C&quot;\] | Same answer |
| Decider v1.1 | `B` — \[&quot;B&quot;, &quot;C&quot;\] | `B` — \[&quot;B&quot;, &quot;C&quot;\] | Same answer |
| Jev | `B` — \[&quot;B&quot;, &quot;C&quot;\] | `B` — \[&quot;B&quot;, &quot;C&quot;\] | Same answer |
| Microsoft Decision-1 | `B` — \[&quot;B&quot;, &quot;C&quot;\] | `B` — \[&quot;B&quot;, &quot;C&quot;\] | Same answer |
| Clef | `B` — \[&quot;B&quot;, &quot;C&quot;\] | `B` — \[&quot;B&quot;, &quot;C&quot;\] | Same answer |
| Luna Decisions | `B` — \[&quot;B&quot;, &quot;C&quot;\] | `B` — \[&quot;B&quot;, &quot;C&quot;\] | Same answer |
| Clef Flash | `B` — \[&quot;B&quot;, &quot;C&quot;\] | `B` — \[&quot;B&quot;, &quot;C&quot;\] | Same answer |
| Strands Decider | `C` — \[&quot;C&quot;\] | `C` — \[&quot;C&quot;\] | Same answer |
| GLiNER2.5 Decide | `H` — \[&quot;A&quot;, &quot;B&quot;\] | `A` — \[&quot;B&quot;\] | Different answer |
| Laya | `B` — \[&quot;B&quot;, &quot;C&quot;\] | `E` — \[&quot;A&quot;, &quot;B&quot;, &quot;C&quot;\] | Different answer |
| CalDec v1 | `B` — \[&quot;B&quot;, &quot;C&quot;\] | `E` — \[&quot;A&quot;, &quot;B&quot;, &quot;C&quot;\] | Different answer |

Clef and Clef Flash sort answer choices in their published input-processing code. Their choice-order results describe that preprocessing.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `spartqa/d1358533de5389e13e27/option_order/rotate_1`

**Input fingerprint:** `ccf3ef58f658e137fdc4599b2cb351599693720aab3908aebbe552cc76a440f8`

| Change | Recorded version |
| --- | --- |
| Option order | Move the first answer choice to the end |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/spatial-cognition/spartqa-d1358533de5389e13e27.md).
