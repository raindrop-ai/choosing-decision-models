# Similar distractors · Add more similar but irrelevant items variant

[Original question](../../../questions/retrieval/spartqa-7e594cb9c752644a8f52.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** question instructions.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> We have two blocks, A and B. Block A is to the left of B. Block A contains one small blue square. Block B has two big yellow triangles. One small black circle and a small blue triangle are also in this block. One big yellow circle is also touching the bottom edge of this block. To the right of big yellow triangle number one which is near to the big yellow circle there is the small blue triangle. This block also has a medium blue square.. Big yellow triangle number two is touching the right edge of this block. The medium blue square is touching the right edge of this block. Far from, to the left of and below big yellow triangle number two there is the big yellow circle.

## Question

> Which blocks don't have any small blue square?
>
> «Is the teal cylinder Ovelin above the amber prism Nerath?»
>
> «Does the violet pyramid Zelmin touch the silver cone Travon?»
>
> «Is the copper sphere Dervak far from the cyan cube Melvar?»

## Answer choices

- **A.** \[&quot;A&quot;, &quot;B&quot;, &quot;C&quot;\]
- **B.** \[&quot;B&quot;\]
- **C.** \[\]
- **D.** \[&quot;A&quot;, &quot;B&quot;\]
- **E.** \[&quot;A&quot;\]
- **F.** \[&quot;A&quot;, &quot;C&quot;\]
- **G.** \[&quot;C&quot;\]
- **H.** \[&quot;B&quot;, &quot;C&quot;\]

**Reference answer:** `B`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "We have two blocks, A and B. Block A is to the left of B. Block A contains one small blue square. Block B has two big yellow triangles. One small black circle and a small blue triangle are also in this block. One big yellow circle is also touching the bottom edge of this block. To the right of big yellow triangle number one which is near to the big yellow circle there is the small blue triangle. This block also has a medium blue square.. Big yellow triangle number two is touching the right edge of this block. The medium blue square is touching the right edge of this block. Far from, to the left of and below big yellow triangle number two there is the big yellow circle.",
  "question": "Which blocks don't have any small blue square?\n\n«Is the teal cylinder Ovelin above the amber prism Nerath?»\n\n«Does the violet pyramid Zelmin touch the silver cone Travon?»\n\n«Is the copper sphere Dervak far from the cyan cube Melvar?»",
  "choices": {
    "A": "[\"A\", \"B\", \"C\"]",
    "B": "[\"B\"]",
    "C": "[]",
    "D": "[\"A\", \"B\"]",
    "E": "[\"A\"]",
    "F": "[\"A\", \"C\"]",
    "G": "[\"C\"]",
    "H": "[\"B\", \"C\"]"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `B` — \[&quot;B&quot;\] | `B` — \[&quot;B&quot;\] | Same answer |
| Decider v1.1 | `B` — \[&quot;B&quot;\] | `B` — \[&quot;B&quot;\] | Same answer |
| Jev | `B` — \[&quot;B&quot;\] | `B` — \[&quot;B&quot;\] | Same answer |
| Microsoft Decision-1 | `B` — \[&quot;B&quot;\] | `H` — \[&quot;B&quot;, &quot;C&quot;\] | Different answer |
| Clef | `B` — \[&quot;B&quot;\] | `E` — \[&quot;A&quot;\] | Different answer |
| Luna Decisions | `B` — \[&quot;B&quot;\] | `B` — \[&quot;B&quot;\] | Same answer |
| Clef Flash | `G` — \[&quot;C&quot;\] | `G` — \[&quot;C&quot;\] | Same answer |
| Strands Decider | `B` — \[&quot;B&quot;\] | `B` — \[&quot;B&quot;\] | Same answer |
| GLiNER2.5 Decide | `H` — \[&quot;B&quot;, &quot;C&quot;\] | `H` — \[&quot;B&quot;, &quot;C&quot;\] | Same answer |
| Laya | `B` — \[&quot;B&quot;\] | `B` — \[&quot;B&quot;\] | Same answer |
| CalDec v1 | `B` — \[&quot;B&quot;\] | `B` — \[&quot;B&quot;\] | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `spartqa/7e594cb9c752644a8f52/similar_distractors/high/clean-source_first_spartqa_near_questions_full_0223`

**Input fingerprint:** `8d9d11f5ef165ddf50b4e981a428357a45b8fae260bac85d991d78642f1a243f`

| Change | Recorded version |
| --- | --- |
| Similar distractors | Add more similar but irrelevant items |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/retrieval/spartqa-7e594cb9c752644a8f52.md).
