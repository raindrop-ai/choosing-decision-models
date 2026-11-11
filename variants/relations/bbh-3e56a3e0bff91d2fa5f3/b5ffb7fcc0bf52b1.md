# Option order · Reverse the answer choices variant

[Original question](../../../questions/relations/bbh-3e56a3e0bff91d2fa5f3.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** answer choices or their order.

[How the edits were constructed](../../../docs/variant-methods.md)

## Question

> The following paragraphs each describe a set of three objects arranged in a fixed order. The statements are logically consistent within each paragraph. In a golf tournament, there were three golfers: Amy, Ana, and Joe. Amy finished below Ana. Ana finished below Joe.

## Answer choices

- **C.** Joe finished last
- **B.** Ana finished last
- **A.** Amy finished last

**Reference answer:** `A`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "",
  "question": "The following paragraphs each describe a set of three objects arranged in a fixed order. The statements are logically consistent within each paragraph. In a golf tournament, there were three golfers: Amy, Ana, and Joe. Amy finished below Ana. Ana finished below Joe.",
  "choices": {
    "C": "Joe finished last",
    "B": "Ana finished last",
    "A": "Amy finished last"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `A` — Amy finished last | `A` — Amy finished last | Same answer |
| Decider v1.1 | `A` — Amy finished last | `A` — Amy finished last | Same answer |
| Jev | `A` — Amy finished last | `A` — Amy finished last | Same answer |
| Microsoft Decision-1 | `A` — Amy finished last | `A` — Amy finished last | Same answer |
| Clef | `A` — Amy finished last | `A` — Amy finished last | Same answer |
| Luna Decisions | `A` — Amy finished last | `A` — Amy finished last | Same answer |
| Clef Flash | `A` — Amy finished last | `A` — Amy finished last | Same answer |
| Strands Decider | `A` — Amy finished last | `A` — Amy finished last | Same answer |
| GLiNER2.5 Decide | `A` — Amy finished last | `B` — Ana finished last | Different answer |
| Laya | `A` — Amy finished last | `A` — Amy finished last | Same answer |
| CalDec v1 | `A` — Amy finished last | `A` — Amy finished last | Same answer |

Clef and Clef Flash sort answer choices in their published input-processing code. Their choice-order results describe that preprocessing.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `bbh/3e56a3e0bff91d2fa5f3/option_order/reverse`

**Input fingerprint:** `7682c775c20ca4c3535976f22a82a752219a4889a9ed63bfffb534ce106a8d28`

| Change | Recorded version |
| --- | --- |
| Option order | Reverse the answer choices |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/relations/bbh-3e56a3e0bff91d2fa5f3.md).
