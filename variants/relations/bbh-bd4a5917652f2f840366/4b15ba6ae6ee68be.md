# Option order · Reverse the answer choices variant

[Original question](../../../questions/relations/bbh-bd4a5917652f2f840366.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** answer choices or their order.

[How the edits were constructed](../../../docs/variant-methods.md)

## Question

> The following paragraphs each describe a set of five objects arranged in a fixed order. The statements are logically consistent within each paragraph. In a golf tournament, there were five golfers: Joe, Mya, Eve, Amy, and Ana. Eve finished below Joe. Ana finished below Amy. Eve finished above Amy. Mya finished above Joe.

## Answer choices

- **E.** Ana finished last
- **D.** Amy finished last
- **C.** Eve finished last
- **B.** Mya finished last
- **A.** Joe finished last

**Reference answer:** `E`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "",
  "question": "The following paragraphs each describe a set of five objects arranged in a fixed order. The statements are logically consistent within each paragraph. In a golf tournament, there were five golfers: Joe, Mya, Eve, Amy, and Ana. Eve finished below Joe. Ana finished below Amy. Eve finished above Amy. Mya finished above Joe.",
  "choices": {
    "E": "Ana finished last",
    "D": "Amy finished last",
    "C": "Eve finished last",
    "B": "Mya finished last",
    "A": "Joe finished last"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `E` — Ana finished last | `E` — Ana finished last | Same answer |
| Decider v1.1 | `E` — Ana finished last | `E` — Ana finished last | Same answer |
| Jev | `E` — Ana finished last | `E` — Ana finished last | Same answer |
| Microsoft Decision-1 | `E` — Ana finished last | `E` — Ana finished last | Same answer |
| Clef | `E` — Ana finished last | `E` — Ana finished last | Same answer |
| Luna Decisions | `E` — Ana finished last | `E` — Ana finished last | Same answer |
| Clef Flash | `E` — Ana finished last | `E` — Ana finished last | Same answer |
| Strands Decider | `E` — Ana finished last | `E` — Ana finished last | Same answer |
| GLiNER2.5 Decide | `C` — Eve finished last | `C` — Eve finished last | Same answer |
| Laya | `C` — Eve finished last | `E` — Ana finished last | Different answer |
| CalDec v1 | `C` — Eve finished last | `B` — Mya finished last | Different answer |

Clef and Clef Flash sort answer choices in their published input-processing code. Their choice-order results describe that preprocessing.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `bbh/bd4a5917652f2f840366/option_order/reverse`

**Input fingerprint:** `8818a80985b7b3e89983e82da0a32fa0e5042acf652357e0690cc0abf20403aa`

| Change | Recorded version |
| --- | --- |
| Option order | Reverse the answer choices |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/relations/bbh-bd4a5917652f2f840366.md).
