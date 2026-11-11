# Option order · Move the first answer choice to the end variant

[Original question](../../../questions/relations/clutrr-5da4a0da272a5ef3672b.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** answer choices or their order.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> \[Johnny\] was so excited to surprise his son, \[Leo\], with the tickets to the playoffs. \[Gene\]'s mother \[Helen\] had to help him with his homework because he was having a test soon. \[Kecia\] and her sister, \[Helen\], frequently bicker. However, they always make up quickly. \[Gene\] asked his brother \[Clyde\] if he would come help him fix his car next weekend. \[Joanne\] took her father \[Johnny\] to his doctor's appointment and afterward her brother \[Clyde\] came over and visited for awhile.

## Question

> What is Kecia’s relationship to Leo?

## Answer choices

- **brother.** brother
- **daughter.** daughter
- **daughter-in-law.** daughter-in-law
- **father.** father
- **father-in-law.** father-in-law
- **granddaughter.** granddaughter
- **grandfather.** grandfather
- **grandmother.** grandmother
- **grandson.** grandson
- **mother.** mother
- **mother-in-law.** mother-in-law
- **nephew.** nephew
- **niece.** niece
- **sister.** sister
- **son.** son
- **son-in-law.** son-in-law
- **uncle.** uncle
- **aunt.** aunt

**Reference answer:** `aunt`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "[Johnny] was so excited to surprise his son, [Leo], with the tickets to the playoffs. [Gene]'s mother [Helen] had to help him with his homework because he was having a test soon. [Kecia] and her sister, [Helen], frequently bicker. However, they always make up quickly. [Gene] asked his brother [Clyde] if he would come help him fix his car next weekend. [Joanne] took her father [Johnny] to his doctor's appointment and afterward her brother [Clyde] came over and visited for awhile.",
  "question": "What is Kecia’s relationship to Leo?",
  "choices": {
    "brother": "brother",
    "daughter": "daughter",
    "daughter-in-law": "daughter-in-law",
    "father": "father",
    "father-in-law": "father-in-law",
    "granddaughter": "granddaughter",
    "grandfather": "grandfather",
    "grandmother": "grandmother",
    "grandson": "grandson",
    "mother": "mother",
    "mother-in-law": "mother-in-law",
    "nephew": "nephew",
    "niece": "niece",
    "sister": "sister",
    "son": "son",
    "son-in-law": "son-in-law",
    "uncle": "uncle",
    "aunt": "aunt"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `aunt` — aunt | `aunt` — aunt | Same answer |
| Decider v1.1 | `aunt` — aunt | `aunt` — aunt | Same answer |
| Jev | `aunt` — aunt | `aunt` — aunt | Same answer |
| Microsoft Decision-1 | `aunt` — aunt | `aunt` — aunt | Same answer |
| Clef | `aunt` — aunt | `aunt` — aunt | Same answer |
| Luna Decisions | Refused | Refused | — |
| Clef Flash | `aunt` — aunt | `aunt` — aunt | Same answer |
| Strands Decider | `sister` — sister | `sister` — sister | Same answer |
| GLiNER2.5 Decide | `brother` — brother | `brother` — brother | Same answer |
| Laya | `sister` — sister | `sister` — sister | Same answer |
| CalDec v1 | `mother` — mother | `mother-in-law` — mother-in-law | Different answer |

Clef and Clef Flash sort answer choices in their published input-processing code. Their choice-order results describe that preprocessing.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `clutrr/5da4a0da272a5ef3672b/option_order/rotate_1`

**Input fingerprint:** `a1b04945539c9754b3f6f58ad3a06a0d581b355b695bf7494d2fd3abec3111b4`

| Change | Recorded version |
| --- | --- |
| Option order | Move the first answer choice to the end |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/relations/clutrr-5da4a0da272a5ef3672b.md).
